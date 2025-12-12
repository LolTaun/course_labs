<div align="center">
<h1><a id="intro">Лабораторная работа №3</a><br></h1>
<a href="https://docs.github.com/en"><img src="https://img.shields.io/static/v1?logo=github&logoColor=fff&label=&message=Docs&color=36393f&style=flat" alt="GitHub Docs"></a>
<a href="https://daringfireball.net/projects/markdown"><img src="https://img.shields.io/static/v1?logo=markdown&logoColor=fff&label=&message=Markdown&color=36393f&style=flat" alt="Markdown"></a> 
<a href="https://symbl.cc/en/unicode-table"><img src="https://img.shields.io/static/v1?logo=unicode&logoColor=fff&label=&message=Unicode&color=36393f&style=flat" alt="Unicode"></a> 
<a href="https://shields.io"><img src="https://img.shields.io/static/v1?logo=shieldsdotio&logoColor=fff&label=&message=Shields&color=36393f&style=flat" alt="Shields"></a>
<a href="https://img.shields.io/badge/Risk_Analyze-2448a2"><img src="https://img.shields.io/badge/Course-Risk_Analysis-2448a2" alt= "RA"></a> <img src="https://img.shields.io/badge/AppSec-2448a2" alt= "RA"></a> <img src="https://img.shields.io/badge/Contributor-Кузнецов Д. А.-8b9aff" alt="Contributor Badge"></a></div>


- [x] 1. Опишите используемые методы по их назначению, как они функционируют и какие результаты могут дать для оценки. Используйте сноску из материалов выше по флагам команд.

| Scan type            | nmap option      | Описание |
|----------------------|------------------|-----------|
| **TCP Connect**      | `-sT`            | Полный TCP-handshake для определения открытых портов; легко обнаруживается. |
| **TCP SYN (stealth)**| `-sS`            | Полуоткрытое скрытное SYN-сканирование; минимальные следы, быстрый анализ состояния порта. |
| **UDP Scan**         | `-sU`            | Проверка UDP-служб через анализ ответов сервиса или ICMP ошибок; медленнее, но необходимо для UDP. |
| **TCP FIN**          | `-sF`            | FIN-пакет для обхода простых фильтров; отсутствие ответа = open\|filtered, RST = closed. |
| **TCP ACK**          | `-sA`            | Определение фильтрации: RST = unfiltered, отсутствие ответа = filtered. |
| **TCP Xmas Tree**    | `-sX`            | FIN/PSH/URG-пакет; тестирование стека и скрытность; аналог поведения NULL/FIN. |
| **TCP NULL**         | `-sN`            | Пакет без флагов; отсутствие ответа = open\|filtered, RST = closed. |
| **ICMP Ping Scan**   | `-sn`, `-PE/PP/PM` | Определение активности хостов через ICMP Echo/Timestamp/Netmask. |
| **FTP-Proxy Scan**   | (FTP proxy)      | Косвенное сканирование через FTP-сервер, заставляя его подключаться к целевым портам. |
| **Idle Scan**        | `-sI`            | Полностью скрытное сканирование с использованием «зомби» и анализа IPID; источник не раскрывается. |


- [x] 2. Выведите на терминале и проанализируйте следующие команды консоли

```bash
loltaun@LT-New:~/course_labs$ nmap localhost
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-12-01 19:13 EAT
Nmap scan report for localhost (127.0.0.1)
Host is up (0.000032s latency).
Not shown: 999 closed tcp ports (conn-refused)
PORT     STATE SERVICE
3306/tcp open  mysql

Nmap done: 1 IP address (1 host up) scanned in 0.02 seconds
loltaun@LT-New:~/course_labs$ nmap -sC localhost
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-12-01 19:13 EAT
Nmap scan report for localhost (127.0.0.1)
Host is up (0.000029s latency).
Not shown: 999 closed tcp ports (conn-refused)
PORT     STATE SERVICE
3306/tcp open  mysql
| mysql-info:
|   Protocol: 10
|   Version: 5.5.5-10.11.13-MariaDB-0ubuntu0.24.04.1
|   Thread ID: 34
|   Capabilities flags: 63486
|   Some Capabilities: InteractiveClient, Support41Auth, ConnectWithDatabase, SupportsCompression, Speaks41ProtocolOld, IgnoreSigpipes, SupportsTransactions, SupportsLoadDataLocal, Speaks41ProtocolNew, LongColumnFlag, DontAllowDatabaseTableColumn, ODBCClient, IgnoreSpaceBeforeParenthesis, FoundRows, SupportsMultipleStatments, SupportsMultipleResults, SupportsAuthPlugins
|   Status: Autocommit
|   Salt: KXW-y>d^+[hzLKt)jZgt
|_  Auth Plugin Name: mysql_native_password

Nmap done: 1 IP address (1 host up) scanned in 0.16 seconds


loltaun@LT-New:~/course_labs$ nmap -p localhost
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-12-01 19:13 EAT
Found no matches for the service mask 'localhost' and your specified protocols
QUITTING!


loltaun@LT-New:~/course_labs$ nmap -O localhost
TCP/IP fingerprinting (for OS scan) requires root privileges.
QUITTING!


loltaun@LT-New:~/course_labs$ sudo nmap -O localhost
[sudo] password for loltaun:
Sorry, try again.
[sudo] password for loltaun:
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-12-01 19:14 EAT
Nmap scan report for localhost (127.0.0.1)
Host is up (0.000028s latency).
Not shown: 999 closed tcp ports (reset)
PORT     STATE SERVICE
3306/tcp open  mysql
Device type: general purpose
Running: Linux 2.6.X
OS CPE: cpe:/o:linux:linux_kernel:2.6.32
OS details: Linux 2.6.32
Network Distance: 0 hops

OS detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 1.38 seconds

loltaun@LT-New:~/course_labs$ nmap -p 80 localhost
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-12-01 19:24 EAT
Nmap scan report for localhost (127.0.0.1)
Host is up (0.000067s latency).

PORT   STATE  SERVICE
80/tcp closed http

Nmap done: 1 IP address (1 host up) scanned in 0.01 seconds


loltaun@LT-New:~/course_labs$ nmap -p 443 localhost
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-12-01 19:24 EAT
Nmap scan report for localhost (127.0.0.1)
Host is up (0.000061s latency).

PORT    STATE  SERVICE
443/tcp closed https

Nmap done: 1 IP address (1 host up) scanned in 0.01 seconds


loltaun@LT-New:~/course_labs$ nmap -p 8443 localhost
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-12-01 19:24 EAT
Nmap scan report for localhost (127.0.0.1)
Host is up (0.000059s latency).

PORT     STATE  SERVICE
8443/tcp closed https-alt

Nmap done: 1 IP address (1 host up) scanned in 0.01 seconds


loltaun@LT-New:~/course_labs$ nmap -p "*" localhost
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-12-01 19:24 EAT
Nmap scan report for localhost (127.0.0.1)
Host is up (0.000038s latency).
Not shown: 8367 closed tcp ports (conn-refused)
PORT     STATE SERVICE
3306/tcp open  mysql

Nmap done: 1 IP address (1 host up) scanned in 0.06 seconds


loltaun@LT-New:~/course_labs$ nmap -sV -p 22,8080 localhost
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-12-01 19:24 EAT
Nmap scan report for localhost (127.0.0.1)
Host is up (0.000059s latency).

PORT     STATE  SERVICE    VERSION
22/tcp   closed ssh
8080/tcp closed http-proxy

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 0.09 seconds


loltaun@LT-New:~/course_labs$ nmap -sP 192.168.31.0/24
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-12-01 21:38 EAT
Nmap scan report for 192.168.31.1 (192.168.31.1)
Host is up (0.0016s latency).
Nmap scan report for 192.168.31.49 (192.168.31.49)
Host is up (0.0019s latency).
Nmap scan report for 192.168.31.88 (192.168.31.88)
Host is up (0.079s latency).
Nmap scan report for lt-proxmox.loltaun.internal (192.168.31.166)
Host is up (0.00089s latency).
Nmap scan report for 192.168.31.167 (192.168.31.167)
Host is up (0.00082s latency).
Nmap scan report for host.docker.internal (192.168.31.177)
Host is up (0.000037s latency).
Nmap scan report for 192.168.31.190 (192.168.31.190)
Host is up (0.0011s latency).
Nmap done: 256 IP addresses (7 hosts up) scanned in 2.51 seconds


loltaun@LT-New:~/course_labs$ nmap --open 192.168.31.1
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-12-01 21:40 EAT
Nmap scan report for 192.168.31.1 (192.168.31.1)
Host is up (0.012s latency).
Not shown: 996 closed tcp ports (conn-refused)
PORT     STATE SERVICE
53/tcp   open  domain
80/tcp   open  http
443/tcp  open  https
8080/tcp open  http-proxy

Nmap done: 1 IP address (1 host up) scanned in 0.20 seconds


loltaun@LT-New:~/course_labs$ nmap --packet-trace 192.168.31.1
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-12-01 21:41 EAT
CONN (0.0121s) TCP localhost > 192.168.31.1:80 => Operation now in progress
CONN (0.0122s) TCP localhost > 192.168.31.1:443 => Operation now in progress
CONN (0.0132s) TCP localhost > 192.168.31.1:80 => Connected
NSOCK INFO [0.0130s] nsock_iod_new2(): nsock_iod_new (IOD #1)
NSOCK INFO [0.0130s] nsock_connect_udp(): UDP connection requested to 10.255.255.254:53 (IOD #1) EID 8
NSOCK INFO [0.0130s] nsock_read(): Read request from IOD #1 [10.255.255.254:53] (timeout: -1ms) EID 18
NSOCK INFO [0.0130s] nsock_write(): Write request for 43 bytes to IOD #1 EID 27 [10.255.255.254:53]
NSOCK INFO [0.0130s] nsock_trace_handler_callback(): Callback: CONNECT SUCCESS for EID 8 [10.255.255.254:53]
NSOCK INFO [0.0130s] nsock_trace_handler_callback(): Callback: WRITE SUCCESS for EID 27 [10.255.255.254:53]
NSOCK INFO [0.1130s] nsock_trace_handler_callback(): Callback: READ SUCCESS for EID 18 [10.255.255.254:53] (69 bytes): %............1.31.168.192.in-addr.arpa..................192.168.31.1.
NSOCK INFO [0.1130s] nsock_read(): Read request from IOD #1 [10.255.255.254:53] (timeout: -1ms) EID 34
NSOCK INFO [0.1130s] nsock_iod_delete(): nsock_iod_delete (IOD #1)
NSOCK INFO [0.1130s] nevent_delete(): nevent_delete on event #34 (type READ)
CONN (0.1126s) TCP localhost > 192.168.31.1:110 => Operation now in progress
CONN (0.1126s) TCP localhost > 192.168.31.1:443 => Operation now in progress
CONN (0.1126s) TCP localhost > 192.168.31.1:113 => Operation now in progress
CONN (0.1126s) TCP localhost > 192.168.31.1:111 => Operation now in progress
CONN (0.1127s) TCP localhost > 192.168.31.1:135 => Operation now in progress
CONN (0.1127s) TCP localhost > 192.168.31.1:995 => Operation now in progress
...
CONN (0.1916s) TCP localhost > 192.168.31.1:981 => Connection refused
CONN (0.1917s) TCP localhost > 192.168.31.1:1971 => Connection refused
Nmap scan report for 192.168.31.1 (192.168.31.1)
Host is up (0.0068s latency).
Not shown: 996 closed tcp ports (conn-refused)
PORT     STATE SERVICE
53/tcp   open  domain
80/tcp   open  http
443/tcp  open  https
8080/tcp open  http-proxy

Nmap done: 1 IP address (1 host up) scanned in 0.19 seconds


loltaun@LT-New:~/course_labs$ nmap --packet-trace scanme.nmap.org
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-12-01 21:44 EAT
CONN (0.1143s) TCP localhost > 45.33.32.156:80 => Operation now in progress
CONN (0.1143s) TCP localhost > 45.33.32.156:443 => Operation now in progress
CONN (0.1150s) TCP localhost > 45.33.32.156:443 => Connected
NSOCK INFO [0.1150s] nsock_iod_new2(): nsock_iod_new (IOD #1)
NSOCK INFO [0.1150s] nsock_connect_udp(): UDP connection requested to 10.255.255.254:53 (IOD #1) EID 8
NSOCK INFO [0.1150s] nsock_read(): Read request from IOD #1 [10.255.255.254:53] (timeout: -1ms) EID 18
NSOCK INFO [0.1150s] nsock_write(): Write request for 43 bytes to IOD #1 EID 27 [10.255.255.254:53]
NSOCK INFO [0.1150s] nsock_trace_handler_callback(): Callback: CONNECT SUCCESS for EID 8 [10.255.255.254:53]
NSOCK INFO [0.1150s] nsock_trace_handler_callback(): Callback: WRITE SUCCESS for EID 27 [10.255.255.254:53]
NSOCK INFO [0.2210s] nsock_trace_handler_callback(): Callback: READ SUCCESS for EID 18 [10.255.255.254:53] (97 bytes)
NSOCK INFO [0.2210s] nsock_read(): Read request from IOD #1 [10.255.255.254:53] (timeout: -1ms) EID 34
NSOCK INFO [0.2210s] nsock_iod_delete(): nsock_iod_delete (IOD #1)
NSOCK INFO [0.2210s] nevent_delete(): nevent_delete on event #34 (type READ)
CONN (0.2220s) TCP localhost > 45.33.32.156:1025 => Operation now in progress
CONN (0.2221s) TCP localhost > 45.33.32.156:5900 => Operation now in progress
CONN (0.2221s) TCP localhost > 45.33.32.156:80 => Operation now in progress
...
CONN (0.2833s) TCP localhost > 45.33.32.156:17 => Connected
CONN (0.2833s) TCP localhost > 45.33.32.156:1093 => Connected
CONN (0.2833s) TCP localhost > 45.33.32.156:7007 => Connected
Nmap scan report for scanme.nmap.org (45.33.32.156)
Host is up (0.00090s latency).
Other addresses for scanme.nmap.org (not scanned): 2600:3c01::f03c:91ff:fe18:bb2f

PORT      STATE SERVICE
1/tcp     open  tcpmux
3/tcp     open  compressnet
4/tcp     open  unknown
6/tcp     open  unknown
7/tcp     open  echo
9/tcp     open  discard
13/tcp    open  daytime
17/tcp    open  qotd
19/tcp    open  chargen
20/tcp    open  ftp-data
21/tcp    open  ftp
22/tcp    open  ssh
23/tcp    open  telnet
24/tcp    open  priv-mail
25/tcp    open  smtp
26/tcp    open  rsftp
30/tcp    open  unknown
32/tcp    open  unknown
33/tcp    open  dsp
37/tcp    open  time
42/tcp    open  nameserver
43/tcp    open  whois
49/tcp    open  tacacs
53/tcp    open  domain
70/tcp    open  gopher
79/tcp    open  finger
80/tcp    open  http
81/tcp    open  hosts2-ns
82/tcp    open  xfer
83/tcp    open  mit-ml-dev
84/tcp    open  ctf
85/tcp    open  mit-ml-dev
88/tcp    open  kerberos-sec
89/tcp    open  su-mit-tg
90/tcp    open  dnsix
99/tcp    open  metagram
100/tcp   open  newacct
106/tcp   open  pop3pw
109/tcp   open  pop2
110/tcp   open  pop3
111/tcp   open  rpcbind
113/tcp   open  ident
119/tcp   open  nntp
125/tcp   open  locus-map
...
61900/tcp open  unknown
62078/tcp open  iphone-sync
63331/tcp open  unknown
64623/tcp open  unknown
64680/tcp open  unknown
65000/tcp open  unknown
65129/tcp open  unknown
65389/tcp open  unknown

Nmap done: 1 IP address (1 host up) scanned in 0.29 seconds


loltaun@LT-New:~/course_labs$ nmap --iflist
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-12-01 21:45 EAT
************************INTERFACES************************
DEV       (SHORT)     IP/MASK                   TYPE     UP   MTU   MAC
lo        (lo)        127.0.0.1/8               loopback up   65536
lo        (lo)        10.255.255.254/8          loopback up   65536
lo        (lo)        ::1/128                   loopback up   65536
eth0      (eth0)      (none)/0                  ethernet down 1500  00:50:56:C0:00:08
eth1      (eth1)      (none)/0                  ethernet down 1500  00:50:56:C0:00:0A
eth2      (eth2)      (none)/0                  ethernet down 1500  2C:9C:58:51:37:57
eth3      (eth3)      172.19.0.1/28             ethernet up   9000  00:15:5D:FE:A5:0B
eth4      (eth4)      (none)/0                  ethernet down 1500  00:FF:19:22:B7:1D
eth5      (eth5)      192.168.31.177/24         ethernet up   1500  60:CF:84:AA:4A:4A
eth5      (eth5)      fe80::841:e1e:1419:306/64 ethernet up   1500  60:CF:84:AA:4A:4A
eth6      (eth6)      (none)/0                  ethernet down 1500  00:50:56:C0:00:01
loopback0 (loopback0) (none)/0                  ethernet up   1500  00:15:5D:90:A3:1E
eth7      (eth7)      (none)/0                  ethernet down 1500  2E:9C:58:51:07:67
eth8      (eth8)      (none)/0                  ethernet down 1500  2E:9C:58:51:17:77

**************************ROUTES**************************
DST/MASK                   DEV  METRIC GATEWAY
192.168.31.1/32            eth5 281
172.19.0.0/28              eth3 256
192.168.31.0/24            eth5 281
0.0.0.0/0                  eth3 0
0.0.0.0/0                  eth5 281    192.168.31.1
::1/128                    lo   0
fe80::841:e1e:1419:306/128 eth5 0
fe80::/64                  eth5 281
ff00::/8                   eth5 256


loltaun@LT-New:~/course_labs$ nmap -iL scanme.nmap.org
Failed to open input file scanme.nmap.org for reading: No such file or directory (2)


loltaun@LT-New:~/course_labs$ nmap -A -iL scanme.nmap.org
Failed to open input file scanme.nmap.org for reading: No such file or directory (2)


loltaun@LT-New:~/course_labs$ sudo nmap -sA scanme.nmap.org
[sudo] password for loltaun:
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-12-01 22:36 EAT
Nmap scan report for scanme.nmap.org (45.33.32.156)
Host is up (0.00026s latency).
Other addresses for scanme.nmap.org (not scanned): 2600:3c01::f03c:91ff:fe18:bb2f
All 1000 scanned ports on scanme.nmap.org (45.33.32.156) are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)
MAC Address: 00:15:5D:95:E7:26 (Microsoft)


loltaun@LT-New:~/course_labs$ nmap -PN scanme.nmap.org
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-12-01 22:38 EAT
Nmap scan report for scanme.nmap.org (45.33.32.156)
Host is up (0.0026s latency).
Other addresses for scanme.nmap.org (not scanned): 2600:3c01::f03c:91ff:fe18:bb2f

PORT      STATE SERVICE
1/tcp     open  tcpmux
3/tcp     open  compressnet
4/tcp     open  unknown
6/tcp     open  unknown
7/tcp     open  echo
9/tcp     open  discard
13/tcp    open  daytime
17/tcp    open  qotd
19/tcp    open  chargen
20/tcp    open  ftp-data
21/tcp    open  ftp
22/tcp    open  ssh
23/tcp    open  telnet
24/tcp    open  priv-mail
25/tcp    open  smtp
...
65129/tcp open  unknown
65389/tcp open  unknown

Nmap done: 1 IP address (1 host up) scanned in 0.06 seconds


loltaun@LT-New:~/course_labs$ nmap --script=vuln localhost -vv
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-12-01 22:44 EAT
NSE: Loaded 105 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 2) scan.
Initiating NSE at 22:44
Completed NSE at 22:44, 10.01s elapsed
NSE: Starting runlevel 2 (of 2) scan.
Initiating NSE at 22:44
Completed NSE at 22:44, 0.00s elapsed
Initiating Ping Scan at 22:44
Scanning localhost (127.0.0.1) [2 ports]
Completed Ping Scan at 22:44, 0.00s elapsed (1 total hosts)
Initiating Connect Scan at 22:44
Scanning localhost (127.0.0.1) [1000 ports]
Discovered open port 3389/tcp on 127.0.0.1
Discovered open port 445/tcp on 127.0.0.1
Discovered open port 135/tcp on 127.0.0.1
Discovered open port 3306/tcp on 127.0.0.1
Discovered open port 902/tcp on 127.0.0.1
Discovered open port 2179/tcp on 127.0.0.1
Discovered open port 1236/tcp on 127.0.0.1
Discovered open port 10000/tcp on 127.0.0.1
Discovered open port 912/tcp on 127.0.0.1
Discovered open port 5357/tcp on 127.0.0.1
Completed Connect Scan at 22:44, 0.01s elapsed (1000 total ports)
NSE: Script scanning 127.0.0.1.
NSE: Starting runlevel 1 (of 2) scan.
Initiating NSE at 22:44
NSE: [tls-ticketbleed 127.0.0.1:135] Not running due to lack of privileges.
NSE: [firewall-bypass 127.0.0.1] lacks privileges.

loltaun@LT-New:~/course_labs$ sudo nmap --script=vuln localhost -vv
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-12-01 22:44 EAT
NSE: Loaded 105 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 2) scan.
Initiating NSE at 22:44
Completed NSE at 22:44, 10.01s elapsed
NSE: Starting runlevel 2 (of 2) scan.
Initiating NSE at 22:44
Completed NSE at 22:44, 0.00s elapsed
Initiating Ping Scan at 22:44
Scanning localhost (127.0.0.1) [4 ports]
Completed Ping Scan at 22:44, 0.04s elapsed (1 total hosts)
Initiating SYN Stealth Scan at 22:44
Scanning localhost (127.0.0.1) [1000 ports]
Discovered open port 3306/tcp on 127.0.0.1
Completed SYN Stealth Scan at 22:44, 0.03s elapsed (1000 total ports)
NSE: Script scanning 127.0.0.1.
NSE: Starting runlevel 1 (of 2) scan.
Initiating NSE at 22:44
Completed NSE at 22:44, 0.03s elapsed
NSE: Starting runlevel 2 (of 2) scan.
Initiating NSE at 22:44
Completed NSE at 22:44, 0.00s elapsed
Nmap scan report for localhost (127.0.0.1)
Host is up, received reset ttl 64 (0.0000020s latency).
Scanned at 2025-12-01 22:44:46 EAT for 0s
Not shown: 999 closed tcp ports (reset)
PORT     STATE SERVICE REASON
3306/tcp open  mysql   syn-ack ttl 64
|_mysql-vuln-cve2012-2122: ERROR: Script execution failed (use -d to debug)

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 2) scan.
Initiating NSE at 22:44
Completed NSE at 22:44, 0.00s elapsed
NSE: Starting runlevel 2 (of 2) scan.
Initiating NSE at 22:44
Completed NSE at 22:44, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Nmap done: 1 IP address (1 host up) scanned in 10.23 seconds
           Raw packets sent: 1004 (44.152KB) | Rcvd: 1002 (40.084KB)


loltaun@LT-New:~/course_lab1$ nmap -sV --script vuln -oN nmapres_new.txt localhost
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-12-01 23:12 EAT
Nmap scan report for localhost (127.0.0.1)
Host is up (0.0011s latency).
Not shown: 990 closed tcp ports (conn-refused)
PORT      STATE SERVICE            VERSION
135/tcp   open  msrpc              Microsoft Windows RPC
445/tcp   open  microsoft-ds?
902/tcp   open  ssl/vmware-auth    VMware Authentication Daemon 1.10 (Uses VNC, SOAP)
|_ssl-ccs-injection: No reply from server (TIMEOUT)
912/tcp   open  vmware-auth        VMware Authentication Daemon 1.0 (Uses VNC, SOAP)
1236/tcp  open  tcpwrapped
2179/tcp  open  vmrdp?
3306/tcp  open  mysql              MySQL 5.5.5-10.11.13-MariaDB-0ubuntu0.24.04.1
|_mysql-vuln-cve2012-2122: ERROR: Script execution failed (use -d to debug)
3389/tcp  open  ssl/ms-wbt-server?
5357/tcp  open  http               Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
|_http-csrf: Couldn't find any CSRF vulnerabilities.
|_http-dombased-xss: Couldn't find any DOM based XSS.
10000/tcp open  snet-sensor-mgmt?
|_http-vuln-cve2006-3392: ERROR: Script execution failed (use -d to debug)
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_smb-vuln-ms10-054: false
|_smb-vuln-ms10-061: Could not negotiate a connection:SMB: Failed to receive bytes: ERROR
|_samba-vuln-cve-2012-1182: Could not negotiate a connection:SMB: Failed to receive bytes: ERROR

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 218.55 seconds



loltaun@LT-New:~/course_lab1$ cat nmapres_new.txt
# Nmap 7.94SVN scan initiated Mon Dec  1 23:46:10 2025 as: nmap -sV --script vuln -oN nmapres_new.txt localhost
Nmap scan report for localhost (127.0.0.1)
Host is up (0.0016s latency).
Not shown: 990 closed tcp ports (conn-refused)
PORT      STATE SERVICE            VERSION
135/tcp   open  msrpc              Microsoft Windows RPC
445/tcp   open  microsoft-ds?
902/tcp   open  ssl/vmware-auth    VMware Authentication Daemon 1.10 (Uses VNC, SOAP)
|_ssl-ccs-injection: No reply from server (TIMEOUT)
912/tcp   open  vmware-auth        VMware Authentication Daemon 1.0 (Uses VNC, SOAP)
1236/tcp  open  tcpwrapped
2179/tcp  open  vmrdp?
3306/tcp  open  mysql              MySQL 5.5.5-10.11.13-MariaDB-0ubuntu0.24.04.1
|_mysql-vuln-cve2012-2122: ERROR: Script execution failed (use -d to debug)
3389/tcp  open  ssl/ms-wbt-server?
5357/tcp  open  http               Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-csrf: Couldn't find any CSRF vulnerabilities.
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
|_http-dombased-xss: Couldn't find any DOM based XSS.
10000/tcp open  snet-sensor-mgmt?
|_http-vuln-cve2006-3392: ERROR: Script execution failed (use -d to debug)
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_smb-vuln-ms10-054: false
|_samba-vuln-cve-2012-1182: Could not negotiate a connection:SMB: Failed to receive bytes: ERROR
|_smb-vuln-ms10-061: Could not negotiate a connection:SMB: Failed to receive bytes: ERROR

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Dec  1 23:49:49 2025 -- 1 IP address (1 host up) scanned in 218.52 seconds


loltaun@LT-New:~/course_lab1$ grep "VULNERABLE" nmapres_new.txt


loltaun@LT-New:~/course_lab1$ nmap -sV -p 8080 --script vuln -oN ~/project/reports/nmapres_new.txt -oX ~/project/reports/nmapres_new.xml localhost
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-12-11 19:31 EAT
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00037s latency).

PORT     STATE  SERVICE    VERSION
8080/tcp closed http-proxy

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 10.12 seconds


loltaun@LT-New:~/course_lab1$ xsltproc ~/project/reports/nmapres_new.xml -o ~/project/reports/nmapres_new.html
```
Отчет:
![alt text](https://raw.githubusercontent.com/LolTaun/course_labs/refs/heads/lab3/labs/lab03/Report/image.png)

Анализ команд:
1. До переключения в Mirrored-режим (WSL как обычный NAT/видимый как Linux):
    - При сканировании localhost обнаружен один стабильный открытый порт: 3306/tcp (MySQL/MariaDB).
    - Типичные веб- и SSH-порты (80, 443, 22, 8080 и т.д.) — закрыты.
    - OS-сканирование определяет хост как Linux, расстояние 0 hops (локальная WSL-машина).
2. Сканирование локальной сети:
    - В подсети 192.168.31.0/24 найдено несколько активных хостов, включая роутер 192.168.31.1.
    - У роутера открыты 53, 80, 443, 8080/tcp, что указывает на DNS и веб-интерфейсы управления.
    - По интерфейсам видно, что хосчтовой Windows с WSL имеет адрес 192.168.31.177/24 и использует 192.168.31.1 как шлюз.
3. После перевода WSL в Mirrored-режим сети:
    - При последующих сканах localhost стали видны типичные Windows-службы: 135 (MSRPC), 445 (SMB), 3389 (RDP), 5357 (Microsoft HTTPAPI), 902/912/2179/10000 и др.
    - Nmap определяет ОС как Windows.
4. Поиск уязвимостей:
    - Уязвимостные скрипты были запущены как против Linux-служб (MySQL), так и против Windows-служб.
    - Часть проверок прошла успешно и не выявила критичных проблем (нет явных VULNERABLE в отчёте), остальная часть завершилась с ошибками.


- [x] 3. Используйте команду `tree` и выведите все вложенные файлы по директориям.
```bash
loltaun@LT-New:~/course_labs$ tree .
.
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE.md
├── NOTICE.md
├── README.md
├── SECURITY.md
├── artifacts
│   ├── cheetsheet
│   │   ├── Docker_Image_Security_Best_Practices.pdf
│   │   └── gitscm.jpg
│   ├── exmpls
│   │   ├── Аналитический отчет по уязвимости PrintNightmare.pdf
│   │   ├── Пример - Multisignature - Безопасности криптовалютных платежей.pdf
│   │   └── Пример_аналитических_отчетов_по_задачам_ИБ.pdf
│   ├── owasp
│   │   ├── OWASP_Top_10_CICD_Risks.pdf
│   │   ├── Авторизация (Authorization).pdf
│   │   ├── Атаки на клиентов (Client-side Attacks).pdf
│   │   ├── Аутентификация (Authentication).pdf
│   │   ├── Выполнение кода (Command Execution).pdf
│   │   ├── Логические атаки (Logical Attacks).pdf
│   │   └── Разглашение информации (Information Disclosure).pdf
│   └── ppt
│       └── Лекция_Управление Рисками ИБ_intro.pdf
├── assets
│   ├── logotype
│   │   └── logo.jpg
│   └── style
│       └── style.css
├── labs
│   ├── lab01
│   │   ├── README.md
│   │   ├── Report
│   │   │   ├── README.md
│   │   │   └── img
│   │   │       ├── 10-1.png
│   │   │       ├── 11-1.png
│   │   │       ├── 11-2.png
│   │   │       ├── 11-3.png
│   │   │       ├── 12-1.png
│   │   │       ├── 12-2.png
│   │   │       ├── 12-3.png
│   │   │       ├── 12-4.png
│   │   │       ├── 13-1.png
│   │   │       ├── 14-1.png
│   │   │       ├── 15-1.png
│   │   │       ├── 15-2.png
│   │   │       ├── 15-3.png
│   │   │       ├── 16-1.png
│   │   │       ├── 17-1.png
│   │   │       ├── 18-1.png
│   │   │       ├── 19-1.png
│   │   │       ├── 2-1.png
│   │   │       ├── 20-1.png
│   │   │       ├── 20-2.png
│   │   │       ├── 21-1.png
│   │   │       ├── 21-2.png
│   │   │       ├── 22-1.png
│   │   │       ├── 22-2.png
│   │   │       ├── 23-1.png
│   │   │       ├── 24-1.png
│   │   │       ├── 24-2.png
│   │   │       ├── 25-1.png
│   │   │       ├── 25-2.png
│   │   │       ├── 26-1.png
│   │   │       ├── 27-1.png
│   │   │       ├── 29-1.png
│   │   │       ├── 29-2.png
│   │   │       ├── 3-1.png
│   │   │       ├── 6-1.png
│   │   │       ├── 6-2.png
│   │   │       ├── 7-1.png
│   │   │       ├── 8-1.png
│   │   │       ├── 8-2.png
│   │   │       ├── 8-3.png
│   │   │       ├── 8-4.png
│   │   │       └── 9-1.png
│   │   └── typersteel.py
│   ├── lab02
│   │   ├── README.md
│   │   ├── Report
│   │   │   ├── README.md
│   │   │   └── image.png
│   │   ├── exmpl_hello.py
│   │   └── pygamesteel.py
│   ├── lab03
│   │   ├── README.md
│   │   ├── Report
│   │   │   ├── README.md
│   │   │   └── image.png
│   │   └── exmp_targets.txt
│   ├── lab04
│   │   └── README.md
│   ├── lab05
│   │   ├── README.md
│   │   ├── client
│   │   │   ├── Dockerfile
│   │   │   ├── client.py
│   │   │   └── requirements.txt
│   │   ├── docker-compose.yml
│   │   ├── server
│   │   │   ├── Dockerfile
│   │   │   ├── app.py
│   │   │   └── requirements.txt
│   │   └── source
│   │       ├── Dockerfile
│   │       ├── hello.py
│   │       └── requirements.txt
│   └── lab06
│       └── README.md
└── nmapres_new.txt

23 directories, 89 files
```
- [x] 4.Найдите IP сетевой карты `Ethernet`, которая соответствует вашей виртуальной машине используя `ifconfig` и выполните команду

```bash
nmap -sP inet_addr
```

```bash
loltaun@LT-New:~/course_labs$ ifconfig
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 9000
        inet 172.19.0.1  netmask 255.255.255.240  broadcast 172.19.0.15
        ether 00:15:5d:04:a0:e7  txqueuelen 1000  (Ethernet)
        RX packets 1  bytes 42 (42.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 7  bytes 414 (414.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

eth2: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.31.177  netmask 255.255.255.0  broadcast 192.168.31.255
        inet6 fe80::841:e1e:1419:306  prefixlen 64  scopeid 0x20<link>
        ether 60:cf:84:aa:4a:4a  txqueuelen 1000  (Ethernet)
        RX packets 4863  bytes 910768 (910.7 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 169  bytes 11973 (11.9 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 349  bytes 60704 (60.7 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 349  bytes 60704 (60.7 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

loopback0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        ether 00:15:5d:2b:30:f1  txqueuelen 1000  (Ethernet)
        RX packets 41548  bytes 64990808 (64.9 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 41539  bytes 64986078 (64.9 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

```bash
loltaun@LT-New:~/course_labs$ nmap -sP 192.168.31.0/24
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-12-11 20:49 EAT
Nmap scan report for 192.168.31.1 (192.168.31.1)
Host is up (0.0012s latency).
Nmap scan report for 192.168.31.16 (192.168.31.16)
Host is up (0.042s latency).
Nmap scan report for 192.168.31.49 (192.168.31.49)
Host is up (0.0011s latency).
Nmap scan report for 192.168.31.88 (192.168.31.88)
Host is up (0.083s latency).
Nmap scan report for 192.168.31.93 (192.168.31.93)
Host is up (0.0015s latency).
Nmap scan report for 192.168.31.151 (192.168.31.151)
Host is up (0.0026s latency).
Nmap scan report for 192.168.31.152 (192.168.31.152)
Host is up (0.0026s latency).
Nmap scan report for lt-proxmox.loltaun.internal (192.168.31.166)
Host is up (0.0014s latency).
Nmap scan report for 192.168.31.167 (192.168.31.167)
Host is up (0.0025s latency).
Nmap scan report for host.docker.internal (192.168.31.177)
Host is up (0.000032s latency).
Nmap scan report for 192.168.31.190 (192.168.31.190)
Host is up (0.00087s latency).
Nmap done: 256 IP addresses (11 hosts up) scanned in 2.33 seconds
```

- [x] 5. Определите ОС, данные ssh, telnet  с помощью `nmap` и выведите о них информацию.
```bash
loltaun@LT-New:~/course_labs$ sudo nmap -A -p 22,23 192.168.31.0/24
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-12-11 20:51 EAT
Nmap scan report for 192.168.31.1 (192.168.31.1)
Host is up (0.00080s latency).

PORT   STATE  SERVICE VERSION
22/tcp closed ssh
23/tcp closed telnet
MAC Address: 5C:02:14:BB:36:EE (Beijing Xiaomi Mobile Software)
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: phone|broadband router|storage-misc|WAP|general purpose
Running: Google Android 5.X, Linksys embedded, Linux 2.4.X|2.6.X, TP-LINK embedded
OS CPE: cpe:/o:google:android:5.0.1 cpe:/h:linksys:wrv200 cpe:/h:linksys:nas200 cpe:/o:linux:linux_kernel:2.4.36 cpe:/o:linux:linux_kernel:2.6.22 cpe:/h:tp-link:tl-wa801nd
OS details: Android 5.0.1, Linksys WRV200 wireless broadband router, Linksys NAS200 NAS device, DD-WRT v24-sp2 (Linux 2.4.36), Linux 2.6.22 (Kubuntu, x86), Linux 2.6.25 (openSUSE 11.0), Linux 2.6.32, TP-LINK TL-WA801ND WAP (Linux 2.6.36)
Network Distance: 1 hop

TRACEROUTE
HOP RTT     ADDRESS
1   0.80 ms 192.168.31.1 (192.168.31.1)

Nmap scan report for 192.168.31.16 (192.168.31.16)
Host is up (0.030s latency).

PORT   STATE  SERVICE VERSION
22/tcp closed ssh
23/tcp closed telnet
MAC Address: 64:FF:0A:DE:71:4D (Wistron Neweb)
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: phone|broadband router|storage-misc|WAP|general purpose
Running: Google Android 5.X, Linksys embedded, Linux 2.4.X|2.6.X, TP-LINK embedded
OS CPE: cpe:/o:google:android:5.0.1 cpe:/h:linksys:wrv200 cpe:/h:linksys:nas200 cpe:/o:linux:linux_kernel:2.4.36 cpe:/o:linux:linux_kernel:2.6.22 cpe:/h:tp-link:tl-wa801nd
OS details: Android 5.0.1, Linksys WRV200 wireless broadband router, Linksys NAS200 NAS device, DD-WRT v24-sp2 (Linux 2.4.36), Linux 2.6.22 (Kubuntu, x86), Linux 2.6.25 (openSUSE 11.0), Linux 2.6.32, TP-LINK TL-WA801ND WAP (Linux 2.6.36)
Network Distance: 1 hop

TRACEROUTE
HOP RTT      ADDRESS
1   30.16 ms 192.168.31.16 (192.168.31.16)

Nmap scan report for 192.168.31.49 (192.168.31.49)
Host is up (0.00084s latency).

PORT   STATE  SERVICE VERSION
22/tcp open   ssh     OpenSSH 9.2p1 Debian 2+deb12u7 (protocol 2.0)
| ssh-hostkey:
|   256 da:40:aa:55:2c:36:14:34:70:2b:2e:89:97:66:9c:34 (ECDSA)
|_  256 7b:af:df:04:ee:3d:d3:08:ba:05:7f:4d:a2:28:aa:4c (ED25519)
23/tcp closed telnet
MAC Address: BC:24:11:BB:49:FB (Unknown)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.94SVN%E=4%D=12/11%OT=22%CT=23%CU=40004%PV=Y%DS=1%DC=D%G=Y%M=BC2
OS:411%TM=693B04CF%P=x86_64-pc-linux-gnu)SEQ()SEQ(II=I)ECN(R=N)T1(R=N)T2(R=
OS:N)T3(R=N)T4(R=N)T5(R=N)T6(R=N)T7(R=N)U1(R=Y%DF=N%T=40%IPL=164%UN=0%RIPL=
OS:G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=40%CD=S)

Network Distance: 1 hop
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE
HOP RTT     ADDRESS
1   0.84 ms 192.168.31.49 (192.168.31.49)

Nmap scan report for 192.168.31.88 (192.168.31.88)
Host is up (0.056s latency).

PORT   STATE  SERVICE VERSION
22/tcp closed ssh
23/tcp closed telnet
MAC Address: 58:B6:23:62:58:0E (Beijing Xiaomi Mobile Software)
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Aggressive OS guesses: FreeBSD 8.0-RC1-p1 (97%), Cisco 2600 router (IOS 11.3) (92%), Cisco 2500 router (IOS 12.1) (92%), Cisco 2811 router (IOS 12.X) (92%), Cisco 5300 router (IOS 12.3) (92%), Cisco 7200 router (IOS 12.4) (92%), Cisco 870, 2821, 6506, or 7206VXR router (IOS 12.2 - 15.1) (92%), Cisco IOS 12.2 (92%), Cisco 2950, 2960, 3550, 3560, or 3750 switch (IOS 12.1 - 12.2) (92%), Cisco 2960 or 3650 switch (92%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 1 hop

TRACEROUTE
HOP RTT      ADDRESS
1   55.66 ms 192.168.31.88 (192.168.31.88)

Nmap scan report for 192.168.31.93 (192.168.31.93)
Host is up (0.00092s latency).

PORT   STATE  SERVICE VERSION
22/tcp open   ssh     OpenSSH 9.2p1 Debian 2+deb12u7 (protocol 2.0)
| ssh-hostkey:
|   256 0d:f5:e2:d4:85:6c:e7:99:c1:ea:0b:77:f2:37:b6:03 (ECDSA)
|_  256 1f:66:96:c3:ae:52:73:84:e6:74:70:e5:f1:83:ba:43 (ED25519)
23/tcp closed telnet
MAC Address: BC:24:11:55:48:96 (Unknown)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.94SVN%E=4%D=12/11%OT=22%CT=23%CU=30208%PV=Y%DS=1%DC=D%G=Y%M=BC2
OS:411%TM=693B04CF%P=x86_64-pc-linux-gnu)SEQ()SEQ(II=I)ECN(R=N)T1(R=N)T2(R=
OS:N)T3(R=N)T4(R=N)T5(R=N)T6(R=N)T7(R=N)U1(R=Y%DF=N%T=40%IPL=164%UN=0%RIPL=
OS:G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=40%CD=S)

Network Distance: 1 hop
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE
HOP RTT     ADDRESS
1   0.92 ms 192.168.31.93 (192.168.31.93)

Nmap scan report for 192.168.31.151 (192.168.31.151)
Host is up (0.00082s latency).

PORT   STATE  SERVICE VERSION
22/tcp open   ssh     OpenSSH 9.2p1 Debian 2+deb12u7 (protocol 2.0)
| ssh-hostkey:
|   256 b5:1c:31:d6:eb:0c:c2:cd:e5:08:29:0c:bf:7d:1d:07 (ECDSA)
|_  256 c2:29:05:99:b3:bd:ed:6d:f7:17:06:cb:91:75:3e:19 (ED25519)
23/tcp closed telnet
MAC Address: BC:24:11:DD:AE:45 (Unknown)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.94SVN%E=4%D=12/11%OT=22%CT=23%CU=35294%PV=Y%DS=1%DC=D%G=Y%M=BC2
OS:411%TM=693B04CF%P=x86_64-pc-linux-gnu)SEQ()SEQ(II=I)ECN(R=N)T1(R=N)T2(R=
OS:N)T3(R=N)T4(R=N)T5(R=N)T6(R=N)T7(R=N)U1(R=Y%DF=N%T=40%IPL=164%UN=0%RIPL=
OS:G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=40%CD=S)

Network Distance: 1 hop
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE
HOP RTT     ADDRESS
1   0.82 ms 192.168.31.151 (192.168.31.151)

Nmap scan report for 192.168.31.152 (192.168.31.152)
Host is up (0.00081s latency).

PORT   STATE  SERVICE VERSION
22/tcp open   ssh     OpenSSH 9.2p1 Debian 2+deb12u7 (protocol 2.0)
| ssh-hostkey:
|   256 b5:1c:31:d6:eb:0c:c2:cd:e5:08:29:0c:bf:7d:1d:07 (ECDSA)
|_  256 c2:29:05:99:b3:bd:ed:6d:f7:17:06:cb:91:75:3e:19 (ED25519)
23/tcp closed telnet
MAC Address: BC:24:11:0C:0C:21 (Unknown)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.94SVN%E=4%D=12/11%OT=22%CT=23%CU=41075%PV=Y%DS=1%DC=D%G=Y%M=BC2
OS:411%TM=693B04CF%P=x86_64-pc-linux-gnu)SEQ()SEQ(II=I)ECN(R=N)T1(R=N)T2(R=
OS:N)T3(R=N)T4(R=N)T5(R=N)T6(R=N)T7(R=N)U1(R=Y%DF=N%T=40%IPL=164%UN=0%RIPL=
OS:G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=40%CD=S)

Network Distance: 1 hop
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE
HOP RTT     ADDRESS
1   0.81 ms 192.168.31.152 (192.168.31.152)

Nmap scan report for lt-proxmox.loltaun.internal (192.168.31.166)
Host is up (0.00070s latency).

PORT   STATE  SERVICE VERSION
22/tcp open   ssh     OpenSSH 9.2p1 Debian 2+deb12u7 (protocol 2.0)
| ssh-hostkey:
|   256 20:63:d6:20:79:f0:26:ce:e9:d1:1a:93:df:8e:47:95 (ECDSA)
|_  256 5f:c4:ec:79:90:66:ab:6c:a3:b5:4d:d6:85:9c:55:d6 (ED25519)
23/tcp closed telnet
MAC Address: B0:41:6F:0D:24:FC (Shenzhen Maxtang Computer)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.94SVN%E=4%D=12/11%OT=22%CT=23%CU=30039%PV=Y%DS=1%DC=D%G=Y%M=B04
OS:16F%TM=693B04CF%P=x86_64-pc-linux-gnu)SEQ()SEQ(II=I)ECN(R=N)T1(R=N)T2(R=
OS:N)T3(R=N)T4(R=N)T5(R=N)T6(R=N)T7(R=N)U1(R=Y%DF=N%T=40%IPL=164%UN=0%RIPL=
OS:G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=40%CD=S)

Network Distance: 1 hop
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE
HOP RTT     ADDRESS
1   0.70 ms lt-proxmox.loltaun.internal (192.168.31.166)

Nmap scan report for 192.168.31.167 (192.168.31.167)
Host is up (0.00071s latency).

PORT   STATE  SERVICE VERSION
22/tcp open   ssh     OpenSSH 9.2p1 Debian 2+deb12u7 (protocol 2.0)
| ssh-hostkey:
|   256 ab:61:36:2d:64:c2:25:b5:a2:ff:95:17:b1:08:b1:62 (ECDSA)
|_  256 e1:4d:55:a6:e5:b8:06:4c:ad:2e:54:c2:85:35:7d:a5 (ED25519)
23/tcp closed telnet
MAC Address: 58:47:CA:7A:9D:BC (Shenzhen Meigao Electronic Equipment)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.94SVN%E=4%D=12/11%OT=22%CT=23%CU=32225%PV=Y%DS=1%DC=D%G=Y%M=584
OS:7CA%TM=693B04CF%P=x86_64-pc-linux-gnu)SEQ()SEQ(II=I)ECN(R=N)T1(R=N)T2(R=
OS:N)T3(R=N)T4(R=N)T5(R=N)T6(R=N)T7(R=N)U1(R=Y%DF=N%T=40%IPL=164%UN=0%RIPL=
OS:G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=40%CD=S)

Network Distance: 1 hop
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE
HOP RTT     ADDRESS
1   0.71 ms 192.168.31.167 (192.168.31.167)

Nmap scan report for 192.168.31.190 (192.168.31.190)
Host is up (0.00083s latency).

PORT   STATE  SERVICE VERSION
22/tcp open   ssh     OpenSSH 9.2p1 Debian 2+deb12u3 (protocol 2.0)
| ssh-hostkey:
|   256 62:b2:f2:9b:47:b4:40:36:e6:64:7f:ed:bb:65:a0:69 (ECDSA)
|_  256 84:ac:98:19:c2:d4:d0:02:6c:19:b5:11:d1:bc:aa:ea (ED25519)
23/tcp closed telnet
MAC Address: BC:24:11:5A:CA:B5 (Unknown)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.94SVN%E=4%D=12/11%OT=22%CT=23%CU=42504%PV=Y%DS=1%DC=D%G=Y%M=BC2
OS:411%TM=693B04CF%P=x86_64-pc-linux-gnu)SEQ()SEQ(II=I)ECN(R=N)T1(R=N)T2(R=
OS:N)T3(R=N)T4(R=N)T5(R=N)T6(R=N)T7(R=N)U1(R=Y%DF=N%T=40%IPL=164%UN=0%RIPL=
OS:G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=40%CD=S)

Network Distance: 1 hop
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE
HOP RTT     ADDRESS
1   0.83 ms 192.168.31.190 (192.168.31.190)

Nmap scan report for host.docker.internal (192.168.31.177)
Host is up (0.000043s latency).

PORT   STATE  SERVICE VERSION
22/tcp closed ssh
23/tcp closed telnet
Too many fingerprints match this host to give specific OS details
Network Distance: 0 hops

Post-scan script results:
| ssh-hostkey: Possible duplicate hosts
| Key 256 c2:29:05:99:b3:bd:ed:6d:f7:17:06:cb:91:75:3e:19 (ED25519) used by:
|   192.168.31.151
|   192.168.31.152
| Key 256 b5:1c:31:d6:eb:0c:c2:cd:e5:08:29:0c:bf:7d:1d:07 (ECDSA) used by:
|   192.168.31.151
|_  192.168.31.152
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 256 IP addresses (11 hosts up) scanned in 24.09 seconds
```

- [x] 6. Результаты из `nmapres_new.txt` надо перенести в `nmapres.txt` и оставить оба файла рядом в локальном репозитории. Желательно использовать `cp` в консоли через редактор.
```bash
loltaun@LT-New:~/course_lab1$ cp nmapres_new.txt nmapres.txt
loltaun@LT-New:~/course_lab1$ git add nmapres.txt nmapres_new.txt
loltaun@LT-New:~/course_lab1$ git commit -m "Fill nmapres.txt with data from nmapres_new.txt"
[master 78e6076] Fill nmapres.txt with data from nmapres_new.txt
 2 files changed, 62 insertions(+)
 create mode 100644 nmapres_new.txt
```
- [x] 7. Оформить `README.md` по аналогии и использовать `shield`, etc.
Это он и есть ;)
- [x] 8. Составить `gist` отчет и отправить ссылку личным сообщением
Ссылка - https://gist.github.com/LolTaun/8e5c7b8916484d1cdb0d00fe32a332c5


***

Copyright (c) 2025 Denis Kuznetsov