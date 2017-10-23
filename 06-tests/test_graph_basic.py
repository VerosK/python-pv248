
import pytest
from graph import Graph, GraphException

def test_empty_graph():
    g = Graph()
    assert g.node_count() == 0

def test_node_insert():
    g = Graph()
    g.add_node('a')
    g.add_node('b')
    g.add_node(42)
    assert g.node_count() == 3

def test_node_duplicate_insert():
    g = Graph()
    g.add_node('single')
    g.add_node('duplicate')
    with pytest.raises(GraphException):
        g.add_node('duplicate')

def test_edge_insert():
    g = Graph()
    g.add_node('A')
    g.add_node('B')
    g.add_edge('A', 'B')


def test_edge_invalid():
    g = Graph()
    g.add_node('A')
    with pytest.raises(GraphException):
        g.add_edge('A', 'missing')

def test_edge_insert_duplicate():
    g = Graph()
    for i in ['A', 'B', 'C']:
        g.add_node(i)
    g.add_edge('A', 'B')
    g.add_edge('B', 'C')
    with pytest.raises(GraphException):
        g.add_edge('A', 'B')

def test_edge_is_stored():
    g = Graph()
    for i in ['A', 'B', 'C']:
        g.add_node(i)
    g.add_edge('A', 'B')
    g.add_edge('B', 'C')
    assert g.has_edge('A', 'B') == True
    assert g.has_edge('B', 'C') == True
    assert g.has_edge('B', 'A') == False
