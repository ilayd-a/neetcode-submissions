class Solution {
public:
    int climbStairs(int n) {
        vector<int>stairs;
        if (n<=2){
            return n;}
        stairs.push_back(1);
        stairs.push_back(2);
        for(int i = 2; i<n; i++){
            stairs.push_back(stairs[i-1]+stairs[i-2]);
        }
        return stairs[n-1];
    }
};

