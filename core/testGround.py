import re
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
