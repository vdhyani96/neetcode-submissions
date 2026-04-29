class Solution:

    def encode(self, strs: List[str]) -> str:
        output = []
        for word in strs:
            length = str(len(word))
            output.append(length + ":" + word)
        final = "".join(output)
        print(final)
        return final

    def decode(self, s: str) -> List[str]:
        i = 0
        output = []
        while i < len(s):
            j = i
            length = []
            while s[j] != ':':
                length.append(s[j])
                j += 1
            length = int("".join(length))
            print(length)
            word = s[j+1:(j+1)+length]
            output.append(word)
            i = j + 1 + length
        return output