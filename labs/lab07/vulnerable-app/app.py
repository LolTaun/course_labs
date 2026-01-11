from flask import Flask, request, make_response
import sqlite3
import os
import subprocess
import pickle
import logging
import ipaddress
import re
import ast
import operator

app = Flask(__name__)

SAFE_OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
    ast.Pow: operator.pow,
}


app.config["DEBUG"] = True

DB_USER = "admin"
DB_PASSWORD = "SuperSecret123"
DB_PATH = "app.db"

logging.basicConfig(level=logging.DEBUG)


def get_db():
    conn = sqlite3.connect(DB_PATH)
    return conn


@app.route("/")
def index():
    return "Vulnerable lab07 app is running!"


@app.route("/user")
def get_user():
    username = request.args.get("name", "")
    conn = get_db()
    cur = conn.cursor()
    query = f"SELECT id, name, email FROM users WHERE name = '{username}'"  # nosec B608
    app.logger.debug("Executing query: %s", query)
    rows = cur.execute(query).fetchall()
    conn.close()
    return {"result": rows}


@app.route("/search")
def search():
    q = request.args.get("q", "")
    html = f"<h1>Results for: {q}</h1>"
    return make_response(html, 200)


@app.route("/ping")
def ping():
    host = request.args.get("host", "127.0.0.1")
    try:
        ipaddress.ip_address(host)
    except ValueError:
        return "Invalid host", 400
    subprocess.run(["ping", "-c", "1", host], check=False, timeout=3)
    return f"Pinged {host}"


@app.route("/backup")
def backup():
    target = request.args.get("target", "/tmp/backup.sql")  # nosec B108
    cmd = ["sh", "-c", f"pg_dump mydb > {target}"]
    subprocess.call(cmd)
    return f"Backup to {target} started"

# Не имеет смысла, так как нет необходимости показывать файл /etc/passwd, специально выделенной директории для чтения файлов нет.
# @app.route("/read")
# def read_file():
#     path = request.args.get("path", "/etc/passwd")
#     try:
#         with open(path, "r") as f:
#             data = f.read()
#         return f"<pre>{data}</pre>"
#     except Exception as e:
#         return str(e), 500

# Не имеет смысла
# @app.route("/load")
# def load():
#     data = request.args.get("data", "")
#     try:
#         obj = pickle.loads(bytes.fromhex(data))  # nosec B301
#         return f"Loaded object: {obj}"
#     except Exception as e:
#         return f"Error: {e}", 500


def _eval_ast(node):
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value
    if isinstance(node, ast.UnaryOp) and type(node.op) in SAFE_OPS:
        return SAFE_OPS[type(node.op)](_eval_ast(node.operand))
    if isinstance(node, ast.BinOp) and type(node.op) in SAFE_OPS:
        return SAFE_OPS[type(node.op)](_eval_ast(node.left), _eval_ast(node.right))
    raise ValueError("Unsupported expression")


@app.route("/calc")
def calc():
    expr = request.args.get("expr", "1+1")
    try:
        result = _eval_ast(ast.parse(expr, mode="eval").body)
        return str(result)
    except Exception as e:
        return f"Invalid expression: {e}", 400



@app.route("/debug")
def debug():
    headers = dict(request.headers)
    env = dict(os.environ)
    return {
        "headers": headers,
        "env_sample": {k: env[k] for k in list(env)[:10]},
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)  # nosec B104
