# 문제
# 두 자연수 A와 B가 있을 때, A = BC를 만족하는 자연수 C를 A의 약수라고 한다. 예를 들어, 2의 약수는 1, 2가 있고, 24의 약수는 1, 2, 3, 4, 6, 8, 12, 24가 있다. 자연수 A의 약수의 합은 A의 모든 약수를 더한 값이고, f(A)로 표현한다. x보다 작거나 같은 모든 자연수 y의 f(y)값을 더한 값은 g(x)로 표현한다.

# 자연수 N이 주어졌을 때, g(N)을 구해보자.

# 입력
# 첫째 줄에 자연수 N(1 ≤ N ≤ 1,000,000)이 주어진다.

# 출력
# 첫째 줄에 g(N)를 출력한다.

# 예제 입력 1 
# 1
# 예제 출력 1 
# 1
# 예제 입력 2 
# 2
# 예제 출력 2 
# 4
# 예제 입력 3 
# 10
# 예제 출력 3 
# 87
# 예제 입력 4 
# 70
# 예제 출력 4 
# 4065
# 예제 입력 5 
# 10000
# 예제 출력 5 
# 82256014

# 풀이 1 : N을 입력 받아서 그 밑의 자연수들 각각의 모든 약수를 더한다. 약수는 나머지 연산으로 계산한다. => 시간초과
# num = int(input())
# sum = 0
# while num > 0:
#     value = num
#     while value > 0:
#         if num%value == 0:
#             sum+=value
#         value-=1
#     num-=1
# print(sum)

# 풀이 2 : N을 입력 받아서, 1~N의 자연수중 i를 약수로 가지는 개수는 N/i가 된다. => 원리는 아직 잘 모르겠음
# // 연산자 : 나눠서 나머지 버린 몫
num = int(input())
sum = 0
for i in range(1,num+1):
    sum = sum + num//i*i
print(sum)