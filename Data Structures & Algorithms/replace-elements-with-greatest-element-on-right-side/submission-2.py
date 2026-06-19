class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        

        n = len(arr)
        ans = [0] * n 
        for i in range(n - 1, -1, -1):
            if i == n - 1:
                max = -1
            elif arr[i+1] > max:
                max = arr[i+1]
            ans[i] = max
        return ans