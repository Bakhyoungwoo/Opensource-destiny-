import numpy as np
from sklearn.linear_model import LinearRegression

# 키와 몸무게 데이터
X = np.array([[185, 75], [176, 65], [167, 68], [174, 65], [173, 75],[173, 73],[180, 98],[164, 59],[173, 78],[185, 95],[171, 60],[170, 74],[178, 81],[170, 74],[166,70],[189,90],[174,61],[180,60],[178,69],[176,80],[180,73],[177,68],[171,67],[178,72],[158,48],[172,64],[173,61],[178,73],[173,56],[176,72],[187,90],[180,75],[175,69],[173,80],[165,65],[178,70],[171,66],[170,64],[178,73],[178,74],[179,88],[168,64],[180,80]])  # 입력 데이터 (키와 몸무게)
y = np.array([100, 95, 100, 100, 100, 100, 100, 95, 95,100,95,105,105,110,110,115,95,110,100,110,100,100,95,100,95,100,100,100,95,100,115,105,100,105,95,105,95,95,100,100,110,100,105])  # 출력 데이터 (옷 사이즈)
y = y.reshape(-1, 1)  # 출력 데이터 (옷 사이즈)

# 선형 회귀 모델 훈련
model = LinearRegression()
model.fit(X, y)

# 사용자로부터 키와 몸무게 입력 받기
print("주의: 정확하지 않은 값일 수도 있습니다.")
height = float(input("키를 입력하세요 (cm): "))
weight = float(input("몸무게를 입력하세요 (kg): "))

# 입력 데이터로 예측하기
size = model.predict([[height, weight]])
if 85 <= size < 90:
    output_size = 'xs'
elif 90 <= size <95:
    output_size = "s"
elif  95 <= size < 100:
    output_size = "M"
elif 100 <= size < 105:
    output_size = "L"
elif 105 <= size < 110:
    output_size = "XL"
elif 110 <= size < 115:
    output_size = "XXL"
else:
    output_size = "사이즈를 결정할 수 없습니다."

# 결과 출력
print(f"예상 옷 사이즈는 {output_size}입니다.")