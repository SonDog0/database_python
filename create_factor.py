import pymysql

# 연결, 커서 생성
conn = pymysql.connect(host='52.78.219.78', user= 'bigdata', password= 'big401',db='ProjectDB', charset='utf8')
curs = conn.cursor(pymysql.cursors.DictCursor)

inputX = 126.9880
inputY = 37.5698
bus_cnt = 0
school_cnt = 0

numofcnt = [0,0,0,0,0,0]
factor_tbl = ['sbus_point_info' , 'schools' , 'subway' , 'seoul_park' , 'toursights', 'sangga' ]


for i in range (0 , len(factor_tbl)):

    sql = 'select round(x_value,4) as x_value , y_value from ' + '' + factor_tbl[i] + ''
    # sql = 'select round(x_value,4) as x_value , y_value from toursights'
    curs.execute(sql)
    # check = []
    x_val = []
    y_val = []

    for rs in curs.fetchall():
        x_val.append(rs['x_value'])
        y_val.append(rs['y_value'])
        # check.append()

    # print(len(x_val)) # 11018 DB와 같음
    # print(x_val)
    # print(y_val)

    for j in range (0,len(x_val)):
        if (abs(126.9880- x_val[j]) < 0.0018) and(abs(37.5698 - y_val[j])) < 0.0023 :
            numofcnt[i] += 1

#
# X 0.001794 : 실제 200M X값
# Y 0.0023 : 실제 200M Y값

print(numofcnt)
# 테이블 제거


# 테이블 생성
sql = 'create table showFactor( bus_cnt int, school_cnt int , subway_cnt int , park_cnt int , tour_cnt int , sangga_cnt int )'

curs.execute(sql)

insert_sql = "insert into showFactor values( " \
             + str(numofcnt[0]) + ' , ' + str(numofcnt[1]) + ' , ' + str(numofcnt[2]) + ' , ' + str(numofcnt[3]) + ' , '\
             + str(numofcnt[4]) + ' , ' + str(numofcnt[5]) + " ) "

print(insert_sql)
curs.execute(insert_sql)

conn.commit()

