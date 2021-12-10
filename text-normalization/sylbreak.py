import argparse
import re

parser = argparse.ArgumentParser(description='Syllable segmentation for Myanmar language')
parser.add_argument('-i', '--input', type=str, help='input file', required=True)
parser.add_argument('-o', '--output', type=str, default='sylbreak_out.txt', help='output file')
parser.add_argument('-s', '--separator', type=str, default=r'|', help='the separator option for syllable (e.g. -s "/"), default is "|"')
args = parser.parse_args()

inputFile = getattr(args, 'input')
outFile = getattr(args, 'output')
sOption = getattr(args, 'separator')

myConsonant = r"က-အ"
enChar = r"a-zA-Z0-9"
otherChar = r"ဣဤဥဦဧဩဪဿ၌၍၏၀-၉၊။!-/:-@[-`{-~\s"
ssSymbol = r"္"
aThat = r"်င်္"

CleanPattern = re.compile(r'\d+|[၊။!-/:-@[-`{-~\t ]|[A-za-z0-9]')

def clean_sentence(sentence):
    cleaned = CleanPattern.sub("",sentence)
    return cleaned

BreakPattern = re.compile(r"((?<!" + ssSymbol + r")["+ myConsonant + r"](?![" + aThat + ssSymbol + r"[" + myConsonant + r"]" + r"])" + r"|[" + enChar + otherChar + r"])", re.UNICODE)

data = ""

# Try read file and syllable 
try:
   with open(inputFile, encoding='utf-8') as file:
      for line in file:
         # clean the task
         cleaned = clean_sentence(sentence)
         
         # start breaking
         line = BreakPattern.sub(sOption + r"\1", cleaned)
         data += line
        
except:
   exit('Input file cannot be opened!')

# Writing Data to Output File
if outFile:
   try:
      with open(outFile, 'w',  encoding='utf-8') as file:
         file.write(data)
      print(f"Sylbreak succcessfully done. Write data to {outFile}")
   except:
      exit('Output file cannot be opened!')

