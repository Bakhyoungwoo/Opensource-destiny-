#색깔에 따른 추천 1차
import pandas as pd
from difflib import get_close_matches
import random

# 엑셀 파일 로드
df = pd.read_excel('codi_data.xlsx')

# 유사한 단어 찾기 함수 정의
def get_similar_words(word, words_list):
    return get_close_matches(word, words_list, n=1, cutoff=0.8)

while True:
    # 사용자로부터 정보 입력 받기
    current_color = input("어떤 색깔의 옷을 추천받고 싶으세요?: ")

    # 입력받은 정보와 유사한 데이터 추출
    filtered_df = df[df['color'].str.contains('|'.join(get_similar_words(current_color, df['color'])))]

    # 필터링된 추천 받을 데이터를 배열에 저장
    recommended_outfits = filtered_df['title'].tolist()

    # 추천할 옷 랜덤 선택
    if recommended_outfits:
        random_outfit = random.choice(recommended_outfits)
        print("추천되는 코디:")
        print(random_outfit)
    else:
        print("일치하는 코디가 없습니다.")
        break

    # 사용자의 답변 받기
    answer = input("추천된 코디가 마음에 드나요? (예/아니오): ")
    if answer.lower() == '예':
        print("좋아요! 코디가 마음에 드셨다니 다행입니다!")
        break
    elif answer.lower() == '아니오':
        print("다른 코디를 추천해드릴게요!")
        continue
    else:
        print("예 또는 아니오로 대답해주세요.")
