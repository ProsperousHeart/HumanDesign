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


def export_data(center_list):
    print("Exporting data is not yet coded. Exiting.")


def import_data():
    print("This is not yet coded. Exiting.")


def get_gates():
    cntrs = [[item[0], item[1][0]] for item in utils.en_ctrs.items()]
    gates_dict = dict()
    for idx, ctr in enumerate(cntrs):
        if idx == 0 or idx == len(cntrs):
            print()
        if ctr[0] in [6, 9]:
            gates = []
            for wave in utils.cntr_gates[ctr[0]]:
                gates.extend(wave[1:])
        else:
            gates = list(utils.cntr_gates[ctr[0]])
        print(f"{ctr[1]} center gates:\t{gates}")
        # cntrs[idx].append(gates)
        gates_dict[ctr[0]] = (ctr[1], gates)
    return gates_dict


def get_cntrs():
    def set_def(ctr_num: int, cntr: str):
        print(f"\nIs your {cntr} defined or undefined?\n")
        while True:
            resp = input("1:\tDefined (colored in)\n2:\tUndefined (white)\n")
            if resp not in ["1", "2"]:
                "\nPlease provide a 1 or 2.\n"
                continue
            else:
                comp_open = False
                if int(resp) == 1:
                    resp = True
                else:
                    while True:
                        open_resp = input(utils.undfn_open)
                        if open_resp not in ["1", "2"]:
                            print("\nPlease provide a 1 or 2\n")
                        else:
                            if open_resp == "1":
                                comp_open = True
                            break
                return utils.EnrgyCntr(ctr_num, resp), comp_open

    # def det_gates(ctr_num: int, cntr: str, gates: list):
    def det_gates(cntr: str, gates: list):
        gates_list = []
        for gate in gates:
            while True:
                print(f"\nIn your {cntr} center, is gate {gate} activated?")
                actv_num = input(utils.gate_choice)
                if actv_num not in ["1", "2", "3", "4"]:
                    print("\nPlease provide a 1, 2, 3, or 4\n")
                else:
                    if int(actv_num) != 4:
                        gates_list.append((gate, int(actv_num)))
                    break
        return gates_list

    ctr_gates = get_gates()
    print("\nIt's time to determine your energy center definitions!")
    # begin creation of centers
    center_list = []
    for cntr_num, data in ctr_gates.items():
        center, open_bool = set_def(cntr_num, data[0])
        if open_bool is False:
            # center._actv_gts = det_gates(cntr_num, data[0], data[1])
            center._actv_gts = det_gates(data[0], data[1])
        print(f"{center._cntr} active gates:\t{center._actv_gts}")
        center_list.append(center)

    return center_list


def get_type():
    while True:
        usr_type = input("\nPlease provide the number for your type.\n\n"
                         + utils.type_choice + "\n")
        if usr_type in ["0", "1", "2", "3", "4"]:
            break
        else:
            print("\nPlease provide a number from 0-4.\n")
    usr_type = utils.TypeStrat(int(usr_type))
    usr_type.print_type()
    return usr_type


def start_new():

    usr_data_list = list()

    # get type from user - this determines strategy
    usr_data_list.append(get_type())

    # get authority from user
    ctrs_lst = get_cntrs()
    for ctr in ctrs_lst:
        ctr.print_ctr()

    # get center info from user = gates (active/inactive)

    # get profile from user

    # get incarnation cross from user

    # get activations from user

    # get gates (& channels) from user

    print("\nThe rest of the section for new data not yet coded.")

    return usr_data_list


if __name__ == "__main__":
    # find out if new input or pulling from file/link
    init = welcome()
    if init == 3:
        print("Exiting now without providing insight.")
    elif init == 2:
        import_data()
    else:
        usr_data = start_new()
        export_data()

    # need to confirm if they want to export data

    print("\nExiting...\n")
