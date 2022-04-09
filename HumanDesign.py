import utils

def welcome():
    '''
    This function is run when the program is first run.
    It will determine what the user wishes to do by taking in
    a specific input and returning either a 1, 2, or 3.
    '''
    print(utils.welcome_msg)
    while True:
        chk = input(utils.open_choice)
        if chk in ["1", "2", "3"]:
            chk = int(chk)
            break
        else:
            print("\nPlease provide either a 1, 2, or 3.\n")
    return chk

def import_data():
    print("This is not yet coded. Exiting.")

def start_new():
    print("This is not yet coded. Exiting.")

if __name__ == "__main__":
    # find out if new input or pulling from file/link
    init = welcome()
    if init == 3:
        print("Exiting now without providing insight.")
    elif init == 2:
        import_data()
    else:
        start_new()