import heapq

nums = [1, 2, 4, 10]
heapq.heapify(nums)
print(nums)

sum = 0
while len(nums) != 1:
    first = heapq.heappop(nums)
    second = heapq.heappop(nums)
    nums_ = first + second
    print(f"{first}+{second}={nums_}")
    sum += nums_
    heapq.heappush(nums, nums_)
print(f"порядок об'єднання, який мінімізує загальні витрати до {sum}")
