class Solution(object):
    def stringIndices(self, wordsContainer, wordsQuery):
        class TrieNode:
            def __init__(self):
                self.children = {}
                self.best = None

        root = TrieNode()

        def insert(word, idx):
            cur = root
            cur.best = pick_best(cur.best, idx, word)
            for c in reversed(word):     
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
                cur.best = pick_best(cur.best, idx, word)

        def pick_best(current_best, idx, word):
            if current_best is None:
                return idx
            cur_word = wordsContainer[current_best]
            if (len(word), idx) < (len(cur_word), current_best):
                return idx
            return current_best

        for i, word in enumerate(wordsContainer):
            insert(word, i)

        ans = []
        for query in wordsQuery:
            cur = root
            best = cur.best
            for c in reversed(query):
                if c not in cur.children:
                    break
                cur = cur.children[c]
                best = cur.best 
            ans.append(best)

        return ans