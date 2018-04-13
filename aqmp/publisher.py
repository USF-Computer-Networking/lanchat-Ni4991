#!/usr/bin/env python
""" publisher.py
    
    A small demonstration application that uses AMQP in blocking mode.

    To use, open two console windows - one for publishing and one
    for receiving.
    
    Reference:
      https://www.youtube.com/watch?v=BKDoxM9KOJY
    
    Ni Luo  April 13, 2018
"""

import pika

url = 'amqp://rzbdnysq:al19XcdnQULK3U2xqpox0LlIevEtxKup@otter.rmq.cloudamqp.com/rzbdnysq'
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.basic_publish(exchange = '', routing_key = 'hello', body = 'Hello viewers!')

