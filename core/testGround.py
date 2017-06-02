'''import re
text = '非常_d 快_a 的_u 手机_n ，_w 速度_n 太_d 快_a ，_w 请_v 系_v 好_a 安全带_n 速度_n 快_a 速度_n 速度_n 非常_d 快_a'
pattern1 = re.compile(r'[\s]*?[\S]*_w')  # 除去标点
pattern4 = re.compile(r'(\S*_n)+\s?(\S*_d)?\s?(\S*_v)?\s?(\S*_a)+')  # 名词+副词+形容词
text = pattern1.sub('', text)
print(text)
text2 = pattern4.search(text)
print(text2.group())
text3 = pattern4.findall(text)
print(text3)
for item in range(len(text3)):
    a = ' '.join(text3[item])
    text3[item] = a
print(text3)


'''
'''
from core.DataAnalysis import dataAnalysis
TrainingText = []
for item in range(55):
    fileName = item + 1
    inPath = 'C:\workspace\SentimentClassfication\Reviews\{}.csv'.format(fileName)
    outPath = 'C:\workspace\SentimentClassfication\Reviews\{}_output.csv'.format(fileName)
    filePath = 'C:\workspace\SentimentClassfication\Reviews\pic\{}_outfig.png'.format(fileName)
    temp = dataAnalysis(inPath, outPath, filePath)
    TrainingText.extend(temp)
textFile = open("TrainingText.txt", 'w+', encoding = 'utf-8')
for item in range(len(TrainingText)):
    if len(TrainingText[item]):
        for i in range(len(TrainingText[item])):
            textFile.write(TrainingText[item][i] + '\n')

'''
import os,sys
'''
print(os.path.abspath(os.path.pardir))
file_name = str(input("请输入褒义词词典名（以.txt结尾， 如Pos.txt）："))
file_dir = os.path.join(os.path.abspath(os.path.pardir), "Dict", file_name)
print(file_dir)
'''
# a = '很_d好_a'
# b = '好好'
# print(a.find(b))

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
'''
print(b.find("好"))
'''
import matplotlib.pyplot as plt
