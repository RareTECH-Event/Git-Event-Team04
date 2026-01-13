def main():
    while True:
        print("選択してください：")
        print("1: 奥野、修正したよ！！")
        print("2: match,修正したよ！！")
        print("3: コザワン、修正したよ！！")
        print("q: 終了")

        choice = input("> ")

        if choice == "1":
            print("「奥野」が選ばれました。")
        elif choice == "2":
            print("「match」が選ばれました。")
        elif choice == "3":
            print("コザワンが選ばれました。")
        elif choice == "q":
            print("プログラムを終了します。")
            break
        else:
            print("無効な入力です。もう一度選択してください。")

if __name__ == "__main__":
    main()
