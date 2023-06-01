import pandas as pd
from difflib import get_close_matches
import random

# 엑셀 파일 로드
df = pd.read_excel('codi_data.xlsx')

# 사용자로부터 정보 입력 받기
current_situation = input("어떤 상황에서 입어야 하는 옷인지를 알려주세요: ")

# 유사한 단어 찾기 함수 정의
def get_similar_words(word, words_list):
    return get_close_matches(word, words_list, n=1, cutoff=0.8)

while True:
    # 입력받은 정보와 유사한 데이터 추출
    #'|' (or연산)으로 유사한 단어들을 문자열로 변환 -> codi 열에 이 패턴이 포함되는지 확인 
    # 유사한 단어가 하나라도 포함되어 있다면 filtered_df에 저장 
    filtered_df = df[df['codi'].str.contains('|'.join(get_similar_words(current_situation, df['codi'])))]
    filtered_df = filtered_df.reset_index(drop=True)

    # 필터링된 추천 받을 데이터를 배열에 저장
    #codi 열에 입력받은 상황(current_situation)을 포함하는 데이터만 추출, 해당 데이터의 title 열 값을 리스트로 변환하여 추천할 옷을 선택
    recommended_outfits = filtered_df[filtered_df['codi'].str.contains(current_situation)]['title'].tolist()

    # 추천할 옷 랜덤 선택
    # 상황에 알맞은 코디를 하나만 추천하기 위하여 랜덤으로 하나만 선택. 
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

