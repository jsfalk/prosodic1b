# -*- coding: UTF-8 -*-

import codecs, sys
import Language
from Text import Text
from Word import Word
from Syllable import Syllable
from Phoneme import Phoneme
from ipa import *

def print_intro():
	print "#################"
	print "# Prosodic 1.0b #"
	print "#################"
	print

def print_main_instructions():
	print
	print "Please type one of the following commands:"
	print "/annotation: convert text to IPA"
	print "/ipa: work with IPA features"
	print "/exit or /quit: exit the program"
	print

def print_annotation_instructions():
	print
	print "Current language: " + Language.selected_language.name 
	print "Please type one of the following commands:"
	print "/file [filename]: convert a file to IPA and dispaly the output"
	print "/file [input] [output]: convert a file to IPA and store the output"
	print "/language [lang]: change the language for annotation (" + ", ".join(Language.language_dict.keys()) + ")"
	print "/main: return to the main menu"
	print "or enter " + Language.selected_language.name + " text to display an IPA transcription"
	print

def print_ipa_instructions():
	print
	print "Please type one of the following commands:"
	print "/class [features]: display all phonemes belonging to a natural class"
	print "(e.g.: /class +labial -voice)"
	print "/features: display a list of all phonological features in the system"
	print "/main: return to the main menu"
	print "or enter a phoneme to display its feature values"
	print

def process_files(filenames):
	if len(filenames) < 1 or len(filenames) > 2:
		print "ERROR: enter one or two filenames"
		return
	infile = filenames[0]
	try:
		input = codecs.open(infile, 'r', 'utf-8')
		raw = input.read()
		input.close()
		text = Text(raw)
		if len(filenames) == 1:
			print text
		elif len(filenames) == 2:
			outfile = filenames[1]
			output = codecs.open(outfile, 'w', 'utf-8')
			output.write(unicode(str(text), 'utf-8'))
			output.close()
	except IOError:
		print "ERROR: could not open input file (" + infile + ")"

def run_annotation():
	print_annotation_instructions()
	while True:
		print ">>",
		input = unicode(raw_input(), 'utf-8')
		if input.startswith("/help"):
			print_annotation_instructions()
			continue
		elif input == "/main":
			return
		elif input == "/quit" or input == "/exit":
			sys.exit()
		elif input.startswith("/language"):
			language = input[len("/language"):].strip() # remove the command
			if language in Language.language_dict:
				Language.selected_language = Language.language_dict[language]
				print "Language set to " + language
			else:
				print "ERROR: invalid language choice"
		elif input.startswith("/file "):
			files = input.split(' ')
			process_files(files[1:]) # remove the command
		else:
			text = Text(input)
			print text
		print

def run_ipa():
	print_ipa_instructions()
	while True:
		print ">>",
		input = unicode(raw_input(), 'utf-8')
		if input.startswith("/help"):
			print_ipa_instructions()
			continue
		elif input == "/main":
			return
		elif input == "/quit" or input == "/exit":
			sys.exit()
		elif input.startswith("/class"):
			input = input[len("/class"):] # remove the command
			natural_class = get_natural_class(input)
			print ", ".join(natural_class)
		elif input == "/features":
			print "Vowel features:", ", ".join(vowel_features)
			print "Consonant features:", ", ".join(consonant_features)
		elif input in ipa_to_features:
			print phoneme_feature_string(input)
		else:
			print "ERROR: invalid command or unknown phoneme"
		print

def run_program():
	print_intro()
	while True:
		print_main_instructions()
		print ">>",
		input = raw_input()
		if input == "/annotation":
			run_annotation()
		elif input == "/ipa":
			run_ipa()
		elif input == "/quit" or input == "/exit":
			return
		else:
			print "ERROR: invalid command"

def print_command_instructions():
	print "Usage: python prosodic.py [infile] [outfile]"

if __name__ == "__main__":
	if len(sys.argv) == 1:
		run_program()
	elif len(sys.argv) <= 3: # if given one or two filenames
		process_files(sys.argv[1:])
	else:
		print_command_instructions()