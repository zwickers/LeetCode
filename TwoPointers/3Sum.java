
// TIME COMPLEXITY: O(n)

//checks if A + B + C == 0
public List<List<Integer>> threeSum(int[] nums) {

    List<List<Integer>> result = new ArrayList<List<Integer>>();
 
    if(nums == null || nums.length<3)
        return result;
 
    Arrays.sort(nums);
 
    for(int i=0; i<nums.length; i++){
        // prevent duplicates by checking if this A is equal to the last A
        if(i==0 || nums[i] > nums[i-1]){
            
            int j=i+1;
            int k=nums.length-1;
 
            while(j<k){
                if(nums[i]+nums[j]+nums[k]==0){
                    List<Integer> l = new ArrayList<Integer>();
                    l.add(nums[i]);
                    l.add(nums[j]);
                    l.add(nums[k]);
                    result.add(l);
 
                    j++;
                    k--;
 
                    // handles duplicate here by making sure either B or C is new, in addition to A being new
                    // because if 2 of the 3 values are the same, then the 3rd must also be the same 
                    // and therefore it is a duplicate
                    while(j<k && nums[j]==nums[j-1])
                        j++;
                    while(j<k && nums[k]==nums[k+1])
                        k--;
 
                }else if(nums[i]+nums[j]+nums[k]<0){
                    j++;
                }else{
                    k--;
                }
            }
        }
 
    }
 
    return result;
}
