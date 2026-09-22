class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        make_heap(nums.begin(), nums.end());
        int res;
        while(k){
            res = nums.front();
            pop_heap(nums.begin(), nums.end());
            
            nums.pop_back();
            
            k--;

        }
        return res;
    }
};
