# 국토교통부 아파트매매 실거래 데이터 수집

# - 지역코드
# - 법정동
# - 거래일
# - 아파트명
# - 지번
# - 전용면적
# - 층
# - 건축년도
# - 거래금액

import PublicDataReader as pdr

# Open API 서비스 키 설정
serviceKey = "OPEN API SERVICE KEY HERE"

# 국토교통부 실거래가 Open API 인스턴스 생성
molit = pdr.Transaction(serviceKey)

# 지역코드 조회
bdongName = '분당구'
codeResult = molit.CodeFinder(bdongName)
codeResult.head(1)

# 특정 월 아파트매매 실거래 자료 조회
df = molit.AptTrade(41135, 202004)

# 특정 기간 아파트매매 실거래 자료 조회
df_sum = molit.DataCollector(molit.AptTrade, 41135, 202001, 202003)