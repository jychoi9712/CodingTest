[Python]
- python 여러 입력 받는 경우 : sys.stdin.readline을 사용해야 오류가 발생하지 않음!!!
- print 방식 : 변수 나열보다 옆 방식이 시간이 적게 소요 된다. print("%d = %d + %d"%(a ,b ,c))
- 2차원 배열 선언 : arr = [[0] * cols] * rows 로 선언시 얕은 복사로 인해 rows가 공통으로 처리됨. 
                   맞는 방식 => arr = [[0 for j in range(cols)] for i in range(rows)]
- List는 변수 선언 이후 값이 바뀔수 있는 mutable 변수이기 때문에 함수 내에서 수정해줘도 전역변수처럼 사용이 가능하다.
  But 일반 변수는 함수 내에서 값을 바꾸는 것은 함수 내에서 global 선언하기 전에는 불가능 하다.
- List는 sort, remove, append, pop 함수 사용 가능
- join 함수를 사용하면, 리스트에 있는 요소 하나하나를 합쳐서 하나의 문자열로 바꾸어주는 함수이다. -> '구분자'.join(리스트) -> ''.join(map(str,result))
- 숫자 앞자리 0 채우기 -> str변수.zfill(자릿수)
- sorted 함수 : sorted(list) => 리스트 정렬된 것을 리턴한다. sorted(list, reverse=true) => 리스트 역정렬된 것을 리턴한다.

- 순열(순서 고려 O, (A,B), (B,A)는 다른 것) : 파이썬에서 제공하는 순열 함수가 있다. 리스트를 넘겨 고르는 개수를 넘기고, list로 받으면 된다. 
    ex) import itertools
        arr = ['A', 'B', 'C']
        nPr = itertools.permutations(arr, 2)
        print(list(nPr))
- 조합(순서 고려 X, (A,B), (B,A)는 같은 것) : 파이썬에서 제공하는 조합 함수가 있다. 리스트를 넘겨 고르는 개수를 넘기고, list로 받으면 된다. 
    ex) import itertools
        arr = ['A', 'B', 'C']
        nCr = itertools.combinations(arr, 2)
        print(list(nCr))
        
[Algorithm]
- 약수의 합 : 1~N의 자연수중 i를 약수로 가지는 개수는 N/i가 된다.
- 약수 합 구하는 법 : i*j의 약수는 i,j 임을 이용하여 i와 j를 1부터 구하려는 수까지 반복하여 array[i*j] += i를 해주어 해당 인덱스 숫자에 대한 약수를 구한다.
- 유클리드 호제법 : 최대 공약수를 구하는 방법. A, B의 최대 공약수는 A를 B로 나눈 나머지 R을 구하고, B를 R로 나눈 나머지 R'을 구한다. 이를 반복하여 나누어 떨어졌을 때의 나눈 값이 최대 공약수가 된다. ( R`n-1` % R`n` = 0 에서는 R`n`이 최대 공약수이다.)
- 최소 공배수(Least Common Multiple) 구하는 법 : A 와 B를 곱한 뒤 최대 공약수(Greatest Common Divisor)로 나눈다.
- 에라토스테네스의 체 : 소수 구하는 법. 숫자 N이 소수인지 판단하기 위해서는 2부터 N의 제곱근까지만 나누어떨어지는지 검사하면 된다.
- 브루트 포스(Brute Force, 키 전수조사, 무차별 대입) : 조합 가능한 모든 문자열을 하나씩 대입해 보는 방식

- 달력 표기 문제 : 년도 탐색은 1씩하지 말고, 하나를 잡고 interval 만큼 증가시키면서 비교하여 탐색 구간 줄이기! 최대값일때에는 나머지가 0이지만 표기는 최대값인 경우도 확인!

- 다이나믹 프로그래밍 (DP, Dynamic Programming) : 필요한 계산 값을 저장해두었다가 재사용하는 알고리즘 설계 기법. 큰문제를 동일한 작은 문제들로 나누어 푸는 분할 정복 알고리즘을 사용할 때, 동일한 작은 문제들을 저장해두어 재계산하지 않는 것. ** 규칙을 찾아 간단히 반복계산으로 처리 **

- 백트래킹 (퇴각 검색) : 길을 가다가 이 길이 아닌 것 같으면 왔던 길로 되돌아가 다른 경로로 진행. 보통 재귀로 구현하며 조건이 맞지 않으면 종료한다. DFS(깊이 우선 탐색) 기반
- 비트마스크 (브루트포스 기법중 하나) : 상태가 2개로 나뉘어지는 문제를 2진수에 대입하여 푸는 방식이다. 비트 연산을 사용하여 메모리와 시간 단축에 도움이 된다.
  - 왠만하면 재귀로 처리가 되지만, 가로/세로 등 조건이 복잡할때 비트마스크 방식으로 사용하면 좋다.
-   부분수열의 나열은 원래 수열의 반복이나 역순이 허용되지 않는다.