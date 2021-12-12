## Regular Expressions, Text Normalization, Edit Distance

#### Syllable Segmentation

```text
ဥပမာ။ ။

ကျောင်း + သား -----> ကျောင်းသား
အ + တွေး + အ + ခေါ် -----> အတွေးအခေါ်
တက် + က + သိုလ် -----> တက္ကသိုလ်
ဂျော့ချ် + ဘုရှ် ----> ဂျော့ချ်ဘုရှ်
```
![syllable_structure](syllable-structure.png)

```{r, engine='bash', count_lines}
python ./sylbreak.py -i ../data/input.txt -o output.txt -s " "
```

References : 
[1] Maung, Zin Maung, and Yoshiki Mikami. "A rule-based syllable segmentation of Myanmar text." Proceedings of the IJCNLP-08 Workshop on NLP for Less Privileged Languages. 2008.

