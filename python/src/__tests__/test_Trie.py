from src.Trie import Trie


def test_Trie():
    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple") == True
    assert trie.search("app") == False
    assert trie.startsWith("app") == True
    trie.insert("app")
    assert trie.search("app") == True
