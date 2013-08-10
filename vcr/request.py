class Request(object):

    def __init__(self, host, port, method, path, body, headers):
        self.host = host
        self.port = port
        self.method = method
        self.path = path
        self.body = body
        self.headers = frozenset(headers.items())

    @property
    def url(self):
        return self.host + self.path

    def __key(self):
        return (self.host, self.port, self.method, self.path, self.body, self.headers)

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __str__(self):
        return "<Request ({0}) {1}>".format(self.method, self.body)
