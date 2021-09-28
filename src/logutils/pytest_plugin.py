"""A pytest plugin for testing the logutils package.

This plugin can be enabled via the `pytest_plugins` conftest.py variable.

Examples:
    The following line should be found in the "tests/conftest.py" file:

    >>> pytest_plugins = ["logutils.pytest_plugin"]
"""

from pytest import fixture
from pytest_mock.plugin import MockerFixture


@fixture
def mock_dynamic_log_fields(mocker: MockerFixture) -> None:
    """Mock dynamic fields that may be contained in log records."""
    mocker.patch("logutils.logutils.getpid", return_value=12345)

    frameinfo = mocker.MagicMock()
    setattr(frameinfo, "function", "fake_function")
    setattr(frameinfo, "lineno", "123")
    mocker.patch(
        "logutils.logutils.getframeinfo",
        return_value=frameinfo,
    )

    mod = mocker.MagicMock()
    setattr(mod, "__name__", "fake_module")
    mocker.patch("logutils.logutils.getmodule", return_value=mod)
