import math
import typing


class Convertor:
    regex = ""

    def convert(self, value: str) -> typing.Any:
        raise NotImplementedError()  # pragma: no cover

    def to_string(self, value: typing.Any) -> str:
        raise NotImplementedError()  # pragma: no cover


class StringConvertor(Convertor):
    regex = "[^/]+"

    def convert(self, value: str) -> typing.Any:
        return value

    def to_string(self, value: typing.Any) -> str:
        value = str(value)
        if "/" in value:
            raise AssertionError("May not contain path separators")
        assert value, "Must not be empty"
        return value


class PathConvertor(Convertor):
    regex = ".*"

    def convert(self, value: str) -> typing.Any:
        return str(value)

    def to_string(self, value: typing.Any) -> str:
        return str(value)


class IntegerConvertor(Convertor):
    regex = "[0-9]+"

    def convert(self, value: str) -> typing.Any:
        return int(value)

    def to_string(self, value: typing.Any) -> str:
        value = int(value)
        if value < 0:
            raise AssertionError("Negative integers are not supported")
        return str(value)


class FloatConvertor(Convertor):
    regex = "[0-9]+(.[0-9]+)?"

    def convert(self, value: str) -> typing.Any:
        return float(value)

    def to_string(self, value: typing.Any) -> str:
        value = float(value)
        if value < 0.0:
            raise AssertionError("Negative floats are not supported")
        if math.isnan(value):
            raise AssertionError("NaN values are not supported")
        if math.isinf(value):
            raise AssertionError("Infinite values are not supported")
        return ("%0.20f" % value).rstrip("0").rstrip(".")


CONVERTOR_TYPES = {
    "str": StringConvertor(),
    "path": PathConvertor(),
    "int": IntegerConvertor(),
    "float": FloatConvertor(),
}
