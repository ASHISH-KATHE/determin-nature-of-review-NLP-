# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 09:59:30 2019

@author: Ashish
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 20:18:48 2019

@author: Ashish
"""
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()
ww=[]
wwi=[]
def check(wrd):
    for word in ww:
        if word == wrd:
            return 1
    return 0

import spacy
import pandas as pd
from nltk.stem.snowball import SnowballStemmer
p_stem=SnowballStemmer(language='english')

df = pd.read_csv('Restaurant_Reviews.tsv', delimiter = '\t', quoting = 3)

print('spaCy Version: %s' % (spacy.__version__))
spacy_nlp = spacy.load('en_core_web_sm')
y=[]
y=df['Liked']
df_fin=[]
df_fin.append([])
s_stop= spacy.lang.en.stop_words.STOP_WORDS
s_stop.add('')
print('Number of stop words: %d' % len(s_stop))
#string='This story is about surfing Catching waves is fun Surfing is a popular water sport.'
#print(string)
str2=[]
k=0
for str1 in df['Review']:
    str1=str1.lower()
    str2.clear()
    str1=str1.split()
    i=len(str1)
    j=0
    while j<i:
        if str1[j] in s_stop:
            str1.remove(str1[j])
            i=i-1
            continue
        j=j+1
    
    for word in str1:
        str2.append(p_stem.stem(word))
    length=len(str2)
    temp=0
    while temp<length:
        str2[temp] = "".join(c for c in str2[temp] if c not in ('!','.',':',',','?','@'))
        if len(ps.stem(str2[temp]))>2:
            df_fin[k].append(ps.stem(str2[temp]))
        temp=temp+1
    df_fin.append([])
    k=k+1
    str1.clear()
df_fin.pop()
from sklearn.model_selection import train_test_split

#x_train,x_test,y_train,y_test=train_test_split(df_fin,df['label'],test_size=0.33)

temp=0
for word in df_fin:
    for let in word:
        if check(let)==1:
            if y[temp]==0:
                wwi[ww.index(let)]+=0.1
            elif y[temp]==1:
                wwi[ww.index(let)]-=0.1
                    
        else:
            ww.append(let)
            wwi.append(0)
    temp+=1

wwi[ww.index('wasn\'t')]=400
wwi[ww.index('not')]=400


sw=[]
temp=0
for word in df_fin:
    sw.append(0)
    for let in word:
        sw[temp]+=wwi[ww.index(let)]
    temp+=1
y_pred=[]


for x in sw:
    if x>0:
        y_pred.append(0)
    elif x<0:
        y_pred.append(1)
    else :
        y_pred.append(0)




from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y, y_pred)

print(cm)

print('Rating is :- ')
print(((cm[0][0]+cm[1][1])/(cm[0][1]+cm[1][0]+cm[0][0]+cm[1][1]))*100)

summ=0
i=0
while i<1 :
    ss=input('enter a review :- ')
    ss=ss.split(' ')
    for word in ss:
        word = "".join(c for c in word if c not in ('!','.',':',',','?','@'))
        if word in ww:
            summ=summ+wwi[ww.index(word)]
    i+=1
if summ>0:
    print('bad')
else:
    print('good')
'''for str1 in df['tweet']:
    str1=str1.lower()
    str2.clear()
    str1=str1.split()
    i=len(str1)
    j=0
    while j<i:
        if str1[j] in s_stop:
            str1.remove(str1[j])
            i=i-1
            continue
        j=j+1
    length=len(str2)
    temp=0
    while temp<length:
        df_fin[k].append(str2[temp])
        temp=temp+1
    df_fin.append([])
    k=k+1
    str1.clear()
df_fin.pop()'''


