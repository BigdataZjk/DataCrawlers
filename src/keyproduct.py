import itertools as its

words = '1234567890'  # ²ÉÓÃµÄ×Ö·û

r = its.product(words, repeat=4)
with open(r'D:\GitProjects\DataCrawlers\resources\Keys.txt', mode='a') as f1:
    # f1.truncate()
    for key in r:
        f1.write(''.join(key))
        f1.write(''.join('\n'))
    f1.close()
