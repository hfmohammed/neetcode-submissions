class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        from collections import deque
                
        words = set(wordList)
        if endWord not in words:
            return 0

        forward = {beginWord}
        backward = {endWord}
        visited = {beginWord, endWord}

        count = 2
        while forward and backward:
            if len(forward) > len(backward):
                forward, backward = backward, forward

            next_level = set()
            
            for node in forward:
                for i in range(len(node)):
                    for c in range(26):
                        neighbor = node[:i] + chr(ord("a") + c) + node[i+1:]
                        if neighbor in backward:
                            return count

                        if neighbor not in visited and neighbor in words:
                            visited.add(neighbor)
                            next_level.add(neighbor)
            
            forward = next_level
            count += 1

        return 0

