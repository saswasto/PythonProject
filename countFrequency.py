def freq_word():
    str = input("Enter a string: ")
    li = str.split()
    d= {}
    for i in li:
        if i not in d.keys():
            d[i]=0
        d[i] = d[i] +1
    print(d)
freq_word()