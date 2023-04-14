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

# 입력받은 정보와 유사한 데이터 추출
filtered_df = df[df['codi'].str.contains('|'.join(get_similar_words(current_situation, df['codi'])))]
filtered_df = filtered_df.reset_index(drop=True)

# 추천 받을 데이터를 배열에 저장
recommended_outfits = filtered_df['title'].tolist()

# 추천할 옷 랜덤 선택
if recommended_outfits:
    random_outfit = random.choice(recommended_outfits)
    print("추천되는 코디:")
    print(random_outfit)
else:
    print("일치하는 코디가 없습니다.")

# 입력받은 정보 출력하기
print(current_situation +" 상황에 입기 좋은 옷을 추천해보았습니다!")

