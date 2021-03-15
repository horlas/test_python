#!/usr/bin/python3
import re
import os
import sys

def text_lower(path_to_text):

	with open(path_to_text , 'r') as text:
		content = text.read()
		# remove caps characters
		return content.lower()

def text_only_word(content):

	return re.sub(pattern = "[^\w\s]", repl = "", string = content)

def list_of_words(content):

	list_words = re.split(r'\s', content)
	# remove empty item
	return [word for word in list_words if word != ""]

def sort_word_by_frequency(list_of_words):

	# build collection word / occurence
	word_occurrence = {}
	for word in list_of_words:
		word_occurrence.update({word: list_of_words.count(word)})
		# sort word by occurence
	return sorted(word_occurrence.items(), key=lambda x: x[1], reverse = True)

def user_interface():

	print( "Type 1 to list the frequency of all words in the text \nType 2 to get the three most frequent words in the text \nENTER: ")
	return input()

if __name__ == '__main__':

	path = os.path.join(os.getcwd(), sys.argv[1])
	if os.path.exists(path):

		text_lower = text_lower(path)
		clear_text = text_only_word(text_lower)
		print('Please wait ...', flush=True)
		list_of_words = list_of_words(clear_text)
		sorted_words = sort_word_by_frequency(list_of_words)
	
		# user interface
		SIGNAL = True
		while SIGNAL:
			
			user_input = user_interface()
		
			if user_input == "1":
				for pair in sorted_words:
					print(f'the word {pair[0]} occurs {pair[1]} times in the text')
				

			elif user_input == "2":
				for pair in sorted_words[0:3]:
					print(f'the word {pair[0]} occurs {pair[1]} times in the text')

			# escape all wrong answers
			else:
				SIGNAL = False
	else:
		print('file not found')	
