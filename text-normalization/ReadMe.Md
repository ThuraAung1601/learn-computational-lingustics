## Regular Expressions, Text Normalization, Edit Distance

#### Syllable Segmentation

```text
ဥပမာ။ ။

ကျောင်း + သား -----> ကျောင်းသား
အ + တွေး + အ + ခေါ် -----> အတွေးအခေါ်
တက် + က + သိုလ် -----> တက္ကသိုလ်
ဂျော့ချ် + ဘုရှ် ----> ဂျော့ချ်ဘုရှ်
```

```{r, engine='bash', count_lines}
python ./sylbreak.py -i ../data/input.txt -o output.txt -s " "
```

References : 
[Swan Htet's ReSegment](https://github.com/swanhtet1992/ReSegment)
[Ye Kyaw Thu's syllbreak](https://github.com/ye-kyaw-thu/sylbreak)

