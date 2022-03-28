import string
import pathlib
import os
from cassius.utilities import Util

class Analysis:
    """Class to do analysis on a ciphertext."""
    
    def __init__(self, ciphertext, language="en"):
        """Do a first pass of the ciphertext. Get the actual ciphertext, the 
        length, and the length without characters. Get the letter frequencies in
        specified language."""

        # Get various useful stats about the ciphertext
        self.ciphertext = ciphertext
        self.ciphertext_length = len(ciphertext)
        self.language = language

        letters = [ letter for letter in ciphertext if letter in string.ascii_letters ]
        self.num_ciphertext_letters = len(letters)

        # Get language stats
        self.unigram_frequencies = self.__parse_language_file(f"language/{self.language}_u_frequencies.txt")


    # Private methods start
    ############################################################################


    def __analyze_unigrams_all(self):
        """Parse all characters in the text."""

        for char in self.ciphertext:
            if char in self.ciphertext_characters:
                self.ciphertext_characters[char] += 1
            else:
                self.ciphertext_characters[char] = 0

    def __analyze_unigrams_letters_only(self):
        """Parse only the letters in the text."""

        parsed_ciphertext = [ letter for letter in self.ciphertext if letter in string.ascii_letters ]

        for char in parsed_ciphertext:
            if char in self.ciphertext_characters:
                self.ciphertext_characters[char] += 1
            else:
                self.ciphertext_characters[char] = 0

    def __eliminate_capitals(self):        # Update the character list and letter list
        for key in self.ciphertext_characters:
            if key in string.ascii_uppercase:
                self.ciphertext_characters[key.lower()] += self.ciphertext_characters[key]

    def __calculate_unigram_percentages(self, include_nonletters=False):
        if include_nonletters:
            for key in self.ciphertext_characters.keys():
                self.ciphertext_character_percents[key] = round((self.ciphertext_characters[key] / self.ciphertext_length) * 100, 1)
        else:
            for key in self.ciphertext_characters.keys():
                self.ciphertext_character_percents[key] = round((self.ciphertext_characters[key] / self.num_ciphertext_letters) * 100, 1)
    
    def __parse_language_file(self, file):
        return Util.parse_file_dictionary(file)

    # Private methods end
    ############################################################################


    def analyze_unigrams(self, include_nonletters=False, ignore_capitals=True, silent=False):
        """Parse the ciphertext."""

        # Clear the dictionaries
        self.ciphertext_characters = {}
        self.ciphertext_character_percents = {}
        
        # Get numbers and percents
        if include_nonletters:
            self.__analyze_unigrams_all()
        else:
            self.__analyze_unigrams_letters_only()

        if ignore_capitals:
            self.__eliminate_capitals()
        

        if not silent:
            print("Data parsing successful.")


        # Do unigram percentage analysis
        self.__calculate_unigram_percentages()

        if not silent:
            print("Percentage analysis successful.")

