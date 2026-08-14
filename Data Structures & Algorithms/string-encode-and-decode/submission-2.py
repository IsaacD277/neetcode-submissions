import re

class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for i in strs:
            output += f"#{len(i)}#{i}"
        return output

    def decode(self, s: str) -> List[str]:
        decoded = re.split("[#]\\d+[#]", s)
        return decoded[1:]