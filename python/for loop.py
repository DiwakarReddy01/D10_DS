for i in range(1,21):
    if i%3==0:
        print(i,'fizz')
    elif i%5==0:
        print(i,'buzz')
    elif i%3 and i%5:
        print(i,'fizzbuzz') 
    else:
        print("invalid num")