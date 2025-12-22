<div align="center">
<h1><a id="intro">Лабораторная работа №6</a><br></h1>
<a href="https://docs.github.com/en"><img src="https://img.shields.io/static/v1?logo=github&logoColor=fff&label=&message=Docs&color=36393f&style=flat" alt="GitHub Docs"></a>
<a href="https://daringfireball.net/projects/markdown"><img src="https://img.shields.io/static/v1?logo=markdown&logoColor=fff&label=&message=Markdown&color=36393f&style=flat" alt="Markdown"></a> 
<a href="https://symbl.cc/en/unicode-table"><img src="https://img.shields.io/static/v1?logo=unicode&logoColor=fff&label=&message=Unicode&color=36393f&style=flat" alt="Unicode"></a> 
<a href="https://shields.io"><img src="https://img.shields.io/static/v1?logo=shieldsdotio&logoColor=fff&label=&message=Shields&color=36393f&style=flat" alt="Shields"></a>
<a href="https://img.shields.io/badge/Risk_Analyze-2448a2"><img src="https://img.shields.io/badge/Course-Risk_Analysis-2448a2" alt= "RA"></a> <img src="https://img.shields.io/badge/AppSec-2448a2" alt= "RA"></a> <img src="https://img.shields.io/badge/Contributor-Шмаков_И._С.-8b9aff" alt="Contributor Badge"></a></div>

***

## Задание

- [x] 1. Необходимо установить `Docker Engine` для Linux

```bash
$ sudo apt-get update
$ sudo apt-get install -y docker.io
$ sudo usermod -aG docker "$USER"

$ sudo systemctl start docker
$ docker pull docker/docker-bench-security
```

Был установлен ранее.

- [x] 2. Проверьте работу докера и сделать скрипт `audit.sh` исполняемым
```bash
loltaun@LT-New:~/course_labs/labs/lab06$ chmod +x audit.sh
```
- [x] 3. Развернуть уязвимое приложение как отдельные стенды

```bash
$ docker compose up -d # основной web, app, postgres
$ docker-compose -f vulnerable-app.yml up -d # поверх для vulnerable-web, debug-shell
    -f # file
    up # создает и поднимает файлы из compose
    -d # фоновый режим
```
Поднято

- [x] 4. Запустите скрипт из `venv` и проанализируйте то, что вывело на терминале и что вывело при конвертировании

```bash
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install openpyxl odfpy
$ ./audit.sh
$ deactivate # или $ deactivate 2>/dev/null || true
```
 
```bash
(venv) loltaun@LT-New:~/course_labs/labs/lab06$ ./audit.sh
Starting Docker CIS & Image Security Audit
==========================================
Detected platform: Linux
Using docker-bench-security image: docker/docker-bench-security:latest
Reports will be saved to: ./audit_reports/

Running Trivy scan for docker/docker-bench-security:latest...
2025-12-22T17:34:18+03:00       INFO    [vuln] Vulnerability scanning is enabled
2025-12-22T17:34:18+03:00       INFO    [secret] Secret scanning is enabled
2025-12-22T17:34:18+03:00       INFO    [secret] If your scanning is slow, please try '--scanners vuln' to disable secret scanning
2025-12-22T17:34:18+03:00       INFO    [secret] Please see https://trivy.dev/docs/v0.68/guide/scanner/secret#recommendation for faster secret detection
2025-12-22T17:34:18+03:00       INFO    Detected OS     family="alpine" version="3.8.2"
2025-12-22T17:34:18+03:00       INFO    [alpine] Detecting vulnerabilities...   os_version="3.8" repository="3.8" pkg_num=25
2025-12-22T17:34:18+03:00       INFO    Number of language-specific files       num=0
2025-12-22T17:34:18+03:00       WARN    This OS version is no longer supported by the distribution      family="alpine" version="3.8.2"
2025-12-22T17:34:18+03:00       WARN    The vulnerability detection may be insufficient because security updates are not provided
Saved to: ./audit_reports/json/docker-bench-security-trivy.json

Scanning lab images for vulnerabilities...

=== Trivy scan for nginx:alpine ===
2025-12-22T17:34:18+03:00       INFO    [vuln] Vulnerability scanning is enabled
2025-12-22T17:34:18+03:00       INFO    [secret] Secret scanning is enabled
2025-12-22T17:34:18+03:00       INFO    [secret] If your scanning is slow, please try '--scanners vuln' to disable secret scanning
2025-12-22T17:34:18+03:00       INFO    [secret] Please see https://trivy.dev/docs/v0.68/guide/scanner/secret#recommendation for faster secret detection
2025-12-22T17:34:18+03:00       INFO    Detected OS     family="alpine" version="3.23.2"
2025-12-22T17:34:18+03:00       WARN    This OS version is not on the EOL list  family="alpine" version="3.23"
2025-12-22T17:34:18+03:00       INFO    [alpine] Detecting vulnerabilities...   os_version="3.23" repository="3.23" pkg_num=71
2025-12-22T17:34:18+03:00       INFO    Number of language-specific files       num=0
Saved to: ./audit_reports/json/nginx-alpine-trivy.json

=== Trivy scan for python:3.11-alpine ===
2025-12-22T17:34:18+03:00       INFO    [vuln] Vulnerability scanning is enabled
2025-12-22T17:34:18+03:00       INFO    [secret] Secret scanning is enabled
2025-12-22T17:34:18+03:00       INFO    [secret] If your scanning is slow, please try '--scanners vuln' to disable secret scanning
2025-12-22T17:34:18+03:00       INFO    [secret] Please see https://trivy.dev/docs/v0.68/guide/scanner/secret#recommendation for faster secret detection
2025-12-22T17:34:18+03:00       INFO    Detected OS     family="alpine" version="3.23.2"
2025-12-22T17:34:18+03:00       WARN    This OS version is not on the EOL list  family="alpine" version="3.23"
2025-12-22T17:34:18+03:00       INFO    [alpine] Detecting vulnerabilities...   os_version="3.23" repository="3.23" pkg_num=38
2025-12-22T17:34:18+03:00       INFO    Number of language-specific files       num=1
2025-12-22T17:34:18+03:00       INFO    [python-pkg] Detecting vulnerabilities...
Saved to: ./audit_reports/json/python-3.11-alpine-trivy.json

=== Trivy scan for postgres:16-alpine ===
2025-12-22T17:34:18+03:00       INFO    [vuln] Vulnerability scanning is enabled
2025-12-22T17:34:18+03:00       INFO    [secret] Secret scanning is enabled
2025-12-22T17:34:18+03:00       INFO    [secret] If your scanning is slow, please try '--scanners vuln' to disable secret scanning
2025-12-22T17:34:18+03:00       INFO    [secret] Please see https://trivy.dev/docs/v0.68/guide/scanner/secret#recommendation for faster secret detection
2025-12-22T17:34:18+03:00       INFO    Detected OS     family="alpine" version="3.23.2"
2025-12-22T17:34:18+03:00       WARN    This OS version is not on the EOL list  family="alpine" version="3.23"
2025-12-22T17:34:18+03:00       INFO    [alpine] Detecting vulnerabilities...   os_version="3.23" repository="3.23" pkg_num=45
2025-12-22T17:34:18+03:00       INFO    Number of language-specific files       num=1
2025-12-22T17:34:18+03:00       INFO    [gobinary] Detecting vulnerabilities...
2025-12-22T17:34:18+03:00       WARN    Using severities from other vendors for some vulnerabilities. Read https://trivy.dev/docs/v0.68/guide/scanner/vulnerability#severity-selection for details.
Saved to: ./audit_reports/json/postgres-16-alpine-trivy.json

Linux host detected – configuring mounts for CIS Docker Benchmark coverage

Mounting /usr/lib/systemd
Mounting /var/log
Running Docker Bench Security container (CIS host audit)

# ------------------------------------------------------------------------------
# Docker Bench for Security v1.3.4
#
# Docker, Inc. (c) 2015-
#
# Checks for dozens of common best-practices around deploying Docker containers in production.
# Inspired by the CIS Docker Community Edition Benchmark v1.1.0.
# ------------------------------------------------------------------------------

Initializing Mon Dec 22 14:34:18 UTC 2025


[INFO] 1 - Host Configuration
[WARN] 1.1  - Ensure a separate partition for containers has been created
[NOTE] 1.2  - Ensure the container host has been Hardened
[PASS] 1.3  - Ensure Docker is up to date
[INFO]      * Using 28.5.1 which is current
[INFO]      * Check with your operating system vendor for support and security maintenance for Docker
[INFO] 1.4  - Ensure only trusted users are allowed to control Docker daemon
[INFO]      * docker:x:1001:loltaun
[WARN] 1.5  - Ensure auditing is configured for the Docker daemon
[INFO] 1.6  - Ensure auditing is configured for Docker files and directories - /var/lib/docker
[INFO]      * Directory not found
[INFO] 1.7  - Ensure auditing is configured for Docker files and directories - /etc/docker
[INFO]      * Directory not found
[INFO] 1.8  - Ensure auditing is configured for Docker files and directories - docker.service
[INFO]      * File not found
[INFO] 1.9  - Ensure auditing is configured for Docker files and directories - docker.socket
[INFO]      * File not found
[INFO] 1.10  - Ensure auditing is configured for Docker files and directories - /etc/default/docker
[INFO]      * File not found
[INFO] 1.11  - Ensure auditing is configured for Docker files and directories - /etc/docker/daemon.json
[INFO]      * File not found
[INFO] 1.12  - Ensure auditing is configured for Docker files and directories - /usr/bin/docker-containerd
[INFO]      * File not found
[INFO] 1.13  - Ensure auditing is configured for Docker files and directories - /usr/bin/docker-runc
[INFO]      * File not found


[INFO] 2 - Docker daemon configuration
[WARN] 2.1  - Ensure network traffic is restricted between containers on the default bridge
[PASS] 2.2  - Ensure the logging level is set to 'info'
[PASS] 2.3  - Ensure Docker is allowed to make changes to iptables
[PASS] 2.4  - Ensure insecure registries are not used
[PASS] 2.5  - Ensure aufs storage driver is not used
[WARN] 2.6  - Ensure TLS authentication for Docker daemon is configured
[WARN]      * Docker daemon currently listening on TCP without TLS
[INFO] 2.7  - Ensure the default ulimit is configured appropriately
[INFO]      * Default ulimit doesn't appear to be set
[WARN] 2.8  - Enable user namespace support
[PASS] 2.9  - Ensure the default cgroup usage has been confirmed
[PASS] 2.10  - Ensure base device size is not changed until needed
[WARN] 2.11  - Ensure that authorization for Docker client commands is enabled
[WARN] 2.12  - Ensure centralized and remote logging is configured
[INFO] 2.13  - Ensure operations on legacy registry (v1) are Disabled (Deprecated)
[PASS] 2.14  - Ensure live restore is Enabled (Incompatible with swarm mode)
[WARN] 2.15  - Ensure Userland Proxy is Disabled
[INFO] 2.16  - Ensure daemon-wide custom seccomp profile is applied, if needed
[PASS] 2.17  - Ensure experimental features are avoided in production
[WARN] 2.18  - Ensure containers are restricted from acquiring new privileges


[INFO] 3 - Docker daemon configuration files
[INFO] 3.1  - Ensure that docker.service file ownership is set to root:root
[INFO]      * File not found
[INFO] 3.2  - Ensure that docker.service file permissions are set to 644 or more restrictive
[INFO]      * File not found
[INFO] 3.3  - Ensure that docker.socket file ownership is set to root:root
[INFO]      * File not found
[INFO] 3.4  - Ensure that docker.socket file permissions are set to 644 or more restrictive
[INFO]      * File not found
[INFO] 3.5  - Ensure that /etc/docker directory ownership is set to root:root
[INFO]      * Directory not found
[INFO] 3.6  - Ensure that /etc/docker directory permissions are set to 755 or more restrictive
[INFO]      * Directory not found
[INFO] 3.7  - Ensure that registry certificate file ownership is set to root:root
[INFO]      * Directory not found
[INFO] 3.8  - Ensure that registry certificate file permissions are set to 444 or more restrictive
[INFO]      * Directory not found
[INFO] 3.9  - Ensure that TLS CA certificate file ownership is set to root:root
[INFO]      * No TLS CA certificate found
[INFO] 3.10  - Ensure that TLS CA certificate file permissions are set to 444 or more restrictive
[INFO]      * No TLS CA certificate found
[INFO] 3.11  - Ensure that Docker server certificate file ownership is set to root:root
[INFO]      * No TLS Server certificate found
[INFO] 3.12  - Ensure that Docker server certificate file permissions are set to 444 or more restrictive
[INFO]      * No TLS Server certificate found
[INFO] 3.13  - Ensure that Docker server certificate key file ownership is set to root:root
[INFO]      * No TLS Key found
[INFO] 3.14  - Ensure that Docker server certificate key file permissions are set to 400
[INFO]      * No TLS Key found
[PASS] 3.15  - Ensure that Docker socket file ownership is set to root:docker
[PASS] 3.16  - Ensure that Docker socket file permissions are set to 660 or more restrictive
[INFO] 3.17  - Ensure that daemon.json file ownership is set to root:root
[INFO]      * File not found
[INFO] 3.18  - Ensure that daemon.json file permissions are set to 644 or more restrictive
[INFO]      * File not found
[INFO] 3.19  - Ensure that /etc/default/docker file ownership is set to root:root
[INFO]      * File not found
[INFO] 3.20  - Ensure that /etc/default/docker file permissions are set to 644 or more restrictive
[INFO]      * File not found


[INFO] 4 - Container Images and Build File
[WARN] 4.1  - Ensure a user for the container has been created
[WARN]      * Running as root: registry.1.ux6q3c95n42tue0b9xirrkrwg
[NOTE] 4.2  - Ensure that containers use trusted base images
[NOTE] 4.3  - Ensure unnecessary packages are not installed in the container
[NOTE] 4.4  - Ensure images are scanned and rebuilt to include security patches
[WARN] 4.5  - Ensure Content trust for Docker is Enabled
[WARN] 4.6  - Ensure HEALTHCHECK instructions have been added to the container image
[WARN]      * No Healthcheck found: [course_lab1-hello:latest]
[WARN]      * No Healthcheck found: [lab05-server:latest]
[WARN]      * No Healthcheck found: [lab05-client:latest]
[WARN]      * No Healthcheck found: [nginx:alpine]
[WARN]      * No Healthcheck found: [python:3.11-alpine]
[WARN]      * No Healthcheck found: [postgres:16-alpine]
[WARN]      * No Healthcheck found: [alpine:latest]
[WARN]      * No Healthcheck found: [my-hello-appsec:latest]
[WARN]      * No Healthcheck found: [hellow-appsec-world:latest]
[WARN]      * No Healthcheck found: [LolTaun/hello-appsec-world:latest hello-appsec-world:latest loltaun/hello-appsec-world:latest]
[WARN]      * No Healthcheck found: [LolTaun/hello-appsec-world:latest hello-appsec-world:latest loltaun/hello-appsec-world:latest]
[WARN]      * No Healthcheck found: [ghcr.io/digininja/dvwa:latest]
[WARN]      * No Healthcheck found: [hadoop/submit:3.4.2]
[WARN]      * No Healthcheck found: [nginx:latest]
[WARN]      * No Healthcheck found: [hadoop/basic:3.4.2]
[WARN]      * No Healthcheck found: [jupyterlab/core:4.4.9]
[WARN]      * No Healthcheck found: [spark/core:3.5.7]
[WARN]      * No Healthcheck found: [127.0.0.1:5000/mpi:latest@sha256:7c4617d46f34f515c97cc84b060fa24b22142970c76dadc250d5552c4e330c2e]
[WARN]      * No Healthcheck found: [127.0.0.1:5000/mpi:latest]
[WARN]      * No Healthcheck found: [mariadb:10]
[WARN]      * No Healthcheck found: [structurizr/onpremises:latest]
[WARN]      * No Healthcheck found: [ubuntu:latest]
[WARN]      * No Healthcheck found: [voice_recognizer-asr:latest]
[WARN]      * No Healthcheck found: [registry:2@sha256:a3d8aaa63ed8681a604f1dea0aa03f100d5895b6a58ace528858a7b332415373]
[INFO] 4.7  - Ensure update instructions are not use alone in the Dockerfile
[INFO]      * Update instruction found: [course_lab1-hello:latest]
[INFO]      * Update instruction found: [lab05-server:latest]
[INFO]      * Update instruction found: [lab05-client:latest]
[INFO]      * Update instruction found: [my-hello-appsec:latest]
[INFO]      * Update instruction found: [hellow-appsec-world:latest]
[INFO]      * Update instruction found: [LolTaun/hello-appsec-world:latest hello-appsec-world:latest loltaun/hello-appsec-world:latest]
[INFO]      * Update instruction found: [LolTaun/hello-appsec-world:latest hello-appsec-world:latest loltaun/hello-appsec-world:latest]
[INFO]      * Update instruction found: [ghcr.io/digininja/dvwa:latest]
[INFO]      * Update instruction found: [hadoop/submit:3.4.2]
[INFO]      * Update instruction found: [hadoop/historyserver:3.4.2]
[INFO]      * Update instruction found: [hadoop/nodemanager:3.4.2]
[INFO]      * Update instruction found: [hadoop/resourcemanager:3.4.2]
[INFO]      * Update instruction found: [hadoop/datanode:3.4.2]
[INFO]      * Update instruction found: [hadoop/namenode:3.4.2]
[INFO]      * Update instruction found: [hadoop/basic:3.4.2]
[INFO]      * Update instruction found: [jupyterlab/core:4.4.9]
[INFO]      * Update instruction found: [spark/core:3.5.7]
[INFO]      * Update instruction found: [structurizr/onpremises:latest]
[INFO]      * Update instruction found: [structurizr/lite:latest]
[INFO]      * Update instruction found: [voice_recognizer-asr:latest]
[NOTE] 4.8  - Ensure setuid and setgid permissions are removed in the images
[INFO] 4.9  - Ensure COPY is used instead of ADD in Dockerfile
[INFO]      * ADD in image history: [nginx:alpine]
[INFO]      * ADD in image history: [python:3.11-alpine]
[INFO]      * ADD in image history: [postgres:16-alpine]
[INFO]      * ADD in image history: [alpine:latest]
[INFO]      * ADD in image history: [hadoop/submit:3.4.2]
[INFO]      * ADD in image history: [hadoop/historyserver:3.4.2]
[INFO]      * ADD in image history: [hadoop/nodemanager:3.4.2]
[INFO]      * ADD in image history: [hadoop/resourcemanager:3.4.2]
[INFO]      * ADD in image history: [hadoop/datanode:3.4.2]
[INFO]      * ADD in image history: [hadoop/namenode:3.4.2]
[INFO]      * ADD in image history: [hadoop/basic:3.4.2]
[INFO]      * ADD in image history: [jupyterlab/core:4.4.9]
[INFO]      * ADD in image history: [spark/core:3.5.7]
[INFO]      * ADD in image history: [127.0.0.1:5000/mpi:latest@sha256:7c4617d46f34f515c97cc84b060fa24b22142970c76dadc250d5552c4e330c2e]
[INFO]      * ADD in image history: [127.0.0.1:5000/mpi:latest]
[INFO]      * ADD in image history: [mariadb:10]
[INFO]      * ADD in image history: [structurizr/onpremises:latest]
[INFO]      * ADD in image history: [structurizr/lite:latest]
[INFO]      * ADD in image history: [ubuntu:latest]
[INFO]      * ADD in image history: [registry:2@sha256:a3d8aaa63ed8681a604f1dea0aa03f100d5895b6a58ace528858a7b332415373]
[INFO]      * ADD in image history: [docker/docker-bench-security:latest]
[NOTE] 4.10  - Ensure secrets are not stored in Dockerfiles
[NOTE] 4.11  - Ensure verified packages are only Installed


[INFO] 5 - Container Runtime
[WARN] 5.1  - Ensure AppArmor Profile is Enabled
[WARN]      * No AppArmorProfile Found: vulnerable-web
[WARN]      * No AppArmorProfile Found: registry.1.ux6q3c95n42tue0b9xirrkrwg
[WARN] 5.2  - Ensure SELinux security options are set, if applicable
[WARN]      * No SecurityOptions Found: registry.1.ux6q3c95n42tue0b9xirrkrwg
[WARN] 5.3  - Ensure Linux Kernel Capabilities are restricted within containers
[WARN]      * Capabilities added: CapAdd=[ALL] to vulnerable-web
[WARN] 5.4  - Ensure privileged containers are not used
[WARN]      * Container running in Privileged mode: vulnerable-web
[PASS] 5.5  - Ensure sensitive host system directories are not mounted on containers
[PASS] 5.6  - Ensure ssh is not run within containers
[PASS] 5.7  - Ensure privileged ports are not mapped within containers
[NOTE] 5.8  - Ensure only needed ports are open on the container
[WARN] 5.9  - Ensure the host's network namespace is not shared
[WARN]      * Container running with networking mode 'host': vulnerable-web
[WARN] 5.10  - Ensure memory usage for container is limited
[WARN]      * Container running without memory restrictions: vulnerable-web
[WARN]      * Container running without memory restrictions: registry.1.ux6q3c95n42tue0b9xirrkrwg
[WARN] 5.11  - Ensure CPU priority is set appropriately on the container
[WARN]      * Container running without CPU restrictions: vulnerable-web
[WARN]      * Container running without CPU restrictions: registry.1.ux6q3c95n42tue0b9xirrkrwg
[WARN] 5.12  - Ensure the container's root filesystem is mounted as read only
[WARN]      * Container running with root FS mounted R/W: vulnerable-web
[WARN]      * Container running with root FS mounted R/W: registry.1.ux6q3c95n42tue0b9xirrkrwg
[PASS] 5.13  - Ensure incoming container traffic is binded to a specific host interface
[WARN] 5.14  - Ensure 'on-failure' container restart policy is set to '5'
[WARN]      * MaximumRetryCount is not set to 5: vulnerable-web
[WARN]      * MaximumRetryCount is not set to 5: registry.1.ux6q3c95n42tue0b9xirrkrwg
[WARN] 5.15  - Ensure the host's process namespace is not shared
[WARN]      * Host PID namespace being shared with: vulnerable-web
[PASS] 5.16  - Ensure the host's IPC namespace is not shared
[PASS] 5.17  - Ensure host devices are not directly exposed to containers
[INFO] 5.18  - Ensure the default ulimit is overwritten at runtime, only if needed
[INFO]      * Container no default ulimit override: vulnerable-web
[INFO]      * Container no default ulimit override: registry.1.ux6q3c95n42tue0b9xirrkrwg
[PASS] 5.19  - Ensure mount propagation mode is not set to shared
[PASS] 5.20  - Ensure the host's UTS namespace is not shared
[WARN] 5.21  - Ensure the default seccomp profile is not Disabled
[WARN]      * Default seccomp profile disabled: vulnerable-web
[NOTE] 5.22  - Ensure docker exec commands are not used with privileged option
[NOTE] 5.23  - Ensure docker exec commands are not used with user option
[PASS] 5.24  - Ensure cgroup usage is confirmed
[WARN] 5.25  - Ensure the container is restricted from acquiring additional privileges
[WARN]      * Privileges not restricted: vulnerable-web
[WARN]      * Privileges not restricted: registry.1.ux6q3c95n42tue0b9xirrkrwg
[WARN] 5.26  - Ensure container health is checked at runtime
[WARN]      * Health check not set: vulnerable-web
[WARN]      * Health check not set: registry.1.ux6q3c95n42tue0b9xirrkrwg
[INFO] 5.27  - Ensure docker commands always get the latest version of the image
[WARN] 5.28  - Ensure PIDs cgroup limit is used
[WARN]      * PIDs limit not set: vulnerable-web
[WARN]      * PIDs limit not set: registry.1.ux6q3c95n42tue0b9xirrkrwg
[PASS] 5.29  - Ensure Docker's default bridge docker0 is not used
[PASS] 5.30  - Ensure the host's user namespaces is not shared
[WARN] 5.31  - Ensure the Docker socket is not mounted inside any containers
[WARN]      * Docker socket shared: vulnerable-web


[INFO] 6 - Docker Security Operations
[INFO] 6.1  - Avoid image sprawl
[INFO]      * There are currently: 33 images
[INFO] 6.2  - Avoid container sprawl
[INFO]      * There are currently a total of 30 containers, with only 3 of them currently running


[INFO] 7 - Docker Swarm Configuration
[WARN] 7.1  - Ensure swarm mode is not Enabled, if not needed
[PASS] 7.2  - Ensure the minimum number of manager nodes have been created in a swarm
[WARN] 7.3  - Ensure swarm services are binded to a specific host interface
[WARN] 7.4  - Ensure data exchanged between containers are encrypted on different nodes on the overlay network
[WARN]      * Unencrypted overlay network: ingress (swarm)
[INFO] 7.5  - Ensure Docker's secret management commands are used for managing secrets in a Swarm cluster
[WARN] 7.6  - Ensure swarm manager is run in auto-lock mode
[NOTE] 7.7  - Ensure swarm manager auto-lock key is rotated periodically
[INFO] 7.8  - Ensure node certificates are rotated as appropriate
[INFO] 7.9  - Ensure CA certificates are rotated as appropriate
[INFO] 7.10  - Ensure management plane traffic has been separated from data plane traffic

[INFO] Checks: 105
[INFO] Score: -9

CIS audit output saved to: ./audit_reports/text/docker-bench-security-cis.txt

Converting Trivy JSON reports to XLSX/ODT formats...
✓ Saved to XLSX: ./audit_reports/xlsx/postgres-16-alpine-trivy.xlsx
✓ Saved to ODT: ./audit_reports/odt/postgres-16-alpine-trivy.odt
✓ Saved to XLSX: ./audit_reports/xlsx/docker-bench-security-trivy.xlsx
✓ Saved to ODT: ./audit_reports/odt/docker-bench-security-trivy.odt
✓ Saved to XLSX: ./audit_reports/xlsx/nginx-alpine-trivy.xlsx
✓ Saved to ODT: ./audit_reports/odt/nginx-alpine-trivy.odt
✓ Saved to XLSX: ./audit_reports/xlsx/python-3.11-alpine-trivy.xlsx
✓ Saved to ODT: ./audit_reports/odt/python-3.11-alpine-trivy.odt

==========================================
Audit complete!
Reports directory structure:
   ./audit_reports/
   ├── json/          (Trivy JSON outputs)
   ├── text/          (CIS audit text outputs)
   ├── xlsx/          (Excel spreadsheets)
   └── odt/           (OpenDocument Text files)

For CIS Docker Benchmark details, see:
https://www.cisecurity.org/benchmark/docker

```

- [x] 5. Проведите анализ уязвимостей, опишите их причину возникновения
- Хост: нет аудита /var/lib/docker и /etc/docker, TLS на TCP демона отсутствует, user namespace не включён, централизованный логгинг не настроен, authz для клиентских команд выключен, userland-proxy не отключён, seccomp по умолчанию отключён, AppArmor/SELinux не применён, лимиты CPU/MEM/PIDs отсутствуют, privileged/host network/host PID/ALL capabilities у vulnerable-web.

- Образы (Trivy):
docker/docker-bench-security: базовый alpine 3.8 EOL → потенциальные unpatched CVE.
    - nginx:alpine, python:3.11-alpine, postgres:16-alpine: свежий alpine 3.23, но есть уязвимые пакеты (см. xlsx/odt отчёты), healthcheck отсутствует.
    - Собственные образы (lab05-server/client, my-hello-appsec, hello-appsec-world): нет healthcheck, есть одиночные RUN update, отсутствие пользователя в контейнере.

- Контейнеры runtime:
    - vulnerable-web: privileged, host network, host PID, cap_add=ALL, без seccomp/AppArmor/ulimits/memory/CPU/PIDs лимитов, rw rootfs, нет healthcheck.
    - registry.1.*: без seccomp/AppArmor/ulimits, нет healthcheck, rw rootfs, нет ограничений CPU/MEM/PIDs.

- [x] 6. Опишите влияния уязвимостей, их сценарий атаки
- TLS/без authz на демоне: перехват/подмена трафика к API докера → удалённый root-доступ к контейнерам/хосту (supply-chain, lateral movement).
- Нет user namespace/нет аудита путей докера: утечки UID 0 из контейнера на хост; сложнее расследовать инциденты.
- Privileged + cap_add=ALL + host network/PID (vulnerable-web): побег из контейнера через /proc, загрузка модулей, доступ к хост-сокетам и сетевым интерфейсам; sniffing/DoS/миграция на хост.
- RW rootfs + без лимитов CPU/MEM/PIDs: устойчивая запись малвари, майнинг/DoS контейнером или любым RCE внутри.
- Нет seccomp/AppArmor/SELinux: расширенная поверхность системных вызовов → эксплуатация kernel/RCE/контейнер escape.
- Нет healthcheck и restart policy on-failure=5: тихий отказ сервисов, отсутствие авто-восстановления → отказ в обслуживании.
- EOL базовый образ (alpine 3.8) и уязвимые пакеты (Trivy): использование известных CVE для RCE/priv-esc в контейнере, затем цепочка до хоста.
- Одиночные RUN update и отсутствие pinned версий: дрейф зависимостей, воспроизводимость и непредсказуемые CVE.
- Нет отдельного пользователя в образах: процессы под root внутри → при escape совпадает с root хоста.
- Нет централизованного логирования: трудности обнаружения/реагирования.

- [x] 7. Оцените риски ИБ и предложите меры для их снижения: 
> Следует разобрать `.yaml` описав, что в них считается не безопасным и почему
> Опишите сценарии реализации рисков CR, DL
> Предложили исправленные `.yaml`

**Разбор `.yaml` (почему небезопасно):**
- vulnerable-app.yml: privileged+cap_add=ALL, network_mode/pid host, монтирование `/` и docker.sock, seccomp/apparmor unconfined, root-пользователь, RW конфиги и backup, секреты в env, нет healthcheck/лимитов.
- labs/lab06/docker-compose.yml: секреты и `DEBUG=true` в env, слабые пароли, публичные образы без пина, нет healthcheck/лимитов/ротации логов, RW volume для кода.

**Сценарии рисков (CR, DL):**
- CR: через смонтированный docker.sock или host PID/NET контейнер получает root-доступ к хосту и управляющим сокетам; возможна подмена образов и побег в хост.
- DL: монтирование `/` и открытые креды позволяют вычитать конфиги/базы, перехватывать трафик на host network и утянуть секреты из backup/ENV.

**Исправленные `.yaml` (пример):**
```yaml
# vulnerable-app.yml
version: "3.8"
services:
    vulnerable-web:
        image: nginx:alpine
        container_name: vulnerable-web
        user: "101:101"
        ports:
            - "8081:80"
        volumes:
            - ./config/nginx.conf:/etc/nginx/nginx.conf:ro
            - ./backup:/var/backups:ro
        cap_drop: [ALL]
        security_opt:
            - no-new-privileges:true
        read_only: true
        tmpfs:
            - /var/cache/nginx
            - /run
        healthcheck:
            test: ["CMD", "wget", "-q", "http://127.0.0.1", "-O", "-"]
            interval: 30s
            timeout: 3s
            retries: 3
        restart: on-failure:5
        environment:
            - DB_HOST=db
            - DB_USER_FILE=/run/secrets/db_user
            - DB_PASSWORD_FILE=/run/secrets/db_password
        secrets:
            - db_user
            - db_password

    debug-shell:
        image: alpine:latest
        container_name: debug-shell
        user: "1000:1000"
        network_mode: bridge
        cap_drop: [ALL]
        security_opt:
            - no-new-privileges:true
        command: ["sleep", "infinity"]
        restart: on-failure:3

secrets:
    db_user:
        file: ./secrets/db_user.txt
    db_password:
        file: ./secrets/db_password.txt
```

```yaml
# docker-compose.yml
version: '3.8'
services:
    vulnerable-web:
        image: nginx:alpine@sha256:<pin>
        container_name: vulnerable-nginx
        depends_on: [insecure-db, app]
        ports: ["8080:80"]
        volumes:
            - ./config/nginx.conf:/etc/nginx/nginx.conf:ro
        user: "101:101"
        security_opt: [no-new-privileges:true]
        read_only: true
        tmpfs: [/var/cache/nginx, /run]
        healthcheck:
            test: ["CMD", "wget", "-q", "http://127.0.0.1", "-O", "-"]
            interval: 30s
            retries: 3
        restart: on-failure:5

    insecure-db:
        image: postgres:16-alpine@sha256:<pin>
        environment:
            - POSTGRES_PASSWORD_FILE=/run/secrets/db_password
            - POSTGRES_DB=vulnapp
            - POSTGRES_USER=vulnuser
        secrets: [db_password]
        volumes:
            - ./db/init.sql:/docker-entrypoint-initdb.d/init.sql:ro
        healthcheck:
            test: ["CMD-SHELL", "pg_isready -U vulnuser"]
            interval: 30s
            retries: 5
        restart: on-failure:5

    app:
        image: python:3.11-alpine@sha256:<pin>
        working_dir: /app
        volumes:
            - ./app:/app:ro
        command: ["python", "app.py"]
        environment:
            - APP_SECRET_KEY_FILE=/run/secrets/app_key
            - DB_URL=postgresql://vulnuser:@insecure-db:5432/vulnapp
            - DEBUG=false
        secrets: [app_key]
        healthcheck:
            test: ["CMD", "wget", "-q", "http://127.0.0.1:5000/health", "-O", "-"]
            interval: 30s
            retries: 3
        restart: on-failure:5

secrets:
    db_password:
        file: ./secrets/db_password.txt
    app_key:
        file: ./secrets/app_key.txt
```

Главные меры: убрать privileged/host network/pid и docker.sock, переключиться на non-root + no-new-privileges, включить healthcheck/restart, использовать secrets вместо ENV, пиновать образы, задавать read-only rootfs и tmpfs для данных.

- [ ] 8. Сделайте анализ уязвимостей из сгенерированных файлов .odt, .xslx и опишите их в отчете. Файлы конвертируются в эти директории

Краткий разбор по отчетам Trivy (xlsx/odt):
- docker/docker-bench-security (alpine 3.8 EOL): множество устаревших пакетов без патчей; использовать поддерживаемый базовый образ. Отчеты: [labs/lab06/audit_reports/xlsx/docker-bench-security-trivy.xlsx](labs/lab06/audit_reports/xlsx/docker-bench-security-trivy.xlsx), [labs/lab06/audit_reports/odt/docker-bench-security-trivy.odt](labs/lab06/audit_reports/odt/docker-bench-security-trivy.odt).
- nginx:alpine (3.23): присутствуют уязвимости средней/высокой важности в базовых библиотеках Alpine; планово обновлять образ до свежего минорного релиза и пересобирать. Отчеты: [audit_reports/xlsx/nginx-alpine-trivy.xlsx](audit_reports/xlsx/nginx-alpine-trivy.xlsx), [audit_reports/odt/nginx-alpine-trivy.odt](audit_reports/odt/nginx-alpine-trivy.odt).
- python:3.11-alpine (3.23): уязвимости в системных пакетах и питон-зависимостях; требуется обновление образа и зависимостей, пиновать версии. Отчеты: [audit_reports/xlsx/python-3.11-alpine-trivy.xlsx](audit_reports/xlsx/python-3.11-alpine-trivy.xlsx), [audit_reports/odt/python-3.11-alpine-trivy.odt](audit_reports/odt/python-3.11-alpine-trivy.odt).
- postgres:16-alpine (3.23): найденные CVE в базовых библиотеках и исполняемых файлах; обновить образ до последнего патча и пересобрать. Отчеты: [audit_reports/xlsx/postgres-16-alpine-trivy.xlsx](audit_reports/xlsx/postgres-16-alpine-trivy.xlsx), [audit_reports/odt/postgres-16-alpine-trivy.odt](audit_reports/odt/postgres-16-alpine-trivy.odt).

Главные выводы из отчетов: обновлять базовые образы до актуальных патчей, избегать старые версии ОС (alpine 3.8), пересобрать собственные образы после фиксов, добавить healthcheck и non-root пользователей.

```bash
"├── json/          (Trivy JSON outputs)"
"├── text/          (CIS audit text outputs)"
"├── xlsx/          (Excel spreadsheets)"
"└── odt/           (OpenDocument Text files)"
```

- [ ] 9. Подготовьте отчет `gist`.
Это он и есть ;)
- [ ] 10. Почистите кеш от `venv` и остановите уязвимостей приложение, почистите контейнера

```bash
$ rm -rf venv
$ docker-compose -f demo-vulnerable-app.yml down
$ docker system prune -f
```
 
***

## Troobleshooting

- Права для исполнения скрипта

```bash
$ chmod +x xxx.sh # разрешение прав при permission denied
```

- На macOS/AArch64 docker-bench-security может не запускаться из‑за ограничений Docker Desktop и это работает для Linux‑VM. На Mac используем Trivy‑скан и разбор конфигурации compose‑файлов.


***

Copyright (c) 2025 Denis Kuznetsov