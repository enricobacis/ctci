from linkedlist import Node

def test_node():
    tail = Node(2)
    head = Node(1, tail)

    assert head.value == 1
    assert head.next == tail
    assert tail.value == 2
    assert tail.next == None

def test_linkedlist():
    lst = list(range(10))
    head = Node.from_iterable(lst)
    assert head.to_list() == lst
