import os
import unittest


class TestPerformanceOfFileWriting(unittest.TestCase):
    def tearDown(self) -> None:
        try:
            os.remove("delete-me.txt")
        except OSError:
            pass

    # 1sec 27ms
    def test_open(self):
        for _ in range(10_000):
            with open("delete-me.txt", "w") as fp:
                fp.write("a" * 1024)

    # 118ms
    def test_truncate(self):
        with open("delete-me.txt", "w") as fp:
            for _ in range(10_000):
                fp.seek(0, os.SEEK_SET)
                fp.write("a" * 1024)
                fp.truncate()
                fp.flush()
