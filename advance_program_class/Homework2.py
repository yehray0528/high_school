def tsv_to_sorted_csv(t):
    tem = []
    tem = t.split('\t')
    c = []
    i = 0
    while i < len(tem):
        c.append(int(tem[i]))
        i += 1
    c = sorted(c, reverse=True)
    a = ""
    a = ','.join([str(k) for k in c])
    return a
