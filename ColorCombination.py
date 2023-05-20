import pandas as pd

# shirts 엑셀 파일 불러오기
shirts_file = 'shirts.xlsx'
shirts_data = pd.read_excel(shirts_file)

# pants 엑셀 파일 불러오기
pants_file = 'pants.xlsx'
pants_data = pd.read_excel(pants_file)

# 사용자로부터 상의 이름 입력 받기
shirt_name = input("찾고 계신 상의 이름을 입력하세요: ")

# shirts 엑셀 파일에서 상의 색상 추출
shirt_color = shirts_data.loc[shirts_data['title'] == shirt_name, 'color']
if len(shirt_color) > 0:
    shirt_color = shirt_color.values[0]
    print(f"입력하신 상의 '{shirt_name}'의 색상: {shirt_color}")
else:
    print(f"입력하신 상의 '{shirt_name}'에 대한 정보를 찾을 수 없습니다.")
    exit()

# 사용자로부터 하의 이름 입력 받기
pants_name = input("찾고 계신 하의 이름을 입력하세요: ")

# pants 엑셀 파일에서 하의 색상 추출
pants_color = pants_data.loc[pants_data['title'] == pants_name, 'color']
if len(pants_color) > 0:
    pants_color = pants_color.values[0]
    print(f"입력하신 하의 '{pants_name}'의 색상: {pants_color}")
else:
    print(f"입력하신 하의 '{pants_name}'에 대한 정보를 찾을 수 없습니다.")
    exit()

# 잘 어울리는 색상 조합 정보를 담은 딕셔너리 생성
best_color_combinations = {
    '빨강': ['진청', '검정'],
    '핑크': ['흰색'],
    '노랑': ['검정'],
    '초록': ['진청', '검정'],
    '파랑': ['흰색'],
    '남색': ['흰색'],
    '흰색': ['연청', '진청'],
    '검정': ['연청', '베이지']
}

# 어느 정도 어울리는 색상 조합 정보를 담은 딕셔너리 생성
good_color_combinations = {
    '빨강': ['회색'],
    '핑크': ['회색', '연청','검정'],
    '노랑': ['회색', '진청'],
    '초록': ['회색','베이지'],
    '파랑': ['회색', '베이지'],
    '남색': ['회색', '검정','베이지'],
    '흰색': ['회색', '검정'],
    '검정': ['회색', '진청','검정']
}

# 어느 정도 어울리지 않는 색상 조합 정보를 담은 딕셔너리 생성
not_bad_color_combinations = {
    '빨강': ['흰색'],
    '핑크': ['베이지'],
    '노랑': [],
    '초록': ['연청','흰색'],
    '파랑': [],
    '남색': ['연청'],
    '흰색': ['베이지'],
    '검정': ['흰색']
}

# 잘 어울리지 않는 색상 조합 정보를 담은 딕셔너리 생성
worst_color_combinations = {
    '빨강': ['연청','베이지'],
    '핑크': [],
    '노랑': ['연청','베이지','흰색'],
    '초록': [],
    '파랑': ['연청','진청','베이지'],
    '남색': [],
    '흰색': ['흰색'],
    '검정': []
}


# 사용자가 고른 옷의 색상 조합 평가 기능 추가
if shirt_color == pants_color:
    print("상의와 하의의 색상이 일치합니다. 평범하지만 괜찮은 조합입니다!")
else:
    if shirt_color in color_combinations and pants_color in color_combinations[shirt_color]:
        print(f"상의와 하의의 색상 조합이 잘 어울립니다! ({shirt_color}, {pants_color})")
    else:
        print(f"상의와 하의의 색상 조합이 잘 어울리지 않습니다. 다른 조합을 고려해 보세요!")
