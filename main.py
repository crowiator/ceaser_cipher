alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

logo = '''  ___ __ _  ___  ___  __ _ _ __ 
 / __/ _` |/ _ \/ __|/ _` | '__|
| (_| (_| |  __/\__ \ (_| | |   
 \___\__,_|\___||___/\__,_|_|   

      _       _               
     (_)     | |              
  ___ _ _ __ | |__   ___ _ __ 
 / __| | '_ \| '_ \ / _ \ '__|
| (__| | |_) | | | |  __/ |   
 \___|_| .__/|_| |_|\___|_|   
       | |                    
       |_|                    '''
print(logo)


def ceaser(direction, word, shift):
    new_text = ""

    message = "encoded"
    if direction == "decode":
        shift *= -1
        message = "decoded"
    for letter in word:
        if letter in alphabet:
            postion = alphabet.index(letter)
            new_text += alphabet[(postion + shift) % len(alphabet)]
        else:
            new_text += letter
    print(f"The {message} word is {new_text}")


run = True
while run:
    direction = input("Type 'encode' to encrypt, type 'decode' to       decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceaser(direction, text, shift)
    choice = input("Do you wanna continue? Y or N ")
    if (choice == "N"):
        run = False
        print("Goodbye")