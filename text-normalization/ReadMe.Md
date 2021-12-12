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

```{r, engine='bash', count_lines}
python ./sylbreak.py -i ../data/input.txt -o output.txt -s " "
```

References : 
[1] Maung, Zin Maung, and Yoshiki Mikami. "A rule-based syllable segmentation of Myanmar text." Proceedings of the IJCNLP-08 Workshop on NLP for Less Privileged Languages. 2008.

