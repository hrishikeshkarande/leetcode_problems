class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq_map = {}

        for num in arr:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1

        seen = set()

        for count in freq_map.values():
            if count in seen:
                return False
            else:
                seen.add(count)
        
        return True

        