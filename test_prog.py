
#!/usr/bin/python3
import os
import unittest
from prog import text_lower, text_only_word, list_of_words, sort_word_by_frequency

class SomeTest(unittest.TestCase):

	def setUp(self):
		self.path = os.path.join(os.getcwd(), 'test_text.txt')
		self.content = text_lower(self.path)
		self.clear_text = text_only_word(self.content)
		self.list_words = list_of_words(self.clear_text)

	def test_text_lower(self):
		self.assertEqual(text_lower(self.path), "aurevoir demain hier hier . puis, jamais, jamais, jamais, . depuis et toujours!\n")

	def test_text_without_punctuation(self):
		self.assertEqual(text_only_word(self.content), 'aurevoir demain hier hier  puis jamais jamais jamais  depuis et toujours\n')

	def test_list_of_words(self):
		self.assertEqual(list_of_words(self.clear_text), ['aurevoir', 'demain', 'hier', 'hier', 'puis', 'jamais', 'jamais', 'jamais', 'depuis', 'et', 'toujours'])

	def test_sort_word_by_frequency(self):
		self.assertEqual(sort_word_by_frequency(self.list_words), [('jamais', 3), ('hier', 2), ('aurevoir', 1), ('demain', 1), ('puis', 1), ('depuis', 1), ('et', 1), ('toujours', 1)])

if __name__ == '__main__':
	unittest.main()
