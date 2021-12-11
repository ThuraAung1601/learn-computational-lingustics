## Regular Expressions, Text Normalization, Edit Distance

#### Syllable Segmentation

```text
အနက်ပေးသံစဉ်
(toneme)
|
|
| ----> ဝဏ္ဏ   -----> သဒ္ဒါရုပ်ရင်း -----> စကားလုံး -----> စကားစု -----> ဝါကျငယ် (သို့) ဝါကျ
|     (syllable)    (morpheme)       (word)       (phrase)    (clause or sentence)
|
အနက်ပေးသံရင်း
(phoneme)
```

```{r, engine='bash', count_lines}
python ./sylbreak.py -i ../data/input.txt -o output.txt -s " "
```

References : 
![Swan Htet's ReSegment](https://github.com/swanhtet1992/ReSegment)
![Ye Kyaw Thu's syllbreak](https://github.com/ye-kyaw-thu/sylbreak)

