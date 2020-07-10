import csv
import sys


def show_menu():
    print("初期表示：1 一覧 ・ 2 新規 ・ 0 終了")
    choice = input("選択してください\n")
    print(choice)
    if choice == "0":
        end_memu()
    elif choice == "1":
        show_list()
    elif choice == "2":
        entry_todo()


def show_list():
    print("**********一覧start********")
    with open('todos.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row[0]+ ": " + row[1])

    print("**********一覧end**********")
    print("操作：9戻る")
    choice = input("選択してください")
    if choice == "9":
        show_menu()


def entry_todo():
    print("新しいtodoを追加します")
    when = input("いつの予定ですか?")
    what = input("内容を教えてください")

    #todoを保存
    with open("todos.csv", "a", encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([when,what])

    print("新しいTODOを保存しました")
    print("操作：9戻る")
    choice = input("選択してください")
    if choice == "9":
        show_menu()


def end_memu():
    print("終了します")
    sys.exit()


show_menu()
