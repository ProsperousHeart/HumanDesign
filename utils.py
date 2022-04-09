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
