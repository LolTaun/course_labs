<div align="center">
<h1><a id="intro">Лабораторная работа №7</a><br></h1>
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
$ pip install -r vulnerable-app/requirements.txt
```

- [x] 2. Запустите уязвимое приложение

```bash
$ docker-compose -f docker-compose.yml up -d --build # http://localhost:8080
```

- [x] 3. Запустите SAST Semgrep и проанализируйте выведенный лог в консоли и опишите логику правил для `semgrep-rules.yml` исходя из паттернов, которые используются. Отчет будет в директории SAST

```bash
(venv) loltaun@LT-New:~/course_labs/labs/lab07$ semgrep --config sast/semgrep-rules.yml \
  --json \
  --output sast/semgrep-report.json \
  vulnerable-app/

┌──── ○○○ ────┐
│ Semgrep CLI │
└─────────────┘

...

┌──────────────┐
│ Scan Summary │
└──────────────┘
✅ Scan completed successfully.
 • Findings: 5 (5 blocking)
 • Rules run: 16
 • Targets scanned: 2
 • Parsed lines: ~100.0%
 • Scan was limited to files tracked by git
 • For a detailed list of skipped files and lines, run semgrep with the --verbose flag
Ran 16 rules on 2 files: 5 findings.
```

- [x] 4. Запустите SAST Checkov по Dockerfile, compose и проанализируйте выведенный лог в консоли и опишите логику правил для `checkov-config.yaml` по `Docker`. Отчет будет в директории SAST

Логика правил `checkov-config.yaml` по Docker:
Набор настроек ограничивает запуск Checkov только на Docker/Helm и включает только выбранные проверки (run_all_checks: false). В секции enforce.docker перечислены политики, которые должны проверяться:
- CKV_DOCKER_2 / CKV_DOCKER_8: контейнер должен стартовать не под root, пользователь явно задан.
- CKV_DOCKER_3 / CKV_DOCKER_9: минимизировать лишние пакеты/- слои и уменьшать attack surface.
- CKV_DOCKER_5: не использовать тег latest без необходимости.
- CKV_DOCKER_7: не применять ADD, предпочитать COPY.
- CKV_DOCKER_10: обязателен HEALTHCHECK.
- CKV_DOCKER_12: не хранить секреты в ENV.
- CKV_DOCKER_13: запрет привилегированного режима.
- CKV_DOCKER_14: ограничивать Linux capabilities.
- CKV_DOCKER_16: root FS по возможности read-only.


```bash
(venv) loltaun@LT-New:~/course_labs/labs/lab07$ checkov   --framework dockerfile   --file vulnerable-app/Dockerfile docker-compose.yml   --output json   --output-file-path sast/checkov-report.json   --soft-fail
2026-01-09 19:58:52,462 [MainThread  ] [WARNI]  /home/loltaun/course_labs/labs/lab07/venv/lib/python3.12/site-packages/paramiko/pkey.py:59: CryptographyDeprecationWarning: TripleDES has been moved to cryptography.hazmat.decrepit.ciphers.algorithms.TripleDES and will be removed from cryptography.hazmat.primitives.ciphers.algorithms in 48.0.0.
  'cipher': algorithms.TripleDES,

2026-01-09 19:58:52,480 [MainThread  ] [WARNI]  /home/loltaun/course_labs/labs/lab07/venv/lib/python3.12/site-packages/paramiko/transport.py:193: CryptographyDeprecationWarning: TripleDES has been moved to cryptography.hazmat.decrepit.ciphers.algorithms.TripleDES and will be removed from cryptography.hazmat.primitives.ciphers.algorithms in 48.0.0.
  'class': algorithms.TripleDES,

[ dockerfile framework ]: 100%|████████████████████|[1/1], Current File Scanned=vulnerable-app/Dockerfile
{
    "check_type": "dockerfile",
    "results": {

    ...

    "summary": {
        "passed": 50,
        "failed": 2,
        "skipped": 0,
        "parsing_errors": 0,
        "resource_count": 1,
        "checkov_version": "3.2.497"
    },
    "url": "Add an api key '--bc-api-key <api-key>' to see more detailed insights via https://bridgecrew.cloud"
}
```



- [x] 5. Подготовка зависимостей Java и Maven‑скан для проведения SCA. Отчеты будут в директории SCA. Будет ошибка, которую надо поправить, что бы уязвимости определялись или добавить дополнительные уязвимости для их вывода в отчете

```bash
$ cd sca
$ ./dependency-check.sh --update # обновление и поставка базы NVD API
$ mvn dependency:resolve
$ mvn dependency:copy-dependencies -DoutputDirectory=./lib # зависимости из $ pom.xml как jar в ./lib
$ mvn org.owasp:dependency-check-maven:check || true # Maven-плагин OWASP
```

- [x] 6. Запустите SCA CLI OWASP Dependency-Check для уязвимого приложения. Отчеты будут в директории SCA. Опишите как работает сканирование SCA для `pom.xml` и `app.py`

Сканирование `pom.xml` через Maven-плагин OWASP:
```bash
(venv) loltaun@LT-New:~/course_labs/labs/lab07/sca$ mvn org.owasp:dependency-check-maven:check || true
[INFO] Scanning for projects...
[INFO]
[INFO] ---------------------------< lab07:sca-demo >---------------------------
[INFO] Building sca-demo 1.0.0
[INFO] --------------------------------[ jar ]---------------------------------
[INFO]
[INFO] --- dependency-check-maven:12.1.0:check (default-cli) @ sca-demo ---
[INFO]

Dependency-Check is an open source tool performing a best effort analysis of 3rd party dependencies; false positives and false negatives may exist in the analysis performed by the tool. Use of the tool and the reporting provided constitutes acceptance for use in an AS IS condition, and there are NO warranties, implied or otherwise, with regard to the analysis or its use. Any use of the tool and the reporting provided is at the user's risk. In no event shall the copyright holder or OWASP be held liable for any damages whatsoever arising out of or in connection with the use of this tool, the analysis performed, or the resulting report.


   About ODC: https://jeremylong.github.io/DependencyCheck/general/internals.html
   False Positives: https://jeremylong.github.io/DependencyCheck/general/suppression.html

💖 Sponsor: https://github.com/sponsors/jeremylong


[INFO] Analysis Started
[INFO] Finished Archive Analyzer (0 seconds)
[INFO] Finished File Name Analyzer (0 seconds)
[INFO] Finished Jar Analyzer (0 seconds)
[INFO] Finished Dependency Merging Analyzer (0 seconds)
[INFO] Finished Hint Analyzer (0 seconds)
[INFO] Finished Version Filter Analyzer (0 seconds)
WARNING: A restricted method in java.lang.foreign.Linker has been called
WARNING: java.lang.foreign.Linker::downcallHandle has been called by the unnamed module
WARNING: Use --enable-native-access=ALL-UNNAMED to avoid a warning for this module

Jan 09, 2026 9:08:22 PM org.apache.lucene.store.MemorySegmentIndexInputProvider <init>
INFO: Using MemorySegmentIndexInput and native madvise support with Java 21 or later; to disable start with -Dorg.apache.lucene.store.MMapDirectory.enableMemorySegments=false
Jan 09, 2026 9:08:22 PM org.apache.lucene.internal.vectorization.VectorizationProvider lookup
WARNING: Java vector incubator module is not readable. For optimal vector performance, pass '--add-modules jdk.incubator.vector' to enable Vector API.
[INFO] Created CPE Index (1 seconds)
[INFO] Finished CPE Analyzer (1 seconds)
[INFO] Finished False Positive Analyzer (0 seconds)
[INFO] Finished NVD CVE Analyzer (0 seconds)
[WARNING] An error occurred while analyzing '/home/loltaun/.m2/repository/org/codehaus/groovy/groovy-all/2.1.6/groovy-all-2.1.6.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/tmp/dctemp1cec9184-0f60-459f-a81a-64651c2a8999/check12187182641899205758tmp/7/pom.xml' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/home/loltaun/.m2/repository/commons-codec/commons-codec/1.2/commons-codec-1.2.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/home/loltaun/.m2/repository/commons-logging/commons-logging/1.0.4/commons-logging-1.0.4.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/home/loltaun/.m2/repository/commons-httpclient/commons-httpclient/3.1/commons-httpclient-3.1.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/home/loltaun/.m2/repository/com/fasterxml/jackson/module/jackson-module-jaxb-annotations/2.4.6/jackson-module-jaxb-annotations-2.4.6.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/home/loltaun/.m2/repository/com/fasterxml/jackson/core/jackson-annotations/2.4.0/jackson-annotations-2.4.0.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/home/loltaun/.m2/repository/com/fasterxml/jackson/core/jackson-databind/2.4.6/jackson-databind-2.4.6.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/home/loltaun/.m2/repository/com/fasterxml/jackson/core/jackson-core/2.4.6/jackson-core-2.4.6.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/home/loltaun/.m2/repository/com/fasterxml/jackson/jaxrs/jackson-jaxrs-base/2.4.6/jackson-jaxrs-base-2.4.6.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/home/loltaun/.m2/repository/com/fasterxml/jackson/jaxrs/jackson-jaxrs-json-provider/2.4.6/jackson-jaxrs-json-provider-2.4.6.jar' (Sonatype OSS Index Analyzer).
[INFO] Finished Sonatype OSS Index Analyzer (2 seconds)
[INFO] Finished Vulnerability Suppression Analyzer (0 seconds)
[INFO] Finished Known Exploited Vulnerability Analyzer (0 seconds)
[INFO] Finished Dependency Bundling Analyzer (0 seconds)
[INFO] Finished Unused Suppression Rule Analyzer (0 seconds)
[INFO] Analysis Complete (4 seconds)
[INFO] Writing XML report to: /home/loltaun/course_labs/labs/lab07/sca/dependency-check-report/dependency-check-report.xml
[INFO] Writing HTML report to: /home/loltaun/course_labs/labs/lab07/sca/dependency-check-report/dependency-check-report.html
[INFO] Writing JSON report to: /home/loltaun/course_labs/labs/lab07/sca/dependency-check-report/dependency-check-report.json
[INFO] Writing CSV report to: /home/loltaun/course_labs/labs/lab07/sca/dependency-check-report/dependency-check-report.csv
[INFO] Writing SARIF report to: /home/loltaun/course_labs/labs/lab07/sca/dependency-check-report/dependency-check-report.sarif
[INFO] Writing JENKINS report to: /home/loltaun/course_labs/labs/lab07/sca/dependency-check-report/dependency-check-jenkins.html
[INFO] Writing JUNIT report to: /home/loltaun/course_labs/labs/lab07/sca/dependency-check-report/dependency-check-junit.xml
[INFO] Writing GITLAB report to: /home/loltaun/course_labs/labs/lab07/sca/dependency-check-report/dependency-check-gitlab.json
[WARNING]

One or more dependencies were identified with known vulnerabilities in sca-demo:

commons-httpclient-3.1.jar (pkg:maven/commons-httpclient/commons-httpclient@3.1, cpe:2.3:a:apache:commons-httpclient:3.1:*:*:*:*:*:*:*, cpe:2.3:a:apache:httpclient:3.1:*:*:*:*:*:*:*) : CVE-2012-5783, CVE-2020-13956
groovy-all-2.1.6.jar (pkg:maven/org.codehaus.groovy/groovy-all@2.1.6, cpe:2.3:a:apache:groovy:2.1.6:*:*:*:*:*:*:*) : CVE-2015-3253, CVE-2016-6814, CVE-2020-17521
jackson-annotations-2.4.0.jar (pkg:maven/com.fasterxml.jackson.core/jackson-annotations@2.4.0, cpe:2.3:a:fasterxml:jackson-modules-java8:2.4.0:*:*:*:*:*:*:*) : CVE-2018-1000873
jackson-core-2.4.6.jar (pkg:maven/com.fasterxml.jackson.core/jackson-core@2.4.6, cpe:2.3:a:fasterxml:jackson-modules-java8:2.4.6:*:*:*:*:*:*:*) : CVE-2018-1000873
jackson-databind-2.4.6.jar (pkg:maven/com.fasterxml.jackson.core/jackson-databind@2.4.6, cpe:2.3:a:fasterxml:jackson-databind:2.4.6:*:*:*:*:*:*:*, cpe:2.3:a:fasterxml:jackson-modules-java8:2.4.6:*:*:*:*:*:*:*) : CVE-2017-15095, CVE-2017-17485, CVE-2017-7525, CVE-2018-11307, CVE-2018-14718, CVE-2018-14719, CVE-2018-7489, CVE-2019-14379, CVE-2019-14540, CVE-2019-14892, CVE-2019-16335, CVE-2019-16942, CVE-2019-16943, CVE-2019-17267, CVE-2019-17531, CVE-2019-20330, CVE-2020-8840, CVE-2020-9547, CVE-2020-9548, CVE-2020-10673, CVE-2018-5968, CVE-2020-10650, CVE-2020-24616, CVE-2020-24750, CVE-2020-35490, CVE-2020-35491, CVE-2020-36179, CVE-2020-36180, CVE-2020-36181, CVE-2020-36182, CVE-2020-36183, CVE-2020-36184, CVE-2020-36185, CVE-2020-36186, CVE-2020-36187, CVE-2020-36188, CVE-2020-36189, CVE-2021-20190, CVE-2018-12022, CVE-2019-12086, CVE-2019-14439, CVE-2020-36518, CVE-2022-42003, CVE-2022-42004, CVE-2018-1000873, CVE-2019-12384, CVE-2019-12814, CVE-2023-35116


See the dependency-check report for more details.


[INFO] ------------------------------------------------------------------------
[INFO] BUILD FAILURE
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  6.887 s
[INFO] Finished at: 2026-01-09T21:08:27+03:00
[INFO] ------------------------------------------------------------------------
[ERROR] Failed to execute goal org.owasp:dependency-check-maven:12.1.0:check (default-cli) on project sca-demo:
[ERROR]
[ERROR] One or more dependencies were identified with vulnerabilities that have a CVSS score greater than or equal to '0.0':
[ERROR]
[ERROR] commons-httpclient-3.1.jar (pkg:maven/commons-httpclient/commons-httpclient@3.1, cpe:2.3:a:apache:commons-httpclient:3.1:*:*:*:*:*:*:*, cpe:2.3:a:apache:httpclient:3.1:*:*:*:*:*:*:*): CVE-2020-13956(5.3), CVE-2012-5783(5.8)
[ERROR] groovy-all-2.1.6.jar (pkg:maven/org.codehaus.groovy/groovy-all@2.1.6, cpe:2.3:a:apache:groovy:2.1.6:*:*:*:*:*:*:*): CVE-2015-3253(9.8), CVE-2016-6814(9.8), CVE-2020-17521(5.5)
[ERROR] jackson-annotations-2.4.0.jar (pkg:maven/com.fasterxml.jackson.core/jackson-annotations@2.4.0, cpe:2.3:a:fasterxml:jackson-modules-java8:2.4.0:*:*:*:*:*:*:*): CVE-2018-1000873(6.5)
[ERROR] jackson-core-2.4.6.jar (pkg:maven/com.fasterxml.jackson.core/jackson-core@2.4.6, cpe:2.3:a:fasterxml:jackson-modules-java8:2.4.6:*:*:*:*:*:*:*): CVE-2018-1000873(6.5)
[ERROR] jackson-databind-2.4.6.jar (pkg:maven/com.fasterxml.jackson.core/jackson-databind@2.4.6, cpe:2.3:a:fasterxml:jackson-databind:2.4.6:*:*:*:*:*:*:*, cpe:2.3:a:fasterxml:jackson-modules-java8:2.4.6:*:*:*:*:*:*:*): CVE-2017-17485(9.8), CVE-2020-9547(9.8), CVE-2018-12022(7.5), CVE-2018-5968(8.1), CVE-2020-9548(9.8), CVE-2019-14379(9.8), CVE-2020-36180(8.1), CVE-2020-24616(8.1), CVE-2020-36182(8.1), CVE-2019-14439(7.5), CVE-2020-36181(8.1), CVE-2020-35491(8.1), CVE-2020-36184(8.1), CVE-2020-35490(8.1), CVE-2020-36183(8.1), CVE-2019-12814(5.9), CVE-2019-20330(9.8), CVE-2020-24750(8.1), CVE-2020-10673(8.8), CVE-2018-11307(9.8), CVE-2018-14718(9.8), CVE-2018-1000873(6.5), CVE-2018-7489(9.8), CVE-2018-14719(9.8), CVE-2020-36186(8.1), CVE-2019-17531(9.8), CVE-2020-36185(8.1), CVE-2020-36188(8.1), CVE-2020-36187(8.1), CVE-2020-10650(8.1), CVE-2020-36189(8.1), CVE-2019-12086(7.5), CVE-2019-14540(9.8), CVE-2019-12384(5.9), CVE-2023-35116(4.7), CVE-2017-15095(9.8), CVE-2019-16942(9.8), CVE-2019-16943(9.8), CVE-2021-20190(8.1), CVE-2017-7525(9.8), CVE-2020-36518(7.5), CVE-2019-17267(9.8), CVE-2019-16335(9.8), CVE-2020-36179(8.1), CVE-2020-8840(9.8), CVE-2019-14892(9.8), CVE-2022-42003(7.5), CVE-2022-42004(7.5)
[ERROR]
[ERROR] See the dependency-check report for more details.
[ERROR]
[ERROR]
[ERROR] -> [Help 1]
[ERROR]
[ERROR] To see the full stack trace of the errors, re-run Maven with the -e switch.
[ERROR] Re-run Maven using the -X switch to enable full debug logging.
[ERROR]
[ERROR] For more information about the errors and possible solutions, please read the following articles:
[ERROR] [Help 1] http://cwiki.apache.org/confluence/display/MAVEN/MojoFailureException
```

Сканирование `app.py` через OWASP Dependency-Check CLI:
```bash
(venv) loltaun@LT-New:~/course_labs/labs/lab07/sca$ ./dependency-check.sh
OWASP Dependency-Check SCA
[*] Running scan using cached data in /home/loltaun/.dependency-check-data (no full re-download)
[*] Scanning:
    - /home/loltaun/course_labs/labs/lab07/vulnerable-app/requirements.txt
    - /home/loltaun/course_labs/labs/lab07/sca/lib
[INFO]

Dependency-Check is an open source tool performing a best effort analysis of 3rd party dependencies; false positives and false negatives may exist in the analysis performed by the tool. Use of the tool and the reporting provided constitutes acceptance for use in an AS IS condition, and there are NO warranties, implied or otherwise, with regard to the analysis or its use. Any use of the tool and the reporting provided is at the user's risk. In no event shall the copyright holder or OWASP be held liable for any damages whatsoever arising out of or in connection with the use of this tool, the analysis performed, or the resulting report.


   About ODC: https://dependency-check.github.io/DependencyCheck/general/internals.html
   False Positives: https://dependency-check.github.io/DependencyCheck/general/suppression.html


[INFO] Analysis Started
[INFO] Finished File Name Analyzer (0 seconds)
[INFO] Finished pip Analyzer (0 seconds)
[INFO] Finished Dependency Merging Analyzer (0 seconds)
[INFO] Finished Hint Analyzer (0 seconds)
[INFO] Finished Version Filter Analyzer (0 seconds)
[INFO] Created CPE Index (0 seconds)
[INFO] Finished NPM CPE Analyzer (1 seconds)
[INFO] Created CPE Index (0 seconds)
[INFO] Finished CPE Analyzer (0 seconds)
[INFO] Finished False Positive Analyzer (0 seconds)
[INFO] Finished NVD CVE Analyzer (0 seconds)
[WARN] Disabling OSS Index analyzer due to missing user/password credentials. Authentication is now required: https://ossindex.sonatype.org/doc/auth-required
[INFO] Finished Vulnerability Suppression Analyzer (0 seconds)
[INFO] Finished Known Exploited Vulnerability Analyzer (0 seconds)
[INFO] Finished Dependency Bundling Analyzer (0 seconds)
[INFO] Finished Unused Suppression Rule Analyzer (0 seconds)
[INFO] Analysis Complete (2 seconds)
[INFO] Writing HTML report to: /home/loltaun/course_labs/labs/lab07/sca/dependency-check-report/dependency-check-report.html
[INFO] Writing JSON report to: /home/loltaun/course_labs/labs/lab07/sca/dependency-check-report/dependency-check-report.json
[+] Reports saved to: /home/loltaun/course_labs/labs/lab07/sca/dependency-check-report
[i] To refresh NVD data occasionally, run: bash sca/dependency-check.sh --update
```

Описание сканирования SCA для `pom.xml` и `app.py`:
1. `pom.xml` (для Java-приложений):
- Запуск через Maven‑плагин `org.owasp:dependency-check-maven:check`.
- Плагин читает `pom.xml`, ищет зависимости, строит перечень артефактов (jar), сопоставляет их с CPE, сверяет по NVD/KEV (и OSS Index, если заданы учётные данные), формирует отчёты (HTML/JSON/SARIF и др.).
- Найдённые CVE приводят к `BUILD FAILURE` при пороге CVSS ≥ 0, согласно значениям в `pom.xml`.
2. `app.py` (для Python-приложений):
- CLI `dependency-check.sh` сканирует `vulnerable-app/requirements.txt`, используя pip Analyzer.
- Для каждого пакета/версии пытается сматчить CPE и проверить по NVD/KEV (OSS Index опционален, по умолчанию отключён без кредов).
- Результат сохраняется в `sca/dependency-check-report-python-app/*`.

- [x] 7. Соберите единый отчет из всех сканирований в виде `html`, `csv`, `json`

```bash
$ bash sca/generate_unified_report.sh
```
Файл выше отсутствует в репозитории.

Итоговые таблицы с уязвимостями SCA:
1. Для `pom.xml`

| Dependency | Vulnerability IDs | Package | Highest Severity | CVE Count | Confidence | Evidence Count |
| --- | --- | --- | --- | --- | --- | --- |
| commons-httpclient-3.1.jar | ``cpe:2.3:a:apache:commons-httpclient:3.1:*:*:*:*:*:*:*``<br>``cpe:2.3:a:apache:httpclient:3.1:*:*:*:*:*:*:*`` | ``pkg:maven/commons-httpclient/commons-httpclient@3.1`` | MEDIUM | 2 | Highest | 91 |
| groovy-all-2.1.6.jar | ``cpe:2.3:a:apache:groovy:2.1.6:*:*:*:*:*:*:*`` | ``pkg:maven/org.codehaus.groovy/groovy-all@2.1.6`` | CRITICAL | 3 | Highest | 259 |
| jackson-annotations-2.4.0.jar | ``cpe:2.3:a:fasterxml:jackson-modules-java8:2.4.0:*:*:*:*:*:*:*`` | ``pkg:maven/com.fasterxml.jackson.core/jackson-annotations@2.4.0`` | MEDIUM | 1 | Low | 38 |
| jackson-core-2.4.6.jar | ``cpe:2.3:a:fasterxml:jackson-modules-java8:2.4.6:*:*:*:*:*:*:*`` | ``pkg:maven/com.fasterxml.jackson.core/jackson-core@2.4.6`` | MEDIUM | 1 | Low | 42 |
| jackson-databind-2.4.6.jar | ``cpe:2.3:a:fasterxml:jackson-databind:2.4.6:*:*:*:*:*:*:*``<br>``cpe:2.3:a:fasterxml:jackson-modules-java8:2.4.6:*:*:*:*:*:*:*`` | ``pkg:maven/com.fasterxml.jackson.core/jackson-databind@2.4.6`` | CRITICAL | 48 | Highest | 40 |

2. Для `app.py`

| Dependency | Vulnerability IDs | Package | Highest Severity | CVE Count | Confidence | Evidence Count |
| --- | --- | --- | --- | --- | --- | --- |
| PyYAML:5.3.1 | ``cpe:2.3:a:pyyaml:pyyaml:5.3.1:*:*:*:*:*:*:*``<br>``cpe:2.3:a:yaml_project:yaml:5.3.1:*:*:*:*:*:*:*`` | ``pkg:pypi/pyyaml@5.3.1`` | CRITICAL | 1 | Low | 3 |
| certifi:2018.4.16 | ``cpe:2.3:a:certifi:certifi:2018.4.16:*:*:*:*:*:*:*`` | ``pkg:pypi/certifi@2018.4.16`` | CRITICAL | 2 | Highest | 3 |
| paramiko:2.4.1 | ``cpe:2.3:a:paramiko:paramiko:2.4.1:*:*:*:*:*:*:*`` | ``pkg:pypi/paramiko@2.4.1`` | HIGH | 3 | Highest | 3 |
| pyjwt:1.7.1 | ``cpe:2.3:a:pyjwt_project:pyjwt:1.7.1:*:*:*:*:*:*:*`` | ``pkg:pypi/pyjwt@1.7.1`` | HIGH | 1 | Highest | 3 |



- [x] 8. Проанализируйте все уязвимости и обьясните для SAST Checkov сработки статуса `Unknown`. Классифицируйте их и укажите какие не должны быть в отчетах. Внесите исправления и запустите повторное сканирование и убедитесь, что они устранены. Приложите исправленный файл и отчет без уязвимостей. 

В отчёте Checkov по Dockerfile есть 2 реальные сработки:
- CKV_DOCKER_2 — отсутствует HEALTHCHECK. Класс: Hardening/Observability.
- CKV_DOCKER_3 — приложение в контейнере запускается от root, не создан USER. Класс: Hardening/Privilege escalation.

Две найденные проблемы актуальны и должны быть в отчёте. 

Исправленный Dockerfile:
```Dockerfile
FROM python:3.11-slim
WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        libjpeg-dev zlib1g-dev \
        libxml2-dev libxslt1-dev && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app
EXPOSE 8080

# Создание непривилегированного пользователя и переключение на него
RUN adduser --disabled-password --gecos "" appuser
USER appuser

# Добавление HEALTHCHECK для мониторинга состояния приложения
HEALTHCHECK --interval=30s --timeout=5s --retries=3 CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8080/').read()" || exit 1

ENV FLASK_ENV=development
ENV DEBUG=true
CMD ["python", "app.py"]
```


```json
  "summary": {
    "passed": 70,
    "failed": 0,
    "skipped": 0,
    "parsing_errors": 0,
    "resource_count": 1,
    "checkov_version": "3.2.497"
  },
```

- [x] 9. Опишите выведенные уязвимости для SAST Semgrep и принцип их работы. Поправьте скрипт `app.py`. Запустите повторное сканирование и убедитесь, что они устранены. Приложите исправленный файл `app.py` и отчет без уязвимостей.

Уязвимости Semgrep:
- `sast.py-info-version-disclosure` (LOW) — маршрут отдаёт строку с версией приложения, раскрывая лишнюю информацию (строчка кода 26).
- `sast.py-os-system-rce` (CRITICAL) — вызов `os.system(...)` с пользовательским вводом позволяет выполнить произвольные команды (строчка кода 52).
- `sast.py-arbitrary-file-read` (CRITICAL) — `open(..., "r")` с путём из запроса даёт LFI/чтение произвольных файлов (строчка кода 68).
- `sast.py-unsafe-pickle-deserialization` (CRITICAL) — `pickle.loads(...)` на данных пользователя ведёт к RCE через небезопасную десериализацию (строчка кода 79).
- `sast.py-eval-user-input` (HIGH) — `eval(...)` на пользовательском вводе позволяет выполнить произвольный код (строчка кода 88).

Исправленный `app.py`:
```python
from flask import (
    Flask,
    request,
    make_response,
    render_template_string,
    redirect,
    url_for,
)
import sqlite3
import os

app = Flask(__name__)

DB_PATH = os.environ.get("APP_DB_PATH", "app.db")


def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT,
            role TEXT
        )
        """
    )
    cur.execute("DELETE FROM users")
    cur.execute(
        "INSERT INTO users (username, password, role) VALUES ('admin', 'admin123', 'admin')"
    )
    cur.execute(
        "INSERT INTO users (username, password, role) VALUES ('user', 'user123', 'user')"
    )
    conn.commit()
    conn.close()


@app.route("/")
def index():
    html = """
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
    """
    resp = make_response(html)
    resp.set_cookie("session", "guest-session-id")
    return resp


@app.route("/echo")
def echo():
    msg = request.args.get("msg", "")
    template = """
    <h2>Echo</h2>
    <p>Сообщение: {msg}</p>
    <p>Попробуйте передать что-нибудь вроде: <code>&lt;script&gt;alert('XSS')&lt;/script&gt;</code></p>
    <a href="/">Назад</a>
    """.format(msg=msg)
    return render_template_string(template)


@app.route("/search")
def search():
    username = request.args.get("username", "")
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    query = f"SELECT id, username, role FROM users WHERE username = '{username}'"  # nosec B608
    rows = []
    error = None
    try:
        for row in cur.execute(query):
            rows.append(row)
    except Exception as e:
        error = str(e)

    conn.close()

    template = """
    <h2>Поиск пользователя</h2>
    <p>Запрос: <code>{{ query }}</code></p>
    {% if error %}
      <p style="color:red;">SQL error: {{ error }}</p>
    {% endif %}
    {% if rows %}
      <ul>
      {% for id, username, role in rows %}
        <li>{{ id }} – {{ username }} ({{ role }})</li>
      {% endfor %}
      </ul>
    {% else %}
      <p>Ничего не найдено</p>
    {% endif %}
    <p>Попробуйте, например: <code>?username=admin' OR '1'='1</code></p>
    <a href="/">Назад</a>
    """
    return render_template_string(template, query=query, rows=rows, error=error)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        form = """
        <h2>Логин</h2>
        <form method="post">
          <label>Username: <input type="text" name="username"></label><br>
          <label>Password: <input type="password" name="password"></label><br>
          <button type="submit">Login</button>
        </form>
        <p>Попробуйте: admin / admin123 или user / user123</p>
        <a href="/">Назад</a>
        """
        return render_template_string(form)

    username = request.form.get("username", "")
    password = request.form.get("password", "")

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    query = f"SELECT id, username, role FROM users WHERE username = '{username}' AND password = '{password}'"  # nosec B608
    row = cur.execute(query).fetchone()
    conn.close()

    if row:
        _, uname, role = row
        resp = make_response(
            f"<h2>Добро пожаловать, {uname} ({role})!</h2><a href='/'>На главную</a>"
        )

        resp.set_cookie("user", uname)
        resp.set_cookie("role", role)
        return resp
    else:
        return render_template_string(
            "<h2>Неверные учетные данные</h2><a href='/login'>Попробовать снова</a>"
        )


@app.route("/profile")
def profile():
    username = request.cookies.get("user", "guest")
    role = request.cookies.get("role", "guest")

    template = """
    <h2>Профиль пользователя</h2>
    <p>Имя: {{ username }}</p>
    <p>Роль: {{ role }}</p>
    <p>Cookie легко подделать: можно выдать себе роль 'admin'.</p>
    <a href="/">Назад</a>
    """
    return render_template_string(template, username=username, role=role)


@app.route("/admin")
def admin():
    role = request.cookies.get("role", "guest")
    if role != "admin":
        return (
            "<h2>Доступ запрещён: вы не admin</h2><p>Попробуйте изменить cookie 'role'.</p><a href='/'>Назад</a>",
            403,
        )

    template = """
    <h2>Admin panel</h2>
    <p>Секретные настройки приложения (демо).</p>
    <ul>
      <li>DEBUG: true</li>
      <li>FEATURE_FLAG: experimental_mode</li>
    </ul>
    <a href="/">Назад</a>
    """
    return render_template_string(template)


@app.route("/files/")
@app.route("/files/<path:subpath>")
def files(subpath=""):
    base_dir = os.path.abspath(os.path.dirname(__file__))
    target_dir = os.path.join(base_dir, "files")

    full_path = os.path.join(target_dir, subpath)

    if not os.path.exists(full_path):
        return "<h2>Путь не найден</h2><a href='/'>Назад</a>", 404

    if os.path.isdir(full_path):
        entries = os.listdir(full_path)
        items = "".join(
            f"<li><a href='/files/{subpath}{'' if subpath.endswith('/') or subpath == '' else '/'}{e}'>{e}</a></li>"
            for e in entries
        )
        html = f"""
        <h2>Files under /files/{subpath}</h2>
        <ul>{items}</ul>
        <p>Пример directory listing без ограничений.</p>
        <a href="/">Назад</a>
        """
        return html

    with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    return f"<pre>{content}</pre>"


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=8080, debug=True)  # nosec B201,B104
```

Отчет Semgrep после исправлений:
```bash
┌──────────────┐
│ Scan Summary │
└──────────────┘
✅ Scan completed successfully.
 • Findings: 0 (0 blocking)
 • Rules run: 16
 • Targets scanned: 2
 • Parsed lines: ~100.0%
 • Scan was limited to files tracked by git
 • For a detailed list of skipped files and lines, run semgrep with the --verbose flag
Ran 16 rules on 2 files: 0 findings.

✨ If Semgrep missed a finding, please send us feedback to let us know!
   See https://semgrep.dev/docs/reporting-false-negatives/
```

- [x] 10. Доработайте SCA уязвимости, что бы они только остались в фиинальной версии отчетов.

1. Для `pom.xml`:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
                             http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>lab07</groupId>
    <artifactId>sca-demo</artifactId>
    <version>1.0.1</version>
    <packaging>jar</packaging>

    <name>sca-demo</name>

    <properties>
        <!-- Актуальные версии зависимостей -->
        <groovy.version>5.0.3</groovy.version>
        <jackson.version>2.20.1</jackson.version>
        <httpclient5.version>5.6</httpclient5.version>
    </properties>

    <!-- BOM'ы для выравнивания версий модулей -->
    <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>org.apache.groovy</groupId>
                <artifactId>groovy-bom</artifactId>
                <version>${groovy.version}</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>

            <dependency>
                <groupId>com.fasterxml.jackson</groupId>
                <artifactId>jackson-bom</artifactId>
                <version>${jackson.version}</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
        </dependencies>
    </dependencyManagement>

    <dependencies>
        <!-- Groovy (вместо устаревшего org.codehaus.groovy:groovy-all:2.1.6) -->
        <dependency>
            <groupId>org.apache.groovy</groupId>
            <artifactId>groovy-all</artifactId>
            <version>${groovy.version}</version>
            <type>pom</type>
        </dependency>


        <!-- Jackson JAX-RS JSON provider (обновлён до 2.20.1 через jackson-bom) -->
        <dependency>
            <groupId>com.fasterxml.jackson.jaxrs</groupId>
            <artifactId>jackson-jaxrs-json-provider</artifactId>
        </dependency>

        <!-- ВМЕСТО commons-httpclient:commons-httpclient:3.1 -->
        <dependency>
            <groupId>org.apache.httpcomponents.client5</groupId>
            <artifactId>httpclient5</artifactId>
            <version>${httpclient5.version}</version>
        </dependency>
    </dependencies>

    <build>
    <plugins>
        <plugin>
        <groupId>org.owasp</groupId>
        <artifactId>dependency-check-maven</artifactId>
        <version>12.1.0</version>
        <configuration>
            <format>ALL</format>
            <outputDirectory>${project.basedir}/dependency-check-report</outputDirectory>
            <failBuildOnCVSS>0.0</failBuildOnCVSS>
            <autoUpdate>false</autoUpdate>
            <ossindexAnalyzerEnabled>false</ossindexAnalyzerEnabled>
        </configuration>
        <executions>
            <execution>
            <goals>
                <goal>check</goal>
            </goals>
            </execution>
        </executions>
        </plugin>
    </plugins>
    </build>

</project>
```
Результат отчета SCA для `pom.xml` после доработок:
![alt text](https://raw.githubusercontent.com/LolTaun/course_labs/refs/heads/lab7/labs/lab07/Report/image-1.png)
2. Для `app.py`:
```txt
Flask==3.0.3
Werkzeug==3.0.4
Jinja2==3.1.4
itsdangerous==2.2.0
click==8.1.7
gunicorn==22.0.0
```
Были удалены лишние зависимости, обновлены требуемые. Результат отчета SCA для `app.py` после доработок:
![alt text](https://raw.githubusercontent.com/LolTaun/course_labs/refs/heads/lab7/labs/lab07/Report/image.png)

- [x] 11. Проверьте себя по найденным сработкам анализаторов и так вы сможете помочь себе разобраться в ситуации, если возникнут сложности

```bash
$ bash cheat_check_yuorself.sh
```

Успешно выполняется данный скрипт, все шаги выполнены корректно и без уязвимостей. Вывод не размещается здесь ввиду его большого объема (около 5500 строк).

- [x] 12. Делайте все коммиты на соответствующих шагах, далее заливайте изменения в удаленный репозиторий.
Исправлены ошибки Checkov - 59873fd
Исправлены ошибки Semgrep - 5e3e11df
Опубликованы обновленные отчеты SAST - 3305097
Исправлены уязвимости SCA - 236da2c
Опубликованы обновленные отчеты SCA - e695bd2 
- [x] 13. Подготовьте отчет `gist`.

https://gist.github.com/LolTaun/085cefd96a0d5772ac5d03186cad0558

- [x] 14. Почистите кеш от `venv` и остановите уязвимое приложение

```bash
$ deactivate
$ rm -rf venv
$ docker-compose -f ххх down
$ docker-compose -f docker-compose.yml down
$ docker system prune -f
```

---

Copyright (c) 2025 Denis Kuznetsov