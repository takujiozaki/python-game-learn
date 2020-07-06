import csv

# csvモジュールで読み込む
# withをつけて開くと閉じるは自動で行われる
with open("memo.csv",encoding='utf-8') as f:
  for row in csv.reader(f):
    print(row)
    print(type(row))


