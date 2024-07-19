def mySqrt(x):
    if x < 2:
        return x
    left, right = 2, x // 2
    while left <= right:
        mid = (left + right) // 2
        num = mid * mid
        if num == x:
            return mid
        elif num > x:
            right = mid - 1
        else:
            left = mid + 1
    return right

x = 8
print(mySqrt(x))
