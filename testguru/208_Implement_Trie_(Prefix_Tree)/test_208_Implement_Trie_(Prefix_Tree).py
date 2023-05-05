import pytest


@pytest.fixture
def trie():
    return Trie()


def test_trie_node_creation():
    node = TrieNode()
    assert node.links == [None] * 26
    assert node.isEnd == False


def test_trie_insert(trie):
    trie.insert("hello")
    assert trie.search("hello") == True
    assert trie.search("world") == False


def test_trie_searchPrefix(trie):
    trie.insert("hello")
    node = trie.searchPrefix("h")
    assert node is not None
    assert node.get("e") is not None


def test_trie_search(trie):
    trie.insert("hello")
    assert trie.search("hello") == True
    assert trie.search("world") == False


def test_trie_starts_with(trie):
    trie.insert("hello")
    assert trie.startsWith("he") == True
    assert trie.startsWith("w") == False