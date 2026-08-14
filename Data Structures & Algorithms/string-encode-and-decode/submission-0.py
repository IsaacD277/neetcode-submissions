import re

class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for i in strs:
            output += f"#{len(i)}#{i}"
        print(output)
        return output

    def decode(self, s: str) -> List[str]:
        decoded = re.split("[#]\\d+[#]", s)
        print(decoded[1:])
        return decoded[1:]