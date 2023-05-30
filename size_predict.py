import numpy as np
from sklearn.linear_model import LinearRegression

# 키와 몸무게 데이터
X = np.array([[150, 50], [160, 55], [170, 60], [180, 65], [190, 70]])  # 입력 데이터 (키와 몸무게)
y = np.array([1, 2, 3, 4, 5])  # 출력 데이터 (옷 사이즈)

# 선형 회귀 모델 훈련
model = LinearRegression()
model.fit(X, y)

# 사용자로부터 키와 몸무게 입력 받기
height = float(input("키를 입력하세요 (cm): "))
weight = float(input("몸무게를 입력하세요 (kg): "))

# 입력 데이터로 예측하기
size = model.predict([[height, weight]])

# 결과 출력
print(f"예상 옷 사이즈는 {size}입니다.")