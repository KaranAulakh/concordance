# Concordance


Interview exercise to create a concordance given an input text. The concordance denotes how many times and within which sentences a word appears in alphabetical order. For more information on the challenge prompt, please view the included file 'code challenge.pdf'

## Logic Overview
1. Extract the text from the source and split into sentences. This step is implemented using nltk, however nltk alone is not capable of recognizing abbreviations or ellipses resulting in false positives of sentence ends. Thus a regex pattern is also required to recognize this specific cases. This pattern also seperates punction from words except for in the case of hyphenated words. Implemented with the method: **tokenize()**.
	- Time complexity is O(n) where n is the size of the input text.
3. Check each token and determine whether it should be added to the dictionary. Checks to see if the word contains atleast one letter, this eliminates punctation such as commas, colons, etc. Adds words to the dictionary or updates its value if the word is already added. Implemented with the method: **addWord()**.
	- Time complexity is O(n) where n is word length. This is due to iterating through each char to check for alphanumeric values. However since no word should be bigger than even 40 chars, this could be argued as O(40) which equals O(1).
4. Sort the dictionary and print with correct formatting. Technically the actual dictionary is not being sorted but the output is sorted through python's timsort algorithm. Implemented with the method: **printDictionary()**.
	- Sorting results in a Time complexity of O(nlogn). Since iterating sorting with timsort is O(nlogn) and iterating through the dictionary is only O(n) the total time complexity of the print method remains O(nlogn).



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


## Design Decisions
1. Tokenizing
	- nltk is one of python's most powerful tokenizer. It provides many different methods for tokenizing including the ability to use a custom regex pattern. This allows for my code to prevent false positive sentence ends as well as properly split up grammatical punctions such as commas and colons from words. nltk is also easier to use as opposed to something like punkt which involves downloading it on every run. 
3. Storing Words
	- I chose to store each word in a dictionary due to its low cost in adding new words as well as checking if a word already exists. The only drawback in a dictionary is that it is rather inefficient to maintain a sorted dictionary. However sorted it during the print still yields a time complexity of O(nlogn). Alternatively, storing the words in a sorted list or tuple would result in inefficiences upon entering new elements and checking if elements already exist. 
