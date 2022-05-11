# !interpreter [optional-arg]
# -*- coding: utf-8 -*-

"""
This contains sample code on REDIS load test with locust using python.
It has following operations for Redis data-types: String,List,Set,Hash,Sorted Set
"""

# Built-in/Generic Imports
import json
import random
import time
import redis
from locust import User, events, task, tag
import datetime

__author__ = "Manoj Singh"


host_name = "localhost"
port_no = 6379

class RedisClient(object):
    def __init__(self, host=host_name, port=port_no):
        self.rc = redis.StrictRedis(host=host, port=port)

    def get_query_string(self, key, command='GET'):
        result = None
        start_time = time.time()
        try:
            result = self.rc.get(key)
            if not result:
                result = ''
        except Exception as e:
            total_time = int((time.time() - start_time) * 1000)
            events.request_failure.fire(request_type=command, name=key, response_time=total_time, exception=e)
        else:
            total_time = int((time.time() - start_time) * 1000)
            length = len(str(result))
            events.request_success.fire(request_type=command, name=key, response_time=total_time,
                                        response_length=length)
        return result

    def set_query_string(self, key, command='SET'):
        result = None
        bid_price = random.randint(47238, 57238)
        redis_response = {'bids': bid_price}
        start_time = time.time()
        try:
            result = self.rc.set(key, json.dumps(redis_response))
            if not result:
                result = ''
        except Exception as e:
            total_time = int((time.time() - start_time) * 1000)
            events.request_failure.fire(request_type=command, name=key, response_time=total_time, exception=e)
        else:
            total_time = int((time.time() - start_time) * 1000)
            length = len(str(result))
            events.request_success.fire(request_type=command, name=key, response_time=total_time,
                                        response_length=length)
        return result

    def lpush_in_list(self, key, command='LPUSH'):
        result = None
        start_time = time.time()
        try:
            result = self.rc.lpush(key, 0, 0, 0, 0, 0)
            if not result:
                result = ''
        except Exception as e:
            total_time = int((time.time() - start_time) * 1000)
            events.request_failure.fire(request_type=command, name=key, response_time=total_time, exception=e)
        else:
            total_time = int((time.time() - start_time) * 1000)
            length = result.bit_length()
            events.request_success.fire(request_type=command, name=key, response_time=total_time,
                                        response_length=length)
        return result

    def sadd_in_set(self, key, command='SADD'):
        result = None
        visitors = {"dan", "jon", "alex"}
        start_time = time.time()
        try:
            result = self.rc.sadd(key, *visitors)
            if not result:
                result = ''
        except Exception as e:
            total_time = int((time.time() - start_time) * 1000)
            events.request_failure.fire(request_type=command, name=key, response_time=total_time, exception=e)
        else:
            total_time = int((time.time() - start_time) * 1000)
            length = len(str(result))
            events.request_success.fire(request_type=command, name=key, response_time=total_time,
                                        response_length=length)
        return result

    def hset_in_hash(self, key, command='HSET'):
        result = None
        start_time = time.time()
        try:
            result = self.rc.hset(key, "1", "One")
            if not result:
                result = ''
        except Exception as e:
            total_time = int((time.time() - start_time) * 1000)
            events.request_failure.fire(request_type=command, name=key, response_time=total_time, exception=e)
        else:
            total_time = int((time.time() - start_time) * 1000)
            length = len(str(result))
            events.request_success.fire(request_type=command, name=key, response_time=total_time,
                                        response_length=length)
        return result

    def hget_in_hash(self, key, command='HGET'):
        result = None
        start_time = time.time()
        try:
            result = self.rc.hget(key, "1")
            if not result:
                result = ''
        except Exception as e:
            total_time = int((time.time() - start_time) * 1000)
            events.request_failure.fire(request_type=command, name=key, response_time=total_time, exception=e)
        else:
            total_time = int((time.time() - start_time) * 1000)
            length = len(str(result))
            events.request_success.fire(request_type=command, name=key, response_time=total_time,
                                        response_length=length)
        return result

    def hdel_in_hash(self, key, command='HDEL'):
        result = None
        start_time = time.time()
        try:
            result = self.rc.hdel(key, "1")
            if not result:
                result = ''
        except Exception as e:
            total_time = int((time.time() - start_time) * 1000)
            events.request_failure.fire(request_type=command, name=key, response_time=total_time, exception=e)
        else:
            total_time = int((time.time() - start_time) * 1000)
            length = len(str(result))
            events.request_success.fire(request_type=command, name=key, response_time=total_time,
                                        response_length=length)
        return result

    def zadd_in_sorted_set(self, key, command='ZADD'):
        result = None
        playerName = "Player1"
        score = 56
        start_time = time.time()
        try:
            result = self.rc.zadd(key, {playerName: score}, nx=False)
            if not result:
                result = ''
        except Exception as e:
            total_time = int((time.time() - start_time) * 1000)
            events.request_failure.fire(request_type=command, name=key, response_time=total_time, exception=e)
        else:
            total_time = int((time.time() - start_time) * 1000)
            length = len(result.encode())
            events.request_success.fire(request_type=command, name=key, response_time=total_time,
                                        response_length=length)
        return result

    def zrange_in_sorted_set(self, key, command='ZRANGE'):
        result = None
        start_time = time.time()
        try:
            result = self.rc.zrange(key, 0, -1)
            if not result:
                result = ''
        except Exception as e:
            total_time = int((time.time() - start_time) * 1000)
            events.request_failure.fire(request_type=command, name=key, response_time=total_time, exception=e)
        else:
            total_time = int((time.time() - start_time) * 1000)
            length = len(str(result))
            events.request_success.fire(request_type=command, name=key, response_time=total_time,
                                        response_length=length)
        return result


class RedisLocust(User):
    def __init__(self, *args, **kwargs):
        super(RedisLocust, self).__init__(*args, **kwargs)
        self.client = RedisClient()

    @task
    @tag("string")
    def string_operations(self):
        self.client.set_query_string("string_set_operation")
        self.client.get_query_string("string_get_operation")

    @task
    @tag("list")
    def list_operation(self):
        self.client.lpush_in_list("list_lpush_operation")

    @task
    @tag("set")
    def set_operation(self):
        self.client.sadd_in_set("set_sadd_operation")

    @task
    @tag("hash")
    def hash_operation(self):
        self.client.hset_in_hash("hash_hset_operation")
        self.client.hget_in_hash("hash_hget_operation")
        self.client.hdel_in_hash("hash_hdel_operation")

    @task
    @tag("sorted-set")
    def sorted_set_operation(self):
        self.client.zadd_in_sorted_set("sorted_set_zadd_operation")
        self.client.zrange_in_sorted_set("sorted_set_zrange_operation")
