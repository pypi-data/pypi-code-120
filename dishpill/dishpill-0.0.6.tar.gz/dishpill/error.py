class Error(Exception):
    pass


# Local errors


class Unregistered(Error):
    """Raised when the user requests an item from the registry that does
    not actually exist.
    """

    pass


class UnregisteredEnv(Unregistered):
    """Raised when the user requests an env from the registry that does
    not actually exist.
    """

    pass


class NamespaceNotFound(UnregisteredEnv):
    """Raised when the user requests an env from the registry where the
    namespace doesn't exist.
    """

    pass


class NameNotFound(UnregisteredEnv):
    """Raised when the user requests an env from the registry where the
    name doesn't exist.
    """

    pass


class VersionNotFound(UnregisteredEnv):
    """Raised when the user requests an env from the registry where the
    version doesn't exist.
    """

    pass


class UnregisteredBenchmark(Unregistered):
    """Raised when the user requests an env from the registry that does
    not actually exist.
    """

    pass


class DeprecatedEnv(Error):
    """Raised when the user requests an env from the registry with an
    older version number than the latest env with the same name.
    """

    pass


class RegistrationError(Error):
    """Raised when the user attempts to register an invalid env.
    For example, an unversioned env when a versioned env exists.
    """

    pass


class UnseedableEnv(Error):
    """Raised when the user tries to seed an env that does not support
    seeding.
    """

    pass


class DependencyNotInstalled(Error):
    pass


class UnsupportedMode(Exception):
    """Raised when the user requests a rendering mode not supported by the
    environment.
    """

    pass


class ResetNeeded(Exception):
    """When the monitor is active, raised when the user tries to step an
    environment that's already done.
    """

    pass


class ResetNotAllowed(Exception):
    """When the monitor is active, raised when the user tries to step an
    environment that's not yet done.
    """

    pass


class InvalidAction(Exception):
    """Raised when the user performs an action not contained within the
    action space
    """

    pass


# API errors


class APIError(Error):
    def __init__(
        self,
        message=None,
        http_body=None,
        http_status=None,
        json_body=None,
        headers=None,
    ):
        super().__init__(message)

        if http_body and hasattr(http_body, "decode"):
            try:
                http_body = http_body.decode("utf-8")
            except Exception:
                http_body = "<Could not decode body as utf-8.>"

        self._message = message
        self.http_body = http_body
        self.http_status = http_status
        self.json_body = json_body
        self.headers = headers or {}
        self.request_id = self.headers.get("request-id", None)

    def __unicode__(self):
        if self.request_id is not None:
            msg = self._message or "<empty message>"
            return f"Request {self.request_id}: {msg}"
        else:
            return self._message

    def __str__(self):
        try:  # Python 2
            return unicode(self).encode("utf-8")
        except NameError:  # Python 3
            return self.__unicode__()


class APIConnectionError(APIError):
    pass


class InvalidRequestError(APIError):
    def __init__(
        self,
        message,
        param,
        http_body=None,
        http_status=None,
        json_body=None,
        headers=None,
    ):
        super().__init__(message, http_body, http_status, json_body, headers)
        self.param = param


class AuthenticationError(APIError):
    pass


class RateLimitError(APIError):
    pass


# Video errors


class VideoRecorderError(Error):
    pass


class InvalidFrame(Error):
    pass


# Wrapper errors


class DoubleWrapperError(Error):
    pass


class WrapAfterConfigureError(Error):
    pass


class RetriesExceededError(Error):
    pass


# Vectorized environments errors


class AlreadyPendingCallError(Exception):
    """
    Raised when `reset`, or `step` is called asynchronously (e.g. with
    `reset_async`, or `step_async` respectively), and `reset_async`, or
    `step_async` (respectively) is called again (without a complete call to
    `reset_wait`, or `step_wait` respectively).
    """

    def __init__(self, message, name):
        super().__init__(message)
        self.name = name


class NoAsyncCallError(Exception):
    """
    Raised when an asynchronous `reset`, or `step` is not running, but
    `reset_wait`, or `step_wait` (respectively) is called.
    """

    def __init__(self, message, name):
        super().__init__(message)
        self.name = name


class ClosedEnvironmentError(Exception):
    """
    Trying to call `reset`, or `step`, while the environment is closed.
    """

    pass


class CustomSpaceError(Exception):
    """
    The space is a custom dishpill.Space instance, and is not supported by
    `AsyncVectorEnv` with `shared_memory=True`.
    """

    pass
