#!/usr/bin/python3

import sys
import os
import csv

"""
if len( sys.argv ) < 3:
  print("USAGE: %s exec keyword"%(sys.argv[0]))
  sys.exit()
"""
exec = sys.argv[1]
keyword = sys.argv[2]
"""
# check valid exec
if !os.path.isfile( sys.argv[1] ):
  print("%s is not Exist"%sys.argv[1])
  sys.exit()
"""

distro = ''
# check keyword in "dicDistro.csv"
with open('dicDistro.csv') as f:
  distro_reader = csv.reader( f, delimiter=',' )
  for x in list(distro_reader)[1:]:
    if keyword in x[1:]:
      distro = x[0]
      break
  if distro == '':
    print("not match keyword")
    sys.exit()


if not os.path.isfile( 'flag.txt' ):
  print("Create fake flag: 'flag.txt'")
  with open('flag.txt',mode='w') as f:
    f.write("flag{%s_you_are_hackerman}"%exec )

# ref: liveoverflow
# https://github.com/LiveOverflow/pwn_docker_example/blob/master/challenge/Dockerfile
Dockerfile = """
FROM {DISTRO}

RUN apt-get update

RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN echo "ctf:ctf" | chpasswd

WORKDIR /home/ctf

COPY {EXEC} .
COPY flag.txt .
COPY ynetd .

RUN chown -R root:root /home/ctf

USER ctf
CMD ./ynetd -p 1024 ./system_health_check
""".format( DISTRO=distro, EXEC=exec )
print( Dockerfile )

path = os.getcwd()
print( path )

# all ok
print("Success!! you run it")
print("sudo docker build ...") #create image
print("sudo docker run ...") #create container