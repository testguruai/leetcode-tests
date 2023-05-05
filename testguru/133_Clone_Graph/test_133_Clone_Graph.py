import pytest
from solution import Solution, UndirectedGraphNode

def test_cloneGraph_none():
    s = Solution()
    assert s.cloneGraph(None) == None

def test_cloneGraph_dfs():
    node1 = UndirectedGraphNode(1)
    node2 = UndirectedGraphNode(2)
    node3 = UndirectedGraphNode(3)
    node4 = UndirectedGraphNode(4)
    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]
    s = Solution()
    cloned = s.cloneGraph(node1)
    assert cloned.label == node1.label
    assert len(cloned.neighbors) == len(node1.neighbors)
    assert cloned.neighbors[0].label == node1.neighbors[0].label
    assert len(cloned.neighbors[0].neighbors) == len(node1.neighbors[0].neighbors)
    assert cloned.neighbors[0].neighbors[0].label == node1.neighbors[0].neighbors[0].label

def test_cloneGraph_bfs():
    node1 = UndirectedGraphNode(1)
    node2 = UndirectedGraphNode(2)
    node3 = UndirectedGraphNode(3)
    node4 = UndirectedGraphNode(4)
    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]
    s = Solution()
    cloned = s.cloneGraph(node1)
    assert cloned.label == node1.label
    assert len(cloned.neighbors) == len(node1.neighbors)
    assert cloned.neighbors[0].label == node1.neighbors[0].label
    assert len(cloned.neighbors[0].neighbors) == len(node1.neighbors[0].neighbors)
    assert cloned.neighbors[0].neighbors[0].label == node1.neighbors[0].neighbors[0].label
