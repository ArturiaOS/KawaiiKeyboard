import os


def main():
    file = open("Library/Documents/RM.txt", "r")
    file_contents = file.read()
    file.close()
    print(file_contents)

    import KawaiiKeyboard
    KawaiiKeyboard.run()

    os.system("cls")
    print("Thank you for using Kawaii Keyboard! Goodbye!")
    exit()


if __name__ == "__main__":
    main()