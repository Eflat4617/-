import math
#극소 위치 찾기 by 경사하강법

de = 0.000001 #델타값, 0에 가까울수록 정확도 상승
def f(x):
    return x*(x+7)*(x-8)*(x-1) #극값위치 계산할 함수 입력
def d(x):
    return (f(de + x)-f(x))/de #미분계수의 정의
ls = []
alpha = 0.001 #stepsize, 0에 가까울수록 정확도 상승

for c in range(-10,10):
    while abs(d(c))>0.0001:
        c = c - (alpha * d(c))
        print(c)
    ls.append(round(c,3))

print(set(ls))