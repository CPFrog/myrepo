# -*- coding: utf-8 -*-
"""201021_01_DL.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qQeasrkUozEpxPR4PGMveOIzDbVMEs9i

### 딥러닝
"""

import tensorflow as tf
import keras
import numpy as np
import sys
import pandas as pd

print(tf.__version__)
print(keras.__version__)
print(sys.version)

train=pd.read_csv('train.csv', parse_dates=['datetime'])
test=pd.read_csv('test.csv', parse_dates=['datetime'])
sub=pd.read_csv('sampleSubmission.csv')

input_col = ['temp', 'atemp']   # 온도, 체감온도
X = train[input_col]   # 학습 데이터의 입력
Y = train['count']     # 학습 데이터의 출력

# 새로운 데이터
X_test = test[input_col]

### 머신러닝 - 딥러닝

from keras.models import Sequential
from keras.layers import Dense

model=Sequential()

# input_dim : 입력층의 노드수
# 30 : 입력층 다음의 노드 수
model.add(Dense(30,input_dim=3, activation='relu'))
model.add(Dense(15,'relu'))
model.add(Dense(15,'relu'))
model.add(Dense(1))

"""### 미니배치의 이해
* 이미지 하나씩 학습시키는 것보다 여러 개를 한꺼번에 학습시키는 쪽이 효과가 좋음
* 많은 메모리와 높은 컴퓨터 성능이 필요하므로 일반적으로 데이터를 적당한 크기로 잘라서 학습시킨다. 이를 **미니배치** 라고 한다.

### 딥러닝 실행
"""

# 오차 함수, 최적화 함수
model.compile(loss='mean_squared_error', optimizer='rmsprop')

# epochs = 데이터가 10000개가 있을 때 몇 번 훈련시킬 건지
# batch_size = 한 번 훈련시킬 때, 데이터를 몇개씩 할건지
model.fit(X,Y,epochs=20,batch_size=10)

pred=model.predict(X_test)

sub=pd.read_csv('sampleSubmission.csv')
sub['count']=pred;

sub.loc[sub['count']<0, 'count']=0

#처음 만드는 제출용 csv파일, 행 번호 제거
sub.to_csv('NNsub01.csv',index=False)

"""### 실습 1.
01. 은닉층을 하나로 만들어 실행한다. (노드수 10) model.evaluate 확인
02. 은닉충을 두개로 만든다 (노드 수 10, 10)
03. 은닉 층 2개의 노드수를 32, 32로 바꾸고 결과 확인해보기
"""

model_P1=Sequential()

model_P1.add(Dense(30,input_dim=2, activation='relu'))
model_P1.add(Dense(10,'relu'))
model_P1.add(Dense(1))

model_P1.compile(loss='mean_squared_error', optimizer='rmsprop')

model_P1.fit(X,Y,epochs=10,batch_size=100)

pred=model.predict(X_test)

sub=pd.read_csv('sampleSubmission.csv')
sub['count']=pred;

sub.loc[sub['count']<0, 'count']=0

sub.to_csv('NNsub02.csv',index=False)

model_P2=Sequential()

model_P2.add(Dense(30,input_dim=2, activation='relu'))
model_P2.add(Dense(10,'relu'))
model_P2.add(Dense(10,'relu'))
model_P2.add(Dense(1))

model_P2.compile(loss='mean_squared_error', optimizer='rmsprop')

model_P2.fit(X,Y,epochs=20,batch_size=10)

pred=model.predict(X_test)

sub=pd.read_csv('sampleSubmission.csv')
sub['count']=pred;

sub.loc[sub['count']<0, 'count']=0

sub.to_csv('NNsub03.csv',index=False)

model_P3=Sequential()

model_P3.add(Dense(30,input_dim=2, activation='relu'))
model_P3.add(Dense(32,'relu'))
model_P3.add(Dense(32,'relu'))
model_P3.add(Dense(1))

model_P3.compile(loss='mean_squared_error', optimizer='rmsprop')

model_P3.fit(X,Y,epochs=20,batch_size=10)

sub.to_csv('NNsub04.csv',index=False)

