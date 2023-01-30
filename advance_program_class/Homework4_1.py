from collections import Counter
import os

files = ['file1.txt', 'file2.txt', 'file3.txt', 'file4.txt', 'file5.txt']

j = 0
while j < len(files):
    os.chdir('/content')
    file = open('file%d.txt' % (j+1), 'r')
    os.mkdir('file%d_ans' % (j+1))
    os.chdir('/content/file%d_ans' % (j+1))
    lst = Counter(file)
    k = 0
    while k < len(lst):
        os.chdir('/content/file%d_ans' % (j+1))
        fileWriter = open('%s.txt' % lst.most_common()[k][0].split()[0],
                    'a', encoding='utf-8')

        i = k
        while lst.most_common()[i][0].split()[0] == lst.most_common()[k][0].split()[0]:
            fileWriter.write(lst.most_common()[i][0].split()[1])
            fileWriter.write(' ')
            fileWriter.write(str(lst.most_common()[i][1]))
            fileWriter.write('\n')
            i += 1
            if i >= len(lst):
                break
        k = i
        fileWriter.close()
    j += 1
