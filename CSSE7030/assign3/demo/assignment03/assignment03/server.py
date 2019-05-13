#!/usr/bin/env python3
# coding:utf-8

from tornado import web, ioloop, gen, httpclient, httpserver
import time
import datetime as dt
import pandas as pd
import json
from back_end import BackEndManager


class LongQueueDataHandler(web.RequestHandler):
    def get(self):
        json_data = pd.read_csv('data/long.csv').to_json(orient='records')
        self.write(json_data)


class QuickQueueDataHandler(web.RequestHandler):
    def get(self):
        json_data = pd.read_csv('data/quick.csv').to_json(orient='records')
        self.write(json_data)


class SubmitHandler(web.RequestHandler):
    def post(self):
        name = self.get_body_argument(name='name')
        content = self.get_body_argument(name='content')
        question_type = self.get_body_argument(name='question_type')
        result = self.application.backend.submit_question(
            name=name, type=question_type, question_content=content)
        self.write(result)


class DataHandler(web.RequestHandler):
    def get(self):
        question_type = self.get_query_argument(name='question_type')
        data_from_backend = self.application.backend.get_active_data(
            type=question_type)
        data_from_backend['status'] = 'OK'
        self.write(json.dumps(data_from_backend))


class CancelHandler(web.RequestHandler):
    def post(self):
        question_type = self.get_body_argument(name='question_type')
        name = self.get_body_argument(name='name')
        result = self.application.backend.cancel_question(
            name=name, question_type=question_type)
        self.write(result)


class StatisticsHandler(web.RequestHandler):
    def get(self):
        question_type = self.get_query_argument('question_type')
        data_from_backend = self.application.backend.get_statistics_summary(
            question_type)
        data_from_backend['status'] = "OK"
        self.write(json.dumps(data_from_backend))


class AcceptHandler(web.RequestHandler):
    def post(self):
        question_type = self.get_body_argument(name='question_type')
        name = self.get_body_argument(name='name')
        result = self.application.backend.accept_question(
            name=name, question_type=question_type)
        self.write(result)


class TestingDataHandler(web.RequestHandler):
    def get(self):
        self.write(pd.read_csv('data/testing.csv').to_json(orient='records'))


class Application(web.Application):
    def __init__(self):
        super().__init__(
            handlers=[
                ('/long', LongQueueDataHandler),
                ('/short', QuickQueueDataHandler),
                ('/testing', TestingDataHandler),
                ('/submit', SubmitHandler),
                ('/data', DataHandler),
                ('/cancel', CancelHandler),
                ('/accept', AcceptHandler),
                ('/statistics', StatisticsHandler),
            ],
            default_host='0.0.0.0',
            template_path='templates',
            debug=True)
        self._backend = BackEndManager()

    @property
    def backend(self):
        return self._backend


def main():
    server = httpserver.HTTPServer(Application())
    server.listen(8888)
    ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
