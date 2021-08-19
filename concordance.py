'''
	Logic Overview

		1) Tokenize(): Extract the text from the source and split into sentences 
			- This step is implemented using punkt from nltk, however punkt alone is not capable of recognizes abbreviations, ellipses results in false positives 
			of sentence ends. Thus a regex pattern is also required to recognize this specific cases. 
			
		2) addWord(): Check each token and determine whether it should be added to the dictionary
			- Checks to see if the word contains atleast one letter, this eliminates punctation such as commas, colons, etc.
				- Time complexity is O(W) where W is word length
			- Adds words to the dictionary or updates its value if the word is already added
				- Time complexity is O(1)

		3) Sort the dictionary and print with correct formatting 
			- Technically the actual dictionary is not being sorted but the output is sorted through python's timsort algorithm which results in a 
			time complexity of O(nlogn). Since iterating the dictionary is only O(n) the total time complexity of the print method remains O(nlogn)



	Installations
		1) python
			- 
		2) nlkt
			- nlkt requires python 3.5 or newer
			- pip install --user -U nltk (for MAC/UNIX)  ...   https://www.nltk.org/install.html
			- run the provided file nltk.py which will open a GUI window and download punkt under models, this needs to be down before running concordance.py


	Questions & Modifications
		1) AM I USING PUNKT ANYMORE?
'''


import nltk

def addWord(newWord, sentenceNumber, myWords):	

	# Check if i is a word or punctuation symbols, need to check each character individually to account for abbreviations
	containsLetter = False
	for i in newWord:
		if i.isalpha():
			containsLetter = True
			break

	# Return before adding the punctation 
	if not containsLetter: 
		return 

	# Check if the word is already within the dictionary, in which case increment the count and add the new sentence number to the list
	# Otherwise add a new key into the dictionary with a frequency occurence of 1
	if newWord in myWords:
		myWords[newWord].append(sentenceNumber)
		myWords[newWord][0] += 1
	else:
		myWords[newWord] = [1, sentenceNumber]


def tokenize(inputString):

	# Create a regex pattern to look for situations that may seem like the end of a sentence but are not such as abbreviations. This also looks for
	# situations that may cause an early split in hypenated words. For example, high-tech should be treated as a single word and not tokenized seperately	
	regex = r'''(?x)         
		(?:[A-Za-z]\.)+        # Looks for abbreviations such as i.e. or U.S.A. 
		| \w+(?:-\w+)*         # Looks for words with hyphens within them
		| [][.,;"'?():_`-]     # Looks for and seperates grammatical tokens such as , or ; 
		'''

	return nltk.regexp_tokenize(inputString, regex)


def printDictionary(d):
	
	# letters, index, and multiples vars are used for 'numbering' each word. index saves the letter numbers and multiples is used to denote how many letters are needed
	letters = "abcdefghijklmnopqrstuvwxyz"       
	index = 0				
	multiples = 1

	# iterate through dictionary and print 
	for key,val in sorted(d.items()):	
		# Format the sentence numbers into a temp var for ease of printing
		tmp = '{' + str(val[0]) + ': '
		for i in val[1:]:
			tmp = tmp + str(i) + ','
		# omits the last comma and adds '}' 	
		tmp = tmp[:len(tmp) - 1] + '}'  

		# create 3 columns of 45 characters to allow for long texts, also the longest word in an English Oxford dictionary is 45 letters
		print("{: <45} {: <45} {: <45}".format(letters[index]*multiples + '.', key, tmp))
	
		# increment the letter for numbering and if the letter is at z, wrap back around to a with an additional letter
		index += 1
		if index == 26:
			multiples += 1
			index = 0

def readFile():
	with open ("input.txt", "r") as myFile:
		inputString = myFile.readlines()

	return str(inputString)

def main():

	# This program supports reading from a txt file as well as a hard coded string. Feel free to test both methods. Simply uncomment the method you wish to use
	# and leave the other one commented out. 

	inputString = """Given an arbitrary text document written in English, write a program that will generate a concordance, i.e. an alphabetical list of all word occurrences, labeled with word frequencies. Bonus: label each word with the sentence numbers in which each occurrence appeared.""" 
	#inputString = readFile()
	sentenceNumber = 1
	myWords = {}

	mySentences = tokenize(inputString)

	# Check for end of sentences and sent all words to be added to dictionary
	for i in mySentences:
		if (i == '.'):
			sentenceNumber += 1
		else:
			addWord(i.lower(), sentenceNumber, myWords)

	printDictionary(myWords)


if __name__ == "__main__": main()



