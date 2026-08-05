class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        count = len(strs)
        seen = {}

        for i in range(count):
          
            sort_key = "".join(sorted(strs[i]))
            if sort_key in seen:
                seen[sort_key].append(strs[i])
            else:
                seen[sort_key] = [strs[i]]

        return list(seen.values())