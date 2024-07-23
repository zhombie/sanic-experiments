from sanic_ext import CountedRequest

__all__ = ['APIRequest']


class APIRequest(CountedRequest):

    def to_dict(self):
        return {
            'i': str(self.id),
            'm': self.method,
            'u': self.url,
            'c': self.count,

            # 'h': {k: v for k, v in self.headers.items()},
            # 'a': self.args,
            # 'j': self.json,
            # 'f': self.form
        }
