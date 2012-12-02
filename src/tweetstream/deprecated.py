from .streamclasses import FilterStream, SampleStream

class DeprecatedStream(FilterStream):
    def __init__(self, *args, **kwargs):
        import warnings
        warnings.warn("%s is deprecated. Use FilterStream instead" % self.__class__.__name__, DeprecationWarning)
        super(DeprecatedStream, self).__init__(*args, **kwargs)


class FollowStream(DeprecatedStream):
    def __init__(self, username, password, follow, catchup=None, url=None):
        super(FollowStream, self).__init__(username, password, follow=follow, catchup=catchup, url=url)


class TrackStream(DeprecatedStream):
    def __init__(self, username, password, track, catchup=None, url=None, slow=False):
        super(TrackStream, self).__init__(username, password, track=track, catchup=catchup, url=url)


class LocationStream(DeprecatedStream):
    def __init__(self, username, password, locations, catchup=None, url=None, slow=False):
        super(LocationStream, self).__init__(username, password, locations=locations, catchup=catchup, url=url)


class TweetStream(SampleStream):
    def __init__(self, *args, **kwargs):
        import warnings
        warnings.warn("%s is deprecated. Use SampleStream instead" % self.__class__.__name__, DeprecationWarning)
        SampleStream.__init__(self, *args, **kwargs)


class ReconnectingTweetStream(TweetStream):
    """TweetStream class that automatically tries to reconnect if the
    connecting goes down. Reconnecting, and waiting for reconnecting, is
    blocking.

    :param username: See :TweetStream:

    :param password: See :TweetStream:

    :keyword url: See :TweetStream:

    :keyword reconnects: Number of reconnects before a ConnectionError is
        raised. Default is 3

    :error_cb: Optional callable that will be called just before trying to
        reconnect. The callback will be called with a single argument, the
        exception that caused the reconnect attempt. Default is None

    :retry_wait: Time to wait before reconnecting in seconds. Default is 5

    """

    def __init__(self, username, password, url="sample",
                 reconnects=3, error_cb=None, retry_wait=5):
        self.max_reconnects = reconnects
        self.retry_wait = retry_wait
        self._reconnects = 0
        self._error_cb = error_cb
        TweetStream.__init__(self, username, password, url=url)

    def next(self):
        while True:
            try:
                return TweetStream.next(self)
            except ConnectionError, e:
                self._reconnects += 1
                if self._reconnects > self.max_reconnects:
                    raise ConnectionError("Too many retries")

                # Note: error_cb is not called on the last error since we
                # raise a ConnectionError instead
                if  callable(self._error_cb):
                    self._error_cb(e)

                time.sleep(self.retry_wait)
        # Don't listen to auth error, since we can't reasonably reconnect
        # when we get one.



