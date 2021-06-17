import pymysql

#회원가입
def addmember(user_ID,user_Passward):
    #user_db와의 연동
    user_db = pymysql.connect(
        user='root',
        passwd='1234',
        host='127.0.0.1',
        db='user_db',
        charset='utf8'
    )
    # 커서 지정
    cursor = user_db.cursor(pymysql.cursors.SSCursor)

    #user_info 테이블 select
    sql = "SELECT * FROM user_info"
    cursor.execute(sql)
    dateSet = cursor.fetchall()

    #chcker값 0으로 초기회
    checker = 0

    #user_ID 중복확인
    for i in range(0, len(dateSet)):
        if dateSet[i][0] == user_ID:
            checker = 1
    if checker == 1:
        print("아이디가 이미 존재합니다.")
        return checker
    #userID가 존재하지 않을 시, db에 insert(아이디 생성)
    else:
        sql = "INSERT INTO user_info(user_ID, user_Passward, user_MemberType) VALUES(%s, %s, %s);"

        #커서 생성후, user_db commit
        cursor.executemany(sql, [[user_ID,user_Passward,123]])
        user_db.commit()
        #select로 user_info 테이블 내 계정확인
        sql = "SELECT * FROM user_info"
        cursor.execute(sql)
        dateSet = cursor.fetchall()

        print(dateSet)
        return checker

#addmember('userA','7878')






