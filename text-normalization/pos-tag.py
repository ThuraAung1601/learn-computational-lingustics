'''
author : Thura Aung
Viterbi Algorithm for POS Tagging with Trained HMM model
'''
import argparse
import re
import pyidaungsu as pds

parser = argparse.ArgumentParser(description='POS-tagging for Myanmar language')
parser.add_argument('-i', '--input', type=str, help='input file', required=True)
parser.add_argument('-m', '--model', type=str, default='hmmmodel.txt', help='the model for tagging', required=True)
parser.add_argument('-o', '--output', type=str, default='output.txt', help='output file', required=True)
args = parser.parse_args()

inputFile = getattr(args, 'input')
outFile = getattr(args, 'output')
modelFile = getattr(args, 'model')

# variables to keep possible tags and words
possible_tags = set()
possible_words = set()
        
# variable to keep possible tags count
possible_tags_count = dict()
        
# variables to keep the probabilities
emission_probabilities = dict()
transition_probabilities = dict()

 with open(modelFile) as file:
            lines = file.readlines()
            for line in lines:
                var_array = line.split(" ")
                if var_array[0] == "em":
                    emission_probabilities[var_array[1]] = float(var_array[2].strip())
                    word_tag = var_array[1]
                    word = word_tag.rsplit("/")[0]
                    possible_words.add(word)
        
                elif var_array[0] == "tr":
                    transition_probabilities[var_array[1]] = float(var_array[2].strip())
        
                elif var_array[0] == "tg":
                    possible_tags.add(var_array[1].strip())
                    possible_tags_count[var_array[1]] = int(var_array[2].strip())

def smooth_probabilities(word, prev_tag, cur_tag):
        
        if (prev_tag + "/" + cur_tag) not in transition_probabilities:
            tr_prob = 1 / float(len(possible_tags) + possible_tags_count[prev_tag])
        else:
            tr_prob = transition_probabilities[prev_tag + "/" + cur_tag]
        
        if word not in possible_words:
            em_prob = 1
        elif (word + "/" + cur_tag) not in emission_probabilities:
            em_prob = 0
        else:
            em_prob = emission_probabilities[word + "/" + cur_tag]
            
        return em_prob, tr_prob

def viterbi_algorithm(sentence):
        best_edge = dict()
        best_score = dict()
        words = sentence.split(" ")
        words = [word.strip() for word in words]
       
        for tag in possible_tags:
            em_prob, tr_prob = smooth_probabilities(words[0], "<s>", tag)
            best_score[(words[0], tag, 0)] = em_prob * tr_prob
            best_edge[(words[0], tag, 0)] = "<s>"

        for i in range(1, len(words)):
            for cur_tag in possible_tags:
                temp_score = 0
                if (words[i] in possible_words) and ((words[i] + "/" + cur_tag) not in emission_probabilities):
                    best_score[(words[i], cur_tag, i)] = temp_score
                else:
                    for prev_tag in possible_tags:
                        em_prob, tr_prob = smooth_probabilities(words[i], prev_tag, cur_tag)
                        score = best_score[(words[i-1], prev_tag, i-1)] * em_prob * tr_prob
                        best_score[(words[i], cur_tag, i)] = temp_score
                        
                        if score > temp_score:
                            temp_score = score
                            best_score[(words[i], cur_tag, i)] = score
                            best_edge[(words[i], cur_tag, i)] = prev_tag
        score = 0
        best_tag = None
        tagged_sentence = []
        nth_word = words[-1]
        words_length = len(words) - 1
        for tag in possible_tags:
            if best_score[(nth_word, tag, words_length)] > score:
                score = best_score[(nth_word, tag, words_length)]
                best_tag = tag
        tagged_sentence.append((nth_word, best_tag))
        
        for i in range(len(words) - 2, -1, -1):
            tagged_sentence.append((words[i], best_edge[(words[i+1], best_tag, i+1)]))
            best_tag = best_edge[(words[i+1], best_tag, i+1)]
            
        return tagged_sentence

def tag_sentence(sentence, file_object):
        tagged_sentence = viterbi_algorithm(sentence)
        tagged_sentence = tagged_sentence[::-1]
        
        lnth = len(tagged_sentence)
        for i, word_tag in enumerate(tagged_sentence):
            word = word_tag[0]
            tag = word_tag[1]
            file_object.write(word + "/" + tag)
            if i != lnth - 1:
                file_object.write(" ")
        
        file_object.write("\n")

file_object = open(outFile, "w")

with open(inputFile,encoding='utf-8') as file:
  sentences = file.readlines()
  for i, sentence in enumerate(sentences):
    tag_sentence(sentence, file_object)
            
file_object.close()
