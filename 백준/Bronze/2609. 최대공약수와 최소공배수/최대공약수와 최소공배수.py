# 최대공약수와 최대공배수
# 최대공약수
def greatest_common_divisor(num1,num2):
    if num1<num2:
        i=num1
    else:
        i=num2
    while i>0:
        if num1%i==0 and num2%i==0:
            return i
        else:
            i-=1

def least_common_multiple(num1,num2):
    # 두 수의 곱을 시작점으로
    comm = num1 * num2

    # num1부터 시작해서 공배수 찾기
    for i in range(max(num1, num2), comm + 1, max(num1, num2)):
        if i % num1 == 0 and i % num2 == 0:
            return i

    return comm  # 최악의 경우 두 수의 곱이 최소공배수



num1,num2=map(int,input().split())

print(greatest_common_divisor(num1,num2))
print(least_common_multiple(num1,num2))