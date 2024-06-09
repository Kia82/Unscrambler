import sys
import time

#Takes wordlist and unscrables all the words in wordsToUnscrable.
#CONSTRAINT: ALL words
def unscrable():
    word_map = {}
    with open('../data/wordlist.txt', 'r') as file:
        for line in file:
            word = line.strip()
            wordsSorted = ''.join(sorted(word))
            word_map[wordsSorted] = word
            
    with open('../data/wordsToUnscrable', 'r') as file:
        wordsToUnscrableList = []
        for line in file:
            word = line.strip()
            if(word != ''):
                word = ''.join(sorted(word))
                try:
                    wordsToUnscrableList.append(word_map[word])
                except KeyError as e:
                    print(f"\033[91m KeyError: {e} is not in the wordlist and will be removed from the output\033[0m\n")
                    
            
        print(', '.join(wordsToUnscrableList), end='')

if __name__ == '__main__':
    unscrable()
    

    