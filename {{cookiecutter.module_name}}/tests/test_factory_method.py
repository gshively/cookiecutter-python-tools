from {{cookiecutter.module_name}} import FactoryMethod


def test_success_construct():
    sut = FactoryMethod.factory_method()
    assert sut is not None
    assert isinstance(sut, FactoryMethod)


def test_success_with_true():
    sut = FactoryMethod.factory_method(True)
    assert sut is not None
    assert isinstance(sut, FactoryMethod)


def test_none_for_false_argument():
    sut = FactoryMethod.factory_method(False)
    assert sut is None
