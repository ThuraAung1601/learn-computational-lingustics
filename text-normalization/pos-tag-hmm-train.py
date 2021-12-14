'''
author : Thura Aung
Training for pos-tagging with Hidden Markov Models 
'''
import argparse
import re

parser = argparse.ArgumentParser(description='Pos-tagging for Myanmar language')
parser.add_argument('-i', '--input', type=str, help='input file', required=True)
parser.add_argument('-o', '--output', type=str, default='hmmmodel.txt', help='output file', required=True)
args = parser.parse_args()

inputFile = getattr(args, 'input')
outFile = getattr(args, 'output')

# variables to keep the word/tags and tag/tag
tag_tag_dict = dict()
word_tag_dict= dict()

# variables to keep the counts
unique_tags_count_dict = dict()
        
# variables to keep the probabilities
emission_probabilities = dict()
transition_probabilities = dict()   

def calculate_probabilities():
        
        # emission probability
        for key, value in word_tag_dict.items():
            var_array = key.split("/")
            tag = var_array[-1]
            emission_probabilities[key] = value / float(unique_tags_count_dict[tag])
        
        # transition probability
        for key, value in tag_tag_dict.items():
            prev_tag = key.split("/")[0]
            exclude_tag = prev_tag + "/<~s>"
            exclude_prob = tag_tag_dict[exclude_tag] if exclude_tag in tag_tag_dict else 0
            transition_probabilities[key] = (1+value) / float(len(unique_tags_count_dict) + unique_tags_count_dict[prev_tag] - exclude_prob)

 def parse_sentence(sentence):
        
        previous = "<s>"
        previous = previous.strip()
        if previous not in unique_tags_count_dict:
            unique_tags_count_dict[previous] = 0
            unique_tags_count_dict[previous] += 1
        
        word_tags = sentence.split(" ")
        
        for i, word_tag in enumerate(word_tags):
            word_tag = word_tag.strip()
            var_array = word_tag.split("/")
            tag = var_array[-1]
            tag = tag.strip()
            
            if tag not in unique_tags_count_dict:
              unique_tags_count_dict[tag] = 0
              unique_tags_count_dict[tag] += 1
            
            if word_tag not in word_tag_dict:
                word_tag_dict[word_tag] = 0
                word_tag_dict[word_tag] += 1
            
            if previous + "/" + tag not in tag_tag_dict:
              tag_tag_dict[previous + "/" + tag] = 0
              tag_tag_dict[previous + "/" + tag] += 1
            
            previous = tag
        
        if previous + "/<~s>" not in tag_tag_dict:
            tag_tag_dict[previous + "/<~s>"] = 0
            tag_tag_dict[previous + "/<~s>"] += 1
            
def save_model(outFile):
        file_object = open(outFile, "w")
    
        for string, prob in emission_probabilities.items():
            file_object.write("em " + string + " " + str(prob))
            file_object.write("\n")
    
        for string, prob in transition_probabilities.items():
            file_object.write("tr " + string + " " + str(prob))
            file_object.write("\n")
    
        for tag, count in unique_tags_count_dict.items():
            exclude_count = 0
            if tag + "/<~s>" in tag_tag_dict:
                exclude_count = tag_tag_dict[tag + "/<~s>"]
            file_object.write("tg " + tag + " " + str(count - exclude_count))
            file_object.write("\n")
            
        file_object.close()

with open(inputFile,encoding='utf-8') as file:
  sentences = file.readlines()
  for sentence in sentences:
    parse_sentence(sentence)
            
calculate_probabilities()
save_model(outFile)
