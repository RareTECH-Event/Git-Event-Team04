def main():
    while True:
        print("選択してください：")
        print("1: ryu")
        print("2: たくっち")
        print("3: 選択肢3")
        print("q: 終了")

        choice = input("> ")

        if choice == "1":
            print("ryuが選ばれました。")
        elif choice == "2":
            print("たくっちが選ばれました。")
        elif choice == "3":
            print("選択肢3が選ばれました。")
        elif choice == "q":
            print("プログラムを終了します。")
            break
        else:
            print("無効な入力です。もう一度選択してください。")

if __name__ == "__main__":
    main()
