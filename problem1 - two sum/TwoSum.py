class TwoSum(object):
    #this is O(n) solution
    def twoSum2(self, nums, target):
        numDict = {}
        for index in range(0,len(nums)):
            diff = target - nums[index]
            if diff in numDict and numDict[diff]!=index:
                return [numDict[target - nums[index]], index]
            else:
                numDict[nums[index]] = index

    # this is O(n^2) solution
    def twoSum1(nums, target):
        for i in range(0,len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

            
if __name__ == "__main__":
    temp = TwoSum()

    print(temp.twoSum2([2,7,11,15],9))
    print(temp.twoSum2([3,2,4],6))
    print(temp.twoSum2([3,3],6))
