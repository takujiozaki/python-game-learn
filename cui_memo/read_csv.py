import csv

# csvモジュールで読み込む
# withをつけて開くと閉じるは自動で行われる
with open("memo.csv") as f:
  for row in csv.reader(f):
    print(row)
    print(type(row))

# 書き込みにもcsvモジュールを使用
# open の引数はファイル名とモード(aが追記、wが書き換え)
# 引数はリスト

with open("memo.csv", "a") as f:
  writer = csv.writer(f)
  writer.writerow(['2020-07-07','七夕まつり'])