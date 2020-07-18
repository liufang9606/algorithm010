class Solution:
    #三数之和 = 0
    def threeSum(self, nums: [int]) -> [[int]]:
        #先将数组排序，排序完成后，从左边开始进行循环遍历数组
        nums.sort()
        res, k = [], 0#
        for k in range(len(nums) - 2):
            if nums[k] > 0: break # 如果最小的数，那么等式明显不成立
            if k > 0 and nums[k] == nums[k - 1]: continue # 2. 跳过相同的 `nums[k]`.
            i, j = k + 1, len(nums) - 1#3. i 从k+1开始； j从数组最后边开始
            while i < j: # 4. 不断开始第二层循环，知道i，j相会
                s = nums[k] + nums[i] + nums[j]
                if s < 0:#5. 将 i 右移一位
                    i += 1
                    while i < j and nums[i] == nums[i - 1]: i += 1#跳过相同的num[i]
                elif s > 0:#6. 将 j 左移一位
                    j -= 1
                    while i < j and nums[j] == nums[j + 1]: j -= 1#跳过相同的num[j]
                else:
                    res.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]: i += 1
                    while i < j and nums[j] == nums[j + 1]: j -= 1
        return res



class Solution:
    #接雨水
    def trap(self, height: List[int]) -> int:
        leftmax, rightmax, res = 0, 0, 0
        for i in range(len(height)):
            leftmax = max(leftmax, height[i])   #将左边的最高点求出，得到左边的面积
            rightmax = max(rightmax, height[-1-i]) #将右边的最高点求出，得到右边的面积
            res += leftmax + rightmax - height[i]
        return res - leftmax * len(height)#去除掉多余的矩形面积即可得最后的面积