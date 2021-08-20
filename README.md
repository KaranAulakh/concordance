# Concordance


Interview exercise to create a concordance given an input text. The concordance denotes how many times and which sentences a word appeared in alphabetical order.

## Logic Overview
1. **tokenize():** Extract the text from the source and split into sentences. This step is implemented using punkt from nltk, however punkt alone is not capable of recognizes abbreviations, ellipses results in false positives of sentence ends. Thus a regex pattern is also required to recognize this specific cases. 
2. **addWord():** Check each token and determine whether it should be added to the dictionary. Checks to see if the word contains atleast one letter, this eliminates punctation such as commas, colons, etc. Adds words to the dictionary or updates its value if the word is already added
	- Time complexity is O(W) where W is word length. This is due to iterating through each char to check for alphanumeric values
3. **printDictionary()** Sort the dictionary and print with correct formatting. Technically the actual dictionary is not being sorted but the output is sorted through python's timsort algorithm 
	- Sorting results in a Time complexity of O(nlogn). Since iterating the dictionary is only O(n) the total time complexity of the print method remains O(nlogn)



## Installation and Usage
1. MacOS
	1. Python
		- Python should be preinstalled on MacOs, to verify run `python3 --version` in terminal. Python 3.5 or newer is required to run this project; however, 3.9 or newer is recommended as this project was written in 3.9.1 
	2. pip 
		- pip is needed to install nltk, if you don't have it already use the below commands to install pip3
		- `curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`
		- `python3 get-pip.py`
	3. nltk
		- run the following command in terminal to install nltk
		- `pip3 install --user -U nltk`
	4. Run the code in terminal
		- use cd to navigate to the location of concordance.py (ensure input.txt is in the same location)
		- run the file using `python3 concordance.py`
2. Windows
	1. Python
		- Python can be downloaded from Microsoft Store. Python 3.5 or newer is required to run this project; however, 3.9 or newer is recommended as this project was written in 3.9.1. Once python is installed run `python --version` in powershell to verify. 
		- For more information visit: https://docs.microsoft.com/en-us/windows/python/beginners
	2. Pip will come pre-installed once you download python through the Microsoft Store. Refer here: https://www.liquidweb.com/kb/install-pip-windows/ in case you don't have pip pre installed. To verify run `pip --version`
	3. nltk: run the following command in powershell to install nltk
		- `pip3 install --user -U nltk`
	4. Run the code in powershell
		- use cd to navigate to the location of concordance.py (ensure input.txt is in the same location)
		- run the file using `python concordance.py`
