class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        string = ""
        arr = []
        s = s.strip()
        for i in range(len(s)):
            if s[i] != ' ':
                string += s[i]
            else:
                arr.append(string)
                string = "" 
                
        if string:
            arr.append(string)            

        return len(arr[-1]) if arr else 0