#!/usr/bin/env python3
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
import os

LISTEN = os.environ.get("LISTEN", "0.0.0.0")
PORT = int(os.environ.get("PORT", "8000"))


class HTTPRequestHandler(BaseHTTPRequestHandler):
    """
    https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler
    """

    request_count_get = 0
    request_count_post = 0

    def do_GET(self):
        """
        Handle all GET requests.
        """
        HTTPRequestHandler.request_count_get = (
            HTTPRequestHandler.request_count_get + 1
        )

        text = ""
        text = self._handle_health_check(text)
        text = self._handle_metrics_request(text)
        # text = _handle_foo()
        text = self._check_path_is_valid(text)

        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(str.encode(text))

    def _handle_health_check(self, text):
        if self.path == "/" or self.path == "/health":
            self.send_response(200)
            text = "OK"
        return text

    def _handle_metrics_request(self, text):
        if self.path == "/metrics":
            self.send_response(200)
            metric = "http_request_handler_count"
            help = "# HELP %s request count" % metric
            type = "# TYPE %s counter" % metric
            text = '%s\n%s\n%s{method="get"} %s\n%s{method="post"} %s\n' % (
                help,
                type,
                metric,
                HTTPRequestHandler.request_count_get,
                metric,
                HTTPRequestHandler.request_count_post,
            )
        return text

    # def _handle_foo(self, text):
    #     if self.path == "/foo":
    #         self.send_response(200)
    #         text = "OK"
    #     return text

    def _check_path_is_valid(self, text):
        if text is None:
            self.send_response(404)
            text = "NOT FOUND"
        return text


if __name__ == "__main__":
    # httpd = HTTPServer((LISTEN, PORT), HTTPRequestHandler)
    httpd = ThreadingHTTPServer((LISTEN, PORT), HTTPRequestHandler)
    print("Serving POST requests on %s:%s" % (LISTEN, PORT))
    httpd.serve_forever()