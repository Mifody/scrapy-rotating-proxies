

class BaseProxiesStorage(object):
    """
    Expiring proxies container.

    A proxy can be in 3 states:

    * good;
    * dead;
    * unchecked.

    Initially, all proxies are in 'unchecked' state.
    When a request using scrapera proxy is successful, this proxy moves to 'good'
    state. When a request using a proxy fails, proxy moves to 'dead' state.

    For crawling only 'good' and 'unchecked' proxies are used.

    'Dead' proxies move to 'unchecked' after a timeout (they are called
    'reanimated'). This timeout increases exponentially after each
    unsuccessful attempt to use a proxy.
    """

    def __init__(self, proxy_list, backoff=None, crawler=None):
        raise NotImplementedError

    def get_random(self):
        """ Return a random available proxy (either good or unchecked) """
        raise NotImplementedError

    def get_proxy(self, proxy_address):
        """
        Return complete proxy name associated with a hostport of a given
        ``proxy_address``. If ``proxy_address`` is unknown or empty,
        return None.
        """
        raise NotImplementedError

    def mark_dead(self, proxy, _time=None):
        """ Mark a proxy as dead """
        raise NotImplementedError

    def mark_good(self, proxy):
        """ Mark a proxy as good """
        raise NotImplementedError

    def reanimate(self, _time=None):
        """ Move dead proxies to unchecked if a backoff timeout passes """
        raise NotImplementedError

    def reset(self):
        """ Mark all dead proxies as unchecked """
        raise NotImplementedError

    def add(self, proxy):
        """ Add a proxy to the proxy list """
        raise NotImplementedError

    def remove(self, proxy):
        """
        Permanently remove a proxy. The proxy cannot be recovered, except
        if 'add()' is called.
        """
        raise NotImplementedError


    @property
    def mean_backoff_time(self):
        raise NotImplementedError

    @property
    def reanimated(self):
        raise NotImplementedError

    def __str__(self):
        return  "Base proxy storage class"
