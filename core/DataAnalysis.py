import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
import thulac
import time
import progressbar
'''s = pd.Series([1,3,5,np.nan,6,8])
reviewDateandTime = []
reviewDate = []
reviewUser = []
reviewContent = []
dateWithReviews = []
numberOfReviewsOnSameDate = []
dates = pd.date_range("20170101", periods = 6)
df = pd.read_csv('C:\workspace\SentimentClassfication\input.csv', error_bad_lines = False, header = None)
#df_names = pd.read_csv('C:\workspace\SentimentClassfication\input.csv',
#                       error_bad_lines = False, header = None, names = ['name', 'date', 'content'])
rowCount = len(df.index) #获取总行数
for row in range(rowCount):
    reviewUser.append(df.ix[row][0])
    reviewDateandTime.append(df.ix[row][1])
    reviewContent.append(df.ix[row][2])
#df.set_index('0').index.getduplicates()
df_reviewUser = pd.DataFrame(data = reviewUser, columns = ['reviewUser'])
#df_reviewDate = pd.DataFrame(data = reviewDate, columns = ['reviewDate'])
df_reviewContent = pd.DataFrame(data = reviewContent, columns = ['reviewContent'])
pattern = re.compile(r'\S*')
for item in range(len(reviewDateandTime)):
    date =pattern.findall(reviewDateandTime[item])
    reviewDate.append(date[0])
#print(reviewDate[1])
start = 0
numberOfReviews = 0
item = 0
while item < (len(reviewDate) - 1):
    if(start < len(reviewDate) and reviewDate[item] == reviewDate[start]):
        numberOfReviews += 1
        start += 1
    else:
        numberOfReviewsOnSameDate.append(numberOfReviews)
        dateWithReviews.append(reviewDate[item])
        numberOfReviews = 0
        item = start
numberOfReviewPerDate = list(zip(dateWithReviews, numberOfReviewsOnSameDate))
print(dateWithReviews)
print(numberOfReviewsOnSameDate)
print(numberOfReviewPerDate)
#df_reviewDate = pd.DataFrame(data = dictofReviewDate, columns = ['reviewDate','numberOfReviews'])
'''

def dataAnalysis(inPath, outPath):
    reviewUser = []
    reviewContent = []
    reviewDateAndTime = []
    reviewDate = []
    dateWithReviews = []
    numberOfReviewsOnSameDate = []
    start = 0
    numberOfReviews = 0
    item = 0
    df = pd.read_csv(inPath, error_bad_lines = False, header = None)
    # df_names = pd.read_csv('C:\workspace\SentimentClassfication\input.csv',
    #                       error_bad_lines = False, header = None, names = ['name', 'date', 'content'])
    rowCount = len(df.index)  # 获取总行数
    for row in range(rowCount):
        reviewUser.append(df.ix[row][0])
        reviewDateAndTime.append(df.ix[row][1])
        reviewContent.append(df.ix[row][2])
    # df.set_index('0').index.getduplicates()
    #df_reviewUser = pd.DataFrame(data=reviewUser, columns=['reviewUser'])
    # df_reviewDate = pd.DataFrame(data = reviewDate, columns = ['reviewDate'])
    #df_reviewContent = pd.DataFrame(data=reviewContent, columns=['reviewContent'])
    pattern = re.compile(r'\S*')
    for item in range(len(reviewDateAndTime)):
        try:
            date = pattern.findall(reviewDateAndTime[item])
        except:
            continue
        reviewDate.append(date[0])
    item = 0 #上面经过一次遍历需要重置item值为0
    while item < (len(reviewDate) - 1):
        if (start < len(reviewDate) and reviewDate[item] == reviewDate[start]):
            numberOfReviews += 1
            start += 1
        else:
            numberOfReviewsOnSameDate.append(numberOfReviews)
            dateWithReviews.append(reviewDate[item])
            numberOfReviews = 0
            item = start
    numberOfReviewPerDate = list(zip(dateWithReviews, numberOfReviewsOnSameDate))
    df_date = pd.DataFrame(data = numberOfReviewPerDate, columns = ['Date', 'NumberOfReviews'])

    df_date.time = pd.to_datetime(df_date['Date'], format = '%Y-%m-%d')
    df_date.set_index(['Date'], inplace = True)
    df_date.plot()
    #print(df_date)
    df_date.to_csv(outPath, index = False, header = False)
    wordCut = thulac.thulac()
    #加入进度条显示功能，之后可能会删去
    '''
    p = progressbar.ProgressBar(filt = True)
    p.start(len(reviewContent))
    for item in range(len(reviewContent)):
        try:
            reviewContent[item] = wordCut.cut(reviewContent[item], text = True)
            p.update(item + 1)
        except:
            p.update(item + 1)
            continue
    p.finish()
    #for item in range(len(reviewContent)):
    #    print(reviewContent[item])
    #pattern1 = re.compile(r'[\s]*?[\S]*_w') #除去标点
    #pattern2 = re.compile(r'[[\S]*_n [\S]*_d [\S]*_v]?') #名词+副词+动词 如: 质量 还 行
    #pattern3 = re.compile(r'(\S*_n)+\s?(\S*_d)?\s?(\S*_v)?\s?(\S*_a)+') #名词+形容词 如：外观漂亮
    pattern = re.compile(r'(\S*_n)?\s?(\S*_d)?\s?(\S*_v)?\s?(\S*_a)+') #名词(可能出现）+
                                                                        # 副词（可能出现）+
                                                                        #动词（可能出现）+形容词（一定出现）

    p.start(len(reviewContent))
    for item in range(len(reviewContent)):
        #reviewContent[item] = re.sub(pattern1, '', reviewContent[item])
        #advAdjWords = pattern2.findall(reviewContent[item])
        #nounAdjWords = pattern3.findall(reviewContent[item])
        emotionWords = pattern.findall(reviewContent[item])
        #print(nounAdvAdjWords)
        #for i in range(len(advAdjWords)):
        #    emotionWords.append(advAdjWords[i])
        #for i in range(len(nounAdjWords)):
        #    emotionWords.append(nounAdjWords[i])
        for i in range(len(emotionWords)):
            emotionWords[i] =  ''.join(emotionWords[i])
        reviewContent[item] = emotionWords
        p.update(item + 1)
    p.finish()
    print(reviewContent)
'''

reviewUser = []
reviewContent = []
inPath = 'C:\workspace\SentimentClassfication\largeDataTest.csv'
outPath = 'C:\workspace\SentimentClassfication\ReviewNumberPerDate.csv'
dataAnalysis(inPath, outPath)
plt.show()