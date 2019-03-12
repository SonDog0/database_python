# 연결, 커서 생성
host = '52.78.219.78'
user = 'bigdata'
passwd = 'big401'
db = 'ProjectDB'

import pymysql
conn = pymysql.connect(host=host, user= user, password= passwd,db=db, charset='utf8')
curs = conn.cursor(pymysql.cursors.DictCursor)

code_arr = ['D01','D02','D03','D04','D05','D06','D07','D08','D09','D10','D11',
            'D12','D13','D14','D15','D16','D17','D18','D19','D20','D21','D22','D23','D24',
            'D25','D26','F01','F02','F03','F04','F05','F06','F07','F08','F09','F11','F12',
            'F13','F14','F15','F16','F17','F18','F19','F20','L01','L03','L04','L05','N01',
            'N02','N03','N04','N05','N07','N08','O01','O02','O03','O04','O05','P01','P02',
            'P03','Q01','Q02','Q03','Q04','Q05','Q06','Q07','Q08','Q09','Q10','Q12','Q13',
            'Q14','Q15','R01','R02','R03','R04','R05','R06','R07','R08','R09','R10','R13','S01','S02','S03','S04','S07']
# 문자열 선언
strr_create_sview = ''
strr_create = ''

# 문자열 정의
for i in range(0 ,len(code_arr)):
    if i < len(code_arr) -1:
        strr_create_sview +=  'sum(if(mid_code="' + code_arr[i] + '" , cnt_midcode ,0)) as ' + code_arr[i] + ','
    else:
        strr_create_sview += 'sum(if(mid_code="' + code_arr[i] + '" , cnt_midcode ,0)) as ' + code_arr[i] + ' '


    # if i < len(code_arr) - 1:
    #     strr_create += code_arr[i] + ' int, '
    # else:
    #     strr_create += code_arr[i] + ' int '

# 문자열 확인
print(strr_create_sview)
print(strr_create)

#
# sangga_view 뷰 생성 쿼리( mide_code들의 항목을 컬럼으로 , 각 컬럼의 값에 cnt_midcode )
create_view_sql = ' create view sangga_view as SELECT l_office_no , '+ strr_create_sview + ' from office_sangga group by l_office_no'

# tbl_office_sangga 테이블 생성 쿼리 ( 뷰의 값을 실존하는 table로 저장 )
# create_sql  = 'create table tbl_seoul2(l_office_no int, bus_cnt int, subway_cnt int, park_cnt int , school_cnt int, tour_cnt int, '+ strr_create +' )'


# 쿼리 실행
curs.execute(create_view_sql)
# curs.execute(create_sql)

