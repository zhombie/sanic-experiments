from sanic_ext import CountedRequest

__all__ = ['APIRequest']


class APIRequest(CountedRequest):

    def to_dict(self):
        return {
            'id': str(self.id),
            'method': self.method,
            'url': self.url,
            'headers': {k: v for k, v in self.headers.items()},
            'count': self.count
        }
