class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        new=[]
        sum = 0
        new.append(sum)
        for i in range(len(gain)):
            sum+=gain[i]
            new.append(sum)
        return max(new)


# Or we can also use a variable for storing the greater variable.
