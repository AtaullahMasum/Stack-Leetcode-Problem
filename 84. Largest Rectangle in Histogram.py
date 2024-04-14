# Solution 1
# Time Complexity is O(n)
# Space Complexity is O(n)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        leftsmaller, rightsmaller = [0]*n, [0]*n
        #calculate leftsmaller index 
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if not stack:
                leftsmaller[i] = 0
            else:
                leftsmaller[i] = stack[-1] + 1
            stack.append(i)
        # clear stack to be reused 
        while stack:
            stack.pop()
        #Calculate Rightsamller index
        for i in range(n-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if not stack:
                rightsmaller[i] = n-1
            else:
                rightsmaller[i] = stack[-1] - 1
        # MaxArea replace here so reduce one more iteration
            stack.append(i)
        # Calculate MaxArea in the Histogram
        maxArea = 0
        for i in range(n):
            maxArea = max(maxArea, (rightsmaller[i] - leftsmaller[i] + 1)*heights[i])
        return maxArea
# Solution 2 
# Time Complexity is O(n) + O(n)
# Space Complexity is O(n)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxArea = 0
        stack = []
        for i in range(n+1):
            while stack and (i == n or heights[stack[-1]]>=heights[i]):
                height = heights[stack[-1]]
                stack.pop()
                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1
                maxArea = max(maxArea, height*width)
            stack.append(i)
        return maxArea
                
        