# Testing patterns module
from Singleton import Singleton


def test_singleton():
    singleton_object1 = Singleton()
    singleton_object2 = Singleton()
    singleton_object1.test_me()
    singleton_object2.test_me()


if __name__ == "__main__":
    test_singleton()
