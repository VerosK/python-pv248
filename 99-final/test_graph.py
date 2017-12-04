
import pytest
import requests
from copy import copy

BASE_URL = 'http://localhost:5000'

SMALL_GRAPH = dict(
    rooms=["A","B","C","D","E",'F', 'X'],
    corridors= [ ["A","B"], ["E","B"], ["B","C"], ["C","E"] ]
    )

VALID_DATA = [
    (SMALL_GRAPH, 'A', 'E', 3),
    (SMALL_GRAPH, 'E', 'A', 3),
    (SMALL_GRAPH, 'A', 'A', 1),
    (SMALL_GRAPH, 'A', 'B', 2),
    (SMALL_GRAPH, 'X', 'X', 1),
]


NO_PATH = [
    (SMALL_GRAPH, 'A', 'X'),
]


@pytest.mark.parametrize('graph,start,end,expected_len', VALID_DATA)
def test_valid_graphs(graph,start,end,expected_len):
    graph_data = copy(graph)
    graph_data['start'] = start
    graph_data['end'] = end
    print("Request", graph_data)
    response = requests.post(BASE_URL, json=graph_data)
    assert response.status_code == 200
    answer = response.json()
    print("Response", answer)
    assert type(answer) is dict
    assert type(answer['solution']) in [list,tuple]
    assert len(answer['solution']) == expected_len


@pytest.mark.parametrize('graph,start,end', NO_PATH)
def test_nonexistent_path(graph, start, end):
    graph_data = copy(graph)
    graph_data['start'] = start
    graph_data['end'] = end
    print("Request", graph_data)
    response = requests.post(BASE_URL, json=graph_data)
    assert response.status_code == 200
    answer = response.json()
    print("Response", answer)
    assert type(answer) is dict
    assert answer['solution'] is None


INVALID_DATA = [
    dict(rooms=["A", "B"],  corridors=[["A", "B"], ["X", "X"]],
         start='A', end='C'),
    dict(rooms=["A", "A"], corridors=[],
         start='A', end='A'),
    dict(rooms=["A", "B"], corridors=[],
         start='A', end='X'),
    dict(rooms=["A", "B"], corridors=[],
         start='X', end='A'),
]

@pytest.mark.parametrize('graph,', INVALID_DATA)
def test_invalid_graph(graph):
    print("Request", graph)
    response = requests.post(BASE_URL, json=graph)
    assert response.status_code == 200
    answer = response.json()
    print("Response", answer)
    assert type(answer) is dict
    assert 'error' in answer
    assert answer['solution'] is None
