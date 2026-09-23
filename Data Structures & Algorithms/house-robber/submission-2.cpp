class Solution {
public:
    vector<int>memo;

    int dfs(int i, vector<int>&nums){
        if(i>=nums.size()){
            return 0;
        }
        if(memo[i]!=-1){
            return memo[i];
        }
        memo[i] = max(dfs(i+1, nums), nums[i]+dfs(i+2, nums));
        return memo[i];
        }
    int rob(vector<int>& nums) {
        memo.resize(nums.size(),-1);
        return dfs(0, nums);
    }
};
