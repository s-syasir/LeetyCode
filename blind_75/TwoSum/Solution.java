
import java.util.HashMap;
import java.util.Map;

public class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> storage = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int diff = target - nums[i];
            if (storage.containsKey(diff)) {
                return new int [] {storage.get(diff), i};
            }
            storage.put(nums[i], i);
        }
        return nums;
    }
}