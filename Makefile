.PHONY: bench test report createdb

build:
	virtualenv --no-site-packages --distribute .
	bin/pip install funkload
	bin/pip install gunicorn

test:
	bin/fl-run-test loadtest.py

bench:
	bin/fl-run-bench loadtest.py Bench.test_simple

report:
	bin/fl-build-report --html -o html simple-bench.xml
