// [658. 找到 K 个最接近的元素](https://leetcode-cn.com/problems/find-k-closest-elements/)
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        int left = 0, right = arr.size() - k;
        while(left < right){
            int mid = left + (right - left) / 2;
            if(x - arr[mid] > arr[mid + k] - x)
                left = mid + 1;
            else
                right = mid;
        }

        return vector<int>(arr.begin() + left, arr.begin() + left + k);
    }
};
 
int main(int argc, char** argv)
{
    Solution s;
    // test1
    vector<int> arr{1,2,3,4,5};
    int k = 4, x = 3;

    // // test2
    // vector<int> arr{1,2,3,4,5};
    // int k = 4, x = -1;
    vector<int> res = s.findClosestElements(arr, k, x);
    for(auto i : res) cout << i << " ";
}
