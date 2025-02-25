

nums = [1, 3, 4, 2, 2]

count_nums = {}
for i in range(len(nums)):
    count_nums[nums[i]] = 0 

print(count_nums)

for i in range(len(nums)):
    count_nums[nums[i]] += 1
print(count_nums)

for i, (key, value) in enumerate(count_nums.items()):

    if value == 2:
        print(i)