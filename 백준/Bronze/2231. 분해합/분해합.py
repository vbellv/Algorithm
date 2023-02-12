n = int(input())   # 자연수 N
x = 0
lst = []

def num(n):  
  # 분해합(x) 구하기
  for i in range(1, n):
    x = sum(map(int, str(i))) + i
    
    # 분해합(x) 중 자연수 N과 일치하는 경우, 분해합 하기 전 숫자(i) 리스트에 넣기
    if x == n:
      lst.append(i)

  # 리스트 안의 가장 작은 수 리턴, 리스트 안의 생성자가 없으면 0을 리턴
  if lst :
    return min(lst)
  else:
    return 0

print(num(n))