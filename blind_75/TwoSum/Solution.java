import java.util.Map;
import java.util.HashMap;


public class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] retVal = {1,0};
        Map<Integer, Integer> storage = new HashMap<>();
        for (int i = 0; i < nums.length; i++){
            if (!storage.containsKey(nums[i])) {
                storage.put(nums[i], i);
            }
            int diff = target - nums[i];
            if (storage.containsKey(diff) && storage.get(diff) != i) {
                retVal[0] = storage.get(diff);
                retVal[1] = i;
                break;
            }
        }
        return retVal;
    }
}