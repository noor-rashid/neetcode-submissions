class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #if the len of two lists are not equal, cannot be anagrams
        #then for each list, if anagrams, put them in the same     nested list

        groups = {}

        for w in strs:
            key = "".join(sorted(w))        # change ONLY this line
            if key not in groups:
                groups[key] = []
            groups[key].append(w)

        return list(groups.values())