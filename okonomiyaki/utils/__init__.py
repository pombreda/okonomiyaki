from __future__ import absolute_import

__all__ = ["ZipFile", "compute_md5", "parse_assignments"]

import hashlib

import six

from .misc import parse_assignments
from ._compat import ZipFile


def compute_md5(path):
    """Compute the md5 checksum of the given path.

    Avoids reading the whole file in RAM, and computes the md5 in chunks.

    Parameters
    ----------
    path: str or file object
        If a string, assumed to be the path to the file to be checksumed. If a
        file object, checksum will start at the current file position.
    """
    block_size = 256 * 1024
    m = hashlib.md5()

    def _compute_checksum(fp):
        while True:
            data = fp.read(block_size)
            m.update(data)
            if len(data) < block_size:
                break
        return m.hexdigest()

    if isinstance(path, six.string_types):
        with open(path, "rb") as fp:
            return _compute_checksum(fp)
    else:
        return _compute_checksum(path)
