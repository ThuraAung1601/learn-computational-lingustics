## Regular Expressions, Text Normalization, Edit Distance

#### Syllable Segmentation

```text
ကျောင်းသား -----> ကျောင်း + သား 
အတွေးအခေါ် -----> အ + တွေး + အ + ခေါ်
တက္ကသိုလ် -----> တက် + က + သိုလ် 
ဂျော့ချ်ဘုရှ် ----> ဂျော့ချ် + ဘုရှ်  
မင်္ဂလာပါ ----> မင်် + ဂ + လာ + ပါ
```
![syllable_structure](syllable-structure.png)

- How to run
```{r, engine='bash', count_lines}
python ./sylbreak.py -i ../data/input.txt -o output.txt -s " "
```
#### Word tokenization

```text
ကျန်းမာတယ်၊ ဒါပေမဲ့ အလုပ်များတယ်။ -----> ကျန်းမာ + တယ် + ၊ + ဒါပေမဲ့ + အလုပ် + များ + တယ် + ။
မြန်မာပြည်လူအခွင့်အရေးကိုလျစ်လျူမရှုဖို့တိုက်တွန်း -----> မြန်မာ + ပြည် + လူ + အခွင့် + အရေး + ကို + လျစ်လျူမရှု + ဖို့ + တိုက်တွန်း
```
- How to run
```{r, engine='bash', count_lines}
python ./word-tokenizer.py -i ../data/input.txt -o output.txt -s " "
```


References : 
<br>
[1] Maung, Zin Maung, and Yoshiki Mikami. "A rule-based syllable segmentation of Myanmar text." Proceedings of the IJCNLP-08 Workshop on NLP for Less Privileged Languages. 2008.

