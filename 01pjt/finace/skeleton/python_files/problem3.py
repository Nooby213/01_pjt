import pprint
import requests
# 응답 중 정기예금 상품들의 옵션 리스트를 출력하도록 구성합니다.
# 이 때, 원하는 데이터만 추출하여 새로운 리스트를 만들어 반환하는 함수를 작성하시오.
# [힌트] 아래와 같은 순서로 데이터를 출력하며 진행합니다.
# 1. 응답을 json 형식으로 변환합니다.
# 2. key 값이 "result" 인 데이터를 출력합니다.
# 3. 위의 결과 중 key 값이 "optionList" 인 데이터를 변수에 저장합니다.
# 4. 3번에서 저장된 값을 반복하며, 원하는 데이터만 추출 및 가공하여 결과 리스트에 저장합니다.


def get_deposit_products():
  # 본인의 API KEY 로 수정합니다.
  api_key = ''
  url = 'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'
  params = {
     'auth' : api_key,
     # 금융회사 코드 020000(은행), 030200(여신전문), 030300(저축은행), 050000(보험), 060000(금융투자)
     'topFinGrpNo' : '020000',
     'pageNo': 1
  }
  # 요구사항에 맞도록 이곳의 코드를 수정합니다.
  # 응답을 json 형태로 변환
  response = requests.get(url, params=params).json()
  return response

if __name__ == '__main__':
    # json 형태의 데이터 반환
    result = get_deposit_products()

need = result['result']['optionList']

info_list = []

for info in need:
   data_list = {}
   data_list['금융상품코드'] = info['fin_prdt_cd']
   data_list['저축 금리'] = info['intr_rate']
   data_list['저축 기간'] = info['save_trm']
   data_list['저축금리유형'] = info['intr_rate_type_nm']
   data_list['최고 우대금리'] = info['intr_rate2']
   info_list.append(data_list)

# pprint.pprint(info_list)
pprint.pprint(data_list)









    
    
    
   