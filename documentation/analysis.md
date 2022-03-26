# Analysis Class Documentation
Documentation for the main analysis class of Cassius
## Functions

`self.analyze\_unigrams(include\_nonletters=False, ignore\_capitals=True, silent=False)`  
#### Description
Analyze the unigrams, or single letters in the the ciphertext.

#### Arguments
 * include\_nonletters=False  
    Type: boolean  
    Efffect: determines whether or not to pay attention to nonletter characters  
 * ignore\_capitals=True  
    Type: boolean  
    Effect determines whether or not to be case sensitive on capitals  
 * silent=False  
    Type: boolean  
    Effect: determines whether or not to print logging output  

#### Output
 * return value: Nothing
 * prints: basic logging information
 * sets `self.ciphertext_characters`
 * sets `self.ciphertext_character_percents`
---
