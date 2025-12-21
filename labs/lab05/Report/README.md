## Задание

- [x] 1. Поставьте `Docker` и `buildkit`
- [x] 2. Перейдите в `source` и выведите на терминале, далее проанализируйте следующие команды консоли

```bash
loltaun@LT-New:~/course_labs/labs/lab05/source$ docker buildx build -t hello-appsec-world .
[+] Building 2.7s (13/13) FINISHED                                                                                                           docker:default
 => [internal] load build definition from Dockerfile                                                                                                   0.0s
 => => transferring dockerfile: 429B                                                                                                                   0.0s
 => [internal] load metadata for docker.io/library/python:3.11-slim                                                                                    2.5s
 => [internal] load .dockerignore                                                                                                                      0.0s
 => => transferring context: 2B                                                                                                                        0.0s
 => [builder 1/4] FROM docker.io/library/python:3.11-slim@sha256:158caf0e080e2cd74ef2879ed3c4e697792ee65251c8208b7afb56683c32ea6c                      0.0s
 => => resolve docker.io/library/python:3.11-slim@sha256:158caf0e080e2cd74ef2879ed3c4e697792ee65251c8208b7afb56683c32ea6c                              0.0s
 => [internal] load build context                                                                                                                      0.0s
 => => transferring context: 63B                                                                                                                       0.0s
 => CACHED [builder 2/4] WORKDIR /hello                                                                                                                0.0s
 => CACHED [builder 3/4] COPY requirements.txt .                                                                                                       0.0s
 => CACHED [builder 4/4] RUN pip install --upgrade pip && pip wheel --wheel-dir=/wheels -r requirements.txt                                            0.0s
 => CACHED [stage-1 3/6] COPY --from=builder /wheels /wheels                                                                                           0.0s
 => CACHED [stage-1 4/6] COPY requirements.txt .                                                                                                       0.0s
 => CACHED [stage-1 5/6] RUN pip install --no-index --find-links=/wheels -r requirements.txt                                                           0.0s
 => CACHED [stage-1 6/6] COPY hello.py .                                                                                                               0.0s
 => exporting to image                                                                                                                                 0.1s
 => => exporting layers                                                                                                                                0.0s
 => => exporting manifest sha256:bb7a79d2a3095dfc48f0fce2cff443f3a19802a3d25d56d4e2c5fa17472f6235                                                      0.0s
 => => exporting config sha256:4e00ea8cf565fd807e5b51267a39a70ce761f2ef4a10775e4e8ae1bae68d6f7f                                                        0.0s
 => => exporting attestation manifest sha256:1e2733a8ead23fafa79c2092337fb63109702e82b8519e92cf14a9c7e00013f4                                          0.0s
 => => exporting manifest list sha256:77cf81e0abccc4edf1c1bbc2e128596ca4094d558dc09dedfb0d08006cfc4600                                                 0.0s
 => => naming to docker.io/library/hello-appsec-world:latest                                                                                           0.0s
 => => unpacking to docker.io/library/hello-appsec-world:latest                                                                                        0.0s

loltaun@LT-New:~/course_labs/labs/lab05$ docker run hello-appsec-world
hello appsec world
loltaun@LT-New:~/course_labs/labs/lab05$ docker run --rm -it hello-appsec-world
hello appsec world

loltaun@LT-New:~/course_labs/labs/lab05$ docker save -o hello.tar hello-appsec-world
loltaun@LT-New:~/course_labs/labs/lab05$ ls
README.md  Report  client  docker-compose.yml  hello.tar  server  source
loltaun@LT-New:~/course_labs/labs/lab05$ docker load -i hello.tar
Loaded image: hello-appsec-world:latest
loltaun@LT-New:~/course_labs/labs/lab05$ docker load -i image.tar
open image.tar: no such file or directory
```
Анализ:
`docker buildx build -t hello-appsec-world .` - сборка образа из Dockerfile
`docker run hello-appsec-world` - запуск контейнера из собранного образа
`docker run --rm -it hello-appsec-world` - запуск контейнера с последующим удалением.
`docker save -o hello.tar hello-appsec-world` - сохранение образа в файл hello.tar
`docker load -i hello.tar` - загрузка образа из файла hello.tar
`docker load -i image.tar` - попытка загрузки образа из файла image.tar, однако его не существует


- [x] 3. Откройте `Dockerfile` и сделайте его анализ. Сделайте `commit`
Анализ:
```dockerfile
# Этап 1: сборка зависимостей
FROM python:3.11-slim AS builder
WORKDIR /hello
# Копируем файл с зависимостями
COPY requirements.txt . 
# Устанавливаем зависимости в отдельную директорию wheelhouse для кеширования
RUN pip install --upgrade pip && pip wheel --wheel-dir=/wheels -r requirements.txt

# Этап 2: запускаемый образ
FROM python:3.11-slim
WORKDIR /hello
# Копируем файл с зависимостями
COPY --from=builder /wheels /wheels # Копируем собранные wheel-пакеты
COPY requirements.txt . 
# Устанавливаем зависимости из wheel-пакетов
RUN pip install --no-index --find-links=/wheels -r requirements.txt
# Копируем исходный код приложения
COPY hello.py .

# Переменные окружения для улучшенной работы Python
ENV PYTHONUNBUFFERED=1
# Запускаем приложение
CMD ["python", "hello.py"] 
```

commit - d3400be:
```bash
loltaun@LT-New:~/course_lab1$ git add source/
loltaun@LT-New:~/course_lab1$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   source/Dockerfile
        new file:   source/hello.py
        new file:   source/hello.tar
        new file:   source/requirements.txt

loltaun@LT-New:~/course_lab1$ git commit -m "Added Hello-Appsec-World with Dockerfile"
[master d3400be] Added Hello-Appsec-World with Dockerfile
 4 files changed, 31 insertions(+)
 create mode 100644 source/Dockerfile
 create mode 100644 source/hello.py
 create mode 100644 source/hello.tar
 create mode 100644 source/requirements.txt
```


- [x] 4. Замените в `Dockerfile`значение скрипта на `python` тем, который вы сделали ранее в прошлых лабораторных работах. Вложите свой файл `python` в директорию. Сделайте анализ своего измененного `Dockerfile` и внесите изменения. Сделайте `commit`. 
Анализ измененного Dockerfile:
```dockerfile
# Этап 1: сборка Python-зависимостей (wheelhouse)
FROM python:3.11-slim AS builder

# Рабочая директория для сборки
WORKDIR /hello

# Копируем файл зависимостей (отдельным слоем для лучшего кеширования)
COPY requirements.txt .

# Обновляем pip и собираем все зависимости в wheel-пакеты в /wheels
# Это ускоряет установку на финальном этапе и позволяет ставить зависимости офлайн
RUN pip install --upgrade pip && pip wheel --wheel-dir=/wheels -r requirements.txt


# Этап 2: финальный (runtime) образ
FROM python:3.11-slim

# Устанавливаем системные библиотеки (часто нужны для OpenCV/GUI/рендеринга в headless-среде)
# --no-install-recommends уменьшает размер образа, очистка apt-кеша также уменьшает слой
RUN apt-get update \
        && apt-get install -y --no-install-recommends \
                libgl1 \
                libglib2.0-0 \
                libsm6 \
                libxext6 \
                libxrender1 \
        && rm -rf /var/lib/apt/lists/*

# Рабочая директория приложения
WORKDIR /hello

# Копируем собранные wheel-пакеты из builder-стадии
COPY --from=builder /wheels /wheels

# Копируем файл зависимостей
COPY requirements.txt .

# Устанавливаем зависимости строго из wheelhouse (без обращения к PyPI), затем удаляем /wheels
RUN pip install --no-index --find-links=/wheels -r requirements.txt \
        && rm -rf /wheels

# Копируем исходники приложения
COPY hello.py screen.py ./

# Переменные окружения:
# PYTHONUNBUFFERED=1 — вывод логов без буферизации
# SDL_AUDIODRIVER=dummy — отключение аудио (полезно в контейнере/CI без аудиоустройств)
ENV PYTHONUNBUFFERED=1 \
        SDL_AUDIODRIVER=dummy

# ENTRYPOINT задаёт базовую команду (python -u), CMD — аргументы по умолчанию
# По умолчанию запускаем hello.py с именем "AppSec", чтобы контейнер работал без параметров
ENTRYPOINT ["python", "-u"]
CMD ["hello.py", "AppSec"]
```

commits - 9243c69, 19ec28d

- [x] 5. Выведите на терминале и проанализируйте следующие команды консоли. Сравните хеш сумму вашего архива с `image.tar` из репозитория, выведите на терминал.

```bash
(venv) loltaun@LT-New:~/course_lab1$ docker buildx build -t hello-appsec-world .
[+] Building 1.3s (15/15) FINISHED                                                                                                           docker:default
 => [internal] load build definition from Dockerfile                                                                                                   0.0s
 => => transferring dockerfile: 2.60kB                                                                                                                 0.0s
 => [internal] load metadata for docker.io/library/python:3.11-slim                                                                                    1.1s
 => [internal] load .dockerignore                                                                                                                      0.0s
 => => transferring context: 2B                                                                                                                        0.0s
 => [internal] load build context                                                                                                                      0.0s
 => => transferring context: 94B                                                                                                                       0.0s
 => [builder 1/4] FROM docker.io/library/python:3.11-slim@sha256:158caf0e080e2cd74ef2879ed3c4e697792ee65251c8208b7afb56683c32ea6c                      0.0s
 => => resolve docker.io/library/python:3.11-slim@sha256:158caf0e080e2cd74ef2879ed3c4e697792ee65251c8208b7afb56683c32ea6c                              0.0s
 => CACHED [stage-1 2/7] RUN apt-get update         && apt-get install -y --no-install-recommends                 libgl1                 libglib2.0-0  0.0s
 => CACHED [stage-1 3/7] WORKDIR /hello                                                                                                                0.0s
 => CACHED [builder 2/4] WORKDIR /hello                                                                                                                0.0s
 => CACHED [builder 3/4] COPY requirements.txt .                                                                                                       0.0s
 => CACHED [builder 4/4] RUN pip install --upgrade pip && pip wheel --wheel-dir=/wheels -r requirements.txt                                            0.0s
 => CACHED [stage-1 4/7] COPY --from=builder /wheels /wheels                                                                                           0.0s
 => CACHED [stage-1 5/7] COPY requirements.txt .                                                                                                       0.0s
 => CACHED [stage-1 6/7] RUN pip install --no-index --find-links=/wheels -r requirements.txt         && rm -rf /wheels                                 0.0s
 => CACHED [stage-1 7/7] COPY hello.py screen.py ./                                                                                                    0.0s
 => exporting to image                                                                                                                                 0.1s
 => => exporting layers                                                                                                                                0.0s
 => => exporting manifest sha256:619372e97f9e579b8d68349b44d82068bf584598c399aedeee3a18831b5231fc                                                      0.0s
 => => exporting config sha256:199cfa8a1e78d606d7eaf0bf82c192d470622191861cfab94834d7b4339f790b                                                        0.0s
 => => exporting attestation manifest sha256:1f8b09df187c73e19901cf0fdd52fb8bfa6bb5ba4784db6cdf262f642fcdaef3                                          0.0s
 => => exporting manifest list sha256:346244254676c3b7d7239c88d0e254e21c4318a0e31c4e493fd2d45559f41a8b                                                 0.0s
 => => naming to docker.io/library/hello-appsec-world:latest                                                                                           0.0s
 => => unpacking to docker.io/library/hello-appsec-world:latest                                                                                        0.0s

(venv) loltaun@LT-New:~/course_lab1$ docker run hello-appsec-world
***********************************
*         Привет, AppSec!         *
*   Классический тёплый привет.   *
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
***********************************
Тема: classic — Классический тёплый привет.
```
Дополнительные необязательные параметры запуска нового контейнера:
![alt text](https://raw.githubusercontent.com/LolTaun/course_labs/refs/heads/lab5/labs/lab05/Report/image.png)

```bash
(venv) loltaun@LT-New:~/course_lab1$ docker save -o my-hello-appsec.tar hello-appsec-world
(venv) loltaun@LT-New:~/course_lab1$ docker load -i my-hello-appsec.tar
Loaded image: hello-appsec-world:latest
(venv) loltaun@LT-New:~/course_lab1$ docker run hello-appsec-world
***********************************
*         Привет, AppSec!         *
*   Классический тёплый привет.   *
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
***********************************
Тема: classic — Классический тёплый привет.

(venv) loltaun@LT-New:~/course_lab1$ docker load -i source/image.tar
Loaded image: hello-appsec-world:latest
(venv) loltaun@LT-New:~/course_lab1$ docker run hello-appsec-world
hello appsec world

(venv) loltaun@LT-New:~/course_lab1$ sha256sum source/image.tar my-hello-appsec.tar
130195490032b1d62660c4d77e798d428b0d4b06d88c3fc0cd8c1848211e02bd  source/image.tar
10a912b941bd55e47ae95030311e9256afb7acef6ffcf084baeae6e61c281705  my-hello-appsec.tar
```
Анализ:
`docker buildx build -t hello-appsec-world .` - сборка образа из Dockerfile с новым скриптом
`docker run hello-appsec-world` - запуск контейнера из собранного образа,
который выводит новое приветствие с именем "AppSec"
`docker save -o my-hello-appsec.tar hello-appsec-world` - сохранение нового образа в файл my-hello-appsec.tar
`docker load -i my-hello-appsec.tar` - загрузка образа из файла, после чего при запуске контейнера выводится новое приветствие
`docker load -i source/image.tar` - загрузка образа из файла image.tar из репозитория, при запуске контейнера выводится старое приветствие "hello appsec world"
`sha256sum source/image.tar my-hello-appsec.tar` - вычисление и сравнение хеш-сумм двух файлов, которые отличаются, что подтверждает различие образов

- [x] 6. Доработайте свой `python` скрипт подключаемыми библиотеками, далее их необходимо разместить в `requirements.txt`. Размещение библиотек в следующем формате:

```txt
typer==0.20.0
pygame==2.6.1
```

Доработан, коммит - 91ec462

- [x] 7. Сделайте `commit`. Повторите сборку приложения по вашему `Dockerfile` для доработанного скрипта `python`. Сохраните `image` в виде .`tar` архива. Сделайте `commit`.
Коммит - 5e48a99
- [x] 8. Выведите на терминале и проанализируйте следующие команды консоли

```bash
$ docker login
$ docker tag hello-appsec-world yourusername/hello-appsec-world
$ docker push yourusername/hello-appsec-world
$ docker inspect yourusername/hello-appsec-world
$ docker container create --name first hello-appsec-world # выпишите id контейнера

$ docker image pull geminishkv/hello-appsec-world
$ docker inspect geminishkvdev/hello-appsec-world
$ docker container create --name second hello-appsec-world
```

```bash
(venv) loltaun@LT-New:~/course_lab1$ docker login

USING WEB-BASED LOGIN

i Info → To sign in with credentials on the command line, use 'docker login -u <username>'


Your one-time device confirmation code is: JWRK-VTRW
Press ENTER to open your browser or submit your device code here: https://login.docker.com/activate

Waiting for authentication in the browser…
Login Succeeded

(venv) loltaun@LT-New:~/course_lab1$ docker tag hello-appsec-world loltaun/hello-appsec-world
(venv) loltaun@LT-New:~/course_lab1$ docker push loltaun/hello-appsec-world
Using default tag: latest
The push refers to repository [docker.io/loltaun/hello-appsec-world]
2e953ee0c794: Pushed
ac4f86f98c38: Pushed
3f0cdbca744e: Pushed
1733a4cd5954: Pushed
7420d4df59a3: Pushed
4d55cfecf366: Pushed
1c0b66d09925: Pushed
779e18b70bec: Pushed
72cf4c3b8301: Pushed
14f3fef620c1: Pushed
latest: digest: sha256:a2eb96c22b9b47404dfb2a1e04564d5924d14a733338cfd69aeefbe9e2b1f4a6 size: 856

(venv) loltaun@LT-New:~/course_lab1$ docker inspect loltaun/hello-appsec-world
[
    {
        "Id": "sha256:a2eb96c22b9b47404dfb2a1e04564d5924d14a733338cfd69aeefbe9e2b1f4a6",
        "RepoTags": [
            "LolTaun/hello-appsec-world:latest",
            "hello-appsec-world:latest",
            "loltaun/hello-appsec-world:latest"
        ],
        "RepoDigests": [
            "LolTaun/hello-appsec-world@sha256:a2eb96c22b9b47404dfb2a1e04564d5924d14a733338cfd69aeefbe9e2b1f4a6",
            "hello-appsec-world@sha256:a2eb96c22b9b47404dfb2a1e04564d5924d14a733338cfd69aeefbe9e2b1f4a6",
            "loltaun/hello-appsec-world@sha256:a2eb96c22b9b47404dfb2a1e04564d5924d14a733338cfd69aeefbe9e2b1f4a6"
        ],
        "Parent": "",
        "Comment": "buildkit.dockerfile.v0",
        "Created": "2025-12-14T12:14:07.390098427Z",
        "DockerVersion": "",
        "Author": "",
        "Architecture": "amd64",
        "Os": "linux",
        "Size": 49507994,
        "GraphDriver": {
            "Data": null,
            "Name": "overlayfs"
        },
        "RootFS": {
            "Type": "layers",
            "Layers": [
                "sha256:77a2b55fbe8b9984ce0af3ffc0b0ab62507668e63306ec161a585e587a3eb164",
                "sha256:424dc4972605239ec660864fe4cc7bcf6ebdadd752a7ee7ad065a83c34798378",
                "sha256:600af8de593b464a3642857b2dce39ad42474145771745962fb90ea9c276fa9d",
                "sha256:fa384bf02ac198a84ae5f0bbe085a6e4bd2de0be1b595833ba52e9780a936ba9",
                "sha256:b40bbdb63cf48b0fed9d198025ef5580912f8cc406eb6de6e85b7aa40ab2aafb",
                "sha256:0e59c47ca6b8a748d0ddd0d736e8199b70a01b482509ea02fd9ea8d8c8f31471",
                "sha256:560164699b9503033681bbc8378348c40cf6a9fd09a19c3d4e5c595769381daa",
                "sha256:59c396292918f2479488bbd6662800e2de7d40d75382ebe8466f69e14bbe3eb3",
                "sha256:f5c5e925f1359f50faabada2776f4daccec84d99330f967022ddf50d50f2bf2d"
            ]
        },
        "Metadata": {
            "LastTagTime": "2025-12-14T18:17:48.481013936Z"
        },
        "Descriptor": {
            "mediaType": "application/vnd.oci.image.index.v1+json",
            "digest": "sha256:a2eb96c22b9b47404dfb2a1e04564d5924d14a733338cfd69aeefbe9e2b1f4a6",
            "size": 856,
            "annotations": {
                "io.containerd.image.name": "docker.io/library/hello-appsec-world:latest",
                "org.opencontainers.image.ref.name": "latest"
            }
        },
        "Config": {
            "ArgsEscaped": true,
            "Cmd": [
                "python",
                "hello.py"
            ],
            "Entrypoint": null,
            "Env": [
                "PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
                "LANG=C.UTF-8",
                "GPG_KEY=A035C8C19219BA821ECEA86B64E628F8D684696D",
                "PYTHON_VERSION=3.11.14",
                "PYTHON_SHA256=8d3ed8ec5c88c1c95f5e558612a725450d2452813ddad5e58fdb1a53b1209b78",
                "PYTHONUNBUFFERED=1"
            ],
            "Labels": null,
            "OnBuild": null,
            "User": "",
            "Volumes": null,
            "WorkingDir": "/hello"
        }
    }
]

loltaun@LT-New:~/course_lab1$ docker image pull geminishkv/hello-appsec-world
Using default tag: latest
Error response from daemon: pull access denied for geminishkv/hello-appsec-world, repository does not exist or may require 'docker login'

```
Анализ:
`docker login` - аутентификация в Docker Hub для возможности пуша образов
`docker tag hello-appsec-world yourusername/hello-appsec-world` - создание тега для образа с указанием репозитория пользователя
`docker push yourusername/hello-appsec-world` - загрузка образа в указанный репозиторий на Docker Hub
`docker inspect yourusername/hello-appsec-world` - получение подробной информации об образе
`docker container create --name first hello-appsec-world` - создание контейнера с именем "first" из образа hello-appsec-world
`docker image pull geminishkv/hello-appsec-world` - попытка загрузки образа из репозитория другого пользователя, но возникает ошибка доступа, так как репозиторий не существует или требует аутентификации



- [x] 9. Выведите на терминале и проанализируйте в консоли процессы, которые запущены, владельцев по пользователям

```bash 
 $ docker container run -it ubuntu /bin/bash
``` 
```bash
loltaun@LT-New:~/course_lab1$ docker container run -it ubuntu /bin/bash
Unable to find image 'ubuntu:latest' locally
latest: Pulling from library/ubuntu
Digest: sha256:c35e29c9450151419d9448b0fd75374fec4fff364a27f176fb458d472dfc9e54
Status: Downloaded newer image for ubuntu:latest
root@beb437bc9a36:/# whoami
root
root@beb437bc9a36:/# id
uid=0(root) gid=0(root) groups=0(root)
root@beb437bc9a36:/# ps aux
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.0   4588  3328 pts/0    Ss   20:45   0:00 /bin/bash
root        11  0.0  0.0   7888  3840 pts/0    R+   20:46   0:00 ps aux
```

Анализ:
`docker container run -it ubuntu /bin/bash` - запуск интерактивного контейнера с образом Ubuntu и доступом к bash-оболочке
`whoami` - команда для определения текущего пользователя внутри контейнера, который является root
`id` - команда для получения информации о пользователе, подтверждающая, что пользователь имеет UID и GID 0 (root)
`ps aux` - команда для отображения всех запущенных процессов внутри контейнера, показывающая, что запущен только bash-процесс и команда ps aux сама по себе


- [x] 10. Выведите оба контейнера first и second на терминал
```bash
loltaun@LT-New:~/course_lab1$ docker ps -a --filter "name=^/first$"
CONTAINER ID   IMAGE                COMMAND             CREATED      STATUS    PORTS     NAMES
a13d1b83bfb5   hello-appsec-world   "python hello.py"   7 days ago   Created             first

loltaun@LT-New:~/course_lab1$ docker ps -a --filter "name=^/second$"
CONTAINER ID   IMAGE                COMMAND             CREATED         STATUS    PORTS     NAMES
100a9b4e6d10   hello-appsec-world   "python hello.py"   3 minutes ago   Created             second
```
- [x] 11. Перейдите в основной корень `lab05` и выведите на терминале, и проанализируйте

```bash 
$ docker-compose up --build
``` 

```bash
loltaun@LT-New:~/course_labs/labs/lab05$ docker-compose up --build
WARN[0000] /home/loltaun/course_labs/labs/lab05/docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion
[+] Building 17.3s (27/27) FINISHED
 => [internal] load local bake definitions                                                                                                                                                                                                             0.0s
 => => reading from stdin 983B                                                                                                                                                                                                                         0.0s
 => [server internal] load build definition from Dockerfile                                                                                                                                                                                            0.0s
 => => transferring dockerfile: 419B                                                                                                                                                                                                                   0.0s
 => [client internal] load build definition from Dockerfile                                                                                                                                                                                            0.0s
 => => transferring dockerfile: 425B                                                                                                                                                                                                                   0.0s
 => [client internal] load metadata for docker.io/library/python:3.11-slim                                                                                                                                                                             2.4s
 => [auth] library/python:pull token for registry-1.docker.io                                                                                                                                                                                          0.0s
 => [server internal] load .dockerignore                                                                                                                                                                                                               0.0s
 => => transferring context: 2B                                                                                                                                                                                                                        0.0s
 => [client internal] load .dockerignore                                                                                                                                                                                                               0.0s
 => => transferring context: 2B                                                                                                                                                                                                                        0.0s
 => CACHED [server builder 1/4] FROM docker.io/library/python:3.11-slim@sha256:158caf0e080e2cd74ef2879ed3c4e697792ee65251c8208b7afb56683c32ea6c                                                                                                        0.0s
 => => resolve docker.io/library/python:3.11-slim@sha256:158caf0e080e2cd74ef2879ed3c4e697792ee65251c8208b7afb56683c32ea6c                                                                                                                              0.0s
 => [client internal] load build context                                                                                                                                                                                                               0.0s
 => => transferring context: 576B                                                                                                                                                                                                                      0.0s
 => [server internal] load build context                                                                                                                                                                                                               0.0s
 => => transferring context: 842B                                                                                                                                                                                                                      0.0s
 => [server builder 2/4] WORKDIR /app                                                                                                                                                                                                                  0.0s
 => [client builder 3/4] COPY requirements.txt .                                                                                                                                                                                                       0.0s
 => [server builder 3/4] COPY requirements.txt .                                                                                                                                                                                                       0.0s
 => [server builder 4/4] RUN pip install --upgrade pip && pip wheel --wheel-dir=/wheels -r requirements.txt                                                                                                                                           12.1s
 => [client builder 4/4] RUN pip install --upgrade pip && pip wheel --wheel-dir=/wheels -r requirements.txt                                                                                                                                           11.8s
 => [client stage-1 3/6] COPY --from=builder /wheels /wheels                                                                                                                                                                                           0.0s
 => [client stage-1 4/6] COPY requirements.txt .                                                                                                                                                                                                       0.0s
 => [client stage-1 5/6] RUN pip install --no-index --find-links=/wheels -r requirements.txt                                                                                                                                                           1.3s
 => [server stage-1 3/6] COPY --from=builder /wheels /wheels                                                                                                                                                                                           0.0s
 => [server stage-1 4/6] COPY requirements.txt .                                                                                                                                                                                                       0.0s
 => [server stage-1 5/6] RUN pip install --no-index --find-links=/wheels -r requirements.txt                                                                                                                                                           1.4s
 => [client stage-1 6/6] COPY client.py .                                                                                                                                                                                                              0.0s
 => [client] exporting to image                                                                                                                                                                                                                        0.7s
 => => exporting layers                                                                                                                                                                                                                                0.4s
 => => exporting manifest sha256:b3077ee22e6e1be528d146afb1a7897bc8f414535ab5b202b6e8547f618b3e7c                                                                                                                                                      0.0s
 => => exporting config sha256:bf5eed0d9a8ea26fb3d4b29cc99ffa85c3526bf5198b85e617efb0a83f268b1f                                                                                                                                                        0.0s
 => => exporting attestation manifest sha256:e7535863676859da4b9143389be3da82e68f9db4118b84a53fa91f7557b7ab2c                                                                                                                                          0.0s
 => => exporting manifest list sha256:96a6e0a2ebafc2b9be793a8312920c3f05e67710c0328933ac7ac93faca4cd00                                                                                                                                                 0.0s
 => => naming to docker.io/library/lab05-client:latest                                                                                                                                                                                                 0.0s
 => => unpacking to docker.io/library/lab05-client:latest                                                                                                                                                                                              0.2s
 => [server stage-1 6/6] COPY app.py .                                                                                                                                                                                                                 0.1s
 => [server] exporting to image                                                                                                                                                                                                                        0.8s
 => => exporting layers                                                                                                                                                                                                                                0.4s
 => => exporting manifest sha256:fe3243648d17e601ff1f99993cd7b98008f7909bb11157d8dafeb7401c534096                                                                                                                                                      0.0s
 => => exporting config sha256:0da7d3595b8c3fd297d6def96eb6d060a08068c6cda6337e0e48bd049ab03117                                                                                                                                                        0.0s
 => => exporting attestation manifest sha256:cc17bddeab4a8fde92161677067b1b7f278cdfd723ef3947d931c8db6b917176                                                                                                                                          0.0s
 => => exporting manifest list sha256:b8886a2666597d3ed106905e501d0749265db018c96656e4e9f31ba5f68a68b6                                                                                                                                                 0.0s
 => => naming to docker.io/library/lab05-server:latest                                                                                                                                                                                                 0.0s
 => => unpacking to docker.io/library/lab05-server:latest                                                                                                                                                                                              0.2s
 => [client] resolving provenance for metadata file                                                                                                                                                                                                    0.0s
 => [server] resolving provenance for metadata file                                                                                                                                                                                                    0.0s
[+] Running 5/5
 ✔ lab05-server              Built                                                                                                                                                                                                                     0.0s
 ✔ lab05-client              Built                                                                                                                                                                                                                     0.0s
 ✔ Network lab05_app_net     Created                                                                                                                                                                                                                   0.0s
 ✔ Container lab05-server-1  Created                                                                                                                                                                                                                   0.1s
 ✔ Container lab05-client-1  Created                                                                                                                                                                                                                   0.1s
Attaching to client-1, server-1
server-1  |  * Serving Flask app 'app'
server-1  |  * Debug mode: off
server-1  | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
server-1  |  * Running on all addresses (0.0.0.0)
server-1  |  * Running on http://127.0.0.1:8000
server-1  |  * Running on http://172.21.0.2:8000
server-1  | Press CTRL+C to quit
server-1  | 172.21.0.3 - - [21/Dec/2025 20:59:57] "GET / HTTP/1.1" 200 -
client-1  |
client-1  |     <html>
```
Анализ:
`docker-compose up --build` - команда для сборки и запуска многоконтейнерного приложения, определенного в файле docker-compose.yml.
В процессе выполнения команды происходит:
- Сборка образов для сервисов "server" и "client" на основе указанных Dockerfile.
- Создание сети "lab05_app_net" для взаимодействия контейнеров.
- Создание и запуск контейнеров "lab05-server-1" и "lab05-client-1".
- Вывод логов работы контейнеров, включая запуск Flask-сервера и обработку HTTP-запросов.

- [x] 12. Откройте соседнее окно терминала и и выведите на терминале

```bash 
$ open -a "Google Chrome" http://localhost:8000
```
Данная команда только для macOS.
При открытии Chrome по ссылке:
![alt text](https://raw.githubusercontent.com/LolTaun/course_labs/refs/heads/lab5/labs/lab05/Report/image-1.png)

- [ ] 13. Остановите работу `docker-compose`.

```bash 
$ docker ps -a
$ docker ps -q
$ docker images

$ docker ps -q | xargs docker stop
$ docker-compose down
```

```bash
loltaun@LT-New:~/course_lab1$ docker ps -a
CONTAINER ID   IMAGE                           COMMAND                  CREATED          STATUS                      PORTS                                         NAMES
5420a2572331   lab05-client                    "python client.py"       5 seconds ago    Up 4 seconds                                                              lab05-client-1
c18f32f8acbc   lab05-server                    "python app.py"          5 seconds ago    Up 4 seconds                0.0.0.0:8000->8000/tcp, [::]:8000->8000/tcp   lab05-server-1
100a9b4e6d10   hello-appsec-world              "python hello.py"        12 minutes ago   Created                                                                   second
beb437bc9a36   ubuntu                          "/bin/bash"              22 minutes ago   Exited (0) 17 minutes ago                                                 fervent_jang
a5333f5420c1   registry:2                      "/entrypoint.sh /etc…"   6 hours ago      Up 6 hours                  5000/tcp                                      registry.1.osg8h11js4dpq42kcs38u06kc
d25c23739d8e   registry:2                      "/entrypoint.sh /etc…"   7 hours ago      Exited (255) 6 hours ago    5000/tcp                                      registry.1.0npb9y5c5dr8mnofcka2t9v8n
5e1a9ec84291   registry:2                      "/entrypoint.sh /etc…"   4 days ago       Exited (255) 8 hours ago    5000/tcp                                      registry.1.lxcpih6g0wqmi91hgpfv9a4bh
2637fc8ae4da   registry:2                      "/entrypoint.sh /etc…"   6 days ago       Exited (2) 6 days ago                                                     registry.1.s4cifdmqe47rmt3g8vzuumalc
31b11c417863   registry:2                      "/entrypoint.sh /etc…"   6 days ago       Exited (255) 6 days ago     5000/tcp                                      registry.1.mjvezw243q4kr7u9kz35l3xt9
a13d1b83bfb5   hello-appsec-world              "python hello.py"        7 days ago       Created                                                                   first
258d1071b4a8   hello-appsec-world              "python hello.py"        7 days ago       Exited (0) 7 days ago                                                     bold_bartik
872ec83d606b   cd05704168ff                    "python -u hello.py …"   7 days ago       Exited (0) 7 days ago                                                     hardcore_snyder
d390746f1208   cd05704168ff                    "python -u hello.py …"   7 days ago       Exited (0) 7 days ago                                                     quizzical_jang
71438f771101   hello-appsec-world              "python hello.py"        7 days ago       Exited (0) 7 days ago                                                     cool_ride
aa2929a5e256   hello-appsec-world              "python hello.py"        7 days ago       Exited (0) 7 days ago                                                     sweet_pare
3e7073f69a9c   my-hello-appsec                 "python -u docker ru…"   7 days ago       Exited (2) 7 days ago                                                     zealous_keller
3e50f1fe2284   my-hello-appsec                 "python -u Den"          7 days ago       Exited (2) 7 days ago                                                     exciting_feistel
fafa9f0fa5da   my-hello-appsec                 "python -u hello.py"     7 days ago       Exited (2) 7 days ago                                                     elegant_kilby
d33a3d0a6dcb   d447801db342                    "python -u screen.py"    7 days ago       Exited (130) 7 days ago                                                   pensive_banzai
c701a255f95d   290b5236263e                    "python -u Den"          7 days ago       Exited (2) 7 days ago                                                     hardcore_elbakyan
821e59eeff37   290b5236263e                    "python -u hello.py"     7 days ago       Exited (2) 7 days ago                                                     zen_moore
721229b691f9   5d2979a640c2                    "python hello.py"        7 days ago       Exited (0) 7 days ago                                                     strange_chebyshev
f53fe85a4a28   77cf81e0abcc                    "python hello.py"        7 days ago       Exited (0) 7 days ago                                                     eloquent_snyder
d8c306d408fe   ghcr.io/digininja/dvwa:latest   "docker-php-entrypoi…"   8 days ago       Exited (137) 8 days ago                                                   dvwa-dvwa-1
a673a06c7b46   mariadb:10                      "docker-entrypoint.s…"   5 weeks ago      Exited (0) 8 days ago                                                     dvwa-db-1


loltaun@LT-New:~/course_lab1$ docker ps -q
5420a2572331
c18f32f8acbc
a5333f5420c1

loltaun@LT-New:~/course_lab1$ docker images
REPOSITORY                   TAG       IMAGE ID       CREATED         SIZE
lab05-server                 latest    d8382f03bdfd   9 minutes ago   211MB
lab05-client                 latest    5e0e710198fd   9 minutes ago   208MB
<none>                       <none>    cd05704168ff   7 days ago      596MB
my-hello-appsec              latest    a62ded79f402   7 days ago      596MB
<none>                       <none>    77cf81e0abcc   7 days ago      203MB
hellow-appsec-world          latest    68e8e2460d8a   7 days ago      203MB
LolTaun/hello-appsec-world   latest    a2eb96c22b9b   7 days ago      203MB
hello-appsec-world           latest    a2eb96c22b9b   7 days ago      203MB
loltaun/hello-appsec-world   latest    a2eb96c22b9b   7 days ago      203MB
ghcr.io/digininja/dvwa       latest    3f8b0aff6f0f   9 days ago      885MB
hadoop/submit                3.4.2     a68d3ae144af   9 days ago      3.88GB
hadoop/historyserver         3.4.2     4961133b9d73   9 days ago      3.88GB
hadoop/nodemanager           3.4.2     52a7384770b0   9 days ago      3.88GB
hadoop/resourcemanager       3.4.2     93b2d7beccc2   9 days ago      3.88GB
hadoop/datanode              3.4.2     970493243c7f   9 days ago      3.88GB
hadoop/namenode              3.4.2     954c4b3907e9   3 weeks ago     3.88GB
hadoop/basic                 3.4.2     b0d0135f8ad9   3 weeks ago     3.88GB
jupyterlab/core              4.4.9     0b0bdd3fa000   3 weeks ago     4.66GB
spark/core                   3.5.7     d1ae87be15a0   3 weeks ago     3.81GB
127.0.0.1:5000/mpi           latest    7c4617d46f34   5 weeks ago     1.93GB
127.0.0.1:5000/mpi           latest    fe332e19f608   5 weeks ago     1.93GB
mariadb                      10        8763a63f00ec   5 weeks ago     460MB
structurizr/onpremises       latest    4b5ffb5119c8   6 weeks ago     807MB
structurizr/lite             latest    17b4965db511   6 weeks ago     881MB
<none>                       <none>    446ef97ca014   6 weeks ago     868MB
ubuntu                       latest    c35e29c94501   2 months ago    117MB
voice_recognizer-asr         latest    9d9224e1993f   4 months ago    2.02GB
registry                     2         a3d8aaa63ed8   2 years ago     37.2MB

loltaun@LT-New:~/course_lab1$ docker ps -q | xargs docker stop
5420a2572331
c18f32f8acbc
a5333f5420c1

loltaun@LT-New:~/course_labs/labs/lab05$ docker-compose down
WARN[0000] /home/loltaun/course_labs/labs/lab05/docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion
[+] Running 3/3
 ✔ Container lab05-client-1  Removed                                                                                                                                                                                                                   0.0s
 ✔ Container lab05-server-1  Removed                                                                                                                                                                                                                   0.0s
 ✔ Network lab05_app_net     Removed                                                                                                                                                                                                                   0.3s
```

- [x] 14. Доработайте `docker-compose` и скрипт, который вы подготовили ранее, что бы вы смогли воспроизвести шаги п.11 по п.13 с демонстрацией. Сделайте `commit`.

![alt text](https://raw.githubusercontent.com/LolTaun/course_labs/refs/heads/lab5/labs/lab05/Report/image-2.png)
Коммит - e17fbbb

- [x] 15. Залейте изменения в свой удаленный репозиторий, проверьте историю `commit`.
```bash
loltaun@LT-New:~/course_lab1$ git log --oneline --graph --decorate --all
* e17fbbb (HEAD -> master, origin/master) Added docker-compose for local web deployment
* 91ec462 .gitignore and requirements.txt improved
* 19ec28d Minor fixes
* 9243c69 major rework with new Dockerfile for project
* d3400be Added Hello-Appsec-World with Dockerfile
* 78e6076 Fill nmapres.txt with data from nmapres_new.txt
* 9639b81 Added nmapres.txt
* f759ccc Added screen.py for future
*   3e2f07d (patch2) Merge pull request #2 from LolTaun/patch2
|\
| * 4088cd8 (origin/patch2) Code style adjustments (fix coflicts)
|/
* e499909 Minor comment change
*   0d204e1 Merge pull request #1 from LolTaun/patch1
|\
| * f0a026b Added comments to hello.py
| * d539d2a Major hello.py rework for patch1
|/
* 6ea3cd9 Added user name to hello.py
* b48c275 Added hello.py
* 39d47f4 Test
```

- [x] 16. Подготовьте отчет `gist`.
https://gist.github.com/LolTaun/dba58dc3313e629db00a92f61ff596e7
***