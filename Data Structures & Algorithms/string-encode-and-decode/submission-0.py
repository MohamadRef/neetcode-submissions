class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""  #just an empty output
        for s in strs:  #iterating through the array
            output += str(len(s))+ '#' + s  # we add the length of the word + the ' # ' + the word,  " 4#neet"
        return output

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0;
        while i < len(s):  #while 0 < len tb3 s
            j = i # we make them to be the same position of each other in the iteration, like a left and right pointers
            while s[j] != '#': # we increment it by 1 until we reach the j being '#'
                j+=1
            length = int(s[i:j]) # and then we store the length of the word here in length, our first word will be 4
            i = j + 1  #then we make the i start at the first letter of the word(which is after the #)
            j = i + length # and the j will be at the end of the word which is a number
            res.append(s[i:j]) # we add it in the array
            i = j #back to start the loop over again with the same steps
        return res 