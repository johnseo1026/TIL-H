#-*- coding: utf-8 -*-

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
# 표준화(정규화(모든 값을 0-1에 맞게 변환)
# 또는 표준화(평균0, 분산1이 되도록변환)가 필요하다)
from sklearn.preprocessing import StandardScaler

# 데이터 세트 로드
pi_diabetes = pd.read_csv('pima-indians-diabetes.csv', header = None)

x = pi_diabetes.iloc[:, :8]
y = pi_diabetes.iloc[:, 8:].values.flatten()  # 1차원으로 전개

print('x shape : {}, x shape : {}'.format(x.shape, y.shape))

# 훈련데이터와 테스트 데이터의 분리
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state = 0)

# 정규화를 위한 모듈 사용
std_scl = StandardScaler()
std_scl.fit(x_train)
x_train = std_scl.transform(x_train)
x_test = std_scl.transform(x_test)

# 학습 및 테스트
svc = SVC()
svc.fit(x_train, y_train)

print('훈련 점수 : {: .3f}'.format(svc.score (x_train, y_train)))
print('테스트 점수 : {: .3f}'.format(svc.score (x_test, y_test)))