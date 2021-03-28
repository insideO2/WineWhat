import pymysql
import json


#DB에서 데이터 받아오기
def getData():
    review = pymysql.connect(
        user='root',
        passwd='1234',
        host='127.0.0.1',
        db='reviewtestdb',
        charset='utf8'
    )

    cursor = review.cursor(pymysql.cursors.SSCursor)

    sql = "SELECT * FROM reviewtest;"
    cursor.execute(sql)
    dateSet = cursor.fetchall()

    return dateSet

#모든 사용자 ID 목록
def makeUserIDList(dateSet):
    alluserID = []
    for i in range(0, len(dateSet)):
        alluserID.append(dateSet[i][0])

    return alluserID

#모든 사용자 평점 목록
def makeReviewArray(dateSet):
    reviews = []
    allUserReviews = []

    for i in range(0, len(dateSet)):
        reviews.append(json.loads(dateSet[i][1]))
        allUserReviews.append(list(reviews[i].values()))

    return allUserReviews

#추천 요청 사용자 정보
def getUserInfo(alluserID, dateSet):
    userInfo = {}
    for i in range(0, len(dateSet)):
        if dateSet[i][0] == alluserID:
            userInfo[alluserID] = dateSet[i][1]

    return userInfo;


