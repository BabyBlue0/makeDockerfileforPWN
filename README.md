# makeDockerfileforPWN
pwnでheap問を解くとき、libcのバージョンの違いでexploitが実行できないことが多い。  
そこで、Dockerfileを自動生成し、簡易challengeサーバーを建てられるようにしたのがこのスクリプトである。

## install
```
# git clone
git clone https://github.com/BabyBlue0/makeDockerfileforPWN.git ~/
# パスを通す
ln -s ~/makeDockerfileforPWN/crDf.py ~/bin/crDf
```

## 使い方
```
crDf exec keyword
```
exec: 実行ファイル  
keyword: ディストリビューションを特定するためのキーワード  

keywordは、`listDistro.csv`に追加していく必要がある。

## 使用例
```bash:terminal1
$ crDf babyheap 2.27
Create fake flag: 'flag.txt'
copyed ynetd
Success!! you run it
*-=*-=*-=*-=*-=*-=*-=*-=*-=*-=*-=*-=*-=*-=*-=
sudo docker build -t babyheap .
sudo docker run -p 9999:9999 --rm -it babyheap

$ sudo docker build -t babyheap .
Sending build context to Docker daemon  2.087MB
... cutting ...

$ sudo docker run -p 9999:9999 --rm -it babyheap

```
```bash:terminal2
$ nc localhost 9999
Welcome to babyheap challenge!
... cutting ...

$ python3 exploit.py 
... cutting ...
[*] Switching to interactive mode
$ ls
babyheap
flag.txt
ynetd
$ cat flag.txt
flag{babyheap_you_are_hackerman}$  
```