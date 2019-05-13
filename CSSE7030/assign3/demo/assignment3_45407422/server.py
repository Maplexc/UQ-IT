#!/usr/bin/env python3
# coding:utf-8

from tornado import web, ioloop, gen, httpclient, httpserver
import pandas as pd
import json
from back_end import BackEndManager


class SubmitHandler(web.RequestHandler):
    """
    Handler for client to submit question
    name[str]:student name
    content[str]:question content
    question_type[str]: quick or long
    """
    def post(self):
        name = self.get_body_argument(name='name')
        content = self.get_body_argument(name='content')
        question_type = self.get_body_argument(name='question_type')
        result = self.application.backend.submit_question(
            name=name, type=question_type, question_content=content)
        self.write(result)


class DataHandler(web.RequestHandler):
    """
    Handler for client to obtain active students in the question queue
    question_type[str]:quick or long
    """
    def get(self):
        question_type = self.get_query_argument(name='question_type')
        data_from_backend = self.application.backend.get_active_data(
            type=question_type)
        data_from_backend['status'] = 'OK'
        self.write(json.dumps(data_from_backend))


class CancelHandler(web.RequestHandler):
    """
    Handler for client to cancel question request
    question_type[str]: quick or long
    name['str']: the name of the student
    """
    def post(self):
        question_type = self.get_body_argument(name='question_type')
        name = self.get_body_argument(name='name')
        result = self.application.backend.cancel_question(
            name=name, question_type=question_type)
        self.write(json.dumps(result))


class StatisticsHandler(web.RequestHandler):
    """
    Handler for client to get historical statistics information
    about
    mean waiting time,
    median wating time,
    mode waiting time
    and top 10 students who have requestion for the most questions
    question_type[str]: quick or long
    """
    def get(self):
        question_type = self.get_query_argument('question_type')
        data_from_backend = self.application.backend.get_statistics_summary(
            question_type)
        data_from_backend['status'] = "OK"
        self.write(json.dumps(data_from_backend))


class AcceptHandler(web.RequestHandler):
    """
    Handler to mark the request from some student as accepted
    question_type[str]:quick or long
    name[str]: the name of the student
    """
    def post(self):
        question_type = self.get_body_argument(name='question_type')
        name = self.get_body_argument(name='name')
        result = self.application.backend.accept_question(
            name=name, question_type=question_type)
        self.write(result)


class Application(web.Application):
    """
    The core component of tornado web framework
    """
    def __init__(self):
        """
        handlers: register the urls that clients would request for
        _backend: to handle the operations on database
        """
        super().__init__(
            handlers=[
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
        """
        :return: instance to handle operations on database
        """
        return self._backend


def main():
    server = httpserver.HTTPServer(Application())
    server.listen(8080)
    ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
