def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0

    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        new_arr = []
        copiedArr = list(nums)
        for i in range(len(nums)):
            smallest = findSmallest(copiedArr)
            new_arr.append(copiedArr.pop(smallest))
        return new_arr