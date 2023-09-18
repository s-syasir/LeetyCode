import java.util.HashMap;
import java.util.Map;

public class TwoSum {
    public static void main(String[] args){
        Solution runTwoSum = new Solution();
        int[] testInput = {1,3,2,0};
        int[] solution = runTwoSum.twoSum(testInput, 2);
        System.out.println("Indexes of solution are: " + solution[0] + " and " + solution[1]);
    }
    // Static is placed in data section (neither Heap nor Stack)
    // Static means that the method can be run by the
}