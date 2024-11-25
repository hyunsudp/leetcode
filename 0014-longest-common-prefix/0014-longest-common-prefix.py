class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:  # 리스트가 비어있으면 빈 문자열 반환
            return ""
        
        first_word = strs[0]  # 첫 번째 단어를 기준으로 사용

        for i in range(len(first_word)):
            for word in strs[1:]:  # 나머지 단어들과 비교
                if i >= len(word) or word[i] != first_word[i]:
                    return first_word[:i]  # 불일치가 발생한 위치까지의 접두사 반환
        
        return first_word  # 불일치가 없으면 첫 번째 단어 전체 반환
