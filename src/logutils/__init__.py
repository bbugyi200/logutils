"""logutils

Better logging made easy with support for structlog and the standard logging
module.
"""

__author__ = "Bryan M Bugyi"
__email__ = "bryanbugyi34@gmail.com"
__version__ = "0.1.4"


from logutils.api import (
    BetterBoundLogger,
    Log,
    LogFormat,
    Logger,
    LogLevel,
    get_default_logfile,
    init_logging,
)
