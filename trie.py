import json

class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        self.load()

    def insert(self, word: str) -> None:
        cur = self.root
        
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True
        
    def load(self, file: str = 'words_dictionary.json') -> None:
        with open(file, 'r') as f:
            data = json.load(f)
            for word in data:
                self.insert(word)

    def search(self, word: str) -> bool:
        cur = self.root
        
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
    
    def autoComplete(self, prefix: str):
        cur = self.root
        
        if prefix == '':
            return []
        
        for c in prefix:
            if not cur.children.get(c):
                return []
            cur = cur.children[c]
        
        if not cur.children:
            return []
        
        
        rec = list()
        # rec.append(self.autoCompleteHelper(cur, prefix))
        self.autoCompleteHelper(cur, prefix, rec)
        # print(rec)
        return rec[:5] # returning 5 words close to the prefix instead of the entire children list
        
    def autoCompleteHelper(self, node: TrieNode, word, recs: list):
        
        if node.endOfWord:
            # print(word)
            recs.append(word)
        
        for a, n in node.children.items():
            self.autoCompleteHelper(n, word + a, recs)
        