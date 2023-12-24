// https://leetcode.com/problems/valid-anagram/


class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }
        int cnts[26] = {0};
        for (int i = 0; i < s.size(); i++) {
            cnts[s[i] - 'a']++;
        }
        for (int i = 0; i < t.size(); i++) {
            cnts[t[i] - 'a']--;
        }
        for (int i = 0; i < 26; i++) {
            if (cnts[i] != 0) {
                return false;
            }
        }
        return true;
    }
};