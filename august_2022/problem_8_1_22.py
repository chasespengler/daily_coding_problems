'''
Given a list of integers and a number K, return which 
contiguous elements of the list sum to K.

For example, if the list is [1, 2, 3, 4, 5] and K is 9, 
then it should return [2, 3, 4], since 2 + 3 + 4 = 9.
'''
z = [1,2,3,5]

def contig(nums, K):
    nums.sort()
    for i in range(len(nums)):
        start = nums[i]
        print("Start: ", start)
        sum = start
        contigs = [start]
        if sum == K:
            return contigs
        elif sum > K:
            return []
        for z in range(i+1, len(nums)):
            print(nums[z])
            sum += nums[z]
            contigs.append(nums[z])
            if sum == K:
                return contigs
            elif sum > K:
                break

    return []

print(contig(z, 4))