"""
Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
Therefore, in real life, we would likely start a new stack when the previous
stack exceeds some threshold. Implement a data structure SetOfStacks that mimics
this. SetOfStacks should be composed of several stacks and should create.
SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single
stack (that is, pop() should return the same values as it would if there were
just a single stack).
"""


class SetOfStacks(object):

    def __init__(self, threshold):
        self._stacks = list()
        self._threshold = threshold

    def push(self, value):
        if not self._stacks or len(self._stacks[-1]) >= self._threshold:
            self._stacks.append(list())
        self._stacks[-1].append(value)

    def pop(self):
        while not self._stacks[-1]:
            self._stacks.pop()
        return self._stacks[-1].pop()

    def popAt(self, index):
        return self._stacks[index].pop()


def test_stack_of_plates():
    sos = SetOfStacks(threshold=2)      # create a SetOfStacks with threshold=2
    input = list(range(10))             # insert numbers 0..9
    for x in input: sos.push(x)
    assert len(sos._stacks) == 5        # they should be splitted into 5 stacks

    output = []                         # pop should behave as normal stack.pop
    while True:
        try: output.append(sos.pop())
        except IndexError: break
    assert input == output[::-1]

    input = list(range(6))              # create a specific input 0..5
    for x in input: sos.push(x)

    assert sos.popAt(0) == 1
    assert sos.popAt(1) == 3
    assert sos.popAt(1) == 2
    assert sos.popAt(2) == 5
    assert sos.pop()    == 4
    assert sos.pop()    == 0
