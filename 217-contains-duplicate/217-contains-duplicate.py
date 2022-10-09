class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        countList = [elements for elements, _ in Counter(nums).items()]
        return not(len(countList) == len(nums))