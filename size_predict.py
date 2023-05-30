import numpy as np
from sklearn.linear_model import LinearRegression

# 키와 몸무게 데이터
X = np.array([[150, 50], [160, 55], [170, 60], [180, 65], [190, 70]])  # 입력 데이터 (키와 몸무게)
y = np.array([1, 2, 3, 4, 5])  # 출력 데이터 (옷 사이즈)

# 선형 회귀 모델 훈련
model = LinearRegression()
model.fit(X, y)

