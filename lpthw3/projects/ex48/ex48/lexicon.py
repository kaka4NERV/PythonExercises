# 这是一段扫描输入并归类的代码
lexicon = {
    'north': 'direction',
    'south': 'direction',
    'east': 'direction',
    'west': 'direction',
    'down': 'direction',
    'up': 'direction',
    'left': 'direction',
    'right': 'direction',
    'back': 'direction',
    'go': 'verb',
    'stop': 'verb',
    'kill': 'verb',
    'eat': 'verb',
    'the': 'stop',
    'in': 'stop',
    'of': 'stop',
    'from': 'stop',
    'at': 'stop',
    'it': 'stop',
    'door': 'noun',
    'bear': 'noun',
    'princess': 'noun',
    'cabinet': 'noun',
}
def scan(stuff):
    # 接收字符串作为参数，识别字符串对应的词汇类型并与字符串本身组成元组，返回元组组成的列表、
    words = stuff.split(' ')
    num = len(words)
    ls = []
    for i in range(num):
        try:
            words[i] = int(words[i])
            token = 'number'
        except ValueError:
            lower_words = words[i].lower()
            token = lexicon.get(lower_words, 'error')
        ls.append((token, words[i]))
    return ls
