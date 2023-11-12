class Solution {
public:
    int lengthOfLastWord(string s) {
        string::iterator endWord,startWord;

        endWord = s.end() - 1;

        while(*endWord == ' ')
            endWord--;

        startWord = endWord;

        while(startWord != s.begin() - 1 && *startWord != ' ')
            startWord--;

        return std::distance(startWord,endWord);
    }
};
