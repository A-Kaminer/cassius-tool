import string

class Analysis:
    """Class to do analysis on a ciphertext."""
    
    def __init__(self, ciphertext):
        """Do a first pass of the ciphertext. Get the actual ciphertext, the 
        length, and the length without characters. Get the letter frequencies in
        english."""


        # Get various useful stats about the ciphertext
        self.ciphertext = ciphertext
        self.ciphertext_length = len(ciphertext)

        letters = [ letter for letter in ciphertext if letter in string.ascii_letters ]
        self.num_ciphertext_letters = len(letters)

        # Get language stats
        self.__parse_language_file("language-frequencies/en_u_frequencies.txt")


    # Private methods start
    ############################################################################


    def __analyze_unigrams_all(self):
        """Parse all characters in the text."""

        for char in self.ciphertext:
            if char in self.ciphertext_letters:
                self.ciphertext_letters[char] += 1
            else:
                self.ciphertext_letters[char] = 0

    def __analyze_unigrams_letters_only(self):
        """Parse only the letters in the text."""

        parsed_ciphertext = [ letter for letter in self.ciphertext if letter in string.ascii_letters ]

        for char in parsed_ciphertext:
            if char in self.ciphertext_letters:
                self.ciphertext_letters[char] += 1
            else:
                self.ciphertext_letters[char] = 0

    def __eliminate_capitals(self):        # Update the character list and letter list
        for key in self.ciphertext_characters:
            if key in string.ascii_uppercase:
                self.ciphertext_characters[key.lower()] += self.ciphertext_characters[key]
                self.ciphertext_letters[keys.lower()] += self.ciphertext_letters[key]

    def __unigram_percentage_analysis(self):
        
    
    def __parse_language_file(self, file):
        # Parse a language file
        self.en_unigram_frequencies = {}

        with open(file, "r") as lang:
            for line in lang.readlines():
                parts = line.split(":")
                self.en_unigram_frequencies[parts[0]] = parts[1][:-1]


    # Private methods end
    ############################################################################


    def analyze_unigrams(self, include_nonletters=False, ignore_capitals=True, silent=False):
        """Parse the ciphertext."""

        # Clear the dictionaries
        self.ciphertext_letters = {}
        self.ciphertext_characters = {}
        self.ciphertext_character_percents = {}
        self.ciphertext_letter_percents = {}
        
        # Get numbers and percents
        if include_nonletters:
            self.__analyze_unigrams_all()
        else:
            self.__analyze_unigrams_letters_only()

        if ignore_capitals:
            self.__eliminate_capitals()
        

        if not silent:
            print("Data parsing successful")


        # Do unigram percentage analysis
        self.__unigram_percentage_analysis()

        if not silent:
            print("percentage analysis successful")






class Output:
    """Class to deal with the output of the Analysis class. All methods are 
    static and take an Analysis object."""

    @staticmethod
    def print_character_percentages(obj):
        pass
