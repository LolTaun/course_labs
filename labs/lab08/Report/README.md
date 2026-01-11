<div align="center">
<h1><a id="intro">Лабораторная работа №8</a><br></h1>
<a href="https://docs.github.com/en"><img src="https://img.shields.io/static/v1?logo=github&logoColor=fff&label=&message=Docs&color=36393f&style=flat" alt="GitHub Docs"></a>
<a href="https://daringfireball.net/projects/markdown"><img src="https://img.shields.io/static/v1?logo=markdown&logoColor=fff&label=&message=Markdown&color=36393f&style=flat" alt="Markdown"></a> 
<a href="https://symbl.cc/en/unicode-table"><img src="https://img.shields.io/static/v1?logo=unicode&logoColor=fff&label=&message=Unicode&color=36393f&style=flat" alt="Unicode"></a> 
<a href="https://shields.io"><img src="https://img.shields.io/static/v1?logo=shieldsdotio&logoColor=fff&label=&message=Shields&color=36393f&style=flat" alt="Shields"></a>
<a href="https://img.shields.io/badge/Risk_Analyze-2448a2"><img src="https://img.shields.io/badge/Course-Risk_Analysis-2448a2" alt= "RA"></a> <img src="https://img.shields.io/badge/AppSec-2448a2" alt= "RA"></a> <img src="https://img.shields.io/badge/Contributor-Кузнецов Д. А.-8b9aff" alt="Contributor Badge"></a></div>


## Задание

- [x] 1. Разверните и подготовьте окружение для уязвимого приложения

```bash
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt && vulnerable-app/requirements.txt 
```

- [x] 2. Запустите уязвимое приложение

```bash
$ docker-compose up -d --build  # http://localhost:8080
```

- [x] 3. Проверьте доступность приложения

```bash
(venv) loltaun@LT-New:~/course_labs/labs/lab08$ curl -i http://localhost:8080
HTTP/1.1 200 OK
Server: Werkzeug/2.2.3 Python/3.11.14
Date: Sat, 10 Jan 2026 15:50:12 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 625
Set-Cookie: session=guest-session-id; Path=/
Connection: close


    <h1>Vulnerable DAST Demo App</h1>
    <p>Пример уязвимого приложения для лабораторной по DAST.</p>
    <ul>
      <li><a href="/echo?msg=Hello">Reflected XSS / echo</a></li>
      <li><a href="/search?username=admin">SQL Injection / search</a></li>
      <li><a href="/login">Небезопасный логин</a></li>
      <li><a href="/profile">Профиль (зависит от cookie)</a></li>
      <li><a href="/admin">«Админка» без нормальной авторизации</a></li>
      <li><a href="/files/">Directory listing</a></li>
    </ul>
```

- [x] 4. Проведите ручное исследование уязвимостей и опишите почему такое происходит, каким образом реализуются уязвимости и дайте им определение
- [x] 4.1. `/echo` - проверить отражение параметра  `msg`  в `HTML` и использовать `payload` вида  `<script>alert('XSS')</script>` зафиксировав его поведение

```bash
http://localhost:8080/echo?msg=<script>alert('hack with XSS')</script>
```
Уязвимость - **Reflected XSS**
**Определение**: внедрение и исполнение произвольного JS в контексте страницы за счет отражения непроверенного ввода.
**Как реализовано**: параметр msg без экранирования вставляется в HTML-ответ.
**Причина**: отсутствие валидации/экранирования данных и заголовков CSP/X-Content-Type-Options.

- [x] 4.2. `/search` - проверить обычный запрос  `?username=admin` и использовать строку  `?username=admin' OR '1'='1` зафиксировав его поведение описав признак SQLi

```bash
http://localhost:8080/search?username=admin' OR '1'='1
```

Уязвимость - **SQL Injection**
**Определение**: выполнение произвольных SQL-фрагментов через подстановку в запрос без параметризации.
**Как реализовано**: значение username конкатенируется в SQL-строку, что позволяет добавить `' OR '1'='1.`
**Причина**: нет подготовленных выражений/шаблонов и проверки входных данных.

- [x] 4.3. `/login` - войти под  `admin`  и  `user` проверив логику на открытые пароли и простые SQL‑запросы.

Вход был осуществлен успешно с использованием пар логина и пароля:
- admin / admin123
- user / user123
Дополнительно получилось войти с использованием SQL-инъекций:
- Логин: `admin' --`  Пароль: `<любое значение>`
- Логин: `admin` Пароль: `' OR '1'='1`

Уязвимость - **Слабые пароли и SQL Injection**
**Определение**: обход аутентификации из-за слабых учетных данных и возможности SQL-инъекции в поле логина/пароля.
**Как реализовано**: простые пароли (admin123, user123) и конкатенация ввода в SQL позволяют логин через `admin' --` или пароль `' OR '1'='1.`
**Причина**: отсутствие нормальной политики паролей, отсутствие параметризации запросов.

- [x] 4.4. `/profile` - изменить `cookie  role`  на  `admin`  через `DevTools` → `Application` → `Cookies` и обновить  `/profile` (возможно создать `cookie`)

Уязвимость - **Insecure Direct Object / Cookie Tampering**
**Определение**: подделка клиентских файлов (cookie) без серверной верификации, дающая доступ к чужим привилегиям.
**Как реализовано**: роль берется из cookie role без подписи/проверки, изменение на admin дает повышенные права.
**Причина**: доверие к данным клиента, нет MAC/подписи/проверки на сервере.

- [x] 4.5. `/admin` -  проверить, что доступ запрещен без `cookie  role=admin` и далее подделать `cookie`, что «админка» открывается путем изменения через `DevTools`. **Подсказка:** доступ завязан на значение cookie, без подписи/ токена/ серверной проверки.

Уязвимость - **Broken Access Control / Cookie Tampering**
**Определение**: отсутствие серверной авторизации, доступ контролируется только значением cookie.
**Как реализовано**: проверка права доступа сводится к role=admin в cookie, которую можно легко подделать.
**Причина**: нет серверной сессии/токена/ACL, нет привязки к пользователю и подписи cookie.


- [x] 4.6. `/files/` - просмотрите `directory listing` и откройте один из файлов убедившись, что оно выводится
```bash
http://localhost:8080/files/secret.txt
```

Уязвимость - **Directory Listing**
**Определение**: раскрытие списка файлов каталога.
**Как реализовано**: веб-сервер отдает индекс каталога files/, позволяя просматривать и открывать файлы вроде secret.txt.
**Причина**: включен directory listing, нет ограничений на статический контент или контроля доступа.


- [x] 5. Доработайте по пп 4 лабораторную работу развив их содержимое, которое может выводиться (мин 1 пример)

Был добавлен метод ping в файл app.py, который позволяет проверить доступность сервера. Данный метод уязвим к инъекциям команд, так как параметр host напрямую используется в shell-команде без какой-либо валидации.
```python
@app.route("/ping")
def ping():
    host = request.args.get("host", "127.0.0.1")
    proc = os.popen(f"ping -c 1 {host} 2>&1")>
    output = proc.read()
    proc.close()
    return f"<h2>Ping result for {host}</h2><pre>{output}</pre><a href='/'>Назад</a>"
```

```
GET localhost:8080/ping?host=127.0.0.1;cat%20/etc/shadow

<h2>Ping result for 127.0.0.1;cat /etc/shadow</h2>
<pre>PING 127.0.0.1 (127.0.0.1) 56(84) bytes of data.
64 bytes from 127.0.0.1: icmp_seq=1 ttl=64 time=0.023 ms

--- 127.0.0.1 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 0.023/0.023/0.023/0.000 ms
root:*:20451:0:99999:7:::
daemon:*:20451:0:99999:7:::
bin:*:20451:0:99999:7:::
sys:*:20451:0:99999:7:::
sync:*:20451:0:99999:7:::
games:*:20451:0:99999:7:::
man:*:20451:0:99999:7:::
lp:*:20451:0:99999:7:::
mail:*:20451:0:99999:7:::
news:*:20451:0:99999:7:::
uucp:*:20451:0:99999:7:::
proxy:*:20451:0:99999:7:::
www-data:*:20451:0:99999:7:::
backup:*:20451:0:99999:7:::
list:*:20451:0:99999:7:::
irc:*:20451:0:99999:7:::
_apt:*:20451:0:99999:7:::
nobody:*:20451:0:99999:7:::
</pre><a href='/'>Назад</a>
```

- [x] 6. Поставьте `OWASP ZAP` и стяните образ конкртеной версии для него

```bash
$ sudo snap install zaproxy --classic
$ docker pull ghcr.io/zaproxy/zaproxy:stable
```

- [x] 7. Задайте переменные окружения для работы скриптов

```bash
$ export ZAP_IMAGE=ghcr.io/zaproxy/zaproxy:stable
$ TARGET_URL="${TARGET_URL:-http://host.docker.internal:8080}"
```

- [x] 8. Запустите скрипт автоматического сканирования DAST `OWASP ZAP`

```bash
(venv) loltaun@LT-New:~/course_labs/labs/lab08/dast$ ./zap_scan.sh
[*] Running OWASP ZAP baseline scan against http://host.docker.internal:8080
[i] Using image: ghcr.io/zaproxy/zaproxy:stable
[i] Reports will be saved to /home/loltaun/course_labs/labs/lab08/dast/reports
Using the Automation Framework
Total of 13 URLs
PASS: Vulnerable JS Library (Powered by Retire.js) [10003]
PASS: In Page Banner Information Leak [10009]
PASS: Cookie Without Secure Flag [10011]
PASS: Re-examine Cache-control Directives [10015]
PASS: Cross-Domain JavaScript Source File Inclusion [10017]
PASS: Content-Type Header Missing [10019]
PASS: Information Disclosure - Debug Error Messages [10023]
PASS: Information Disclosure - Sensitive Information in HTTP Referrer Header [10025]
PASS: HTTP Parameter Override [10026]
PASS: Information Disclosure - Suspicious Comments [10027]
PASS: Off-site Redirect [10028]
PASS: Cookie Poisoning [10029]
PASS: User Controllable Charset [10030]
PASS: User Controllable HTML Element Attribute (Potential XSS) [10031]
PASS: Viewstate [10032]
PASS: Directory Browsing [10033]
PASS: Heartbleed OpenSSL Vulnerability (Indicative) [10034]
PASS: Strict-Transport-Security Header [10035]
PASS: Server Leaks Information via "X-Powered-By" HTTP Response Header Field(s) [10037]
PASS: X-Backend-Server Header Information Leak [10039]
PASS: Secure Pages Include Mixed Content [10040]
PASS: HTTP to HTTPS Insecure Transition in Form Post [10041]
PASS: HTTPS to HTTP Insecure Transition in Form Post [10042]
PASS: User Controllable JavaScript Event (XSS) [10043]
PASS: Big Redirect Detected (Potential Sensitive Information Leak) [10044]
PASS: Retrieved from Cache [10050]
PASS: X-ChromeLogger-Data (XCOLD) Header Information Leak [10052]
PASS: CSP [10055]
PASS: X-Debug-Token Information Leak [10056]
PASS: Username Hash Found [10057]
PASS: X-AspNet-Version Response Header [10061]
PASS: PII Disclosure [10062]
PASS: Timestamp Disclosure [10096]
PASS: Hash Disclosure [10097]
PASS: Cross-Domain Misconfiguration [10098]
PASS: Weak Authentication Method [10105]
PASS: Reverse Tabnabbing [10108]
PASS: Modern Web Application [10109]
PASS: Dangerous JS Functions [10110]
PASS: Verification Request Identified [10113]
PASS: Script Served From Malicious Domain (polyfill) [10115]
PASS: ZAP is Out of Date [10116]
PASS: Absence of Anti-CSRF Tokens [10202]
PASS: Private IP Disclosure [2]
PASS: Session ID in URL Rewrite [3]
PASS: Script Passive Scan Rules [50001]
PASS: Stats Passive Scan Rule [50003]
PASS: Insecure JSF ViewState [90001]
PASS: Java Serialization Object [90002]
PASS: Sub Resource Integrity Attribute Missing [90003]
PASS: Charset Mismatch [90011]
PASS: Application Error Disclosure [90022]
PASS: WSDL File Detection [90030]
PASS: Loosely Scoped Cookie [90033]
WARN-NEW: Cookie No HttpOnly Flag [10010] x 2
        http://host.docker.internal:8080 (200 OK)
        http://host.docker.internal:8080/ (200 OK)
WARN-NEW: Missing Anti-clickjacking Header [10020] x 5
        http://host.docker.internal:8080 (200 OK)
        http://host.docker.internal:8080/ (200 OK)
        http://host.docker.internal:8080/files/ (200 OK)
        http://host.docker.internal:8080/search?username=admin (200 OK)
        http://host.docker.internal:8080/login (200 OK)
WARN-NEW: X-Content-Type-Options Header Missing [10021] x 5
        http://host.docker.internal:8080/echo?msg=Hello (200 OK)
        http://host.docker.internal:8080/files/ (200 OK)
        http://host.docker.internal:8080/files/secret.txt (200 OK)
        http://host.docker.internal:8080/login (200 OK)
        http://host.docker.internal:8080/search?username=admin (200 OK)
WARN-NEW: Information Disclosure - Sensitive Information in URL [10024] x 1
        http://host.docker.internal:8080/search?username=admin (200 OK)
WARN-NEW: Server Leaks Version Information via "Server" HTTP Response Header Field [10036] x 5
        http://host.docker.internal:8080/admin (403 Forbidden)
        http://host.docker.internal:8080/files/ (200 OK)
        http://host.docker.internal:8080/files/secret.txt (200 OK)
        http://host.docker.internal:8080/sitemap.xml (404 Not Found)
        http://host.docker.internal:8080/login (200 OK)
WARN-NEW: Content Security Policy (CSP) Header Not Set [10038] x 5
        http://host.docker.internal:8080/files/ (200 OK)
        http://host.docker.internal:8080/robots.txt (404 Not Found)
        http://host.docker.internal:8080/script (404 Not Found)
        http://host.docker.internal:8080/sitemap.xml (404 Not Found)
        http://host.docker.internal:8080/login (200 OK)
WARN-NEW: Non-Storable Content [10049] x 6
        http://host.docker.internal:8080/admin (403 Forbidden)
        http://host.docker.internal:8080/echo?msg=Hello (200 OK)
        http://host.docker.internal:8080/files/secret.txt (200 OK)
        http://host.docker.internal:8080/robots.txt (404 Not Found)
        http://host.docker.internal:8080/script (404 Not Found)
WARN-NEW: Cookie without SameSite Attribute [10054] x 2
        http://host.docker.internal:8080 (200 OK)
        http://host.docker.internal:8080/ (200 OK)
WARN-NEW: Permissions Policy Header Not Set [10063] x 5
        http://host.docker.internal:8080/admin (403 Forbidden)
        http://host.docker.internal:8080/files/secret.txt (200 OK)
        http://host.docker.internal:8080/robots.txt (404 Not Found)
        http://host.docker.internal:8080/script (404 Not Found)
        http://host.docker.internal:8080/sitemap.xml (404 Not Found)
WARN-NEW: Source Code Disclosure - SQL [10099] x 1
        http://host.docker.internal:8080/search?username=admin (200 OK)
WARN-NEW: Authentication Request Identified [10111] x 1
        http://host.docker.internal:8080/login (200 OK)
WARN-NEW: Session Management Response Identified [10112] x 3
        http://host.docker.internal:8080 (200 OK)
        http://host.docker.internal:8080/ (200 OK)
        http://host.docker.internal:8080/ (200 OK)
WARN-NEW: Insufficient Site Isolation Against Spectre Vulnerability [90004] x 12
        http://host.docker.internal:8080/echo?msg=Hello (200 OK)
        http://host.docker.internal:8080/files/ (200 OK)
        http://host.docker.internal:8080/files/secret.txt (200 OK)
        http://host.docker.internal:8080/login (200 OK)
        http://host.docker.internal:8080/echo?msg=Hello (200 OK)
FAIL-NEW: 0     FAIL-INPROG: 0  WARN-NEW: 13    WARN-INPROG: 0  INFO: 0 IGNORE: 0       PASS: 54
[+] ZAP scan completed. Reports (if any) in /home/loltaun/course_labs/labs/lab08/dast/reports
-rw-r--r-- 1 loltaun loltaun 102K Jan 10 20:21 /home/loltaun/course_labs/labs/lab08/dast/reports/zap-report-20260110_202132.html
-rw-r--r-- 1 loltaun loltaun  38K Jan 10 20:21 /home/loltaun/course_labs/labs/lab08/dast/reports/zap-report-20260110_202132.json
-rw-r--r-- 1 loltaun loltaun  46K Jan 10 20:21 /home/loltaun/course_labs/labs/lab08/dast/reports/zap-report-20260110_202132.xml
[*] Converting JSON report to ODT/XLSX using /home/loltaun/course_labs/labs/lab08/dast/../venv/bin/python ...
[debug] python: /home/loltaun/course_labs/labs/lab08/venv/bin/python
[debug] odf imported OK
[*] Parsing ZAP JSON report: zap-report-20260110_202132.json
[i] Found 14 alerts
[+] ODT report saved: odt/zap-report-20260110_202132.odt
[+] XLSX report saved: xlsx/zap-report-20260110_202132.xlsx
[+] Report conversion completed!
```

- [x] 9. Изучите сгенерированные отчеты в `dast/reports` и опишите риски ИБ для них, без сценариев, так как ранее вы видели часть из их реализации

#### Medium
- Content Security Policy (CSP) Header Not Set может привести к расширенным векторам атаки XSS и подгрузке вредоносных ресурсов.
- Missing Anti-clickjacking Header (X-Frame-Options) может привести к риску кликджекинга и несанкционированных действий.
- Source Code Disclosure - SQL может привести к помощи атакующему в SQLi и обходах.

#### Low
- Cookie No HttpOnly Flag может привести к риску кражи сессии при XSS.
- Cookie without SameSite Attribute может привести к повышенному риску CSRF и утечки cookie кросс-домен.
- Insufficient Site Isolation Against Spectre может привести к риску межсайтового чтения данных в браузере.
- Permissions Policy Header Not Set может привести к избыточному доступу браузерных API (камера/геопозиция и т.п.).
- Server Leaks Version Information может привести к упрощению подбора известных уязвимостей.
- X-Content-Type-Options Header Missing (MIME-sniffing) может привести к риску XSS через подмену типа контента.

#### Info
- Authentication Request Identified может упростить таргетирование формы логина и подбор атак на аутентификацию.
- Information Disclosure in URL (GET) может привести к утечке данных в логах и реферерерах.
- Раскрытие внутренних IP/сетей в ответах может привести к оглашению топологии сети.

- [x] 10. Внесите исправления по данному отчету `DAST` для `vulnerable-app/app.py`
- [x] 11. Делайте все необходимые коммиты по шагам и отправляйте изменения в удаленный репозиторий
- Исправления Medium уязвимостей - ea25de4
- Исправления Low уязвимостей - d430b91
- Исправления Info уязвимостей - 8ebdc3a

- [x] 12. Подготовьте отчет `gist`.

Отчет - https://gist.github.com/LolTaun/c899cc230bf93c8a62eb91a712ec0cbb

- [x] 13. Почистите кеш от `venv` и остановите уязвимое приложение

```bash
$ deactivate
$ rm -rf venv
$ docker-compose -f docker-compose.yml down
$ docker system prune -f
```


***

Copyright (c) 2025 Denis Kuznetsov