#!/usr/bin/env python3
#coding:utf-8
import pandas as pd
import pprint
df = pd.read_csv('data/long.csv')
pprint.pprint(df.to_json(orient='records'))