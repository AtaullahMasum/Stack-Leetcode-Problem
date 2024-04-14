# Solution 1
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])
        left = [0] * n
        right = [n] * n
        height = [0] * n
        max_area = 0

        for i in range(m):
            cur_left, cur_right = 0, n
            # Update height
            for j in range(n):
                if matrix[i][j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0
            # Update left
            for j in range(n):
                if matrix[i][j] == '1':
                    left[j] = max(left[j], cur_left)
                else:
                    left[j] = 0
                    cur_left = j + 1
            # Update right
            for j in range(n - 1, -1, -1):
                if matrix[i][j] == '1':
                    right[j] = min(right[j], cur_right)
                else:
                    right[j] = n
                    cur_right = j
            # Update area
            for j in range(n):
                max_area = max(max_area, (right[j] - left[j]) * height[j])

        return max_area
# Solution 2 
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
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n , m = len(matrix), len(matrix[0])
        maxArea = 0
        heights = [0]*m
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            area = self.largestRectangleArea( heights)
            maxArea = max(maxArea, area)
        return maxArea
# solution 3
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
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n , m = len(matrix), len(matrix[0])
        maxArea = 0
        heights = [0]*m
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            area = self.largestRectangleArea( heights)
            maxArea = max(maxArea, area)
        return maxArea
            
