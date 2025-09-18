def main():
    while True:
        print("選択してください：")
        print("1: 選択肢1")
        print("2: 選択肢2")
        print("3: 選択肢3")
        print("q: 終了")

        choice = input("> ")

        if choice == "1":
            print("まこが選ばれました。")
        elif choice == "2":
            print("わかが選ばれました。")
        elif choice == "3":
            print("rootが選ばれました。")
        elif choice == "4":
            print("はち子が選ばれました。")
        elif choice == "q":
            print("プログラムを終了します。")
            break
        else:
            print("無効な入力です。もう一度選択してください。")

if __name__ == "__main__":
    main()

