#!/usr/bin/env python3
#coding:utf-8
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import time
import json
import pprint
import statsmodels
import helper


class BackEndManager:
    def __init__(self):
        self._engine = create_engine('sqlite:///data/question.db')
        self._connection = self._engine.connect()

    def get_active_data(self, type='quick'):
        column_name = 'current_{}_id'.format(type)
        active_students = pd.read_sql(
            'select S.name,count(*)-1 as question_count from Student S, Question Q where {} is not null and Q.owner_id=S.rowid and not (Q.accepted=0 and Q.close_time is not null) group by S.name, S.rowid'.
            format(column_name),
            con=self._engine)
        time_series = pd.read_sql(
            'select S.name, Q.submit_time as timestamp from Student S, Question Q where S.{} = Q.rowid'.
            format(column_name),
            con=self._engine)
        merged_data = active_students.merge(time_series)
        records = json.loads(merged_data.to_json(orient='records'))
        return {
            'records': records,
            'avg_time': merged_data.timestamp.mean(),
            'count': merged_data.shape[0],
        }

    def get_statistics_summary(self, question_type='quick'):
        df = pd.read_sql(
            sql=
            'select count(*) as total, S.name from Student S, Question Q where Q.owner_id=S.rowid and Q.type=(?) group by S.name order by count(*) desc',
            params=(question_type, ),
            con=self._engine,
        )
        ranks = json.loads(df.iloc[:10].to_json(orient='records'))
        df_question = pd.read_sql_table(
            table_name='Question', con=self._engine)
        df_question = df_question.loc[(df_question.accepted == 1)
                                      & (df_question.type == question_type)]
        df_question.fillna(0, inplace=True)
        if df_question.shape[0] == 0:
            return {
                'ranks': 'Empty',
                'mean': 'Empty',
                'median': 'Empty',
                'mode': 'Empty',
            }
        waiting_time = df_question.close_time - df_question.submit_time
        print(waiting_time)
        result = {
            'ranks': ranks,
            'mean': helper.display_time(waiting_time.mean()),
            'median': helper.display_time(waiting_time.median()),
            'mode':
            waiting_time.apply(lambda w: helper.display_time(w)).mode()[0],
        }
        return result

    def execute_pure_update_sql(self, sql, params=()):
        print('in execute_pure_update_sql...')
        try:
            self._connection.execute(sql, params)
        except Exception as e:
            print(e)
            return {'status': 'ERROR', 'error': str(e)}
        return {'status': 'OK'}

    def execute_pure_query_sql(self, sql, params=()):
        try:
            result = self._connection.execute(sql, params)
            return [r for r in result]
        except Exception as e:
            return e

    def cancel_question(self, name, question_type):
        active_column_name = 'current_{}_id'.format(question_type)
        sql_question = 'update Question set accepted=0 where rowid = (select {} from Student where name like (?))'.format(
            active_column_name)
        sql_student = 'update Student set {}=-1 where name like (?)'.format(
            active_column_name)
        question_result = self.execute_pure_update_sql(sql_question, (name, ))
        if question_result['status'] == 'OK':
            return json.dumps(
                self.execute_pure_update_sql(sql_student, (name, )))
        else:
            return json.dumps(question_result)

    def accept_question(self, name, question_type):
        active_column_name = 'current_{}_id'.format(question_type)
        sql_question = 'update Question set close_time = (?), accepted=1 where rowid = (select {} from Student where name like (?))'.format(
            active_column_name)
        sql_student = 'update Student set {}=-1 where name like (?)'.format(
            active_column_name)
        question_result = self.execute_pure_update_sql(sql_question,
                                                       (time.time(), name))
        if question_result['status'] == 'OK':
            return json.dumps(
                self.execute_pure_update_sql(sql_student, (name, )))
        else:
            return json.dumps(question_result)

    def submit_question(self, type, name, question_content):
        sql_insert_name = 'insert into Student (name) select (?) where not exists (select * from Student where name = (?))'
        sql_select_last_insert_rowid = 'select last_insert_rowid()'
        sql_select_student_rowid = 'select rowid from Student where name = (?)'
        sql_question = 'insert into Question (owner_id, type, content, submit_time, accepted) values ((?), (?), (?), (?), (?))'
        if type == 'quick':
            sql_update = 'update Student set current_quick_id=(?) where name = (?)'
        else:
            sql_update = 'update Student set current_long_id=(?) where name = (?)'
        student_result = self.execute_pure_update_sql(
            sql=sql_insert_name, params=(name, name))
        if 'error' in student_result:
            return student_result
        owner_id = self.execute_pure_query_sql(
            sql=sql_select_student_rowid, params=(name, ))[0][0]
        print(owner_id)
        question_result = self.execute_pure_update_sql(
            sql_question,
            params=(owner_id, type, question_content, time.time(), 0))
        if 'error' in question_result:
            return question_result
        question_id = self.execute_pure_query_sql(
            sql_select_last_insert_rowid)[0][0]
        print(question_id)
        return self.execute_pure_update_sql(
            sql_update, params=(question_id, name))
