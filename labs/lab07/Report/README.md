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
$ semgrep --config sast/semgrep-rules.yml \
  --json \
  --output sast/semgrep-report.json \
  vulnerable-app/
```


- [x] 4. Запустите SAST Checkov по Dockerfile, compose и проанализируйте выведенный лог в консоли и опишите логику правил для `checkov-config.yaml` по `Docker`. Отчет будет в директории SAST

```bash
$ checkov \
  --framework dockerfile \
  --file vulnerable-app/Dockerfile docker-compose.yml \
  --output json \
  --output-file-path sast/checkov-report.json \
  --soft-fail
```

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

- [ ] 7. Соберите единый отчет из всех сканирований в виде `html`, `csv`, `json`

```bash
$ bash sca/generate_unified_report.sh
```

- [ ] 8. Проанализируйте все уязвимости и обьясните для SAST Checkov сработки статуса `Unknown`. Классифицируйте их и укажите какие не должны быть в отчетах. Внесите исправления и запустите повторное сканирование и убедитесь, что они устранены. Приложите исправленный файл и отчет без уязвимостей. 
- [ ] 9. Опишите выведенные уязвимости для SAST Semgrep и принцип их работы. Поправьте скрипт `app.py`. Запустите повторное сканирование и убедитесь, что они устранены. Приложите исправленный файл `app.py` и отчет без уязвимостей. 
- [ ] 10. Доработайте SCA уязвимости, что бы они только остались в фиинальной версии отчетов.
- [ ] 11. Проверьте себя по найденным сработкам анализаторов и так вы сможете помочь себе разобраться в ситуации, если возникнут сложности

```bash
$ bash cheat_check_yuorself.sh
```

- [ ] 12. Делайте все коммиты на соответствующих шагах, далее заливайте изменения в удаленный репозиторий.
- [ ] 13. Подготовьте отчет `gist`.
- [ ] 14. Почистите кеш от `venv` и остановите уязвимое приложение

```bash
$ deactivate
$ rm -rf venv
$ docker-compose -f ххх down
$ docker-compose -f docker-compose.yml down
$ docker system prune -f
```

---

Copyright (c) 2025 Denis Kuznetsov