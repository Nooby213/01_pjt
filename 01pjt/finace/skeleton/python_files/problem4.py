import pprint
import requests

# 상품과 옵션 정보들을 담고 있는 새로운 객체를 만들어 반환하시오.
# [힌트] 상품 리스트와 옵션 리스트를 금융상품 코드를 기준으로 매칭할 수 있습니다.
# [힌트] 아래와 같은 순서로 데이터를 출력하며 진행합니다.
# 1. 응답을 json 형식으로 변환합니다.
# 2. key 값이 "result" 인 데이터를 변수에 저장합니다.
# 3. 2번의 결과 중 key 값이 "baseList" 인 데이터를 변수에 저장합니다.
# 4. 2번의 결과 중 key 값이 "optionList" 인 데이터를 변수에 저장합니다.
# 5. 3번에서 저장된 변수를 순회하며, 4번에서 저장된 값들에서 금융 상품 코드가 
#     같은 모든 데이터들을 가져와 새로운 딕셔너리로 저장합니다.
#     저장 시, 명세서에 맞게 출력되도록 저장합니다.
# 6. 5번에서 만든 딕셔너리를 결과 리스트에 추가합니다.


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

data = [] # 전체 정보를 나타내는 리스트
#-----------

info_list = [] # 금리정보의 정보
data_list = {} # 저축금리, 저축기간, 저축금리유형 ....
pro_name = {} # 금융상품명
pro_com = {} # 금융회사명

# pprint.pprint(need)
for info in need:
   data_list = {} # 저축금리, 저축기간, 저축금리유형 ....
   data_list['금융상품코드'] = info['fin_prdt_cd']
   data_list['저축 금리'] = info['intr_rate']
   data_list['저축 기간'] = info['save_trm']
   data_list['저축금리유형'] = info['intr_rate_type_nm']
   data_list['최고 우대금리'] = info['intr_rate2']
   info_list.append(data_list)


for i in range(len(result['result']['baseList'])):
   callin_list = []
   for j in range(len(info_list)):
    call_list = {}
    if info_list[j]['금융상품코드'] == result['result']['baseList'][i]['fin_prdt_cd']:
       callin_list.append(info_list[j])
       call_list['금리정보'] = callin_list
       call_list['금융상품명'] = result['result']['baseList'][i]['fin_prdt_nm']
       call_list['금융회사명'] = result['result']['baseList'][i]['kor_co_nm']
       data.append(call_list)
# pprint.pprint(data)
for i in range(len(data)):
   if data[i]['금융상품명'] == str(input('찾으시는 금융상품명을 입력하세요')):
      pprint.pprint(data[i])
# pprint.pprint(info_list)
# pprint.pprint(info_list)

# 리스트 > 딕셔너리 > 리스트 > 딕셔너리
# data = [] # 전체 정보를 나타내는 리스트
# rate_infor = {'금리정보' : []} # 금리정보
# pro_name = {} # 금융상품명
# pro_com = {} # 금융회사명

# for 




    
    
    
   