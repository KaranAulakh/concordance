# Concordance


Interview exercise to create a concordance given an input text. The concordance denotes how many times and which sentences a word appeared in alphabetical order.

## Logic Overview
1. **tokenize():** Extract the text from the source and split into sentences. This step is implemented using punkt from nltk, however punkt alone is not capable of recognizes abbreviations, ellipses results in false positives of sentence ends. Thus a regex pattern is also required to recognize this specific cases. 
2. **addWord():** Check each token and determine whether it should be added to the dictionary. Checks to see if the word contains atleast one letter, this eliminates punctation such as commas, colons, etc.
	- Time complexity is O(W) where W is word length
Adds words to the dictionary or updates its value if the word is already added
	- Time complexity is O(1)
3. **printDictionary()** Sort the dictionary and print with correct formatting. Technically the actual dictionary is not being sorted but the output is sorted through python's timsort algorithm 
	- Sorting results in a Time complexity of O(nlogn). Since iterating the dictionary is only O(n) the total time complexity of the print method remains O(nlogn)



## Installations
1. python
	- a version of 3.5 or higher is required to be compatible with nltk. 3.9 or higher is recommended as this project was written using 3.9.1
2. nlkt
	- nlkt requires python 3.5 or newer
	- pip install --user -U nltk (for MAC/UNIX)  ...   https://www.nltk.org/install.html
	- run the provided file nltk.py which will open a GUI window and download punkt under models, this needs to be down before running concordance.py
