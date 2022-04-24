'''
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''

#First version
def addy_matchy_1(k, nums):
    for num in nums:
        if k - num in nums:
            return True
    
    return False


k = 17
nums = [10, 15, 3, 7]
print(addy_matchy_1(k, nums))

#Second version, use a dictionary as a hashmap to check instead to take advantage of space time
def addy_matchy_2(k, nums):
    comp = {}
    for i in range(len(nums)):
        num = nums[i]
        if k - num in comp:
            return True
        else:
            comp[num] = i

    return False

print(addy_matchy_2(k, nums))