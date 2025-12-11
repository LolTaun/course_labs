<div align="center">
<h1><a id="intro">Лабораторная работа №1</a><br></h1>
<a href="https://docs.github.com/en"><img src="https://img.shields.io/static/v1?logo=github&logoColor=fff&label=&message=Docs&color=36393f&style=flat" alt="GitHub Docs"></a>
<a href="https://daringfireball.net/projects/markdown"><img src="https://img.shields.io/static/v1?logo=markdown&logoColor=fff&label=&message=Markdown&color=36393f&style=flat" alt="Markdown"></a> 
<a href="https://symbl.cc/en/unicode-table"><img src="https://img.shields.io/static/v1?logo=unicode&logoColor=fff&label=&message=Unicode&color=36393f&style=flat" alt="Unicode"></a> 
<a href="https://shields.io"><img src="https://img.shields.io/static/v1?logo=shieldsdotio&logoColor=fff&label=&message=Shields&color=36393f&style=flat" alt="Shields"></a>
<a href="https://img.shields.io/badge/Risk_Analyze-2448a2"><img src="https://img.shields.io/badge/Course-Risk_Analysis-2448a2" alt= "RA"></a> <img src="https://img.shields.io/badge/AppSec-2448a2" alt= "RA"></a> <img src="https://img.shields.io/badge/Contributor-Кузнецов Д. А.-8b9aff" alt="Contributor Badge"></a></div>


1. Создайте локальный репозиторий на машине
2. Проинициализируйте репозиторий
```bash
mkdir course_lab1
cd course_lab1/
git init
```
3. Авторизуйтесь и спользуйте `GitHub CLI` для создания удаленного репозитория
```bash
gh auth login
gh repo create LolTaun/course_lab1 --public --confirm
```
Ссылка на удалённый репозиторий: https://github.com/LolTaun/course_lab1
4. Создайте пустой README.md 
```bash
touch README.md
```
5. Используйте указание URL своего созданного репозитория для присвоения ветки`master` статуса `origin`
```bash
git remote set-url origin git@github.com:LolTaun/course_lab1.git
```
6. В локальном репозитории и сделайте `commit`
```bash
git add README.md
git commit -S -m "Test"
```
ID коммита: 39d47f4
![alt text](https://raw.githubusercontent.com/LolTaun/course_labs/refs/heads/lab1/labs/lab01/Report/img/6-1.png)
![alt text](https://raw.githubusercontent.com/LolTaun/course_labs/refs/heads/lab1/labs/lab01/Report/img/6-2.png)
7. Сделайте публикацию своего `commit` с флагом `-S` в удаленный репозиторий
```bash
git push -u origin master
```
![alt text](https://raw.githubusercontent.com/LolTaun/course_labs/refs/heads/lab1/labs/lab01/Report/img/7-1.png)
8. Создайте файл `hello.py` в локальном репозитории. Реализуйте **Hello appsecworld** на языке python используя несколько интерпретаторов с "грязным" кодом
![alt text](https://raw.githubusercontent.com/LolTaun/course_labs/refs/heads/lab1/labs/lab01/Report/img/8-1.png)
9. Сделайте `commit` с флагом `-S`
ID коммита: b48c275
10. Измените исходный код, что бы скрипт запрашивал имя пользователя и выводил `Helloappsec world from @name`
![alt text](https://raw.githubusercontent.com/LolTaun/course_labs/refs/heads/lab1/labs/lab01/Report/img/10-1.png)
11. Сделайте `commit` с флагом `-S` и сделайте публикацию в удаленный репозиторий.Проверьте вывод истории изменений
ID коммита: 6ea3cd9
![alt text](https://raw.githubusercontent.com/LolTaun/course_labs/refs/heads/lab1/labs/lab01/Report/img/11-3.png)
12. В локальном репозитории создайте ветку `patch1` и внесите изменения исправлению кода и модернизации до следующего вида, что бы код был рабочим. Сделайте публикацию своего `commit` с флагом `-S` в удаленный репозиторий:
```bash
git checkout -b patch1
```
![alt text](https://raw.githubusercontent.com/LolTaun/course_labs/refs/heads/lab1/labs/lab01/Report/img/12-2.png)
![alt text](https://raw.githubusercontent.com/LolTaun/course_labs/refs/heads/lab1/labs/lab01/Report/img/12-3.png)
ID коммита: d539d2a
13. Проверьте, что ветка `patch1` в удалённом репозитории
![alt text](https://raw.githubusercontent.com/LolTaun/course_labs/refs/heads/lab1/labs/lab01/Report/img/13-1.png)
14. Создайте `pull-request` в виде `patch1 -> master`
![alt text](https://raw.githubusercontent.com/LolTaun/course_labs/refs/heads/lab1/labs/lab01/Report/img/14-1.png)
15. В ветке `patch1` добавьте в исходный код комментарии и убедитесь, что естьуказанные изменения в `pull-request`
ID коммита: f0a026b
![alt text](https://raw.githubusercontent.com/LolTaun/course_labs/refs/heads/lab1/labs/lab01/Report/img/15-2.png)
![alt text](https://raw.githubusercontent.com/LolTaun/course_labs/refs/heads/lab1/labs/lab01/Report/img/15-3.png)
16. В удалённый репозитории выполните слияние `pull-request` для `patch1 -> master` иудалите ветку `patch1`
ID коммита: 0d204e1
![alt text](https://raw.githubusercontent.com/LolTaun/course_labs/refs/heads/lab1/labs/lab01/Report/img/16-1.png)
17. Стяните последние актуальные изменения и просмотрите историю изменений для `master`
```bash
git pull origin master
```
18. Удалите локальную ветку `patch1`
```bash
git branch -d patch1
```
19. Создайте новую локальную ветку `patch2`.
```bash
git checkout -b patch2
```
20. Измените *code style* по своему усмотрению
![](https://raw.githubusercontent.com/LolTaun/course_labs/refs/heads/lab1/labs/lab01/Report/img/20-1.png)
![alt text](https://raw.githubusercontent.com/LolTaun/course_labs/refs/heads/lab1/labs/lab01/Report/img/20-2.png)
21. Сделайте публикацию своего `commit` с флагом `-S` в удаленный репозиторий исоздайте pull-request `patch2 -> master`
ID коммита: e0c0f8b
22. В ветке **master** удаленного репозитория явно измените комментарий
ID коммита: e499909
![alt text](https://raw.githubusercontent.com/LolTaun/course_labs/refs/heads/lab1/labs/lab01/Report/img/22-1.png)
23. Увидите, что в `pull-request` появились расхождения
![alt text](https://raw.githubusercontent.com/LolTaun/course_labs/refs/heads/lab1/labs/lab01/Report/img/23-1.png)
24. Локально сделайте **rebase** и исправьте расхождения (это называется **конфликт**)
![alt text](https://raw.githubusercontent.com/LolTaun/course_labs/refs/heads/lab1/labs/lab01/Report/img/24-1.png)
![alt text](https://raw.githubusercontent.com/LolTaun/course_labs/refs/heads/lab1/labs/lab01/Report/img/24-2.png)
25. Сделайте `commit` и опубликуйте изменения в ветке `patch2`
ID коммита: 4088cd8
![alt text](https://raw.githubusercontent.com/LolTaun/course_labs/refs/heads/lab1/labs/lab01/Report/img/25-1.png)
![alt text](https://raw.githubusercontent.com/LolTaun/course_labs/refs/heads/lab1/labs/lab01/Report/img/25-2.png)
26. Убедитель, что пропали конфликтны. 
![alt text](https://raw.githubusercontent.com/LolTaun/course_labs/refs/heads/lab1/labs/lab01/Report/img/26-1.png)
27. Сделайте `merge` для `pull-request` `patch2 -> master`.
ID коммита: 3e2f07d
![alt text](https://raw.githubusercontent.com/LolTaun/course_labs/refs/heads/lab1/labs/lab01/Report/img/27-1.png)
28. Подготовьте отчет `gist`.
**Это он и есть :)**
29. Продемонстрируйте в материалах отчета историю коммитов на локальном и удаленном репозитории.
**Локально:**
![alt text](https://raw.githubusercontent.com/LolTaun/course_labs/refs/heads/lab1/labs/lab01/Report/img/29-1.png)
**Удаленно:**
![alt text](https://raw.githubusercontent.com/LolTaun/course_labs/refs/heads/lab1/labs/lab01/Report/img/29-2.png)



### Дополнительный вопрос
**Права разных типов контрибьюторов на GitHub**
- Read – смотреть код, Issues, PR, форкать, комментировать.
- Triage – всё как Read + метки, закрытие/открытие Issues и PR, управление без записи кода.
- Write – пушить в ветки (где разрешено), создавать/мерджить PR, управлять wiki и т.п.
- Maintain – всё как Write + управление настройками репо (ветки, команды, webhooks), но без полного админства.
- Admin – полный контроль: смена видимости, удаление репо, управление доступами других.
---
Copyright (c) 2025 Denis Kuznetsov
