# -*- coding: utf-8 -*-
"""Lecture_01_konlpy_colab

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EPhse5ELkhHX-5QO2mCNr11aMoKts5cY
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import nltk
import numpy as np

!apt-get update -qq
!apt-get install fonts-nanum* -qq

font_name=fm.FontProperties(fname= '/usr/share/fonts/truetype/nanum/NanumGothic.ttf', size=10).get_name()
print(font_name)
plt.rc('font', family=font_name)

fm._rebuild()

"""### 꼬꼬마(by. 서울대)이용한 분석 
* 문장분석
* 명사분석
* 형태소
"""

!pip install konlpy

from konlpy.tag import Kkma
k=Kkma()

"""### 명사분석"""

k.nouns('안녕하세요! 오늘은 한국어 자연어 분석을 합니다.')

k.sentences('안녕하세요! 오늘은 한국어 자연어 분석을 합니다.')

k.pos('안녕하세요! 오늘은 한국어 자연어 분석을 합니다.')

"""### 실습 1. Hannanum Class를 이용한 문장의 명사, 형태소 분석 실행"""

from konlpy.tag import Hannanum
h=Hannanum()

h.nouns('안녕하세요! 오늘은 한국어 자연어 분석을 합니다.')

h.pos('안녕하세요! 오늘은 한국어 자연어 분석을 합니다.')

h.analyze('안녕하세요! 오늘은 한국어 자연어 분석을 합니다.')