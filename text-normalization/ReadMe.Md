## Regular Expressions, Text Normalization, Edit Distance

#### Syllable-level Segmentation

```text
ကျောင်းသား -----> ကျောင်း + သား 
အတွေးအခေါ် -----> အ + တွေး + အ + ခေါ်
တက္ကသိုလ် -----> တက် + က + သိုလ် 
ဂျော့ချ်ဘုရှ် ----> ဂျော့ချ် + ဘုရှ်  
မင်္ဂလာပါ ----> မင်် + ဂ + လာ + ပါ
```
![syllable_structure](syllable-structure.png)
- (၁) ဗျည်း (Consonant) ၏အနောက်တွင် အသတ် (Asat) မရှိရပါ၊ သို့မဟုတ် ဝိရာမသင်္ကေတ (Virama sign) မရှိရပါ။
- (၂) ဗျည်း (Consonant) ၏အရှေ့တွင် ဝိရာမသင်္ကေတ (Virama sign) မရှိရပါ။
- ဒီနှစ်ချက်လုံးနဲ့ ​သွေဖယ်​တဲ့ ဗျည်း(Consonant) ကိုသာ ဝဏ္ဏအဆုံးသတ်(Syllable Boundary) အဖြစ်သတ်မှတ်၍ ဝဏ္ဏဖြတ်​တောက်နိုင်ပါသည်။

- How to run
```{r, engine='bash', count_lines}
python ./sylbreak.py -i ../data/input.txt -o output.txt -s " "
```
#### Syllable-based Word Segmentation using maximum matching

```text
နောက်ဆုံးဆန်ကာတင် ဖိုင်နယ်ထိ တက်ရောက်နိုင်ခဲ့တဲ့ မယ်လိုဒီခေါင် ---> နောက်ဆုံး + ဆန် + ကာ + တင် + ဖိုင် + နယ် + ထိ + တက်ရေ + ာက + ်နိုင် + ခဲ့ + တဲ့ + မယ် + လို + ဒီ + ခေါင် 
သတင်း ရုပ်ရှင်လောကအတွက် အပြောင်းအလဲ ဖြစ်လာမည်ဟု မျှော်လင့် ---> သတင်း + ရုပ်ရှင် + လောက + အတွက် + အပြောင်းအလဲ + ဖြစ်လာ + မည် + ဟု + မျှော်လင့်
```

- How to run
```{r, engine='bash', count_lines}
python ./syllable-based-word-seg.py -i ../data/input.txt -o output.txt -d word-list.txt
```


#### Myanmar Text Preprocessing

```text
ကျွန်တော် ကျန်းမာတယ်၊ ဒါပေမဲ့ အလုပ်များတယ်။ -----> ကျန်းမာ + တယ် + အလုပ် + များ + တယ်
မြန်မာပြည်လူအခွင့်အရေးကိုလျစ်လျူမရှုဖို့တိုက်တွန်း -----> မြန်မာ + ပြည် + လူ + အခွင့် + အရေး + ကို + လျစ်လျူမရှု + ဖို့ + တိုက်တွန်း
```
- Cleaning the text - remove all punc including "။" and english words and numbers
- Remove stop words and
- Tokenize the text using pyidaungsu library 
```{r, engine='bash', count_lines}
pip install pyidaungsu
```
- How to run - use -s for seperating
```{r, engine='bash', count_lines}
python ./text-preprocessing.py -i ../data/input.txt -o output.txt -s "|"
```

#### Edit distance calculation with Map-1 (Phonetic Mapping), Map-2 (Sound Mapping) and Map-3 (Vowel Position Mapping)
- Used Professor Ye Kyaw Thu's [tool](https://github.com/ye-kyaw-thu/tools/blob/master/python/str2my-edit-distances.py) for edit distance calculation
- How to run
```{r, engine='bash', count_lines}
python ./str2my-edit-distances.py --help
```

References : 
<br>
[1] Maung, Zin Maung, and Yoshiki Mikami. "A rule-based syllable segmentation of Myanmar text." Proceedings of the IJCNLP-08 Workshop on NLP for Less Privileged Languages. 2008.
<br>
[2] Khaing Hsu Wai, Ye Kyaw Thu, Swe Zin Moe, Hnin Aye Thant, Thepchai Supnithi, "Myanmar (Burmese) String Similarity Measures based on Phoneme Similarity", Journal of Intelligent Informatics and Smart Technology, April 1st Issue, 2020, pp. 27-34. (submitted December 21, 2019; accepted March 6, 2020; revised March 16, 2020; published online April 30, 2020) JIIST 2020 Journal Paper
<br>
[3] Khaing Hsu Wai, Ye Kyaw Thu, Hnin Aye Thant, Swe Zin Moe and Thepchai Supnithi, "String Similarity Measures for Myanmar Language (Burmese)", The First Workshop on NLP Solutions for Under Resourced Languages (NSURL 2019), 11-13 September 2019, Trento, Italy
