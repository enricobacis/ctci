import inspect

def pytest_generate_tests(metafunc):
    if 'fn' in metafunc.fixturenames:
        members = inspect.getmembers(metafunc.module, inspect.isfunction)
        functions = [fn for name, fn in members
                     if not name.startswith('test')
                     if not name.startswith('_')]
        metafunc.parametrize("fn", functions)
