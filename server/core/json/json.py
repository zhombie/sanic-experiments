from typing import Union, Optional, Any

import orjson

from core.db.record import Record


def default(obj) -> Any:
    if isinstance(obj, Record):
        return obj.to_dict()
    return str(obj)


def dumps(obj, decode_codec='utf-8') -> Union[bytes, str]:
    out = orjson.dumps(
        obj,
        option=orjson.OPT_PASSTHROUGH_DATETIME | orjson.OPT_NON_STR_KEYS,
        default=default
    )
    if decode_codec:
        return out.decode(decode_codec)  # str
    return out  # bytes


def loads(obj) -> Optional[dict]:
    if obj:
        if isinstance(obj, bytes) or isinstance(obj, str):
            return orjson.loads(obj)
    return None
