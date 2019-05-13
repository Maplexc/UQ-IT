#!/usr/bin/env python3
# coding:utf-8
import json
import time
import pandas as pd
from sqlalchemy import create_engine
import helper


class BackEndManager:
    """
    class to provide api to operate on database
    """
    def __init__(self):
        """
        _engine: indicates the type of database
        _connection: indicates it is ok to operate on database
        """
        self._engine = create_engine('sqlite:///data/question.db')
        self._connection = self._engine.connect()

    def get_active_data(self, type='quick'):
        """

        :param type: question type, either quick or long
        :return: dict
        records: list of {name: str, question_count: int, timestamp:double}
        avg_time:double
        count: int
        """
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
        """
        :param question_type: str quick or long
        :return: dict
        ranks list of {total: int, name:str}
        mean: str such as a few minites ago, an hour ago...
        median: str
        mode: str
        the question which is still active not yet accept nor cancel counts in mean, median and mode time summary
        however as for student who asking questions ranks only the question accepted would count
        """
        df = pd.read_sql(
            sql=
            'select count(*) as total, S.name from Student S, Question Q where Q.owner_id=S.rowid and Q.type=(?) and Q.accepted=1 group by S.name order by count(*) desc',
            params=(question_type,),
            con=self._engine,
        )
        ranks = json.loads(df.iloc[:10].to_json(orient='records'))
        df_question = pd.read_sql_table(
            table_name='Question', con=self._engine)
        df_question = df_question.loc[(df_question.type == question_type)]
        df_question.fillna(time.time(), inplace=True)
        if df_question.shape[0] == 0:
            return {
                'ranks': 'Empty',
                'mean': 'Empty',
                'median': 'Empty',
                'mode': 'Empty',
            }
        waiting_time = df_question.close_time - df_question.submit_time
        result = {
            'ranks': ranks,
            'mean': helper.display_time(waiting_time.mean()),
            'median': helper.display_time(waiting_time.median()),
            'mode':
                waiting_time.apply(lambda w: helper.display_time(w)).mode()[0],
        }
        return result

    def execute_pure_update_sql(self, sql, params=()):
        """
        :param sql:  sql to executed
        :param params: placeholder in sql
        :return: dict
        indicates the sql execution succeeded or failed
        """
        try:
            self._connection.execute(sql, params)
        except Exception as e:
            print(e)
            return helper.format_error(status='ERROR', reason=str(e))
        return {'status': 'OK'}

    def execute_pure_query_sql(self, sql, params=()):
        """
        :param sql: the sql to execute
        :param params: the placeholder in sql
        :return: the query result or the exception
        """
        try:
            result = self._connection.execute(sql, params)
            return [r for r in result]
        except Exception as e:
            return e

    def cancel_question(self, name, question_type):
        """
        :param name: student name
        :param question_type: quick or long
        :return: indicates the execution succeeded or failed
        """
        active_column_name = 'current_{}_id'.format(question_type)
        sql_question = 'update Question set accepted=0 where rowid = (select {} from Student where name like (?))'.format(
            active_column_name)
        sql_student = 'update Student set {}=-1 where name like (?)'.format(
            active_column_name)
        question_result = self.execute_pure_update_sql(sql_question, (name,))
        if question_result['status'] == 'OK':
            return self.execute_pure_update_sql(sql_student, (name,))
        else:
            return question_result

    def accept_question(self, name, question_type):
        """
        :param name: student name
        :param question_type: quick or short
        :return: indicates the execution succeeded or failed
        """
        active_column_name = 'current_{}_id'.format(question_type)
        sql_question = 'update Question set close_time = (?), accepted=1 where rowid = (select {} from Student where name like (?))'.format(
            active_column_name)
        sql_student = 'update Student set {}=-1 where name like (?)'.format(
            active_column_name)
        question_result = self.execute_pure_update_sql(sql_question,
                                                       (time.time(), name))
        if question_result['status'] == 'OK':
            return json.dumps(
                self.execute_pure_update_sql(sql_student, (name,)))
        else:
            return json.dumps(question_result)

    def submit_question(self, type, name, question_content):
        """
        :param type: question type quick or long
        :param name: student name
        :param question_content: the question content
        :return: indicates the exection succeeded or failed
        """
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
            sql=sql_select_student_rowid, params=(name,))[0][0]
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
