#!/usr/bin/python3

import sys
import os
import csv
import shutil

# このスプリクトが動いているディレクトリを取得
dir = os.path.dirname(os.path.realpath(__file__)) + '/'

if len( sys.argv ) < 3:
  print("USAGE: %s exec keyword"%(sys.argv[0]))
  sys.exit()

exec = sys.argv[1]
_exec = exec.split('/')[-1] #実行ファイル名のみ
keyword = sys.argv[2]

# check valid exec
if not os.path.isfile( exec ):
  print("%s is not Exist"%sys.argv[1])
  sys.exit()

distro = ''
# check keyword in "listDistro.csv"
with open( dir + 'listDistro.csv', mode='r' ) as f:
  distro_reader = csv.reader( f, delimiter=',' )
  for x in list(distro_reader)[1:]:
    if keyword in x[1:]:
      distro = x[0]
      break
  if distro == '':
    print("No match keyword.")
    print("please check keyword or Add new distribution." )
    print( dir + 'listDistro.csv' )
    sys.exit()


if not os.path.isfile( 'flag.txt' ):
  print("Create fake flag: 'flag.txt'")
  with open('flag.txt',mode='w') as f:
    f.write("flag{%s_you_are_hackerman}"%_exec )

# copy ynetd to current directory
if not os.path.isfile( 'ynetd' ):
  shutil.copyfile(dir+'ynetd', 'ynetd')
  print("copyed ynetd")

# ref: liveoverflow
# https://github.com/LiveOverflow/pwn_docker_example/blob/master/challenge/Dockerfile
Dockerfile = """\
FROM {DISTRO}

RUN apt-get update

RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN echo "ctf:ctf" | chpasswd

WORKDIR /home/ctf

COPY {EXEC} .
COPY flag.txt .
COPY ynetd .

RUN chown -R root:root /home/ctf
RUN chmod -R 755 /home/ctf/

USER ctf
CMD ./ynetd -p 9999 ./{_EXEC}

EXPOSE 9999
""".format( DISTRO=distro, EXEC=exec, _EXEC=_exec )
with open( 'Dockerfile', mode='w' ) as f:
  f.write( Dockerfile )

# all ok
print("Success!! you run it")
print( '*-=' * 15 )
print("sudo docker build -t %s ."%_exec ) #create image
print("sudo docker run -p 9999:9999 --rm -it %s"%_exec ) #create container
