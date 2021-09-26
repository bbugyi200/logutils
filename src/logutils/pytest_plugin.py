"""A pytest plugin for testing the logutils package.

This plugin can be enabled via the `pytest_plugins` conftest.py variable.

Examples:
    # tests/conftest.py
    pytest_plugins = ["logutils.pytest_plugin"]
"""

from pytest import fixture
from pytest_mock.plugin import MockerFixture


@fixture
def mock_dynamic_log_fields(mocker: MockerFixture) -> None:
    """Mock dynamic fields that may be contained in log records."""
    mocker.patch("logutils.api.getpid", return_value=12345)

    frameinfo = mocker.MagicMock()
    setattr(frameinfo, "function", "fake_function")
    setattr(frameinfo, "lineno", "123")
    mocker.patch(
        "logutils.api.getframeinfo",
        return_value=frameinfo,
    )

    mod = mocker.MagicMock()
    setattr(mod, "__name__", "fake_module")
    mocker.patch("logutils.api.getmodule", return_value=mod)
