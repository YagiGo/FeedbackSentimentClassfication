import os
import re
import math
def openFile():
    error = 1
    file_name = str(input("请输入处理好的文本文件名（以.txt结尾， 如Test.txt）："))
    file_dir = os.path.join(os.path.abspath(os.path.curdir), file_name)
    while error == 1:
        try:
            return open(file_dir, "r", encoding = "utf-8").readlines()
        except:
            file_name = str(input("找不到文件，请确认文件是否处于代码同目录下以及文件名是否正确后，再次输入文件名："))
            file_dir = os.path.join(os.path.abspath(os.path.curdir), file_name)

def loadPosDict():
    error = 1
    posDict = []
    file_name = 'positive.txt'
    file_dir = os.path.join(os.path.abspath(os.path.pardir), "Dict", file_name)
    while error == 1:
        try:
            for line in open(file_dir, "r", encoding="utf-8").readlines():
                posDict.append(line.strip('\n'))
            return posDict
        except:
            file_name = str(input("找不到文件{}，请手动输入正向情感词典的文件名：".format(file_name)))
            file_dir = os.path.join(os.path.abspath(os.path.curdir), file_name)
def loadNegDict():
    error = 1
    negDict = []
    file_name = 'negative.txt'
    file_dir = os.path.join(os.path.abspath(os.path.pardir), "Dict", file_name)
    while error == 1:
        try:
            for line in open(file_dir, "r", encoding="utf-8").readlines():
                negDict.append(line.strip('\n'))
            return negDict
        except:
            file_name = str(input("找不到文件{}，请手动输入负面情感词典的文件名：".format(file_name)))
            file_dir = os.path.join(os.path.abspath(os.path.curdir), file_name)

def SentiClass(sentence, PosDict, NegDict, PosCount, NegCount):
    for item in PosDict:
        # print(line.find(item))
        if sentence.find(item) + 1 > 0:
            PosCount += 1
            break
    for item in NegDict:
        if sentence.find(item) + 1 > 0:
            NegCount += 1
            break
    return PosCount, NegCount

def CalGoodAndBadReviewsCount( reviewContent, PosDict, NegDict):
    PosCount = 0
    NegCount = 0
    #print(openFile())
    #print(PosDict)
    #print(NegDict)
        #print(type(line))
    PosCount, NegCount = SentiClass(reviewContent, PosDict, NegDict, PosCount, NegCount)

    #print("好评数：{}, 差评数：{}".format(PosCount, NegCount))
    return PosCount, NegCount


# TEST PART #
if __name__ == "__main__":
    #text = open("neg.txt", "r", encoding = 'utf-8').readlines()
    text = [['买_v小_a', '挺_d合身_a', '速度_n不错_a'],
            ['买_v小_a', '挺_d合身_a', '速度_n不错_a'],
            ['很_d合身_a', '不_d厚_a', '不_d薄_a', '很_d好_a', '膝盖_n不_d长_a', '不_d短_a'],
            ['粗糙_a'],
            ['小_a', '下_v好_a', '多_a'],
            ['优秀_a'],
            ['优秀_a'],
            ['老_a'],
            ['质量_n很_d好_a', '平常_a', '码数_n偏_d大_a', '选择_v小_a', '更加_d合身_a'],
            ['颜色_n很_d正_a'],
            ['比较_d厚实_a', '包装_v完好_a'],
            ['要_v薄_a'],
            ['购买_v咯_a'],
            ['裤子_n不错_a', '小_a', '很_d赞_a'],
            ['小_a', '霜_n工作_v好_a', '认真_a'],
            ['差_a', '一样_a', '高_a'],
            ['挺_d好_a', '很_d厚实_a'],
            ['质量_n不错_a', '不_d准_a', '买_v小_a'],
            ['大_a'],
            ['起来_v超级_a', '舒服_a', '小_a', '小_a', '很_d好_a'],
            ['很_d好_a', '客服_n小_a', '小_a', '霜_n服务_v不错_a'],
            ['不_d贵_a', '质量_n还_d不错_a'],
            ['还要_v多_a'],
            ['大_a'],
            ['质量_n真心_d不错_a', '布料_n厚实_a'],
            ['太_d肥大_a'],
            ['老_a', '不好_a', '最_d重要_a', '云朵_n热情_a', '周到_a', '超级_a', '超级_a'],
            ['大小_n合适_a'],
            ['很_d合身_a'],
            ['生于_v自由_a', '忠于_v自由_a'],
            ['麻吉_a', '老_a', '提示_v小_a', '合适_a'],
            ['超好看_a', '短裤_n会贵_a'],
            ['裤子_n还_d不错_a', '脏脏_a'],
            ['直接_a'],
            ['衣服_n码_v小_a', '时间_n快_a', '直接_a', '已_d真_a', '非常_a'],
            ['同款_n长_a', '紧_a'],
            ['紧_a'],
            ['很_d宽松_a'],
            ['不_d多_a'],
            ['评价_v晚_a', '灰常_a'],
            ['大_a', '买_v大_a', '码数_n确实_a', '偏_d大_a'],
            ['老_a'],
            ['严重_a', '还_d好_a', '偏_d大_a', '偏_d大_a', '还_d真_a', '偏_v大_a'],
            ['款式_n肥大_a', '走线_n也_d不好_a'],
            ['很_d合身_a'],
            ['挺_d好_a', '就_d是_v纯_a', '布料_n有点_d厚_a', '沉_a'],
            ['不_d多_a'],
            ['码数_n偏_d大_a', '买_v大_a', '店家_n很_d热心_a', '号_n刚好_a', '布料_n有点_d硬_a'],
            ['是_v麻吉_a'],
            ['款式_n好_a', '厚_a'],
            ['裤子_n比较_d潮_a', '布料_n厚实_a', '宽松_a', '舒适_a', '很_d合身_a', '痒_a'],
            ['少_a'],
            ['偏_d大_a'],
            ['挺_d好_a', '有点_d厚_a'],
            ['挺_d好_a', '很_d厚实_a'],
            ['好_a', '厚实_a', '多_a'],
            ['不_d多_a'],
            ['颜色_n一样_a'],
            ['物流_n有点_d慢_a', '很_d不错_a', '喜欢_v麻吉_a'],
            ['老_a', '全_a'],
            ['很_d合身_a'],
            ['版型_n好看_a', '口袋_n多_a', '挺_d厚实_a'],
            ['版型_n好看_a', '口袋_n多_a', '挺_d厚实_a', '有_v一定_a', '穿_v来有型_a'],
            ['款式_n不错_a', '厚_a'],
            ['没_d不好_a'],
            ['纽扣_n老_a'],
            ['粗糙_a', '麻吉_a', '上_v歪歪斜斜_a', '可惜_a'],
            ['一样_a', '太_d一样_a'],
            ['厚_a', '版型_n不错_a', '尺码_n很_d准_a'],
            ['活_a', '大_a', '大_a', '实_a', '恶_a', '大_a'],
            ['东西_n不错_a', '小_a'],
            ['质量_n很_d好_a', '大码_n稍微_d小_a'],
            ['不错_a', '上_v好_a', '挺_d厚_a', '重重_a'],
            ['不错_a', '厚_a'],
            ['东西_n不错_a', '很_d厚实_a'],
            ['大_a'],
            ['麻吉_a', '效果_n不错_a', '整个_a', '厚_a'],
            ['麻吉_a', '效果_n不错_a', '整个_a', '厚_a'],
            ['挺有型_a', '挺_d厚实_a', '态度_n非常_d好_a'],
            ['颜色_n很_d正_a', '料子_n很_d厚实_a', '不错_a'],
            ['颜色_n好看_a', '做工_n真_a', '一般_a'],
            ['宽松_a', '肥_a', '挺_d有范_a'],
            ['合身_a'],
            ['凑_v近_a', '做工_n粗糙_a'],
            ['颜色_n太_d深_a', '太_d好看_a', '特别_d严重_a'],
            ['质量_n很_d好_a', '很_d合身_a', '偏_d厚_a'],
            ['只_d穿_v麻吉_a'],
            ['合身_a'],
            ['黑_a', '发_v白_a', '客服_n很_d有趣_a', '价格_n不_d算_v便宜_a', '提高_v一般_a'],
            ['毛病_n非常_d好_a'],
            ['毛病_n非常_d好_a'],
            ['欢_a', '纯_a'],
            ['偏_d大_a', '宽松_a', '才_d好看_a', '面料_n又_d厚_a', '颜色_n又_d好看_a', '成_v薄_a', '厚_a', '太_d多_a'],
            ['厚实_a', '不错_a'],
            ['依然_a'],
            ['不好_a'],
            ['款式_n好_a', '面料_n厚实_a', '浅_a', '稍_d肥_a'],
            ['麻吉_a'],
            ['老_a'],
            ['老_a'],
            ['很_d好_a', '很_d厚实_a', '色彩_n很_d正_a'],
            ['确实_a'],
            ['很_d合身_a'],
            ['布料_n很_d厚实_a', '麻吉_a', '质量_n不错_a'],
            ['质量_n很_d好_a', '小_a', '纯_a'],
            ['裤子_n大_a', '比较_d厚重_a', '还_d不错_a'],
            ['好_a', '厚实_a'],
            ['色差_n太_d大_a', '也_d快_a'],
            ['裤子_n够_v宽_a', '够_v厚_a', '质量_n实在_a', '码数_n合适_a', '速度_n惊人_a'],
            ['裤子_n够_v宽_a', '够_v厚_a', '质量_n实在_a', '码数_n合适_a', '速度_n惊人_a'],
            ['裤子_n很_d好_a', '要_v厚_a', '很_d扎实_a'],
            ['做工_n很_d好_a', '布料_n挺_d厚实_a'],
            ['老_a'],
            ['好处_n就_d是_v脏_a'],
            ['麻吉_a'],
            ['质量_n很_d不错_a', '挺_d厚实_a'],
            ['好_a', '很_d多_a', '很_d厚实_a', '绝对_a'],
            ['不错_a', '面料_n很_d厚_a'],
            ['大小_n刚_d合适_a'],
            ['做工_n一般_a', '太_d多_a', '很_d好_a'],
            ['买_v小_a', '号_n合适_a'],
            ['麻吉_a'],
            ['大小_n正_d合适_a', '挺_d宽松_a'],
            ['裤子_n很_d厚实_a', '刚_d好_a'],
            ['首先_d短_a', '料子_n很_d厚实_a', '效果_n很_d好_a', '偏_d瘦_a'],
            ['不错_a', '口袋_n深_a', '最_d小_a'],
            ['短裤_n非常_d厚实_a', '质量_n非常_d好_a'],
            ['太_d一样_a', '有点_d偏_a', '黄_a'],
            ['买_v瘦_a'],
            ['本来_d拍_v浅灰_a', '裤子_n很_d宽松_a'],
            ['厚_a', '不错_a'],
            ['裤子版型_n不错_a', '挺_d厚实_a', '紧_a'],
            ['很_d<b_a', '好_a', '很_d<b_a', '厚_a', '实_a'],
            ['不错_a', '厚实_a'],
            ['有点_d长_a'],
            ['很_d<b_a'],
            ['特意_d买_v小_a', '买_v大_a', '是_v瘦_a', '所有_a', '很_d好_a'],
            ['偏_d大_a'],
            ['老_a', '支持_v麻吉_a'],
            ['质量_n挺_d好_a', '有点_d厚_a'],
            ['不_d紧_a', '很_d宽松_a'],
            ['不_d紧_a', '很_d宽松_a'],
            ['大小_n正_d合适_a'],
            ['差_a', '料子_n很_d好_a'],
            ['很_d高_a', '东西_n挺_d厚实_a'],
            ['胖子_n穿_v反_a', '正_a'],
            ['大_a', '紧_a'],
            ['版型_n不错_a', '料子_n不错_a', '线头_n多_a', '不_d买_v随便_a', '差_a', '差_a'],
            ['不错_a', '布料_n很_d厚实_a', '很_d软_a', '豪华_a'],
            ['黄_a', '蓝_a'],
            ['太_d多_a', '麻吉_a'],
            ['麻吉_a'],
            ['非常_d实惠_a'],
            ['裤子_n很_d厚实_a', '码正_a', '合适_a'],
            ['质量_n不错_a', '布料_n太_d厚_a'],
            ['东西_n确实_a', '不错_a', '厚_a'],
            ['非常_d厚实_a', '质地_n不错_a', '线头_n很_d少_a'],
            ['质量_n很_d好_a', '厚实_a', '买_v大_a', '小伙伴_n说_v大_a', '舒服_a'],
            ['款型_n非常_d好_a', '布料_n很_d厚_a'],
            ['不错_a', '很_d厚实_a', '老_a'],
            ['颜色_n很_d正_a', '大小_n合适_a'],
            ['满_a'],
            ['厚_a', '实_a', '很_d<b_a', '好_a', '满_a'],
            ['很_d宽松_a']]
    # process_text = []
    # for line in text:
    #    process_text.append(line.strip("\n"))
    # print(process_text)
    posDict = loadPosDict()
    negDict = loadNegDict()

    positiveFeedback = 0
    negativeFeedback = 0
    neutral = 0
    for item in range(len(text)):
        posCountPerReview = 0
        negCountPerReview = 0
        for sentence in text[item]:
            posCount, negCount = CalGoodAndBadReviewsCount(sentence, posDict, negDict)
            posCountPerReview += posCount
            negCountPerReview += negCount

        weight = math.log(((posCountPerReview + 1) / (negCountPerReview + 1)), 2)
        print(posCountPerReview, negCountPerReview, weight)
        if weight > 0:
            positiveFeedback += 1
        elif weight < 0:
            negativeFeedback += 1
        elif weight == 0:
            neutral += 1
    print(positiveFeedback, negativeFeedback, neutral, len(text))
# TEST PART #