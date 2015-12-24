# -*- coding: UTF-8 -*-

from Phoneme import Phoneme
import Language

def split_syllable(body):
	vowels = Language.selected_language.vowels
	onset = []
	i = 0
	while i < len(body):
		if body[i] in vowels:
			break
		onset.append(Phoneme(body[i]))
		i += 1
	nucleus = []
	while i < len(body):
		if body[i] not in vowels:
			break
		nucleus.append(Phoneme(body[i]))
		i += 1
	coda = [Phoneme(cons) for cons in body[i:]]
	return (onset, nucleus, coda)

class Syllable(object):
	def __init__(self, body):
		content = body
		if body[0] == u'ˈ':
			self.stress = 'P'
			content = body[1:]
		elif body[0] == u'ˌ':
			self.stress = 'S'
			content = body[1:]
		else:
			self.stress = 'U'
		self.body = body
		self.onset, self.nucleus, self.coda = split_syllable(content)
		self.rhyme = self.nucleus + self.coda
		self.phonemes = self.onset + self.rhyme
	
	def __repr__(self):
		return self.body.encode('utf-8')