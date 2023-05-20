import logging
import pandas as pd

# 로그 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# shirts 엑셀 파일 불러오기
shirts_file = 'shirts.xlsx'
try:
    shirts_data = pd.read_excel(shirts_file)
    logger.info(f"파일 '{shirts_file}'을 성공적으로 불러왔습니다.")
except Exception as e:
    logger.error(f"파일 '{shirts_file}'을 불러오는데 실패했습니다: {str(e)}")

# pants 엑셀 파일 불러오기
pants_file = 'pants.xlsx'
try:
    pants_data = pd.read_excel(pants_file)
    logger.info(f"파일 '{pants_file}'을 성공적으로 불러왔습니다.")
except Exception as e:
    logger.error(f"파일 '{pants_file}'을 불러오는데 실패했습니다: {str(e)}")

# 사용자로부터 상의 이름 입력 받기
shirt_name = input("상의 이름을 입력하세요: ")

# shirts 엑셀 파일에서 상의 이름 찾기
shirt_title_exists = shirt_name in shirts_data['title'].values
if shirt_title_exists:
    logger.info(f"입력한 상의 '{shirt_name}'은(는) shirts 엑셀 파일의 title 열에 존재합니다.")
else:
    logger.info(f"입력한 상의 '{shirt_name}'은(는) shirts 엑셀 파일의 title 열에 존재하지 않습니다.")
    
# 사용자로부터 하의 이름 입력 받기
pants_name = input("하의 이름을 입력하세요: ")

# pants 엑셀 파일에서 하의 이름 찾기
pants_title_exists = pants_name in pants_data['title'].values
if pants_title_exists:
    logger.info(f"입력한 하의 '{pants_name}'은(는) pants 엑셀 파일의 title 열에 존재합니다.")
else:
    logger.info(f"입력한 하의 '{pants_name}'은(는) pants 엑셀 파일의 title 열에 존재하지 않습니다.")
