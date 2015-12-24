# -*- coding: UTF-8 -*-

from ipa import *

class Phoneme(object):
	def __init__(self, text):
		if type(text) != type(u''):
			text = unicode(text, 'utf-8')
		self.text = text
		self.broken = False
		if self.text not in ipa_to_features:
			self.broken = True
			self.features = {}
		else:
			self.features = ipa_to_features[self.text]
	
	def __repr__(self):
		return self.text.encode('utf-8')
	
	def __getitem__(self, key):
		if key in abbreviations:
			key = abbreviations[key]
		if key in self.features:
			return self.features[key]
		raise Exception("Phoneme '" + self.text + "' does not have feature '" + key + "'")