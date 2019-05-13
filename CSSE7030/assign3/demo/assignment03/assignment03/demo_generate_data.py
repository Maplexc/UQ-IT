#!/usr/bin/env python3
# coding:utf-8
import pandas as pd
import pprint
import time
import random
import faker
from controller import generate_quick_and_long_question_queue_container
datas = zip(['leslie', 'binbin', 'wongzhibin'],
            [time.time() for _ in range(3)], ['hello', 'world', 'now'])


def generate_initial_data(question_examples, n_count=10):
    return zip([faker.Faker().name() for _ in range(n_count)],
               random.choices(question_examples, k=n_count),
               random.choices([True, False], k=n_count),
               random.choices([True, False], k=n_count),
               [time.time() - random.randint(0, 500) for _ in range(n_count)])


quick, long = generate_quick_and_long_question_queue_container()
columns = ['name', 'question', 'requesting', 'accepted', 'time']
df_quick = pd.DataFrame([{
    'name': name,
    'question': question,
    'requesting': requesting,
    'accepted': accepted,
    'time': timestamp,
} for name, question, requesting, accepted, timestamp in generate_initial_data(
    quick.examples, n_count=5)])
df_long = pd.DataFrame([{
    'name': name,
    'question': question,
    'requesting': requesting,
    'accepted': accepted,
    'time': timestamp,
} for name, question, requesting, accepted, timestamp in generate_initial_data(
    long.examples, n_count=5)])
df_quick.to_csv('data/quick.csv', index=False, columns=columns)
df_long.to_csv('data/long.csv', index=False, columns=columns)
