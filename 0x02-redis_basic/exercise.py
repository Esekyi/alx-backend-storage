#!/usr/bin/env python3
"""Writing strings to Redis"""
import redis
import uuid
from typing import Union


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
