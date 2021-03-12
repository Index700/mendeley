# 概要
pypm(PYthon Papers Manager)
共有サーバーを用いて文献の管理、共有を行なうプログラムです。


# How to start
- mendeley deverloper portal でクライアントを登録する。

http://dev.mendeley.com/

- config.txt を作成する

`
$ cp config.txt.sample config.txt
`

config.txt に必要なものを記入

(例)

`
clientId: {XXXXX}
clientSecret: {XXXXXXXXXXXX}
m_user: {hoge@hoge.com}
pass: {XXXXXXXXXXX}
server:{server}
user:{XXX}
directory:{/share/paper/incoming/mendeley}
`


- pypi から必要なモジュールをダウンロードする。

`
$ pip install requirements.txt
`



# 使い方
`
usage: {} [-o output][-a file] [-d directory] [-w word] [-y min,max] 
  - o Output format:
     text: standard output
     file: download pdf file
  -a Add "file" to your library
  -d Add all pdf files in "directory" to your library
  -w Show the papers whose title has "word" 
  -y Show the papers published from "min" to "max" 
`
