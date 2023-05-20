import pandas as pd

# shirts 엑셀 파일 불러오기
shirts_file = 'shirts.xlsx'
shirts_data = pd.read_excel(shirts_file)

# pants 엑셀 파일 불러오기
pants_file = 'pants.xlsx'
pants_data = pd.read_excel(pants_file)

# 사용자로부터 상의 이름 입력 받기
shirt_name = input("찾고계신 상의 이름을 입력하세요: ")

# 사용자로부터 하의 이름 입력 받기
pants_name = input("찾고계신 하의 이름을 입력하세요: ")

# shirts 엑셀 파일에서 상의 색상 추출
shirt_color = shirts_data.loc[shirts_data['title'] == shirt_name, 'color'].values[0]

# pants 엑셀 파일에서 하의 색상 추출
pants_color = pants_data.loc[pants_data['title'] == pants_name, 'color'].values[0]

print(f"입력하신 상의 '{shirt_name}'의 색상: {shirt_color}")
print(f"입력하신 하의 '{pants_name}'의 색상: {pants_color}")
