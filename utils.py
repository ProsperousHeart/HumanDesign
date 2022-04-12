welcome_msg = """Welcome to the unofficial Human Design helper!

To start, will you be starting a new guide or pulling from a file (locally or online)?"""

open_choice = "1:  New Guide\n2:  Pull From File\n3:  Exit\n"

type_choice = """0:\tManifestor
1:\tGenerator
2:\tManifesting Generator
3:\tProjector
4:\tReflector"""

export_choice = """How would you like to export?
1:  XLSX
2:  Google sheet
3:  Exit (no saving)\n"""

type_dict = {
    0: ["Manifestor", "energy", "to inform",
        "peace", "anger", "116-122"],
    1: ["Generator", "energy", "to respond",
        "satisfaction", "frustration", "123-128"],
    2: ["Manifesting Generator", "energy", "to respond",
        "satisfaction", "frustration", "123-128"],
    3: ["Projector", "non-energy", "waiting for the invitation",
        "success", "bitterness", "129-136"],
    4: ["Reflector", "non-energy", "waiting a lunar cycle",
        "surprise", "disappointment", "137-147"]
}

en_ctrs = {
    1: ("Throat", ("manifestation", ),
        "52-56", (72, 28)),
    2: ("Head", ("pressure - to know", ),
        "57-60", (30, 70)),
    3: ("Root", ("pressure - to do",
                 "motor (energy) - to keep going"),
        "61-65", (60, 40)),
    4: ("Ajna", ("awareness - cognitive", ), "66-70", (47, 53)),
    5: ("Splenic", ("awareness - survival", ), "71-76", (55, 45)),
    6: ("Solar Plexus", ("awareness - relational/social/emotional/spirit",
                         "motor (energy) - desire for more experience/intimacy/spirit awareness"),
        "77-85", (53, 47)
        ),
    7: ("Heart", ("motor (energy) - source of willpower", ),
        "86-90", (37, 63)),
    8: ("Sacral", ("motor (energy) - to support continuation of the species", ),
        "91-96", (66, 34)),
    9: ("G Center", ("Magnetic Monopole - our identity (how we're wired to the universe)", ),
        "97-103", (57, 43))
}

cntr_gates = {
    1: (62, 23, 56, 16, 20, 31, 8, 33, 35, 12, 45),
    2: (64, 61, 63),
    3: (58, 38, 54, 53, 60, 52, 19, 39, 41),
    4: (47, 24, 4, 11, 43, 17),
    5: (48, 57, 44, 50, 32, 28, 18),
    6: (("Tribal Wave - Need", 37, 6, 49),
        ("Individual Wave - Passion", 22, 55),
        ("Collective Wave - Desire", 36, 30)),
    7: (21, 40, 26, 51),
    8: (34, 5, 14, 29, 59, 9, 3, 42, 27),
    9: (("Gates of Direction", 1, 13, 7, 2),
        ("Gates of Love", 15, 10, 25, 46))
}

undfn_open = """\nIs it completely open? (No activated gates?)
1:\tYes, no activated gates at all (completely open)
2:\tNo, some defined gates\n"""

gate_choice = """1:\tYes, red (design) only
2:\tYes, black (personality) only
3:\tYes, both red & black
4:\tNo, not activated by either\n"""


class TypeStrat:
    """Class for HD Types & Strategies.

    This information is in section 4 starting on page 113 of the book.
    This class will allow for providing set info about the types for
    a particular user. Each type:
      - is either energy or non-energy
      - has its own strategy
      - has its own signature (when in alignment)
      - has own not-self theme (when out of alignment)"""

    def __init__(self, type_num: int):
        """

        :param type_num:
        """

        hd_type, en_type, strat, sig, nst, pgs = type_dict[type_num]

        self.hd_type = hd_type
        self.en_type = en_type
        self.strat = strat
        self.sig = sig
        self.nst = nst
        self.pgs = pgs

        @property
        def en_type(self):
            """The energy type property."""
            return self._en_type

        @property
        def strat(self):
            """The strategy property."""
            return self._strat

        @property
        def sig(self):
            """The signature property."""
            return self._sig

        @property
        def nst(self):
            """The not-self theme property."""
            return self._nst

        @property
        def pgs(self):
            """The book location property."""
            return self._pgs

    def print_type(self):
        """Function to print info of class object."""
        print(f"\nHuman Design Type:\t{self.hd_type}")
        print(f"Energy Type:\t\t{self.en_type}")
        print(f"Strategy:\t{self.strat}")
        print(f"Signature:\t{self.sig}")
        print(f"Not-Self Theme:\t{self.nst}")
        print(f"Pages:\t\t{self.pgs}")

    def toDict(self):
        """Returns dictionary version of class object data."""
        return {
            "HD Type": self.hd_type,
            "Energy Type": self.en_type,
            "Strategy": self.strat,
            "Signature": self.sig,
            "Not-Self": self.nst,
            "Pages": self.pgs
        }


class EnrgyCntr:
    """

    """

    def __init__(self, cntr_num: int, def_bool: bool, active_gates: list = []):
        """

        :param cntr_num:
        :param def_bool:
        :param active_gates:
        """

        center = en_ctrs[cntr_num]
        self._cntr = center[0]
        self._explns = center[1]
        self._pgs = center[2]
        self._def_bool = def_bool
        self._actv_gts = active_gates

        @property
        def cntr(self):
            """The center name property."""
            return self._cntr

        @property
        def explns(self):
            """The center explanation property."""
            return self._explns

        @property
        def pgs(self):
            """The center pages property."""
            return self._pgs

        @property
        def def_bool(self):
            """The center definition boolean property."""
            return self._def_bool

        @property
        def actv_gts(self):
            """The active gates property."""
            return self._actv_gts

        @actv_gts.setter
        def actv_gts(self, val_list: list):
            """Set function for "Active" gates."""
            self._actv_gts = val_list

    def print_ctr(self):
        """Function to print info of class object."""
        print(f"\nCenter:\t\t{self._cntr}")
        print(f"Explanations:\t{self._explns}")
        print(f"Pages:\t{self._pgs}")
        print(f"Defined?:\t{str(self._def_bool)}")
        print(f"Active Gates:\t\t{self._actv_gts}")

    def toDict(self):
        """Returns dictionary version of class object data."""
        return {
            "Center": self._cntr,
            "Explanations": self._explns,
            "Pages": self._pgs,
            "Definition": self._def_bool,
            "Gates": ', '.join(str(item) for item in self._actv_gts)
        }

temp_ctrs = [
    EnrgyCntr(1, False, [(62, 2), (31, 2)]),  # throat
    EnrgyCntr(2, False, [(61, 2), (63, 1)]), # head
    EnrgyCntr(3, True, [(58, 3), (54, 2)]),  # root
    EnrgyCntr(4, False, []),  # ajna
    EnrgyCntr(5, True, [(50, 1), (32, 3), (28, 3)]),  # splenic
    EnrgyCntr(6, False, [(36, 3), ]),  # solar plexus
    EnrgyCntr(7, False, [(26, 3), ]),  # heart
    EnrgyCntr(8, False, [(34, 2), (59, 2), (9, 1), (3, 1), (42, 3)]),  # sacral
    EnrgyCntr(9, False, [(2, 1), (15, 1)]),  # g center
]
