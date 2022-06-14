class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters=[]
        digits=[]
        for log in logs:
            if log[-1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        letters = sorted(letters, key=lambda letter: (letter.split()[1:],letter.split()[0]))
        return letters+digits