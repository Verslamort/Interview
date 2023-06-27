# 统计一个文本中单词频次最高的10个单词？
# 方法1
def sort_word():
    txt = open('me_before_you.txt', 'r').read()
    txt = txt.lower()  # 统一成小写
    for ch in '!"#$%&()*+,-./:;<<=>>?@[\\]^_‘{|}~':
        txt = txt.replace(ch, ' ')  # 特殊字符替换为空格
    return txt


if __name__ == '__main__':
    meTxt = sort_word()
    words = meTxt.split()  # 分割获得单词列表
    counts = {}
    for word in words:  # 字典中无，则创建键值对，有，则值+1
        counts[word] = counts.get(word, 0) + 1
    ten = sorted(counts.items(), key=lambda x: x[1], reverse=True)  # 按值降序排列
    print(ten[:10])




