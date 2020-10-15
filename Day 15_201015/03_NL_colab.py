# -*- coding: utf-8 -*-
"""Lecture_03_ _colab.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QVreLuTBLhcRrsSRuA6mrJEXC7OsHk2H

### 사전 작업
"""

!apt-get update -qq
!apt-get install fonts-nanum* -qq

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
import matplotlib as mpl # 기본 설정 만지는 용도
import matplotlib.pyplot as plt # 그래프 그리는 용도
import matplotlib.font_manager as fm # 폰트 관련 용도
import nltk
import numpy as np

path = '/usr/share/fonts/truetype/nanum/NanumGothic.ttf' # 설치된 나눔글꼴중 원하는 녀석의 전체
font_name = fm.FontProperties(fname=path, size=10).get_name()
print(font_name)
plt.rc('font', family=font_name)

## 음수 표시되도록 설정
mpl.rcParams['axes.unicode_minus'] = False

from wordcloud import WordCloud, STOPWORDS
from PIL import Image

doc_ko = open('TheExtreme_utf8.txt').read()
doc_ko[1:1000]

pip install konlpy

# OKT 클래스를 이용한 명사확인
from konlpy.tag import Okt       ### Okt

t = Okt()
doc_nouns = t.nouns(doc_ko)
doc_nouns

# nltk.Text()를 이용하여 nltk가 가지는 많은 기능을 사용 가능해짐.

ko = nltk.Text(doc_nouns, name="분노의 질주")
print(type(ko))
print(len(ko.tokens))

### 단어들의 사용 횟수 확인 - 빈도 분석
ko.vocab()

most_fre = ko.vocab().most_common(50)
most_fre

plt.figure(figsize=(12,6))
ko.plot(50)
plt.show()

### 한글에서는 따로 불용어 사전이 없어, 따로 만들거나 또는 파일로 부터 불러올 수 있다.
stop_words = ['분노', '영화', '액션', '시리즈', '더', 
              '그', '이', '것', '또', '좀', 
              '돈', '것', '다음', '질주', '그냥', 
              '분노의질주', '말', '뭐', '애', '나', '듯', '편', '볼', '점', '중', '로']

new_ko=nltk.Text(new_ko,name='분노의 질주2')
plt.figure(figsize=(12,6))
new_ko.plot(50)

### 중복된 단어를 제거한 개수를 확인
print(len(set(ko.tokens)))