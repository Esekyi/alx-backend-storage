#!/usr/bin/env python3
"""Writing strings to Redis"""
import redis
import uuid
from typing import Union, Callable, Optional


class Cache:
    def __init__(self) -> None:
        """Store an instance of the Redis client."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the input data in Redis with a random key and return the key.

        Parameters:
        data (Union[str, bytes, int, float]): The data to be stored, which
        can be of type str, bytes, int, or float.

        Returns:
        str: The key under which the data is stored.
"""
        key: str = str(uuid.uuid4())

        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable[[bytes], Union[
            str, int, bytes, float]]] = None) -> Optional[Union[
                str, bytes, int, float, None]]:
        """
        Retrieve the data stored at the input key from redis
        """
        data = self._redis.get(key)

        if data is None:
            return None

        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """Convert bytes to str"""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """Convert bytes to int"""
        return self.get(key, fn=int)
