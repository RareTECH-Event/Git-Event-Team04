def main():
    while True:
        print("選択してください：")
        print("1: ryu")
        print("2: たくっち")
        print("3: teru")
        print("4: ryu2")
        print("q: 終了")

        choice = input("> ")

        if choice == "1":
            print("ryuが選ばれました。")
        elif choice == "2":
            print("たくっちが選ばれました。")
        elif choice == "3":
            print("teruが選ばれました。")
        elif choice == "4":
            print("ryu2が選ばれました。")
        elif choice == "q":
            print("プログラムを終了します。")
            break
        else:
            print("無効な入力です。もう一度選択してください。")

if __name__ == "__main__":
    main()
