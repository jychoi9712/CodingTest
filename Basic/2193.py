# 문제
# 0과 1로만 이루어진 수를 이진수라 한다. 이러한 이진수 중 특별한 성질을 갖는 것들이 있는데, 이들을 이친수(pinary number)라 한다. 이친수는 다음의 성질을 만족한다.

# 이친수는 0으로 시작하지 않는다.
# 이친수에서는 1이 두 번 연속으로 나타나지 않는다. 즉, 11을 부분 문자열로 갖지 않는다.
# 예를 들면 1, 10, 100, 101, 1000, 1001 등이 이친수가 된다. 하지만 0010101이나 101101은 각각 1, 2번 규칙에 위배되므로 이친수가 아니다.

# N(1 ≤ N ≤ 90)이 주어졌을 때, N자리 이친수의 개수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N이 주어진다.

# 출력
# 첫째 줄에 N자리 이친수의 개수를 출력한다.

# 예제 입력 1 
# 3
# 예제 출력 1 
# 2

# 풀이 1 : BF 방식 => 시간 초과
# count = int(input())
# array = [1]
# total = 0

# def dp():
#     global total
#     length = len(array)
#     if length == count:
#         total +=1
#         return 
    
#     for i in range(2):
#         if array[length-1] == 1 and i==1:
#             continue
#         array.append(i)
#         dp()
#         array.pop()

# dp()
# print(total)

# 풀이 2 : DP 방식
count = int(input())
dp = [1 for _ in range(count+1)]

for i in range(3,count+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[count])