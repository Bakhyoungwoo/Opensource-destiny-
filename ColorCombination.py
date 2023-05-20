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
