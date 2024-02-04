//class Solution {
//public:
//    int maxLengthBetweenEqualCharacters(string s) {
//        vector<int> firstIndex(26, -1);
//        int ans = -1;
//        for (int i = 0; i < s.size(); i++) {
//            if (firstIndex[s[i] - 'a'] < 0) {
//                firstIndex[s[i] - 'a'] = i;
//            }
//            else {
//                ans = max(ans, i - firstIndex[s[i] - 'a'] - 1);
//            }
//        }
//        return ans;
//    }
//};