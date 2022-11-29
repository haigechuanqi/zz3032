def FizzBuzz(start, finish):
    outlist = []
    for x in range (start, finish+1):
        if x%3==0 and x%5==0:
            print("fizz buzz")
        elif x%3==0:
            print('fizz')
        elif x%5==0:
            print('buzz')
        else:
            print (x)    
    outlist = outlist.append(x)
