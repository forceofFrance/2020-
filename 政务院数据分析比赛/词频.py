import jieba
txt = open("健康码.txt", encoding="utf-8").read()
#加载停用词表
stopwords = [line.strip() for line in open("tyc.txt",encoding="utf-8").readlines()]
words  = jieba.lcut(txt)
counts = {}
for word in words:
    #不在停用词表中
    if word not in stopwords:
        #不统计字数为一的词
        if len(word) == 1:
            continue
        else:
            counts[word] = counts.get(word,0) + 1
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)
for i in range(100):
    word, count = items[i]
    print ("{:<10}{:>7}".format(word, count))