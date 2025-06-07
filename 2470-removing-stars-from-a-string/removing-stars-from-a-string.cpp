class Solution {
public:
    string removeStars(string s) {
    // Step 1: Initialize an empty string to store the result
        string result;
    
    // Step 2: Loop through each character in the input string
    // Range-based for loop: Less typing, more readable, no index management.
    //✅ Here, ch takes on each character in the string s automatically.
    //✅ It’s very concise and commonly used in modern C++ (C++11 and later).
        for(char ch : s){
            // Step 3a: If the current character is not '*', add it to the result
            if (ch != '*'){
                result.push_back(ch);
            }
            // Step 3b: If the current character is '*', remove the last character
            else{
                result.pop_back();
            }
        }
    // Step 4: Return the final string after processing all characters
        return result;   
    }
};

/*
        // Traditional for loop
        for (int i = 0; i < s.size(); ++i) {
            char ch = s[i];
            if (ch != '*') {
                result.push_back(ch);
            } else {
                result.pop_back();
            }
        }
*/