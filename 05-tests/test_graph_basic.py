
import pytest
from graph import Graph, GraphException


@pytest.fixture()
def empty_graph():
    g = Graph()
    return g

@pytest.fixture(params=[0,10,20])
def graph(request):
    g = Graph()
    for i in range(request.param):
        g.add_node('node-{}'.format(i))
    return g

def test_empty_graph(empty_graph):
    print(empty_graph)
    assert empty_graph.node_count() == 0

def test_node_insert(graph):
    old_node_count = graph.node_count()
    graph.add_node('a')
    graph.add_node('b')
    graph.add_node(42)
    new_node_count = graph.node_count()
    assert new_node_count - old_node_count == 3

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
