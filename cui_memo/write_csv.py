# coding:utf-8

import csv

#import gentec

# 書き込みにもcsvモジュールを使用
# open の引数はファイル名とモード(aが追記、wが書き換え)
# 引数はリスト

#enc = getenc.getEncode('memo.csv')
#print(enc)

with open("memo.csv", "a", encoding='utf-8') as f:
  writer = csv.writer(f)
  writer.writerow(['2020-07-10','映画'])
