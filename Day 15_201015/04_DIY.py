# -*- coding: utf-8 -*-
"""201015_Lecture_04_DIY.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oTT4TBik436uuc856rDwvyXDDzd4vlRJ

### 사전 작업
"""

!apt-get update -qq
!apt-get install fonts-nanum* -qq

import matplotlib.font_manager as fm # 폰트 관련 용도
import matplotlib.pyplot as plt

path = '/usr/share/fonts/truetype/nanum/NanumGothicEco.ttf' # 설치된 나눔글꼴중 원하는 녀석의 전체
font_name = fm.FontProperties(fname=path, size=10).get_name()
print(font_name)
plt.rc('font', family=font_name)

fm._rebuild()

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
import matplotlib as mpl # 기본 설정 만지는 용도
import matplotlib.pyplot as plt # 그래프 그리는 용도
import matplotlib.font_manager as fm # 폰트 관련 용도
import nltk
import numpy as np

path = '/usr/share/fonts/truetype/nanum/NanumGothicEco.ttf' # 설치된 나눔글꼴중 원하는 녀석의 전체
font_name = fm.FontProperties(fname=path, size=10).get_name()
print(font_name)
plt.rc('font', family=font_name)

mpl.rcParams['axes.unicode_minus'] = False

from wordcloud import WordCloud, STOPWORDS
from PIL import Image

!pip install konlpy

"""### DIY [한국어]"""

doc_ko=open('SAO_01.txt').read()

from konlpy.tag import Okt

t=Okt()
doc_nouns=t.nouns(doc_ko)
doc_nouns

ko = nltk.Text(doc_nouns, name="분노의 질주")
print(type(ko))
print(len(ko.tokens))

ko.vocab()

most_fre = ko.vocab().most_common(50)
most_fre

print(len(set(ko.tokens)))

plt.figure(figsize=(12,6))
ko.plot(50)
plt.show()

"""### DIY [영어]"""

doc_en=open('Hamlet.txt').read()

stopwords = set(STOPWORDS)
stopwords.add('said')
stopwords

