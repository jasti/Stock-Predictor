"""
Simple Twitter streaming API access
"""
__version__ = "1.1.1"
__author__ = "Rune Halvorsen <runefh@gmail.com>"
__homepage__ = "http://bitbucket.org/runeh/tweetstream/"
__docformat__ = "restructuredtext"


"""
 .. data:: USER_AGENT

     The default user agent string for stream objects
"""

USER_AGENT = "TweetStream %s" % __version__


class TweetStreamError(Exception):
    """Base class for all tweetstream errors"""
    pass


class AuthenticationError(TweetStreamError):
    """Exception raised if the username/password is not accepted"""
    pass


class ConnectionError(TweetStreamError):
    """Raised when there are network problems. This means when there are
    dns errors, network errors, twitter issues"""

    def __init__(self, reason, details=None):
        self.reason = reason
        self.details = details

    def __str__(self):
        return '<ConnectionError %s>' % self.reason


from .streamclasses import SampleStream, FilterStream
from .deprecated import FollowStream, TrackStream, LocationStream, TweetStream, ReconnectingTweetStream
