// [34. 在排序数组中查找元素的第一个和最后一个位置](https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/)
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int binary_search(vector<int>& nums, int target) {
        int left = 0, right = nums.size() - 1; 
        while(left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] < target) {
                left = mid + 1;
            } else if (nums[mid] > target) {
                right = mid - 1; 
            } else if(nums[mid] == target) {
                // 直接返回
                return mid;
            }
        }
        // 直接返回
        return -1;
    }

    int left_bound(vector<int>& nums, int target) {
        int left = 0, right = nums.size() - 1;
        // left = right + 1 跳出循环
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] < target) {
                left = mid + 1;
            } else if (nums[mid] > target) {
                right = mid - 1;
            } else if (nums[mid] == target) {
                // 别返回，锁定左侧边界
                right = mid - 1;
            }
        }
        // 最后要检查 left 越界的情况
        if (left >= nums.size() || nums[left] != target) {
            return -1;
        }
        return left;
    }

    // int left_bound2(vector<int>& nums, int target){
    //     int left = 0, right = nums.size();
    //     while(left < right){
    //         int mid = left + (right - left) / 2;
    //         if(nums[mid] > target)
    //             right = mid - 1;
    //         else if(nums[mid] < target)
    //             left = mid + 1;
    //         else if(nums[mid] == target)
    //             right = mid;
    //     }
    //     return left;
    // }

    int right_bound(vector<int>& nums, int target) {
        int left = 0, right = nums.size() - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] < target) {
                left = mid + 1;
            } else if (nums[mid] > target) {
                right = mid - 1;
            } else if (nums[mid] == target) {
                // 别返回，锁定右侧边界
                left = mid + 1;
                // 这样想：mid = left - 1
            }
        }
        // 最后要检查 right 越界的情况
        if (right < 0 || nums[right] != target) {
            return -1;
        }
        return right;
    }

    vector<int> searchRange(vector<int>& nums, int target) {
        if(!nums.size()) return {-1, -1};
        int left = 0, right = nums.size() - 1;

        // left bound
        while(left <= right) {
            // 防止int溢出
            int mid = left + (right - left) / 2;
            if(nums[mid] < target) left = mid + 1;
            else if(nums[mid] >= target)
                right = mid - 1;
        }
        cout << "left: " << left << endl;
        cout << "right: " << right << endl;

        if(nums[left] != target) return {-1, -1};
        int first = left;
        right = nums.size() - 1;
        while(left < right) {
            int mid = left + (right - left) / 2;
            if(nums[mid] <= target) left = mid + 1;
            else if(nums[mid] > target)
                right = mid - 1;
        }
        cout << "right: " << right << endl;
        return {first, right};
    }
};
 
int main(int argc, char** argv)
{
    Solution s;
    // test1
    vector<int> nums{5, 7, 7, 8, 8, 10};
    int target = 8;

 
    // // test2
    // vector<int> nums{5, 7, 7, 8, 8, 10};
    // int target = 6;

    // // test3
    // vector<int> nums{};
    // int target = 0;

    // // test4
    // vector<int> nums{1};
    // int target = 1;

    vector<int> ans = s.searchRange(nums, target);
    for(auto i : ans) cout << i << " ";
}