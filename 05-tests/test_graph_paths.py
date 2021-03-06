
import pytest
from graph import Graph, GraphException

GRAPH_SINGLE = 'A>B'
GRAPH_LINE = 'A>B B>C C>D D>E'
GRAPH_CIRCLE = 'A>B B>C C>D D>E E>F F>A'
GRAPH_CIRCLES = 'A>B B>A C>D D>C'
GRAPH_TRAP = 'A>B B>A B>C B>F'


TEST_PATHS = [
    # graph,    from,   to,  expected
    #                        (true, false, None=exception)
    [GRAPH_SINGLE, 'A', 'A', False],
    [GRAPH_SINGLE, 'A', 'B', True],
    [GRAPH_SINGLE, 'B', 'A', False],
    [GRAPH_SINGLE, 'B', 'A', False],
    [GRAPH_SINGLE, 'A', 'C', None],

    [GRAPH_LINE, 'A', 'A', False],
    [GRAPH_LINE, 'A', 'B', True],
    [GRAPH_LINE, 'A', 'E', True],
    [GRAPH_LINE, 'B', 'A', False],

    [GRAPH_CIRCLE, 'A', 'A', True],
    [GRAPH_CIRCLE, 'A', 'E', True],
    [GRAPH_CIRCLE, 'B', 'G', None],

    [GRAPH_CIRCLES, 'A', 'B', True],
    [GRAPH_CIRCLES, 'B', 'A', True],
    [GRAPH_CIRCLES, 'A', 'C', False],
    [GRAPH_CIRCLES, 'A', 'E', None],
]

def graph_from_string(description):
    "create graph from string"
    g = Graph()
    for part in description.split():
        if '>' not in part:
            if g not in g.nodes():
                g.add_node(g)
        else:
            node_from,node_to = part.split('>')
            if node_from not in g.nodes():
                g.add_node(node_from)
            if node_to not in g.nodes():
                g.add_node(node_to)
            g.add_edge(node_from, node_to)
    return g


def test_graph_from_string():
    g = graph_from_string('A>B C>D')
    assert g.node_count() == 4
    assert g.has_edge('A', 'B') == True
    assert g.has_edge('D', 'C') == False

@pytest.mark.parametrize("description,node_from,node_to,expected", TEST_PATHS)
def test_path(description, node_from, node_to, expected):
    g = graph_from_string(description)
    if expected is None:
        with pytest.raises(GraphException):
            g.has_path(node_from,node_to)
    else:
        has_path = g.has_path(node_from,node_to)
        assert has_path == expected
