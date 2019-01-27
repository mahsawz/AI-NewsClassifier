
import re
import string
import io 
import random
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer


sport_text = "raw_data_sport.txt"
politics_text = "raw_data_politics.txt"



def stemer(text): # returns the root of the word s jam ru hazf mikone

	words = []
	stemmer= PorterStemmer()
	input_str = text
	input_str = word_tokenize(input_str)
	for word in input_str:
	    words.append(stemmer.stem(word))
	return words

def lemmatizer(text): # zamir o jam o ina ru handle mikone

	words = []
	lemmatizer=WordNetLemmatizer()
	input_str=text
	input_str=word_tokenize(input_str)
	for word in input_str:

	    words.append(lemmatizer.lemmatize(word))
	return words


def cleaning(raw_text, dest1, dest2): # put cleaned words in filtered file
	cleaned_file = open("sport_semi_cleaned.txt", "r+")
	with open(raw_text, 'r') as fileinput:
	   for line in fileinput:
	       line = line.lower()  # Convert text to lowercase
	       line = re.sub(r'\d+', '', line) # Remove numbers
	      
	       cleaned_file.write(line)
	cleaned_file.close()

	# tokenizing and delete stop words from cleaned file 
	stop_words = set(stopwords.words('english')) 


	file1 = open(dest1) 
	line = file1.read()# Use this to read file content as a stream: 

	words = line.split() 
	for r in words: 
	    if not r in stop_words: 
	        appendFile = open(dest2,'a') 
	        appendFile.write(r + " ") 
	        appendFile.close() 


if __name__ == "__main__":

	cleaning(sport_text, "sport_semi_cleaned.txt", 'sport_cleaned.txt')
	cleaning(politics_text, "politics_semi_cleaned.txt", 'politics_cleaned.txt')

	file1 = open('sport_cleaned.txt','r')
	file2 = open('politics_cleaned.txt', 'r')
	text_sport = file1.read()
	text_poli = file2.read()

	
	print (len(test1))
	# print (len(tr))

	# text2 = stemer(text)
	# text = lemmatizer(text)
	# print text
