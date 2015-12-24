Prosodic 1.0b (February 23, 2013)
---------------------------------

Prosodic is a piece of software designed to aid research in phonology. This version of Prosodic can convert text in English or Finnish to an IPA transcription, including syllable boundaries and stress. Prosodic also allows users to convert a phoneme to its feature set, and to get a list of phonemes in a given natural class.

Examples of how to use the script:

python prosodic.pyc
This launches the command line interface to Prosodic.

python prosodic.py [infile]
This converts the text of infile to IPA and prints the result.

python prosodic.py [infile] [outfile]
This converts the text of infile to IPA and stores the result in outfile.

Prosodic currently supports English and Finnish. The language setting can be changed in config.txt

English transcription is done using the CMU pronouncing dictionary. Note that English R-colored vowels are treated as a vowel followed by an /r/ (in contrast to the CMU dictionary). Finnish transcription is done through an original script, with syllable splitting based on Karlsson 1985 and stress based on Anttila 2008 (though simplified). Finnish long vowels are currently represented as doubled short vowels, rather than single phonemes with a length feature.

Prosodic may also be used within a Python script, offering objects that encapsulate texts, words, syllables, and phonemes. To use Prosodic within a script, just type "from prosodic import *" from within Python.

To change the language, type Language.set_language("English")

Prosodic offers the following hierarchy of objects based on containment: Text > Word > Syllable > Phoneme. Any object on the hierarchy contains a list of elements within it. For example, if text is a Text object, text.words is a list of Word objects representing the words within the text, and text.phonemes is a list of Phoneme objects representing the phonemes within the text. The syllable object also has fields for the onset, nucleus, and coda, which are lists of phonemes. The features of a phoneme may be gotten from the feature field, or by direct indexing through brackets. For example, both Phoneme('p').features['labial'] and Phoneme('p')['labial'] will return True. A positive feature value is represented as True, a negative feature value is represented as False, and a zero feature value is represented as None. The feature system is taken from Hayes 2008.

This branch of Prosodic (the "b" branch) was written by Josh Falk, but it is significantly based on earlier versions of Prosodic consisting of joint work by Ryan Heuser, Josh Falk, and Arto Anttila.

Feedback or suggestions are appreciated (falk1729@gmail.com). Search functionality and metrical parsing should be coming soon.

References:
Anttila, Arto. 2008. Word stress in Finnish.

Hayes, Bruce. 2009. Introductory phonology. West Sussex, U.K.: Wiley-Blackwell.

Karlsson, Fred. 1985. Automatic hyphenation of Finnish. In Computational Morphosyntax, Report on Research 1981-84, vol. 13 of Publications of the Department of General Linguistics, University of Helsinki.