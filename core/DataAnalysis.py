import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
import thulac
import time
import progressbar
from core.SentimentClassfication import CalGoodAndBadReviewsCount, loadNegDict, loadPosDict
import math
import random

def dataAnalysis(inPath, outPath, figurePath):
    numberOfReviewsWithContent = 0
    numberOfReviewsWithoutContent = 0
    countOfReviewWithNoContent = 0
    countOfReviewWithContent = 0
    reviewUser = []
    reviewContent = []
    reviewDateAndTime = []
    reviewDate = []
    dateWithReviews = []
    numberOfReviewsOnSameDate = []
    numberOfReviewsWithoutContentOnSameDate = []
    numberOfReviewsWithContentOnSameDate = []
    posReviewDate = []
    negReviewDate = []
    noEmotionReview = []
    start = 0
    numberOfReviews = 0
    neutral = 0
    df = pd.read_csv(inPath, error_bad_lines = False, header = None)
    # df_names = pd.read_csv('C:\workspace\SentimentClassfication\input.csv',
    #                       error_bad_lines = False, header = None, names = ['name', 'date', 'content'])
    # 获取总行数
    df_sorted = df.sort_values(by = [1], ascending = False) # 按照时间顺序排序评论
    # print(df)
    df_sorted.to_csv('C:\workspace\SentimentClassfication\SortTest.csv', index=False, header=False, encoding = 'utf-8')
    df = pd.read_csv('C:\workspace\SentimentClassfication\SortTest.csv', error_bad_lines = False, header = None)
    for row in range(len(df.index)):
        reviewUser.append(df.ix[row][0])
        reviewDateAndTime.append(df.ix[row][1])
        reviewContent.append(df.ix[row][2])
    # df.set_index('0').index.getduplicates()
    # df_reviewUser = pd.DataFrame(data=reviewUser, columns=['reviewUser'])
    # df_reviewDate = pd.DataFrame(data = reviewDate, columns = ['reviewDate'])
    # df_reviewContent = pd.DataFrame(data=reviewContent, columns=['reviewContent'])
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
    item = 0
    while item < len(reviewDate) - 1:
        if (reviewContent[item] == '此用户没有填写评论!') :
            numberOfReviewsWithoutContent += 1
        elif(reviewContent[item] != '此用户没有填写评论!'):
            numberOfReviewsWithContent += 1

        if (reviewDate[item] != reviewDate[item + 1] or item + 2 == len(reviewDate)):
            # print(numberOfReviewsWithoutContent)
            # print(numberOfReviewsWithContent)
            numberOfReviewsWithoutContentOnSameDate.append(numberOfReviewsWithoutContent)
            numberOfReviewsWithContentOnSameDate.append(numberOfReviewsWithContent)
            numberOfReviewsWithoutContent = 0
            numberOfReviewsWithContent = 0
        item += 1
    numberOfReviewsPerDate = list(zip(dateWithReviews, numberOfReviewsOnSameDate))
    # numberOfReviewsWithoutContentPerDate = list(zip(dateWithReviews, numberOfReviewsWithoutContentOnSameDate))
    # numberOfReviewsWithContentPerDate = list(zip(dateWithReviews, numberOfReviewsWithContentOnSameDate))
    # print(numberOfReviewsWithoutContentPerDate)
    # print(numberOfReviewsWithContentPerDate)
    # print(numberOfReviewsPerDate)
    df_date = pd.DataFrame(data = numberOfReviewsPerDate, columns = ['日期', '评论总数'])
    # df_date.insert(2 ,'有内容评论数', numberOfReviewsWithContentOnSameDate)
    # df_date.insert(3 ,'无内容评论数', numberOfReviewsWithoutContentOnSameDate)
    # print(df_date)
    # print(df_date)
    # print(dateWithReviews)
    wordCut = thulac.thulac()
    #加入进度条显示功能，之后可能会删去

    p = progressbar.ProgressBar(filt = True)
    p.start(len(reviewContent))
    countOfReview = len(reviewContent)

    for item in range(len(reviewContent)):
        try:
            reviewContent[item] = wordCut.cut(reviewContent[item], text = True)
            p.update(item + 1)
        except:
            p.update(item + 1)
            continue
    p.finish()
    # print(reviewContent)

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
        # reviewContent[item] = re.sub(pattern1, '', reviewContent[item])
        # advAdjWords = pattern2.findall(reviewContent[item])
        # nounAdjWords = pattern3.findall(reviewContent[item])
        emotionWords = pattern.findall(reviewContent[item])
        # print(nounAdvAdjWords)
        # for i in range(len(advAdjWords)):
        #     emotionWords.append(advAdjWords[i])
        # for i in range(len(nounAdjWords)):
        #     emotionWords.append(nounAdjWords[i])
        for i in range(len(emotionWords)):
            emotionWords[i] =  ''.join(emotionWords[i])
        if len(emotionWords) == 0:
            noEmotionReview.append(reviewContent[item])
        reviewContent[item] = emotionWords
        if len(reviewContent[item]) == 0:
            countOfReviewWithNoContent += 1
        else:
            countOfReviewWithContent += 1
        p.update(item + 1)
    # print(reviewContent)
    p.finish()
    # print(reviewContent)
    print("无内容评论数：{}".format(countOfReviewWithNoContent))
    print("有内容评论数：{}".format(countOfReviewWithContent))
    # print("内容分析失败评论数量：{}".format(countOfReview - countOfReviewWithContent - countOfReviewWithNoContent))
    # print("正面评价数：开发中...")
    # print("负面评价数：开发中...")
    # print(noEmotionReview)
    # plt.show()
    textFile = open("TrainingText.txt", 'w+', encoding= 'utf-8')
    for item in range(len(reviewContent)):
        if len(reviewContent[item]):
            for i in range(len(reviewContent[item])):
                textFile.write(reviewContent[item][i] + '\n')
    posDict = loadPosDict()
    negDict = loadNegDict()
    positiveFeedback = 0
    negativeFeedback = 0
    for item in range(len(reviewContent)):
        # print(reviewContent[item])
        posCountPerReview = 0
        negCountPerReview = 0
        if len(reviewContent[item]):
            for sentence in reviewContent[item]:
                posCount, negCount = CalGoodAndBadReviewsCount(sentence, posDict, negDict)
                posCountPerReview += posCount
                negCountPerReview += negCount
            # print(posCountPerReview, negCountPerReview)
            weight = math.log((posCountPerReview + 1) / (negCountPerReview + 1), 2)
            if weight > 0 :
                positiveFeedback += 1
                posReviewDate.append(reviewDate[item])
            elif weight < 0:
                negativeFeedback += 1
                negReviewDate.append(reviewDate[item])
                # print("Negative: {}".format(reviewContent[item]))
            else:
                neutral += 1
                # print("Neutral: {}".format(reviewContent[item]))
    print("负面词和正面词数量相等的评价数：{}".format(neutral))
    print("正面评价数:{}".format(positiveFeedback))
    print("负面评价数:{}".format(negativeFeedback))
    # print(posReviewDate)
    # print(negReviewDate)
    numberOfNegReviewsPerDate = 0
    numberOfPosReviewsOnSameDate = []
    numberOfNegReviewsOnSameDate = []
    # 按日期找出每天的好评数量 #
    start = 1
    item = 0
    dateWithPosReviews = [] # 有好评的日期
    numberOfPosReviewsPerDate = 0
    while item < (len(posReviewDate) - 1):
        if (start < len(posReviewDate) and posReviewDate[item] == posReviewDate[start]):
            numberOfPosReviewsPerDate += 1
            start += 1
        else:
            dateWithPosReviews.append(posReviewDate[item])
            numberOfPosReviewsOnSameDate.append(numberOfPosReviewsPerDate)
            numberOfPosReviewsPerDate = 0
            item = start
    #                       #
    # 按日期找出每天的差评数量 #
    numberOfNegReviewsPerDate = 0
    dateWithNegReviews = [] # 有差评的日期
    start = 1
    item = 0
    while item < (len(negReviewDate) - 1):
        if (start < len(negReviewDate) and negReviewDate[item] == negReviewDate[start]):
            numberOfNegReviewsPerDate += 1
            start += 1
        else:
            dateWithNegReviews.append(negReviewDate[item])
            numberOfNegReviewsOnSameDate.append(numberOfNegReviewsPerDate)
            numberOfNegReviewsPerDate = 0
            item = start


    #                      #
    # NOPROSM = Number Of Positive Review On Same Date
    # NONROSM = Number Of Negative Review On Same Date
    ExtendOfNOPROSD = []
    ExtendOfNONROSD = []
    # 补齐格式， 对没有差评或者好评的日期，用0补齐
    for item in range(len(dateWithReviews)):
        if dateWithReviews[item] in dateWithPosReviews:
            ExtendOfNOPROSD.append(numberOfPosReviewsOnSameDate[dateWithPosReviews.index(dateWithReviews[item])])
        else:
            ExtendOfNOPROSD.append(0)
    for item in range(len(dateWithReviews)):
        if dateWithReviews[item] in dateWithNegReviews:
            ExtendOfNONROSD.append(numberOfNegReviewsOnSameDate[dateWithNegReviews.index(dateWithReviews[item])])
        else:
            ExtendOfNONROSD.append(0)
    #############################################
    df_date.insert(2, '正面评价数', ExtendOfNOPROSD)
    df_date.insert(3, '负面评价数', ExtendOfNONROSD)
    df_date.to_csv(outPath, index=False, header=False, encoding= 'utf-8')

    df_date.time = pd.to_datetime(df_date['日期'], format = '%Y-%m-%d')
    df_date.set_index(['日期'], inplace = True)
    # df_date.reindex()
    # 配置画图的大小，线型等参数，同时使图表显示中文
    plt.rcParams['font.sans-serif'] = ['SimHei'] # 正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False # 正常显示负号
    styles = ['k-', 'k--', 'k-.'] # 指定线条样式 实线，虚线，点划线
    df_date.plot(style = styles)
    plt.ylabel("评论条数（单位：条）")
    plt.xlabel("日期（顺序：从右向左）")
    plt.xticks(rotation = 45) # 横坐标旋转90度防止重叠
    plt.tight_layout()
    plt.savefig(figurePath, dpi = 500)

    # print(numberOfPosReviewsOnSameDate)
    # print(dateWithPosReviews)
    # print(numberOfNegReviewsOnSameDate)
    # print(dateWithNegReviews)
    # print(len(numberOfNegReviewsOnSameDate))
    # print(len(numberOfPosReviewsOnSameDate))
    # print(len(numberOfReviewsWithContentOnSameDate))
    # print(len(numberOfReviewsWithoutContentOnSameDate))
    # print(len(reviewDate))
    # print(len(dateWithReviews))
    # print(len(ExtendOfNONROSD))
    # print(len(ExtendOfNOPROSD))
    # print(dateWithReviews)
    # print(ExtendOfNOPROSD)
    # print(ExtendOfNONROSD)

if __name__ == '__main__':
    reviewUser = []
    reviewContent = []
    # fileNo = [27,51,32,55,26,39,6,16,44,15]
    '''
    for i in fileNo:
        inPath = 'C:\workspace\SentimentClassfication\Reviews\{}.csv'.format(i)
        outPath = 'C:\workspace\SentimentClassfication\Reviews\ReviewNumberPerDate{}.csv'.format(i)
        figurePath = 'C:\workspace\SentimentClassfication\Reviews\TEST{}.png'.format(i)
        print("File Number is {}".format(i))
        # inPath = "neg.txt"
        # outPath = "neg_out.txt"
        # figurePath = "negFig.png
        reviewContent = dataAnalysis(inPath, outPath, figurePath)
    '''
    fileNo = random.randint(1, 55)
    inPath = 'C:\workspace\SentimentClassfication\largeDataTest.csv'
    outPath = 'C:\workspace\SentimentClassfication\ResultforPaper.csv'
    figurePath = 'C:\workspace\SentimentClassfication\TEST.png'
    # inPath = "neg.txt"
    # outPath = "neg_out.txt"
    # figurePath = "negFig.png
    reviewContent = dataAnalysis(inPath, outPath, figurePath)