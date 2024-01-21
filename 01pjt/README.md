for info in need:
   **data_list = {}**
   data_list['금융상품코드'] = info['fin_prdt_cd']
   data_list['저축 금리'] = info['intr_rate']
   data_list['저축 기간'] = info['save_trm']
   data_list['저축금리유형'] = info['intr_rate_type_nm']
   data_list['최고 우대금리'] = info['intr_rate2']
   info_list.append(data_list)

data_list 변수 정의 위치에 대해 중요함을 느꼈다.
안 된면 줄 별로 주석 처리 후 print 문으로 디버깅하기

for i in range(len(result['result']['baseList'])):
   **callin_list = []**
   for j in range(len(info_list)):
    **call_list = {}**
    if info_list[j]['금융상품코드'] == result['result']['baseList'][i]['fin_prdt_cd']:
       **callin_list.append(info_list[j])**
       call_list['금리정보'] = callin_list
       call_list['금융상품명'] = result['result']['baseList'][i]['fin_prdt_nm']
       call_list['금융회사명'] = result['result']['baseList'][i]['kor_co_nm']
       data.append(call_list)

위와 똑같이 변수 정의 위치를 확인 할 필요성을 느꼈다.
코드가 길다면 줄 별로 print 해보고 확인하고 다음 줄로 넘어가기, 오류가 쌓여서 해결할 수가 없다.
for 문 안에 있는 list.append 메소드에 대해 이해가 좀 더 필요하다.