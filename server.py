import sys
import time
import tempfile
import os


def app(environ, start_response):
    start = time.time()
    try:
        status = '200 OK'
        headers = [('Content-type', 'text/plain')]
        start_response(status, headers)

        # doing I/O and CPU bound things for a realistic
        # bench
        #for i in range(1000000):
        #    10 * 10000000 * 10000

        fd, file = tempfile.mkstemp()
        os.close(fd)
        try:
            with open(file, 'w') as f:
                for i in range(10000):
                    f.write(str(i))

            time.sleep(0.01)
        finally:
            os.remove(file)
    finally:
        ret = ["%.4f" % (time.time() - start)]
    return ret


def main():
    from m2wsgi.io.eventlet import WSGIHandler
    handler = WSGIHandler(app, "ipc:///tmp/send")
    handler.serve()


if __name__ == '__main__':
    main()
