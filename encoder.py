# Brandon Scheiber & Muhammad Ali
# COP3502

def prompt(): 
    #prints menu for the user
    print("Menu\n\n------------\n\n1. Encode\n\n2. Decode\n\n3. Quit\n")

    user_input = input("Please enter an option: ")
    return user_input

def encoder():
    pass


def decoder():
    pass


def main():
    while True:
        user_input = prompt()
        if user_input == "1":
            n_password = encoder()
            # print(str(n_password))  #For testing
        elif user_input == "2":
            decoder(n_password)
        else: #quit
            break


if __name__ == '__main__':
    main()
