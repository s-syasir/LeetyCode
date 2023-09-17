class TwoSum {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> retVal = {0,0};
        map<int, int> store;
        for (int i = 0; i < nums.size(); i++) {
            if (!store.count(nums[i])) {
                store[nums[i]] = i;
            }
            int diff = target - nums[i];
            if (store.count(diff) && store[diff] != i){
                retVal[0] = store.at(diff);
                retVal[1] = i;
                break;
            }
        }
        return retVal;
    }
};