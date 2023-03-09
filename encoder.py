# Brandon Scheiber & Muhammad Ali
# COP3502

def encoder():
    pass


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
