//class Solution {
//public:
//    int lengthOfLongestSubstring(string s) {
//        unordered_map<char, int> hash;
//        int ans = 0;
//        int left = 0;
//        int i;
//        for (i = 0; i < s.length(); ++i)
//        {
//            char cur = s[i];
//            if (hash.count(cur)) {
//                ans = max(ans, i - left);
//                left = max(left, hash[cur] + 1);
//
//            }
//            hash[cur] = i;
//        }
//        return max(ans, i - left);
//    }
//};