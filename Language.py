# -*- coding: UTF-8 -*-

# This method of selecting the language is ugly. I'll try to improve it in the future. (2/23/2013)

import codecs, os
import lib.fi.finnish_annotator

class English(object):
	vowels = set([u'ɑ', u'a', u'æ', u'ə', u'ʌ', u'ɔ', u'ɜ', u'ɛ', u'e', u'ɪ', u'i', u'o', u'ʊ', u'u'])
	name = "English"
	
	def __init__(self):
		self.annotation_dict = {}
		cmu = codecs.open(os.path.join('lib', 'en', 'english.tsv'), 'r', 'utf-8')
		raw = cmu.read()
		words = raw.split('\n')
		for word in words:
			text, transcription = word.split('\t')
			if not text.lower() in self.annotation_dict:
				self.annotation_dict[text.lower()] = transcription
		
	def annotate_word(self, text):
		if type(text) != type(u''):
			text = unicode(text, 'utf-8').lower()
		if not text in self.annotation_dict:
			return None
		return self.annotation_dict[text]

class Finnish(object):
	vowels = set([u'i', u'e', u'æ', u'y', u'ø', u'ɑ', u'u', u'o'])
	name = "Finnish"
	
	def __init__(self):
		pass
	
	def annotate_word(self, text):
		return lib.fi.finnish_annotator.ipa_annotation(text)

language_dict = {'English': English(), 'Finnish': Finnish()}

def set_language(language):
	if language in language_dict:
		global selected_language
		selected_language = language_dict[language]
	else:
		print "ERROR: invalid language choice"

set_language("English")

try:
	f = open('config.txt', 'r')
	for line in f.read().split('\n'):
		if len(line) == 0 or line[0] == '#': # empty or comment
			continue
		configuration = line.split('=')
		if len(configuration) != 2:
			continue
		if configuration[0] == 'language':
			set_language(configuration[1].strip())
except IOError:
	print "ERROR: configuration file not found"