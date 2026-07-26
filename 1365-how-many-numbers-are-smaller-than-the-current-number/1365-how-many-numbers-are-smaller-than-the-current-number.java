class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) {
        int[] sortedNums=nums.clone();
        Arrays.sort(sortedNums);
        Map<Integer,Integer> rank = new HashMap();
        for(int i=0;i<sortedNums.length;i++){
            int num=sortedNums[i];
            if (!rank.containsKey(num)){
                rank.put(num,i);
            }
        }
        int[] result= new int[nums.length];
        for(int i=0;i<nums.length;i++){
            result[i]=rank.get(nums[i]);
        }
        return result;
    }
}