import pandas as pd

# 사용자로부터 옷 이름을 입력받음
cloth_name = input("옷 이름을 입력하세요: ")

# 엑셀 파일을 불러옴
df = pd.read_excel('example.xlsx')

# title열에서 옷 이름이 일치하는 행을 찾음
matching_rows = df.loc[df['title'] == cloth_name]

# 가격 정보를 담을 리스트를 생성
prices = []

# 찾은 행에서 가격 정보를 추출하여 리스트에 추가
for index, row in matching_rows.iterrows():
    prices.append((row['price'])) 

# 가격 정보를 출력 (모든 가격, 평균 가격, 가장 싼 가격 출력)
if len(prices) == 0:
    print("해당하는 옷 이름이 없습니다.")
else:
    average_price = sum(prices) / len(prices)
    min_price = min(prices)
    print(f"{cloth_name}의 가격은 {prices}원이며, 평균 가격은 {average_price}원, 가장 싼 가격은 {min_price}원 입니다.")
