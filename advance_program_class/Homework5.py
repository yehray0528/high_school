for n in range(10):
    lst = testcases[n]

    check = True

    s = []
    i = 1
    idx = 0
    while i <= len(lst) :
        if idx < len(lst) and lst[idx] == i :
            i += 1
            idx += 1
        elif len(s) != 0 and s[-1] == i :
            s.pop()
            i += 1
        elif idx < len(lst) :
            s.append(lst[idx])
            idx += 1
        else :
            check = False
            break

    if check :
        print("success")
    else :
        print("fail")