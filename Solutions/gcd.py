# 유클리드 호제법을 이용하여 최대 공약수를 구함
def gcd(n1, n2):
    if n1 < n2:
        (n1, n2) = (n2, n1)

    while n2 != 0:
        (n1, n2) = (n2, n1 % n2)

    return n1


# 최소 공배수는 n과 m을 곱한후 최대 공약수로 나누어 준다
def solution(n, m):
    answer = [gcd(n, m), (n * m) / gcd(n, m)]
    return answer