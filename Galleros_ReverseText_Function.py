print("* " * 20 + "\n*{:^37}*".format("REVERSE THIS"))
print("* " * 20 + "\n")

while True:
    user_input = input("Enter a text: ")
    if not user_input.isnumeric():
        reverse_word = user_input[::-1]
        print(reverse_word)
        break

    else:
        print("Error Reported! Enter text only\n")
