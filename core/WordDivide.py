import thulac
import re
adjWord = []
pattern = re.compile(r'\s[\S]*_a')
thu1 = thulac.thulac() #Default Mode
text = thu1.cut('外观漂亮，手感好，但电量不够用，我一天下来电话多，都不敢玩其它的。', text = True)
adj = pattern.findall(text)
pattern2 = re.compile(r'[\u4e00-\u9fa5]+')
for item in range(len(adj)):
    adjWord.append(pattern2.findall(adj[item]))
print(text)
print(adj)
print(adjWord)