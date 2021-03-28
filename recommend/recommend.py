import numpy as np
from ast import literal_eval
import getdata
import operator

#코싸인 유사도
def cosine_similarity(a, b):
    #0으로 나누기 방지
    if (np.linalg.norm(a) * (np.linalg.norm(b))) == 0:
        result = 0.0
    else:
        result = np.dot(a, b) / (np.linalg.norm(a) * (np.linalg.norm(b)))

    return result

#코싸인 유사도가 0.8 이상인 유저 목록
def getSimilarUser(userInfo, alluserID, allUserReviews):
    similarUser = {}
    userID = list(userInfo.keys())

    userReview = list(userInfo.values()) #userInfo가 Dictionary이므로 cosine_similarity 함수에서 사용할 수 있도록 lsit 형태로 전환
    userReview = literal_eval(str(userReview[0]))
    userReview = list(userReview.values())


    for i in range(0, len(alluserID)): #코싸인 유사도가 0.8 이상인 {유저ID : 평점} Dictionary 생성
        if cosine_similarity(userReview, allUserReviews[i]) >= 0.8:
                similarUser[alluserID[i]] = allUserReviews[i]

        """print(cosine_similarity(userReview, allUserReviews[i])) #코싸인 유사도 확인용
    print("=======")"""


    #추천 리스트에 자기 자신 밖에 없을 경우, 추천 리스트 Null
    if list(similarUser.keys()) == userID:
        del similarUser[userID[0]]

    # 추천 리스트가 Null일 경우, 모든 유저의 데이터를 통합해, 통상적으로 가장 높은 평점을 받은 와인을 추천
    if len(similarUser) == 0:
        print("유사한 사용자 없음")
        for i in range(0, len(alluserID)):
            similarUser[alluserID[i]] = allUserReviews[i]

    #자기 자신 제거
    del similarUser[userID[0]]

    #print(similarUser)

    return similarUser

#높은 코싸인 유사도의 사용자들의 평점 평균
def getreviewAverage(similarUser):

    averageList = []
    reViewArray = list(similarUser.values())
    for i in range(0, len(reViewArray[0])):
        sum = 0
        for j in range(0, len(reViewArray)):
            sum = sum + reViewArray[j][i]
        averageList.append(sum / len(reViewArray))

    return averageList

#사용자가 리뷰한 와인을 추천 목록에서 삭제
def unReviewed(userInfo, reviewAverage):
    unReviewedList = {}
    userReview = list(userInfo.values())
    userReview = literal_eval(str(userReview[0]))
    userReview = list(userReview.values())


    for i in range(0, len(userReview)):
        if userReview[i] == 0:
           unReviewedList[i + 1] = reviewAverage[i]

    return unReviewedList

#추천 목록 정렬 후, 와인 ID 목록 return
def sortRecommend(unReviedList):
    sortedList = sorted(unReviedList.items(), key=operator.itemgetter(0))
    wineIDList = []

    #print(sortedList)

    for i in range(0, len(sortedList)):
        wineIDList.append(sortedList[i][0])

    return wineIDList

#추천 모듈
def recommendModule(username):
    #데이터 셋팅
    dateSet = getdata.getData()
    allUserID = getdata.makeUserIDList(dateSet)
    allUserReviews = getdata.makeReviewArray(dateSet)
    userInfo = getdata.getUserInfo(username, dateSet)

    #유사도 연산
    similarUser = getSimilarUser(userInfo, allUserID, allUserReviews)

    #추천 목록 생성
    reviewAverage = getreviewAverage(similarUser)
    unReviewedList = unReviewed(userInfo, reviewAverage)
    sortedList = sortRecommend(unReviewedList)

    return sortedList





