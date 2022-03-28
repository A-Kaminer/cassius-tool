import cassius.analysis
from cassius.utilities import Util
import os
import pathlib

class RotCiphers:
    """A class to quickly do simple rotation ciphers."""

    lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
    upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    @classmethod
    def rot(self, analysis_object, key, preserve_caps=False):
        """Rot13 on an analysis_object"""
        if preserve_caps:
            output = ""
            for char in analysis_object.ciphertext:
                if char in RotCiphers.lower_alphabet + RotCiphers.upper_alphabet:
                    if char in RotCiphers.lower_alphabet:
                        index = RotCiphers.lower_alphabet.find(char)
                        output += RotCiphers.lower_alphabet[(index + key) % 26]
                    else:
                        index = RotCiphers.upper_alphabet.find(char)
                        output += RotCiphers.upper_alphabet[(index + key) % 26]
                else:
                    output += char
        else:
            output = ""
            for char in analysis_object.ciphertext:
                if char.upper() in RotCiphers.upper_alphabet:
                    index = RotCiphers.upper_alphabet.find(char.upper())
                    output += RotCiphers.upper_alphabet[(index + key) % 26]
                else:
                    output += char
        return output

    @classmethod
    def rot13(self, analysis_object, preserve_caps=False):
        return RotCiphers.rot(analysis_object, 13, preserve_caps)

    @classmethod
    def rot_brute_force(self, analysis_object, preserve_caps=False, silent=False):
        probable = []

        common_words = Util.parse_file_array("language/en_common_words.txt")
            # do do each possible rot.
        for i in range(26):
            r = RotCiphers.rot(analysis_object, i, preserve_caps)

            # check common words to mark as probable
            for w in common_words:
                if w in r.lower():
                    probable.append(i)
                    break
            if not silent:
                print(f"key: {i}\n{r}\n{'='*20}")

        # report probables
        if not silent:
            print(f"These keys had common words in them: {probable}.\nYou should check them out!")
        return probable

    @classmethod
    def rot_probables(self, analysis_object, preserve_caps):
        """Return the probable rots."""
        probable = RotCiphers.rot_brute_force(analysis_object, preserve_caps, silent=True)

        for index in probable:
            print(f"key: {index}\n{RotCiphers.rot(analysis_object, index, preserve_caps)}\n{'='*20}")
