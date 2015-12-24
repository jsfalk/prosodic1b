# -*- coding: UTF-8 -*-

import Language
from Syllable import Syllable

def word(text):
	return Word(text)

class Word(object):
	def __init__(self, text):
		self.broken = False
		text = text.strip()
		if type(text) != type(u''):
			text = unicode(text, 'utf-8')
		self.text = text
		self.transcription = Language.selected_language.annotate_word(self.text.lower())
		if self.transcription == None:
			self.broken = True
			self.transcription = "[" + self.text + "]" # only kept if broken
			self.syllables = []
		else:
			self.syllables = [Syllable(syll) for syll in self.transcription.split('.')]
		self.phonemes = sum([syll.phonemes for syll in self.syllables], []) # flatten the list of phonemes
	
	def __repr__(self):
		return self.transcription.encode('utf-8')
	
	def __getitem__(self, index):
		return self.phonemes[index]