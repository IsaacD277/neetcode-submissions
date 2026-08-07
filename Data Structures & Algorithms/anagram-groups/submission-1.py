class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}
        for index, item in enumerate(strs):
            words.setdefault("".join(sorted(item)), []).append(item)
        output = []
        for key in words:
            output.append(words[key])
        return output
