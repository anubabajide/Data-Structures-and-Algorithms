class TrieNode:
    def __init__(self):
        self.children=[None]*26
        self.endofword=False
        self.word=''
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.seen=set()
    
    def _charToIndex(self, ch):
        return ord(ch)-ord('a')
    
    def insert(self, key):
        pCrawl = self.root
        for level in range(len(key)):
            index=self._charToIndex(key[level])
            if not pCrawl.children[index]:
                pCrawl.children[index]=TrieNode()
            pCrawl=pCrawl.children[index]
        pCrawl.endofword=True
        pCrawl.word=key
        
    def search(self,i,j,board,rows,columns,pCrawl):
        index=self._charToIndex(board[i][j])

        if not 0<=index<=26:
            return
        if not pCrawl.children[index]: 
            return 
        if pCrawl.children[index] and pCrawl.children[index].endofword:
            self.seen.add(pCrawl.children[index].word)
            pCrawl.children[index].endofword=False
        
        char=board[i][j]
        board[i][j]='#'
        for ni,nj in self.getneighbors(i,j,rows,columns):
            self.search(ni,nj,board,rows,columns,pCrawl.children[index])
        board[i][j]=char
        
    def getneighbors(self,i,j,rows,columns):
        neighbors=[]
        if i>0:
            neighbors.append([i-1,j])
        if j>0:
            neighbors.append([i,j-1])
        if i<rows-1:
            neighbors.append([i+1,j])
        if j<columns-1:
            neighbors.append([i,j+1])
        return neighbors
    
class Solution: 
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows=len(board)
        columns=len(board[0])
        T=Trie()
        
        for word in words:
            T.insert(word)
            
        for i in range(rows):
            for j in range(columns):
                T.search(i,j,board,rows,columns,T.root)
        return(T.seen)
                  
