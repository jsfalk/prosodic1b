import re

def separate_words(text):
	words = re.findall('\s*([^\s\d]+)\s*', text, re.UNICODE) # find sequences of letters and punctuation, separated by whitespace
	words = [''.join(re.findall("[\w']", word, re.UNICODE)) for word in words] # eliminate punctuation, except apostrophe
	return words