# test_fixtures.py
import pytest

# Fixture with the default scope (function)
@pytest.fixture
def setup_function():
    print("\nSetup for function")
    yield
    print("\nTeardown for function")

# Fixture with class scope
@pytest.fixture(scope="class")
def setup_class():
    print("\nSetup for class")
    yield
    print("\nTeardown for class")

# Fixture with module scope
@pytest.fixture(scope="module")
def setup_module():
    print("\nSetup for module")
    yield
    print("\nTeardown for module")

# Fixture with session scope
@pytest.fixture(scope="session")
def setup_session():
    print("\nSetup for session")
    yield
    print("\nTeardown for session")

# test_fixtures.py
def test_function_1(setup_function):
    print("Executing test_function_1")
    assert 2 + 3 == 5

def test_function_2(setup_function):
    print("Executing test_function_2")
    assert 10 % 3 == 1

class TestClass:
    def test_class_1(self, setup_class):
        print("Executing test_class_1")
        assert "pytest" == "pytest"

    def test_class_2(self, setup_class):
        print("Executing test_class_2")
        assert len([1, 2, 3]) == 3

