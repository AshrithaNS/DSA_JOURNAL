a = [1, 2, 3, 4, 5]

left = 0
right = len(a) - 1

while left < right:
    a[left], a[right] = a[right], a[left]
    left += 1
    right -= 1

print("Reversed array:", a)
