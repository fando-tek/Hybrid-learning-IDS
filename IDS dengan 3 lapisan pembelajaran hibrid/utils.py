import uuid
from itertools import islice, zip_longest

import numpy

def grouper(iterable, n, max_groups=0, fillvalue=None):
    """Kumpulan data ke dalam blok dengan panjang tetap"""

    if max_groups > 0:
        iterable = islice(iterable, max_groups * n)

    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)

def random_string():
    return uuid.uuid4().hex[:6].upper().replace("0", "X").replace("O", "Y")

def get_statistics(alist: list):
    """Untuk mendapatkan informasi statistik dari list"""
    iat = dict()

    if len(alist) > 1:
        iat["total"] = sum(alist)
        iat["max"] = max(alist)
        iat["min"] = min(alist)
        iat["mean"] = numpy.mean(alist,dtype=numpy.float64)
        iat["std"] = numpy.sqrt(numpy.var(alist, dtype=numpy.float64))
        #iat["mean"] = numpy.mean(alist)
        #iat["std"] = numpy.sqrt(numpy.var(alist))
    else:
        iat["total"] = 0
        iat["max"] = 0
        iat["min"] = 0
        iat["mean"] = 0
        iat["std"] = 0

    return iat
