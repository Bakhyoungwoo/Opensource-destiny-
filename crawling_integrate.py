import pandas as pd
import glob
import os

# 병합할 엑셀 파일들이 있는 디렉토리 경로
directory_path = r'C:\Users\82102\Desktop\데이터 수집 종합본'

# 병합할 엑셀 파일들의 패턴 (예: 모든 엑셀 파일)
file_pattern = '*.xlsx'

# 모든 엑셀 파일 가져오기
all_files = glob.glob(os.path.join(directory_path, file_pattern))

# 엑셀 파일들을 담을 빈 DataFrame 생성
dfs = []

# 모든 엑셀 파일을 순회하면서 병합
for file in all_files:
    df = pd.read_excel(file)  # 엑셀 파일 읽기
    dfs.append(df)