
import pytest
from graph import Graph, GraphException

@pytest.fixture()
def graph():
    return Graph()

def test_empty_graph(graph):
    assert graph.node_count() == 0

def test_node_insert(graph):
    graph.add_node('a')
    graph.add_node('b')
    graph.add_node(42)
    assert graph.node_count() == 3

def test_node_duplicate_insert(graph):
    graph.add_node('single')
    graph.add_node('duplicate')
    with pytest.raises(GraphException):
        graph.add_node('duplicate')

def test_edge_insert(graph):
    graph.add_node('A')
    graph.add_node('B')
    graph.add_edge('A', 'B')


def test_edge_invalid(graph):
    graph.add_node('A')
    with pytest.raises(GraphException):
        graph.add_edge('A', 'missing')

def test_edge_insert_duplicate(graph):
    for i in ['A', 'B', 'C']:
        graph.add_node(i)
    graph.add_edge('A', 'B')
    graph.add_edge('B', 'C')
    with pytest.raises(GraphException):
        graph.add_edge('A', 'B')

def test_edge_is_stored(graph):
    for i in ['A', 'B', 'C']:
        graph.add_node(i)
    graph.add_edge('A', 'B')
    graph.add_edge('B', 'C')
    assert graph.has_edge('A', 'B') == True
    assert graph.has_edge('B', 'C') == True
    assert graph.has_edge('B', 'A') == False
