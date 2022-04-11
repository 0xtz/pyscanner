# PYSCANNER

![prevue](./assets/demoimg.png)

## INFO



## USAGE

```sh
[tz:.../tools/pyscanner]$ python3 scanner.py --help
usage: scanner.py [-h] -t TARGET [-p PORT]

Port Scanner

optional arguments:
  -h, --help            show this help message and exit
  -t TARGET, --target TARGET
                        Target IP address
  -p PORT, --port PORT  Target port or ports

```

### SCANN ALL PORTS

use the host name or IP adress as an arg

```sh

[tz:.../tools/pyscanner]$ python3 scanner.py -t scanme.nmap.org

```

### Specify some ports

```sh

[tz:.../tools/pyscanner]$ python3 scanner.py -t <IP> -p 22 80 587 ...

```
### fast scan 

-f flag to scann the top used TPC ports 
```bash
[tz:.../tools/pyscanner]$ python3 -OO scanner.py -t 192.168.1.7 -f

```


## ETC

MORE INFO IS GONNA BE ADDED SOONER haha
