import argparse
import re
import pyidaungsu as pds

parser = argparse.ArgumentParser(description='Syllable segmentation for Myanmar language')
parser.add_argument('-i', '--input', type=str, help='input file', required=True)
parser.add_argument('-o', '--output', type=str, default='sylbreak_out.txt', help='output file', required=True)
parser.add_argument('-s', '--separator', type=str, default=r'|', help='the separator option for syllable (e.g. -s "/"), default is "|"', required=True)
args = parser.parse_args()

inputFile = getattr(args, 'input')
outFile = getattr(args, 'output')
sOption = getattr(args, 'separator')
data = "" 

CleanPattern = re.compile(r'\d+|[၊။!-/:-@[-`{-~\t ]|[A-za-z0-9]')

def clean_sentence(sentence):
    sentence = sentence.replace(" ",'')
    sent = CleanPattern.sub("",sentence)
    return sent

def removeStopWord(text,stopwordslist):
    text = text
    returnList = []       
    
    for i in text:
        if i in stopwordslist:
            continue
        else:
            returnList.append(i)

    temp = ""
    for j in returnList:
        if (len(returnList)>0):
            if j == returnList[-1]:
                temp += j
            else:
                temp += j + ""
            
    return temp

def tokenize(line):
    line = removeStopWord(line,"../data/stop_words.txt")
    sentence = pds.tokenize(line,form="word")
    sentence = sOption.join([str(elem) for elem in sentence])
    return sentence

with open(file_path) as fp:
    line = fp.readline()
    while line:
        data += "\n" + tokenize(line)
        line = fp.readline()

# Writing Data to Output File
if outFile:
    with open(outFile, 'w',  encoding='utf-8') as file:
        cleaned = clean_sentence(data)
        file.write(cleaned)
        print(f"Sylbreak succcessfully done. Write data to {outFile}")
