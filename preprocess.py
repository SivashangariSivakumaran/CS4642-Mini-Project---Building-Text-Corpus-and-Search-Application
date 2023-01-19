import json
import codecs
import pandas as pd

f = codecs.open('corpus/tamilsongs_bulk.json', 'w', encoding='utf-8')
df = pd.read_csv('corpus/Corpus-180610U-final.csv')

def checkNull(val):
    return isinstance(val, str)
    
list_ = [[["உருவகம் 1",'Metaphor 1'], ["மூல பொருள் 1",'Source Domain 1'], ["இலக்கு பொருள் 1", 'Target Domain 1'], ["விளக்கம் 1",'Interpretation 1' ]],
[["உருவகம் 2",'Metaphor 2'], ["மூல பொருள் 2",'Source Domain 2'], ["இலக்கு பொருள் 2", 'Target Domain 2'], ["விளக்கம் 2",'Interpretation 2' ]],
[["உருவகம் 3",'Metaphor 3'], ["மூல பொருள் 3",'Source Domain 3'], ["இலக்கு பொருள் 3", 'Target Domain 3'], ["விளக்கம் 3",'Interpretation 3' ]],
[["உருவகம் 4",'Metaphor 4'], ["மூல பொருள் 4",'Source Domain 4'], ["இலக்கு பொருள் 4", 'Target Domain 4'], ["விளக்கம் 4",'Interpretation 4' ]],
[["உருவகம் 5",'Metaphor 5'], ["மூல பொருள் 5",'Source Domain 5'], ["இலக்கு பொருள் 5", 'Target Domain 5'], ["விளக்கம் 5",'Interpretation 5' ]],
[["உருவகம் 6",'Metaphor 6'], ["மூல பொருள் 6",'Source Domain 6'], ["இலக்கு பொருள் 6", 'Target Domain 6'], ["விளக்கம் 6",'Interpretation 6' ]],
[["உருவகம் 7",'Metaphor 7'], ["மூல பொருள் 7",'Source Domain 7'], ["இலக்கு பொருள் 7", 'Target Domain 7'], ["விளக்கம் 7",'Interpretation 7' ]]
]

for i in range(df.shape[0]):
    
    dict_ = {}
    dict_["பாடல் பெயர்"] = df['Song Name'][i]
    dict_["பாடல் வரிகள்"] = df['Lyrics'][i]
    dict_["இசையமைப்பாளர்"] = df['Composer'][i]
    dict_["பாடலாசிரியர்"] = df['Lyricist'][i]
    dict_["பாடகர்"] = df['Singer'][i]
    dict_["திரைப்படம்"] = df['Album'][i]
    dict_["வெளியிடப்பட்ட ஆண்டு"] = df['Year'][i]
    
    for j in range(7):
        for k in range(4):
            val = df[list_[j][k][1]][i]
            if  checkNull(val):
                dict_[list_[j][k][0]] = val
    

    f.write('{ "index" : { "_index" : "tamilsongs_db", "_id" :' + str(i) + ' } }\n')
    json.dump(dict_, f, ensure_ascii=False)
    f.write('\n')
    i += 1
print ("\n\n---Corpus csv is converted to Bulk Json successfully---\n\n")