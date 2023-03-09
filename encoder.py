# Brandon Scheiber & Muhammad Ali
# COP3502

def encoder():
    '''8-digit integer --> list of number '''

    password = list(input("Please enter your password to encode: "))
    new_password = [(int(num) + 3) for num in password]

    print("Your password has been encoded and stored!")
    return new_password



def decoder():
    pass


def main():
    while True:
        #prints menu for the user
        user_input = input(
			'Menu\n'
			'\n------------\n'
			'\n1. Encode\n'
			'\n2. Decode\n'
			'\n3. Quit\n'
			'Please enter an option: '
        )
        
        if user_input == "1":
            n_password = encoder()
        elif user_input == "2":
            decoder(n_password)
        else: #quit
            break


if __name__ == '__main__':
    main()
