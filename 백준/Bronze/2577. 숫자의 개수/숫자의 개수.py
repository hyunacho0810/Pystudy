# 숫자의 개수
dict={'0':0,
      '1':0,
      '2':0,
      '3':0,
      '4':0,
      '5':0,
      '6':0,
      '7':0,
      '8':0,
      '9':0,
      }
num1=int(input())
num2=int(input())
num3=int(input())
num=str(num1*num2*num3)

for i in range(len(num)):
    if num[i] in dict:
        dict[num[i]]+=1

for key,values in dict.items():
    print(values)
    