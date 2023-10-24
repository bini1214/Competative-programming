n = int(input())
arr = list(map(int, input().split()))

even = []
odd = []

for num in arr:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

even.sort()
odd.sort()

result = odd + even

print(*result)
