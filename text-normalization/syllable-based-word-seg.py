'''
Author : Thura Aung
Syllable-based word segmentation using maximum matching
'''

import argparse
import re

parser = argparse.ArgumentParser(description='Syllable-based word segmentation for Myanmar language')
parser.add_argument('-i', '--input', type=str, help='input file', required=True)
parser.add_argument('-o', '--output', type=str, default='sylbreak_out.txt', help='output file', required=True)
parser.add_argument('-d', '--dictionary', type=str, default='word-list.txt', help='dictionary file', required=True)

args = parser.parse_args()

inputFile = getattr(args, 'input')
outFile = getattr(args, 'output')
dictFile = getattr(args,'dictionary')

w_list = []
with open(dictFile, encoding = 'utf8') as filehandle:
    for line in filehandle:
        line = line.replace("\n","")
        w_list.append(line)

CleanPattern = re.compile(r'\d+|[၊။!-/:-@[-`{-~\t ]|[A-za-z0-9]')

def clean_sentence(sentence):
    cleaned = CleanPattern.sub("",sentence)
    return cleaned

BreakPattern = re.compile(r'(?:(?<!္)([က-ဪဿ၊-၏]|[၀-၉]+|[^က-၏]+)(?![ှျ]?[့္်]))')

def sylbreak(sentence):
    line = BreakPattern.sub(" " + r"\1",sentence)
    return line

def max_match(sentence, dictionary):
    if not sentence:
        return ""
    for i in range(len(sentence), -1, -1):
        first_word = sentence[:i]
        first_word=''.join(first_word) # word seg
        
        remainder = sentence[i:]
        remainder=''.join(remainder) # word seg
        
        if first_word in dictionary:
            return first_word + " " + max_match(remainder, dictionary)
        
    first_word = sentence[0]
    remainder = sentence[1:]
    return first_word + max_match(remainder, dictionary)


data = ""

# Try read file and syllable 
try:
   with open(inputFile, encoding='utf-8') as file:
      for line in file:
         # clean the task
         cleaned = clean_sentence(line)
         
         # start breaking
         line = sylbreak(cleaned).split()
         result = max_match(line,w_list)
         data += result
        
except:
   exit('Input file cannot be opened!')

# Writing Data to Output File
if outFile:
   try:
      with open(outFile, 'w',  encoding='utf-8') as file:
         file.write(data)
      print(f"Syllable-based word segmentation succcessfully done. Write data to {outFile}")
   except:
      exit('Output file cannot be opened!')

