import pymysql

#wineID 전체 데이터를 가져오는 함수
def getWineInfo(wine_ID):



    #wine db연동
    wine_db = pymysql.connect(
        user='root',
        passwd='1234',
        host='127.0.0.1',
        db='wine_db',
        charset='utf8'
        )
    #cursor 지정
    cursor = wine_db.cursor(pymysql.cursors.SSCursor)



    #wine_db 내에서 select
    sql = "SELECT * FROM wine_main WHERE wine_ID = %s";
    cursor.execute(sql,(wine_ID))
    dateSet = cursor.fetchall()

    print(dateSet)
    return(dateSet)



#getWineInfo(1)
