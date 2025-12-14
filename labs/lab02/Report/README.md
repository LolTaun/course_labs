<div align="center">
<h1><a id="intro">Лабораторная работа №2</a><br></h1>
<a href="https://docs.github.com/en"><img src="https://img.shields.io/static/v1?logo=github&logoColor=fff&label=&message=Docs&color=36393f&style=flat" alt="GitHub Docs"></a>
<a href="https://daringfireball.net/projects/markdown"><img src="https://img.shields.io/static/v1?logo=markdown&logoColor=fff&label=&message=Markdown&color=36393f&style=flat" alt="Markdown"></a> 
<a href="https://symbl.cc/en/unicode-table"><img src="https://img.shields.io/static/v1?logo=unicode&logoColor=fff&label=&message=Unicode&color=36393f&style=flat" alt="Unicode"></a> 
<a href="https://shields.io"><img src="https://img.shields.io/static/v1?logo=shieldsdotio&logoColor=fff&label=&message=Shields&color=36393f&style=flat" alt="Shields"></a>
<a href="https://img.shields.io/badge/Risk_Analyze-2448a2"><img src="https://img.shields.io/badge/Course-Risk_Analysis-2448a2" alt= "RA"></a> <img src="https://img.shields.io/badge/AppSec-2448a2" alt= "RA"></a> <img src="https://img.shields.io/badge/Contributor-Кузнецов Д. А.-8b9aff" alt="Contributor Badge"></a></div>

- [x] 1. Выведите на терминале и проанализируйте следующие команды консоли

```bash
loltaun@LT-New:~/course_labs$ who | wc -l
1

loltaun@LT-New:~/course_labs$ id
uid=1000(loltaun) gid=1000(loltaun) groups=1000(loltaun),4(adm),20(dialout),24(cdrom),25(floppy),27(sudo),29(audio),30(dip),44(video),46(plugdev),100(users),107(netdev),1001(docker)

loltaun@LT-New:~/course_labs$ whoami
loltaun

loltaun@LT-New:~/course_labs$ hostnamectl
 Static hostname: LT-New
       Icon name: computer-container
         Chassis: container ☐
      Machine ID: 7eaa505f91c64219abe101fd8c165955
         Boot ID: 05e620f04fda4723a138ffb01014fccb
  Virtualization: wsl
Operating System: Ubuntu 24.04.3 LTS
          Kernel: Linux 6.6.87.2-microsoft-standard-WSL2
    Architecture: x86-64
```

- [x] 2. Выведите утилитой `tree` список вложенности дерева диреторий для каталога своего пользователя. Далее используйте `ls -a` и укажите отличие от `ls -l`.
```bash
tree ~
ls -a
```
`ls -a` показывает все файлы, включая скрытые файлы (те, которые начинаются с точки), в то время как `ls -l` предоставляет список файлов в вертикальном виде с информацией о правах доступа, владельце, размере и дате изменения, но не показывает скрытые файлы по умолчанию.
- [x] 3. Используйте утилиту `file` и `df` для определения какая файловая система на разделе `/dev/sda1`.
```bash
loltaun@LT-New:~/course_labs$ sudo file -s /dev/sdd
/dev/sdd: Linux rev 1.0 ext4 filesystem data, UUID=c64b8192-bdab-454f-a149-ca3d53f479fc (needs journal recovery) (extents) (64bit) (large files) (huge files)
```
```bash
loltaun@LT-New:~/course_labs$ df -T
Filesystem     Type     1K-blocks       Used  Available Use% Mounted on
none           overlay   24050732          0   24050732   0% /usr/lib/modules/6.6.87.2-microsoft-standard-WSL2
none           tmpfs     24050732          4   24050728   1% /mnt/wsl
drivers        9p      3906149372 1139105296 2767044076  30% /usr/lib/wsl/drivers
/dev/sdd       ext4    1055762868   42216124  959843272   5% /
none           tmpfs     24050732         88   24050644   1% /mnt/wslg
none           overlay   24050732          0   24050732   0% /usr/lib/wsl/lib
rootfs         rootfs    24045720       2664   24043056   1% /init
none           tmpfs     24050732        608   24050124   1% /run
none           tmpfs     24050732          0   24050732   0% /run/lock
none           tmpfs     24050732          0   24050732   0% /run/shm
none           overlay   24050732        100   24050632   1% /mnt/wslg/versions.txt
none           overlay   24050732        100   24050632   1% /mnt/wslg/doc
C:\            9p      3906149372 1139105296 2767044076  30% /mnt/c
D:\            9p          354304      48668     305636  14% /mnt/d
F:\            9p       929155068  865165108   63989960  94% /mnt/f
G:\            9p      1023998972  903591320  120407652  89% /mnt/g
H:\            9p      4883735548 3266083436 1617652112  67% /mnt/h
I:\            9p      2000397308 1686336084  314061224  85% /mnt/i
J:\            9p       976642044  709874552  266767492  73% /mnt/j
tmpfs          tmpfs     24050732         16   24050716   1% /run/user/1000
```
- [x] 4. Выведите на терминале и проанализируйте следующие команды консоли

```bash
$ which vi
$ locate hello.py
$ sudo updatedb
$ locate hello
$ touch screen
$ find ~ -name screen
$ locate screen
$ sudo updated
$ locate screen
```
```bash
loltaun@LT-New:~/course_labs/labs/lab02$ which vi
/usr/bin/vi
loltaun@LT-New:~/course_labs/labs/lab02$ locate hello.py
/home/loltaun/course_lab1/hello.py
/home/loltaun/course_labs/labs/lab02/exmpl_hello.py
/home/loltaun/course_labs/labs/lab05/source/hello.py

loltaun@LT-New:~/course_labs/labs/lab02$ sudo updatedb
loltaun@LT-New:~/course_labs/labs/lab02$ locate hello
/home/loltaun/.cache/vscode-cpptools/ipch/81fcd091ba0a2b3/hello.ipch
/home/loltaun/course_lab1/hello.py
/home/loltaun/course_labs/labs/lab02/exmpl_hello.py
/home/loltaun/course_labs/labs/lab05/source/hello.py
/home/loltaun/cpp/parallel_cuda/hello
/home/loltaun/cpp/parallel_cuda/hello/CMakeLists.txt
/home/loltaun/cpp/parallel_cuda/hello/hello
/home/loltaun/cpp/parallel_cuda/hello/hello.cu
/opt/nvidia/hpc_sdk/Linux_x86_64/25.9/comm_libs/13.0/hpcx/hpcx-2.24/ompi/tests/examples/hello_c
/opt/nvidia/hpc_sdk/Linux_x86_64/25.9/comm_libs/13.0/hpcx/hpcx-2.24/ompi/tests/examples/hello_c.c
/opt/nvidia/hpc_sdk/Linux_x86_64/25.9/comm_libs/13.0/hpcx/hpcx-2.24/ompi/tests/examples/hello_cxx.cc
/opt/nvidia/hpc_sdk/Linux_x86_64/25.9/comm_libs/13.0/hpcx/hpcx-2.24/ompi/tests/examples/hello_mpifh
/opt/nvidia/hpc_sdk/Linux_x86_64/25.9/comm_libs/13.0/hpcx/hpcx-2.24/ompi/tests/examples/hello_mpifh.f
...
/usr/lib/x86_64-linux-gnu/open-coarrays/openmpi/bin/OpenCoarrays-2.10.2-tests/asynchronous_hello_world
/usr/lib/x86_64-linux-gnu/open-coarrays/openmpi/bin/OpenCoarrays-2.10.2-tests/hello_multiverse
/usr/share/cmake-3.28/Modules/IntelVSImplicitPath/hello.f
/usr/share/doc/gawk/examples/network/hello-serv.awk
/usr/share/doc/libevent-dev/examples/hello-world.c
/usr/share/doc/libpmix-dev/examples/hello.c
/usr/share/doc/node-chrome-trace-event/examples/hello.js

loltaun@LT-New:~/course_labs/labs/lab02$ touch screen
loltaun@LT-New:~/course_labs/labs/lab02$ find ~ -name screen
/home/loltaun/course_labs/labs/lab02/screen

loltaun@LT-New:~/course_labs/labs/lab02$ locate screen
/home/loltaun/course_lab1/venv/lib/python3.12/site-packages/pip/_vendor/rich/screen.py
/home/loltaun/course_lab1/venv/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__/screen.cpython-312.pyc
/home/loltaun/course_lab1/venv/lib/python3.12/site-packages/rich/screen.py
/home/loltaun/course_lab1/venv/lib/python3.12/site-packages/rich/__pycache__/screen.cpython-312.pyc
/home/loltaun/cpp/parallel_hadoop/venv/lib/python3.12/site-packages/pip/_vendor/rich/screen.py
/home/loltaun/cpp/parallel_hadoop/venv/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__/screen.cpython-312.pyc
/opt/nvidia/hpc_sdk/Linux_x86_64/25.9/profilers/13.0/Nsight_Compute/host/linux-desktop-glibc_2_11_3-x64/Plugins/platforms/libqoffscreen.so
/opt/nvidia/hpc_sdk/Linux_x86_64/25.9/profilers/13.0/Nsight_Compute/host/linux-desktop-glibc_2_11_3-x64/Plugins/wayland-shell-integration/libfullscreen-shell-v1.so
/opt/nvidia/hpc_sdk/Linux_x86_64/25.9/profilers/13.0/Nsight_Systems/documentation/_images/cuda-event-screenshot.png
/opt/nvidia/hpc_sdk/Linux_x86_64/25.9/profilers/13.0/Nsight_Systems/documentation/_images/nvtx-screenshot.png
/opt/nvidia/hpc_sdk/Linux_x86_64/25.9/profilers/13.0/Nsight_Systems/documentation/_images/pin-screenshot.png
/opt/nvidia/hpc_sdk/Linux_x86_64/25.9/profilers/13.0/Nsight_Systems/documentation/_static/nvidia-logo-horiz-rgb-1c-blk-for-screen.svg
/opt/nvidia/hpc_sdk/Linux_x86_64/25.9/profilers/13.0/Nsight_Systems/documentation/_static/nvidia-logo-horiz-rgb-1c-wht-for-screen.svg
/opt/nvidia/hpc_sdk/Linux_x86_64/25.9/profilers/13.0/Nsight_Systems/documentation/_static/nvidia-logo-horiz-rgb-blk-for-screen.svg
/opt/nvidia/hpc_sdk/Linux_x86_64/25.9/profilers/13.0/Nsight_Systems/documentation/_static/nvidia-logo-horiz-rgb-wht-for-screen.svg
/opt/nvidia/hpc_sdk/Linux_x86_64/25.9/profilers/13.0/Nsight_Systems/host-linux-x64/Plugins/platforms/libqoffscreen.so
...
/usr/share/icons/Humanity/apps/22/applets-screenshooter.svg
/usr/share/icons/Humanity/apps/22/gnome-screenshot.svg
/usr/share/icons/Humanity/apps/24/applets-screenshooter.svg
/usr/share/icons/Humanity/apps/24/gnome-screenshot.svg
/usr/share/icons/Humanity/apps/24/kscreensaver.svg
/usr/share/icons/Humanity/apps/24/preferences-desktop-screensaver.svg
/usr/share/icons/Humanity/apps/24/screensaver.svg
/usr/share/icons/Humanity/apps/24/xscreensaver.svg
/usr/share/icons/Humanity/apps/48/applets-screenshooter.svg
/usr/share/icons/Humanity/apps/48/gnome-screenshot.svg
/usr/share/icons/Humanity/apps/48/kscreensaver.svg
/usr/share/icons/Humanity/apps/48/preferences-desktop-screensaver.svg
/usr/share/icons/Humanity/apps/48/screensaver.svg
/usr/share/icons/Humanity/apps/48/xscreensaver.svg
/usr/share/man/man1/byobu-screen.1.gz
/usr/share/man/man1/screendump.1.gz
/usr/share/man/man1/xdg-screensaver.1.gz
/usr/share/nmap/scripts/tn3270-screen.nse
/usr/share/nodejs/caniuse-lite/data/features/fullscreen.js
/usr/share/nodejs/caniuse-lite/data/features/offscreencanvas.js
/usr/share/nodejs/caniuse-lite/data/features/screen-orientation.js
/usr/share/terminfo/s/screen
/usr/share/terminfo/s/screen-256color
/usr/share/terminfo/s/screen-256color-bce
/usr/share/terminfo/s/screen-bce
/usr/share/terminfo/s/screen-s
/usr/share/terminfo/s/screen-w
/usr/share/terminfo/s/screen.xterm-256color
/usr/share/vim/vim91/ftplugin/screen.vim
/usr/share/vim/vim91/syntax/screen.vim

loltaun@LT-New:~/course_lab1$ sudo updated
sudo: updated: command not found

$ locate screen
...
```
Анализ:
`which vi` - показывает путь к исполняемому файлу `vi`.
`locate hello.py` - ищет файлы с именем `hello.py` в базе данных `locate`.
`sudo updatedb` - обновляет базу данных для команды `locate`.
`locate hello` - ищет файлы с именем, содержащим `hello`.
`touch screen` - создает пустой файл с именем `screen`.
`find ~ -name screen` - ищет файл с именем `screen` в домашнем каталоге.
`locate screen` - ищет файлы с именем, содержащим `screen`.
`sudo updated` - ошибка, такой команды нет.
`locate screen` - повторный поиск файлов с именем, содержащим `screen`.

- [x]  5. Используйте конструкцию и вставьте ее в созданный файл ранее. Подключите `pygame` - используем исключительно для стилизации окна.
Используемая конструкция:
```py
import os
import pygame

# Чтобы в WSL не ругался на звук (по желанию)
os.environ["SDL_AUDIODRIVER"] = "dummy"

pygame.init()

# Размеры окна
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Hello appsec world")

# Цвет фона
bg_color = (255, 255, 255)

# Текст
font = pygame.font.SysFont(None, 75)
text = font.render("Hello appsec world*", True, (0, 255, 0))
text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # заливаем фон
    screen.fill(bg_color)

    # рисуем рамку вокруг окна
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, screen_width, screen_height), 1)

    # рисуем текст
    screen.blit(text, text_rect)

    # ОБНОВЛЯЕМ ЭКРАН КАЖДЫЙ КАДР
    pygame.display.flip()

pygame.quit()

```

![alt text](https://raw.githubusercontent.com/LolTaun/course_labs/refs/heads/lab2/labs/lab02/Report/image.png)

- [x] 6. Сделайте `commit` и `push` в свой репозиторий с изменениями в `master branch`. На следующих лабораторных работах мы вернемся к этому файлу.
```bash
loltaun@LT-New:~/course_lab1$ git add screen.py
loltaun@LT-New:~/course_lab1$ git commit -S -m "Added screen.py for future"
[master f759ccc] Added screen.py for future
 1 file changed, 40 insertions(+)
 create mode 100644 screen.py
loltaun@LT-New:~/course_lab1$ git push origin master
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 32 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 1.04 KiB | 1.04 MiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To github.com:LolTaun/course_lab1.git
   3e2f07d..f759ccc  master -> master
```
- [x] 7. Выведите на терминале и проанализируйте следующие команды консоли

```bash
$ groups
$ useradd smallman
$ userdel smallman -rf
$ useradd smallman
$ passwd smallman
$ usermod smallman -c 'Hach Hachov Hacherovich,239,45-67,499-239-45-33'
$ passwd smallman
$ id smallman
$ groupadd -g 1500 readgroup
$ usermod -aG readgroup smallman
$ chmod 666 screen 
```
```bash
loltaun@LT-New:~/course_lab1$ groups
loltaun adm dialout cdrom floppy sudo audio dip video plugdev users netdev docker

loltaun@LT-New:~/course_lab1$ sudo useradd smallman

loltaun@LT-New:~/course_lab1$ sudo userdel smallman -rf
userdel: smallman mail spool (/var/mail/smallman) not found
userdel: smallman home directory (/home/smallman) not found

loltaun@LT-New:~/course_lab1$ sudo useradd smallman

loltaun@LT-New:~/course_lab1$ sudo passwd smallman
New password:
Retype new password:
passwd: password updated successfully

loltaun@LT-New:~/course_lab1$ sudo usermod smallman -c 'Hach Hachov Hacherovich,239,45-67,499-239-45-33'

loltaun@LT-New:~/course_lab1$ sudo passwd smallman
New password:
Retype new password:
passwd: password updated successfully

loltaun@LT-New:~/course_lab1$ id smallman
uid=1001(smallman) gid=1002(smallman) groups=1002(smallman)

loltaun@LT-New:~/course_lab1$ sudo groupadd -g 1500 readgroup

loltaun@LT-New:~/course_lab1$ sudo usermod -aG readgroup smallman

loltaun@LT-New:~/course_lab1$ chmod 666 screen.py
```
**Анализ**:
Командой `groups` посмотрели, в какие группы входит пользователь, от чьего имени запущен терминал.

Пользователя `smallman` создали, тут же попытались удалить с `-rf`, но у него ещё не было ни домашнего каталога, ни почтового ящика — указано в результате `userdel`. Потом пользователя снова создали.

Пользователю `smallman` дважды успешно задали пароль и прописали комментарий (ФИО, кабинет, телефоны) через `usermod -c`.

Проверкой `id smallman` убедились, что у него UID 1001, своя основная группа и больше групп пока нет.

Создали группу `readgroup` с GID 1500 и добавили в неё пользователя `smallman` (`usermod -aG`).
Командой chmod 666 screen.py сделали файл screen.py доступным на чтение и запись всем пользователям, но без права выполнения.

- [x] 8. Выведите группу прав для `screen` и измените, что бы файл был доступен только для чтения созданному пользователю и выведите права этого польователя для измененного файла только используя `readgroup`.
```bash
loltaun@LT-New:~/course_lab1$ ls -l screen.py
-rw-rw-rw- 1 loltaun loltaun 1057 Nov 30 22:33 screen.py

loltaun@LT-New:~/course_lab1$ sudo chown smallman:smallman screen.py

loltaun@LT-New:~/course_lab1$ sudo chmod 400 screen.py

loltaun@LT-New:~/course_lab1$ ls -l screen.py
-r-------- 1 smallman smallman 1057 Nov 30 22:33 screen.py
```
- [x] 9. Используйте `POSIX ACL`. Выведите на терминале и проанализируйте следующие команды консоли

```bash
$ touch nmapres.txt
$ setfacl -m u:smallman:rw nmapres.txt
$ setfacl -m g:readgroup:r nmapres.txt
$ getfacl nmapres.txt
```

```bash
loltaun@LT-New:~/course_lab1$ touch nmapres.txt
loltaun@LT-New:~/course_lab1$ setfacl -m u:smallman:rw nmapres.txt
loltaun@LT-New:~/course_lab1$ setfacl -m g:readgroup:r nmapres.txt
loltaun@LT-New:~/course_lab1$ getfacl nmapres.txt
# file: nmapres.txt
# owner: loltaun
# group: loltaun
user::rw-
user:smallman:rw-
group::r--
group:readgroup:r--
mask::rw-
other::r--
```
При помощи `setfacl` мы задаем ACL-записи:
- пользователю smallman разрешено читать и писать файл
- группе readgroup разрешено только чтение файла

`getfacl` показывает текущие ACL-записи для файла.

- [x] 10. Сохраните файл внутри локального репозитория, так как следующая работа будет подразумевать запись в нее данных о nmap.
```bash
loltaun@LT-New:~/course_lab1$ git add nmapres.txt
loltaun@LT-New:~/course_lab1$ git commit -S -m "Added nmapres.txt"
[master 9639b81] Added nmapres.txt
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 nmapres.txt
```

- [x] 11. Для закрепления выведите все списки групп пользователей на вашей ОС и права на верхнеуровневые каталоги.
```bash
loltaun@LT-New:~/course_lab1$ cat /etc/group
root:x:0:
daemon:x:1:
bin:x:2:
sys:x:3:
adm:x:4:syslog,loltaun
tty:x:5:
disk:x:6:
lp:x:7:
mail:x:8:
news:x:9:
uucp:x:10:
man:x:12:
proxy:x:13:
kmem:x:15:
dialout:x:20:loltaun
fax:x:21:
voice:x:22:
cdrom:x:24:loltaun
floppy:x:25:loltaun
tape:x:26:
sudo:x:27:loltaun
audio:x:29:loltaun
dip:x:30:loltaun
www-data:x:33:
backup:x:34:
operator:x:37:
list:x:38:
irc:x:39:
src:x:40:
shadow:x:42:
utmp:x:43:
video:x:44:loltaun
sasl:x:45:
plugdev:x:46:loltaun
staff:x:50:
games:x:60:
users:x:100:loltaun
nogroup:x:65534:
systemd-journal:x:999:
systemd-network:x:998:
crontab:x:997:
systemd-timesync:x:996:
input:x:995:
sgx:x:994:
kvm:x:993:
render:x:992:
messagebus:x:101:
syslog:x:102:
systemd-resolve:x:991:
uuidd:x:103:
_ssh:x:104:
landscape:x:105:
polkitd:x:990:
admin:x:106:
netdev:x:107:loltaun
loltaun:x:1000:
docker:x:1001:loltaun
rdma:x:108:
ssl-cert:x:109:
mysql:x:110:
plocate:x:111:
smallman:x:1002:
readgroup:x:1500:smallman

loltaun@LT-New:~/course_lab1$ ls -la /
total 2776
drwxr-xr-x  23 root root    4096 Nov 30 20:24 .
drwxr-xr-x  23 root root    4096 Nov 30 20:24 ..
drwxr-xr-x   3 root root    4096 Oct 17 20:39 Docker
lrwxrwxrwx   1 root root       7 Apr 22  2024 bin -> usr/bin
drwxr-xr-x   2 root root    4096 Feb 26  2024 bin.usr-is-merged
drwxr-xr-x   2 root root    4096 Apr 22  2024 boot
drwxr-xr-x  15 root root    3860 Nov 30 20:24 dev
drwxr-xr-x 103 root root    4096 Nov 30 23:08 etc
drwxr-xr-x   3 root root    4096 Oct 16 18:32 home
-rwxrwxrwx   1 root root 2724480 Jun  9 21:32 init
lrwxrwxrwx   1 root root       7 Apr 22  2024 lib -> usr/lib
drwxr-xr-x   2 root root    4096 Apr  8  2024 lib.usr-is-merged
lrwxrwxrwx   1 root root       9 Apr 22  2024 lib64 -> usr/lib64
drwx------   2 root root   16384 Oct 16 18:31 lost+found
drwxr-xr-x   2 root root    4096 Jan  6  2025 media
drwxr-xr-x  11 root root    4096 Oct 16 18:31 mnt
drwxr-xr-x   3 root root    4096 Oct 16 18:38 opt
dr-xr-xr-x 429 root root       0 Nov 30 20:24 proc
drwx------   6 root root    4096 Nov 30 20:24 root
drwxr-xr-x  21 root root     620 Nov 30 22:30 run
lrwxrwxrwx   1 root root       8 Apr 22  2024 sbin -> usr/sbin
drwxr-xr-x   2 root root    4096 Mar 31  2024 sbin.usr-is-merged
drwxr-xr-x   2 root root    4096 Oct 16 18:31 snap
drwxr-xr-x   2 root root    4096 Jan  6  2025 srv
dr-xr-xr-x  13 root root       0 Nov 30 20:24 sys
drwxrwxrwt   8 root root   24576 Nov 30 23:09 tmp
drwxr-xr-x  13 root root    4096 Oct 16 18:33 usr
drwxr-xr-x  14 root root    4096 Nov 14 20:45 var
```

- [x] 12. Выведите все права для файлов и директорий локального репозитория которые имеют различные пользователи  (без использования длинных путей)
```bash
loltaun@LT-New:~/course_lab1$ ls -l
total 20
-rw-r--r--  1 loltaun  loltaun     5 Nov 22 22:18 README.md
-rw-r--r--  1 loltaun  loltaun   575 Nov 23 19:50 hello.py
-rw-rw-r--+ 1 loltaun  loltaun     0 Nov 30 22:54 nmapres.txt
-rw-r--r--  1 loltaun  loltaun    16 Nov 23 17:56 requirements.txt
-rw-r--r--  1 smallman smallman 1057 Nov 30 23:08 screen.py
drwxr-xr-x  5 loltaun  loltaun  4096 Nov 23 11:21 venv
```
- [x] 13. Выведите процессы которые у вас запущены в термине и вне его.
В терминале:
```bash
loltaun@LT-New:~/course_lab1$ ps T
    PID TTY      STAT   TIME COMMAND
  23516 pts/7    Ss     0:00 -bash
  44808 pts/7    R+     0:00 ps T
```
Вне терминала:
```bash
loltaun@LT-New:~/course_lab1$ ps aux
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  0.0  0.0  22208 12032 ?        Ss   20:21   0:01 /sbin/init
root           2  0.0  0.0   3060  1536 ?        Sl   20:21   0:00 /init
root          12  0.0  0.0   3076  1792 ?        Sl   20:21   0:00 plan9 --control-socket 7 --log-level 4 --server-fd 8 --pipe-fd 10 --log-truncate
root          58  0.0  0.0  66880 17800 ?        S<s  20:21   0:00 /usr/lib/systemd/systemd-journald
root         107  0.0  0.0  24972  5888 ?        Ss   20:21   0:00 /usr/lib/systemd/systemd-udevd
systemd+     141  0.0  0.0  21456 12544 ?        Ss   20:21   0:00 /usr/lib/systemd/systemd-resolved
systemd+     142  0.0  0.0  91024  7424 ?        Ssl  20:21   0:00 /usr/lib/systemd/systemd-timesyncd
root         187  0.0  0.0   4236  2816 ?        Ss   20:21   0:00 /usr/sbin/cron -f -P
message+     188  0.0  0.0   9812  5376 ?        Ss   20:21   0:00 @dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
root         196  0.0  0.0  17960  8704 ?        Ss   20:21   0:00 /usr/lib/systemd/systemd-logind
root         206  0.0  0.0   3160  1792 hvc0     Ss+  20:21   0:00 /sbin/agetty -o -p -- \u --noclear --keep-baud - 115200,38400,9600 vt220
syslog       209  0.0  0.0 222508  5376 ?        Ssl  20:21   0:00 /usr/sbin/rsyslogd -n -iNONE
root         224  0.0  0.0   3116  1792 tty1     Ss+  20:21   0:00 /sbin/agetty -o -p -- \u --noclear - linux
root         237  0.0  0.0 107008 22528 ?        Ssl  20:21   0:00 /usr/bin/python3 /usr/share/unattended-upgrades/unattended-upgrade-shutdown --wait-for-signal
mysql        305  0.0  0.2 1424948 104300 ?      Ssl  20:21   0:01 /usr/sbin/mariadbd
root         449  0.0  0.0   6824  4096 pts/1    Ss   20:21   0:00 /bin/login -f
loltaun      503  0.0  0.0  20348 11008 ?        Ss   20:21   0:00 /usr/lib/systemd/systemd --user
loltaun      504  0.0  0.0  21152  3520 ?        S    20:21   0:00 (sd-pam)
loltaun      515  0.0  0.0   6072  5120 pts/1    S+   20:21   0:00 -bash
root         543  0.0  0.0   3064   768 ?        Ss   20:21   0:00 /init
root         544  0.0  0.0   3080  1024 ?        S    20:21   0:00 /init
loltaun      545  0.0  0.0   6336  5376 pts/2    Ss+  20:21   0:00 -bash
root         955  0.0  0.0   3064   768 ?        Ss   20:23   0:00 /init
root         956  0.0  0.0   3080   768 ?        S    20:23   0:00 /init
loltaun      957  0.0  0.0   2800  1536 pts/0    Ss+  20:23   0:00 sh -c "$VSCODE_WSL_EXT_LOCATION/scripts/wslServer.sh" bf9252a2fb45be6893dd8870c0bf37e2e1766d61 stable code-server .vscode
loltaun      958  0.0  0.0   2800  1792 pts/0    S+   20:23   0:00 sh /mnt/c/Users/lolta/.vscode/extensions/ms-vscode-remote.remote-wsl-0.104.3/scripts/wslServer.sh bf9252a2fb45be6893dd887
loltaun      964  0.0  0.0   2800  1792 pts/0    S+   20:23   0:00 sh /home/loltaun/.vscode-server/bin/bf9252a2fb45be6893dd8870c0bf37e2e1766d61/bin/code-server --host=127.0.0.1 --port=0 --
loltaun      968  0.0  0.3 11872392 148228 pts/0 Sl+  20:23   0:09 /home/loltaun/.vscode-server/bin/bf9252a2fb45be6893dd8870c0bf37e2e1766d61/node /home/loltaun/.vscode-server/bin/bf9252a2f
root         979  0.0  0.0   3068   768 ?        Ss   20:23   0:00 /init
root         980  0.0  0.0   3084   768 ?        S    20:23   0:00 /init
loltaun      981  0.0  0.1 1018656 59580 pts/3   Ssl+ 20:23   0:01 /home/loltaun/.vscode-server/bin/bf9252a2fb45be6893dd8870c0bf37e2e1766d61/node -e const net = require('net'); process.std
root         988  0.0  0.0   3068   768 ?        Ss   20:23   0:00 /init
root         989  0.0  0.0   3084   768 ?        S    20:23   0:01 /init
loltaun      990  0.0  0.1 1015216 56088 pts/4   Ssl+ 20:23   0:04 /home/loltaun/.vscode-server/bin/bf9252a2fb45be6893dd8870c0bf37e2e1766d61/node -e const net = require('net'); process.std
loltaun     1020  2.2  1.3 77684140 673048 pts/0 Sl+  20:23   4:08 /home/loltaun/.vscode-server/bin/bf9252a2fb45be6893dd8870c0bf37e2e1766d61/node --dns-result-order=ipv4first /home/loltaun
loltaun     1059  0.0  0.1 1265160 63912 pts/0   Sl+  20:23   0:01 /home/loltaun/.vscode-server/bin/bf9252a2fb45be6893dd8870c0bf37e2e1766d61/node /home/loltaun/.vscode-server/bin/bf9252a2f
loltaun     1072  0.0  0.1 1035676 83856 pts/0   Sl+  20:23   0:02 /home/loltaun/.vscode-server/bin/bf9252a2fb45be6893dd8870c0bf37e2e1766d61/node /home/loltaun/.vscode-server/bin/bf9252a2f
root        1112  0.0  0.0   3076   768 ?        Ss   20:23   0:00 /init
root        1113  0.0  0.0   3076   768 ?        S    20:23   0:00 /init
loltaun     1115  0.0  0.0   2800  1536 pts/6    Ss+  20:23   0:00 /bin/sh -c cd '/home/loltaun/course_labs/labs/lab02' && /bin/sh
loltaun     1118  0.0  0.0   2800  1792 pts/6    S+   20:23   0:00 /bin/sh
loltaun     1128  0.0  0.1 1013532 51940 pts/6   Sl+  20:23   0:00 /home/loltaun/.vscode-server/bin/bf9252a2fb45be6893dd8870c0bf37e2e1766d61/node /home/loltaun/.vscode-remote-containers/di
loltaun     1158  0.0  0.0   2800  1792 pts/6    S+   20:23   0:00 /bin/sh
loltaun     1176  0.0  0.1 1017412 59980 pts/0   Sl+  20:23   0:00 /home/loltaun/.vscode-server/bin/bf9252a2fb45be6893dd8870c0bf37e2e1766d61/node /home/loltaun/.vscode-server/bin/bf9252a2f
polkitd    11795  0.0  0.0 308164  7936 ?        Ssl  21:20   0:00 /usr/lib/polkit-1/polkitd --no-debug
loltaun    21163  0.0  0.0   9448  4864 ?        Ss   22:11   0:00 /usr/bin/dbus-daemon --session --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
loltaun    21860  0.0  0.1 1147984 74564 pts/0   Sl+  22:15   0:03 /home/loltaun/.vscode-server/bin/bf9252a2fb45be6893dd8870c0bf37e2e1766d61/node /home/loltaun/.vscode-server/bin/bf9252a2f
loltaun    21871  0.0  0.0   6328  5376 pts/5    Ss+  22:15   0:00 /bin/bash --init-file /home/loltaun/.vscode-server/bin/bf9252a2fb45be6893dd8870c0bf37e2e1766d61/out/vs/workbench/contrib/
root       23508  0.0  0.0   3064   768 ?        Ss   22:24   0:00 /init
root       23509  0.0  0.0   3080  1024 ?        S    22:24   0:00 /init
loltaun    23516  0.0  0.0   7524  6400 pts/7    Ss   22:24   0:00 -bash
root       25957  0.0  0.0   3068   768 ?        Ss   22:31   0:00 /init
root       25958  0.0  0.0   3084   768 ?        S    22:31   0:00 /init
loltaun    25959  0.0  0.1 1022008 61712 pts/8   Ssl+ 22:31   0:00 /home/loltaun/.vscode-server/bin/bf9252a2fb45be6893dd8870c0bf37e2e1766d61/node -e const net = require('net'); process.std
root       25966  0.0  0.0   3068   768 ?        Ss   22:31   0:00 /init
root       25967  0.0  0.0   3084   768 ?        S    22:31   0:00 /init
loltaun    25968  0.0  0.1 1014320 55284 pts/9   Ssl+ 22:31   0:00 /home/loltaun/.vscode-server/bin/bf9252a2fb45be6893dd8870c0bf37e2e1766d61/node -e const net = require('net'); process.std
loltaun    25975  1.9  1.1 76985408 537908 pts/0 Sl+  22:31   1:00 /home/loltaun/.vscode-server/bin/bf9252a2fb45be6893dd8870c0bf37e2e1766d61/node --dns-result-order=ipv4first /home/loltaun
loltaun    25986  0.0  0.1 1262776 60128 pts/0   Sl+  22:31   0:00 /home/loltaun/.vscode-server/bin/bf9252a2fb45be6893dd8870c0bf37e2e1766d61/node /home/loltaun/.vscode-server/bin/bf9252a2f
root       26071  0.0  0.0   3076   768 ?        Ss   22:31   0:00 /init
root       26072  0.0  0.0   3076   768 ?        S    22:31   0:00 /init
loltaun    26073  0.0  0.0   2800  1536 pts/11   Ss+  22:31   0:00 /bin/sh -c cd '/home/loltaun/course_lab1' && /bin/sh
loltaun    26074  0.0  0.0   2800  1792 pts/11   S+   22:31   0:00 /bin/sh
loltaun    26084  0.0  0.1 1013516 52652 pts/11  Sl+  22:31   0:00 /home/loltaun/.vscode-server/bin/bf9252a2fb45be6893dd8870c0bf37e2e1766d61/node /home/loltaun/.vscode-remote-containers/di
loltaun    26132  0.0  0.0   2800  1792 pts/11   S+   22:31   0:00 /bin/sh
loltaun    26172  0.0  0.0   6328  5376 pts/12   Ss+  22:31   0:00 /bin/bash --init-file /home/loltaun/.vscode-server/bin/bf9252a2fb45be6893dd8870c0bf37e2e1766d61/out/vs/workbench/contrib/
loltaun    26645  0.0  0.0 226284  3328 ?        SLsl 22:32   0:00 /usr/bin/gpg-agent --supervised
```

- [x] 14. Оформить `README.md` по аналогии и использовать `shield`, etc.
Это и есть он ;)
- [x] 15. Составить `gist` отчет и отправить ссылку личным сообщением
Ссылка на gist: https://gist.github.com/LolTaun/b3482e88cc18fc2308d63126ec903591
***

Copyright (c) 2025 Denis Kuznetsov