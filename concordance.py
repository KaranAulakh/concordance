
import nltk	# used for tokenizing the text

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
	'''
	Create a regex pattern to look for situations that may seem like the end of a sentence but are not, such as abbreviations. As well as ensure that 
	hypenated words remain together as one token: For example, high-tech should be treated as a single word and not tokenized seperately. The pattern 
	also looks for other grammatical charcters and tokenizes them seperately as to not place them with words
	'''	
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

# Used to read in the entire input of the file into a string (nltk requires a string to be tokenized)
def readFile():
	with open ("input.txt", "r") as myFile:
		inputString = myFile.readlines()

	return str(inputString)

def main():

	# This program supports reading from a txt file as well as a hard coded string. Feel free to test both methods. Simply uncomment the method you wish to use
	# and leave the other one commented out

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



