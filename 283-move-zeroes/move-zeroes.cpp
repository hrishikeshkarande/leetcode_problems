class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int slow = 0;

        //First pass: move non-zero elements forward
        for(int fast = 0; fast < nums.size(); fast++){
            if(nums[fast] != 0){
                nums[slow] = nums[fast];
                slow++;
            }
        }

        //Second pass: fill the rest of the array with zeros
        for(int i = slow; i < nums.size(); i++){
            nums[i] = 0;
        }


        
    }
};