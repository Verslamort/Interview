# 统计一个文本中单词频次最高的10个单词？
# 方法1
import re
from collections import Counter


def test1(filepath):
    distone = {}
    with open(filepath) as f:
        for line in f:
            line = re.sub('\W+', ' ', line)
            lineone = line.split()
            for keyone in lineone:
                if not distone.get(keyone):
                    distone[keyone] = 1
                else:
                    distone[keyone] += 1
    num_ten = sorted(distone.items(), key=lambda x: x[1], reverse=True)[:10]
    num_ten = [x[0] for x in num_ten]
    return num_ten


# 方法2 built-in Counter most_common
def test2(filepath):
    with open(filepath) as f:
        return list(map(lambda c: c[0], Counter(re.sub('\W+', ' ', f.read()).split()).most_common(10)))

