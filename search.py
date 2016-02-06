#! /usr/bin/python

import os
import argparse

def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('keywords', nargs='+')
	parser.add_argument('-e', '--extensions', nargs='+')
	return parser.parse_args()

class ExtensionTester:
	def __init__(self, extFlag):
		self.extensions = extFlag or self.open_extensions_file()
		self.extensions = ['.'+e for e in self.extensions]

	def test(self, filename):
		extension = os.path.splitext(filename)[1];
		return extension.lower() in self.extensions

	def open_extensions_file(self):
		return [(ext).strip('\n') for ext in open('extensions.txt')]

class FileTester:
	def __init__(self, keywords):
		self.keywords = keywords
	
	def test(self, filename):
		linelist = [line.strip('\n') for line in open(filename)]

		for keyword in self.keywords:
			found = False
			for line in linelist:
				if keyword in line:
					break
			else:
				return False
		return True

def test_filename(keywords, filename):
	for keyword in keywords:
		if keyword in filename:
			return True
	return False


if __name__ == '__main__':
	flags = parse_args()
	extTester = ExtensionTester(flags.extensions)
	fileTeste = FileTester(flags.keywords)

	print('Searching for {} in files with these extensions:'.format(flags.keywords), extTester.extensions, '\n')

	filenames = []
	for dirpath, subdirs, files in os.walk(os.getcwd()):
		for x in files:
			if extTester.test(x) and (fileTeste.test(os.path.join(dirpath, x)) or test_filename(flags.keywords, x)):
				filenames.append(os.path.join(dirpath, x))
				print(os.path.join(dirpath, x))

	print('\n{} results.'.format(len(filenames)))