import os, time, jwt, threading, logging
from flask import Flask, send_file, jsonify
from werkzeug.serving import make_server

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

class Serfary_Server():
    def __init__(self,flag,download_file):
        self.app = Flask(__name__)
        self.app.secret_key = 'BSides_Maine_2026'
        self.server = None
        self.thread = None
        self.stop_event = threading.Event()
        self.download_file = download_file

        self.setup_routes()

    def setup_routes(self):

        @self.app.route('/<file_id>')
        def download_file(file_id):
            return send_file(self.download_file)

    def run(self):
        def run_server():
            self.server = make_server('127.0.0.1', 5000, self.app)
            self.server.serve_forever()
            self.server.shutdown()

        self.thread = threading.Thread(target=run_server)
        self.thread.start()

    def stop(self):
        if self.server:
            self.server.shutdown()
        if self.thread:
            self.thread.join()

if __name__ == '__main__':
    server = Server('secure.zip')
    server.run()
    time.sleep(60)
    server.stop()

