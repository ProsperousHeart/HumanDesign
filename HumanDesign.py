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


def export_data():
    pass


def import_data():
    print("This is not yet coded. Exiting.")


def print_usrtype(class_obj: utils.TypeStrat):
    print(f"\nType:\t\t{class_obj.en_type}")
    print(f"Strategy:\t{class_obj.strat}")
    print(f"Signature:\t{class_obj.sig}")
    print(f"Not-Self Theme:\t{class_obj.nst}")
    print(f"Pages:\t\t{class_obj.pgs}")


def start_new():

    # get type from user - this determines strategy
    while True:
        usr_type = input("\nPlease provide the number for your type.\n\n"
                         + utils.type_choice + "\n")
        if usr_type in ["0", "1", "2", "3", "4"]:
            break
        else:
            print("\nPlease provide a number from 0-4.\n")
    usr_type = utils.TypeStrat(int(usr_type))
    print_usrtype(usr_type)

    # get authority from user

    # get center info from user = gates (active/inactive)

    # get profile from user

    # get incarnation cross from user

    # get activations from user

    # get gates (& channels) from user

    print("\nThis rest not yet coded. Exiting.")


if __name__ == "__main__":
    # find out if new input or pulling from file/link
    init = welcome()
    if init == 3:
        print("Exiting now without providing insight.")
    elif init == 2:
        import_data()
    else:
        start_new()

        # need to confirm if they want to export data
