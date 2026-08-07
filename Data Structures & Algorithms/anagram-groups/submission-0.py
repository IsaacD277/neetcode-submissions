class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}
        for index, item in enumerate(strs):
            words.setdefault("".join(sorted(item)), []).append(index)
        output = []
        for key in words:
            entries = []
            for i in words[key]:
                entries.append(strs[i])
            output.append(entries)
        return output
