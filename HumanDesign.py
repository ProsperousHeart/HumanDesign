import utils
import file_manipulations as fm


def welcome():
    """
    This function is run when the program is first run.
    It will determine what the user wishes to do by taking in
    a specific input and returning either a 1, 2, or 3.
    """

    print(utils.welcome_msg)
    while True:
        chk = input(utils.open_choice)
        if chk in ["1", "2", "3"]:
            chk = int(chk)
            break
        else:
            print("\nPlease provide either a 1, 2, or 3.\n")
    return chk


def export_data(data_dict: dict):
    """Takes in, preps, and exports data dictionary to XLSX or Google sheet.

    Keyword arguments:
    data_dict   -- dictionary with keys of class type & value of class object

    Calls on sub-function for easier conversions, since the classes and data dict
    are structured in a way to make export easier.
    """

    def convert_ddict(ddict: dict):
        """Convert data dict to format for export to XLSX or Google sheet.

        Keyword arguments:
        ddict   -- dictionary with keys of data type (for tabs) & class data

        Returns converted data for easy export to sheet file.
        """
        temp_dict = dict()
        for key, vals in ddict.items():
            temp_dict[key] = [item.toDict() for item in vals]
        return temp_dict

    # need to confirm if they want to export data

    while True:
        export_choice = input(f"{utils.export_choice}").strip()
        if export_choice not in ["1", "2", "3"]:
            print("Please provide a 1, 2, or 3 to continue.")
        else:
            dict_data = convert_ddict(data_dict)
            fm.write2file(int(export_choice), dict_data)
            break


def import_data():
    """Import data from a file or Google sheet."""
    print("This is not yet coded. Exiting.")


def get_gates():
    """For each energy center, get input from user on which centers
    are defined/undefined, and which gates are activated.
    """

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
    """User input for EnrgyCntr class object creations with active gates.

    Calls on get_gates() to pull the gates per energy center. This information
    is used to provide dialog between user and class object setup.

    2 internal functions related to manually updating data for
    energy centers & gates. These functions are:
    1. set_def() - to determine which centers are defined, undefined, or open
    2. det_gates() - to determine which gates are 'active'

    Returns list of energy center objects.
    """

    def set_def(ctr_num: int, cntr: str):
        """For each energy center passed in, return class object with definition.

        Keyword arguments:
        ctr_num -- key used to find energy center data in utils.en_ctrs
        cntr    -- energy center name (e.g.:  "Throat", "Splenic", etc.)

        Returns utils.EnrgyCntr class object
        """
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

    def det_gates(cntr: str, gates: list):
        """Based on energy center & user input, determine which gates are activated.

        Gates can be activated in one of the following ways:
            - red (design)
            - black (personality)
            - both
            - no activation

        Keyword arguments:
        cntr    -- energy center name (e.g.:  "Throat", "Splenic", etc.)
        gates   -- list of gates unique to energy center

        Returns a list of activated gates for energy center & how activated.
        """

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

    # get centers and available gates
    ctr_gates = get_gates()

    # begin creation of centers
    print("\nIt's time to determine your energy center definitions!")
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
    """Requests HD type & returns the TypeStrat class object"""
    while True:
        usr_type = input("\nPlease provide the number for your type.\n\n"
                         + utils.type_choice + "\n")
        if usr_type in ["0", "1", "2", "3", "4"]:
            break
        else:
            print("\nPlease provide a number from 0-4.\n")
    usr_type = utils.TypeStrat(int(usr_type))
    # usr_type.print_type()
    return usr_type


def start_new():
    """Manually creates new HD profile.

    Calls on other methods to retrieve data from user:
    1. get_type()
    2. get_cntrs()
    3. get_profile()        -- not yet scripted
    4. get_incarnation()    -- not yet scripted

    Takes data given and returns a dictionary of user HD data.
    """

    usr_ddict = dict()

    # get type from user - this determines strategy
    usr_ddict["Type"] = [get_type(), ]

    # get authority from user

    # get center info from user = gates (active/inactive)
    # channels can be coded, but consider getting manually
    # ctrs_lst = get_cntrs()
    ctrs_lst = utils.temp_ctrs
    for ctr in ctrs_lst:
        ctr.print_ctr()
    usr_ddict["Centers"] = ctrs_lst

    # get profile from user

    # get incarnation cross from user

    print("\nThe rest of the section for new data not yet coded.")

    return usr_ddict


if __name__ == "__main__":
    """Initial start to program.
    
    Beginning of program to either import or create a Human Design profile.
    It then exports the relative data to an XLS file or Google sheet.
    """

    # find out if new input or pulling from file/link
    init = welcome()
    if init == 3:
        print("Exiting now without providing insight.")
    elif init == 2:
        import_data()
    else:
        usr_data_dict = start_new()
        # print(usr_data_dict)

        export_data(usr_data_dict)

    print("\nExiting...\n")
