welcome_msg = """Welcome to the unofficial Human Design helper!

To start, will you be starting a new guide or pulling from a file (locally or online)?"""

open_choice = "1:  New Guide\n2:  Pull From File\n3:  Exit\n"

type_choice = """0:\tManifestor
1:\tGenerator
2:\tManifesting Generator
3:\tProjector
4:\tReflector"""

type_dict = {
    "manifestor": ["energy", "to inform",
                   "peace", "anger", "116-122"],
    "generator": ["energy", "to respond",
                  "satisfaction", "frustration", "123-128"],
    "projector": ["non-energy", "waiting for the invitation",
                  "success", "bitterness", "129-136"],
    "reflector": ["non-energy", "waiting a lunar cycle",
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
    # this information is in section 4 starting on page 113
    # determine set info about the types
    # each type:
    #   - is either energy or non-energy
    #   - has its own strategy
    #   - has its own signature (when in alignment)
    #   - has own not-self theme (when out of alignment)

    def __init__(self, type_num: int):
        if type_num == 0:   # manifestor
            en_type, strat, sig, nst, pgs = type_dict["manifestor"]
        elif type_num in [1, 2]:   # generator or mani-gen
            en_type, strat, sig, nst, pgs = type_dict["generator"]
        elif type_num == 3:   # projector
            en_type, strat, sig, nst, pgs = type_dict["projector"]
        else:   # reflector
            en_type, strat, sig, nst, pgs = type_dict["reflector"]

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
        print(f"\nType:\t\t{self.en_type}")
        print(f"Strategy:\t{self.strat}")
        print(f"Signature:\t{self.sig}")
        print(f"Not-Self Theme:\t{self.nst}")
        print(f"Pages:\t\t{self.pgs}")


class EnrgyCntr:
    def __init__(self, cntr_num: int, def_bool: bool):
        center = en_ctrs[cntr_num]
        self._cntr = center[0]
        self._explns = center[1]
        self._pgs = center[2]
        self._def_bool = def_bool
        self._actv_gts = []

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
        print(f"\nCenter:\t\t{self._cntr}")
        print(f"Explanations:\t{self._explns}")
        print(f"Pages:\t{self._pgs}")
        print(f"Defined?:\t{str(self._def_bool)}")
        print(f"Active Gates:\t\t{self._actv_gts}")
