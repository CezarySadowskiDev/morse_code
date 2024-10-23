from morse_code import MorseCode

if __name__ == '__main__':
    user_input = input("Please enter your text: ").strip().lower()

    conversion_type = input(
        "You can perform the following actions:\n"
        "\t[1] Convert text to Morse code.\n"
        "\t[2] Convert Morse code to text.\n"
        "Please choose type of action you want to perform by providing it's number: "
    )

    text_to_translate = MorseCode(user_input)

    if conversion_type == '1':
        print(text_to_translate.code_to_morse())

    elif conversion_type == '2':
        print(text_to_translate.decode_from_morse())

    else:
        print("Unknown action type")
