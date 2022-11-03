import art

print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def caesar(t = text, s = shift, d = direction):
        changed_alphabet = ""
        for i in t:
            if i in alphabet:
                x = alphabet.index(i)
                if d == "encode":
                    changed_alphabet = changed_alphabet + alphabet[x + s]
                elif d == "decode":
                    changed_alphabet = changed_alphabet + alphabet[x - s]
            else:
                changed_alphabet = changed_alphabet + i
        print(f"The {d}d text is {changed_alphabet}")
    shift = shift % 26
    caesar(text,shift,direction)
    choice = input("type 'yes' if you want to go again. Otherwise type 'no' \n")
    if choice == 'no':
        should_continue = False
        print("Goodbye")



