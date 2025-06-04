class Solution {
public:
    bool isSubsequence(string s, string t) {
        int slow = 0;

        for(int fast = 0; fast < t.size(); fast++){
            if(t[fast]==s[slow]){
                slow++;
            }
        }
        if(slow == s.size()){
            return true;
        }
        else{
            return false;
        }



        
    }
};