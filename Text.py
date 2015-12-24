# -*- coding: UTF-8 -*-

from tools import separate_words
from Word import Word

class Text(object):
	def __init__(self, text):
		if type(text) != type(u''):
			text = unicode(text, 'utf-8')
		self.text = text
		words = separate_words(text)
		self.words = [Word(word) for word in words]
		self.syllables = sum([word.syllables for word in self.words], []) # flatten the list of phonemes
		self.phonemes = sum([word.phonemes for word in self.words], []) # flatten the list of phonemes
	
	def __repr__(self):
		return ' '.join([word.transcription for word in self.words]).encode('utf-8')