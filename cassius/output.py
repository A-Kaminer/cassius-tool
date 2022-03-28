class Output:
    """Class to deal with the output of the Analysis class. All methods are
    static and take an Analysis object."""

    @staticmethod
    def print_character_percentages(self, analysis_object):
        for key in analysis_object.ciphertext_character_percents.keys():
            print(f"{key}: {analysis_object.ciphertext_character_percents[key]}", end=" ")
            print("\n" + "="*30)


