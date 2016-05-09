import math
"""Problem 1"""
def multiples_3_and_5():
    sum=0
    for x in range(1000):
        if x%3==0 or x%5==0:
            sum=sum+x
    return sum

""" Problem 3"""   
def prime_factors(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1
    return max(factors)
""" Problem 4"""
def largest_pol():
    pols=[]
    n=999
    while(n>100):
        m=999
        while(m>100):
            result = m*n
            rslt_lst = list(str(result))
            if len(rslt_lst)== 6:
                if rslt_lst[0]==rslt_lst[5] and rslt_lst[1]==rslt_lst[4] and rslt_lst[2]==rslt_lst[3]:
                    pols.append(result)
            m-=1
        n-=1
    return max(pols)
""" Problem 5"""
def smallest_mult(k):
    smallest_n = 1
    deviders =[1]
    while len(deviders) < k+1:
       # print ("Into main loop")
        ctr = 0
        while ctr < len(deviders):
          #  print ("Into sub loop")
            if smallest_n%deviders[ctr]!= 0:
              #  print ("Into if loop")
                smallest_n+=1
                ctr=0
            else:
                ctr+=1
        
        new_item  = deviders[-1]+1
       # print ("Add new item ", new_item)
        deviders.append(new_item)
    return smallest_n;

    
if __name__=='__main__':
    print(smallest_mult(20))
