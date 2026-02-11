E       sqlalchemy.exc.OperationalError: (psycopg2.OperationalError) connection to server at "localhost" (::1), port 5432 failed: Connection refused
E       	Is the server running on that host and accepting TCP/IP connections?
E       connection to server at "localhost" (127.0.0.1), port 5432 failed: Connection refused
E       	Is the server running on that host and accepting TCP/IP connections?
E       
E       (Background on this error at: https://sqlalche.me/e/20/e3q8)

.venv/lib/python3.11/site-packages/psycopg2/__init__.py:122: OperationalError
=========================== short test summary info ============================
FAILED tests/test_events.py::test_create_and_list_events - sqlalchemy.exc.Operati
