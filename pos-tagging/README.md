## Myanmar POS Tagging 

#### POS Tags

15 Myanmar POS are used in our tag set to meet the necessity of further NLP processing such as information extraction, semantic processing and machine translation. The definitions and descriptions of POS tags are presented in detail as follows:

| POS Tag        | Brief Definition           | Examples  |
| ------------- |-------------|------|
| abb      | Abbreviation | အထက(Basic Education High School), လ.ဝ (Confidentiality) |
| adj      | Adjective      |  ရဲရင့် (brave), လှပ (beautiful), မွန်မြတ် (noble)  |
| adv | Adverb      | ဖြေးဖြေး (slow), နည်းနည်း (less) |
| conj | Conjunction | နှင့် (and), ထို့ကြောင့် (therefore), သို့မဟုတ် (or) |
| fw | Foreign Word | 1, 2, 3, Myanmar, ミャンマー (Myanmar in Japanese), BBC, Google. 缅甸 (Myanmar in Chinese)|
| int | Interjection | အမလေး (Oh My God!) |
| n | Noun | ကျောင်း (school), စာအုပ် (book), ဒေါ်အောင်ဆန်းစုကြည် (Daw Aung San Suu Kyi), လွတ်လပ်ရေး (freedom) |
| num | Number | ၁ (1), ၂ (2), ၃ (3), ၁၀ (10), ၁၀၀ (100), ၁၀၀၀ (1000) |
| part | Particle | များ (used to form the plural nouns as "-s" , "-es"), ခဲ့ (the past tense "-ed"), သင့် (modal verb "shall"), လိမ့် (modal verb "will"), နိုင် (modal verb "can") |
| ppm | Post-positional Marker | သည်, က, ကို, အား, သို့, မှာ, တွင် (at, on ,in, to) |
| pron | Pronoun | ကျွန်တော် (I), ကျွန်မ (I), သင် (you), သူ (he), သူမ (she) |
| punc | Punctuation | ။, ၊, (, ), \, _ , ', " |
| sb | Symbol | ?, #, &, %, $, £, ¥, 𝜆, π, ÷, +, ×, @ |
| tn | Text Number | တစ် (one), နှစ် (two), သုံး (three), တစ်ရာ (one hundred), တစ်ထောင် (one thousand) |
| v | Verb | ကူညီ (help), လိုက်နာ (observe), အားပေး (encourage) |


#### Myanmar POS Tagging with Hidden Markov Models and variation on Viterbi Algorithm

```text
မင်္ဂလာ ပါ ။ -----> မင်္ဂလာ/n ပါ/part ။/punc
နေကောင်း လား ။ -----> နေကောင်း/v လား/part ။/punc
ကျန်းမာ တယ် ၊ ဒါပေမဲ့ အလုပ် များ တယ် ။ -----> ကျန်းမာ/adj တယ်/part ၊/punc ဒါပေမဲ့/conj အလုပ်/n များ/adj တယ်/part ။/punc
မြန်မာ ပြည် လူ အခွင့် အရေး ကို လျစ်လျူမရှုဖို့ တိုက်တွန်း ။ -----> မြန်မာ/n ပြည်/n လူ/n အခွင့်/adj အရေး/n ကို/part လျစ်လျူမရှုဖို့/adj တိုက်တွန်း/adj ။/punc
```

- Extracted 550 sentences from train portion and concatenate with the whole test portion of [myPos-v3.0](https://github.com/ye-kyaw-thu/myPOS/tree/master/corpus-ver-3.0) corpus without pipes "|" for training the HMM

- How to train - input is training tagged corpus and output is model file including tagged word with probabilities
```{r, engine='bash', count_lines}
python ./pos-tag-hmm-train.py -i ../data/pos-tagging-train.txt -o hmmmodel.txt
```

- How to run - input are test data for -i model file for -m and output is the tagged result
```{r, engine='bash', count_lines}
python ./pos-tag.py -i ../data/pos-input.txt -m ./hmmmodel.txt -o output.txt
```

References : 
<br>
[1] Khin War War Htike, Ye Kyaw Thu, Zuping Zhang, Win Pa Pa, Yoshinori Sagisaka and Naoto Iwahashi, "Comparison of Six POS Tagging Methods on 10K Sentences Myanmar Language (Burmese) POS Tagged Corpus", at 18th International Conference on Computational Linguistics and Intelligent Text Processing (CICLing 2017), April 17~23, 2017, Budapest, Hungary.
<br>
[2] Zar Zar Hlaing, Ye Kyaw Thu, Myat Myo Nwe Wai, Thepchai Supnithi, Ponrudee Netisopakul, "Myanmar POS resource extension effects on automatic tagging methods", In Proceedings of the 15th International Joint Symposium on Artificial Intelligence and Natural Language Processing (iSAI-NLP 2020), Nov 18 to Nov 20, 2020, Bangkok, Thailand, pp. 189-194. 
