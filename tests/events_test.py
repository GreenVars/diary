import unittest
import datetime as dt
from diary import Event


class TestEvent(unittest.TestCase):
    INFO = "something was logged"
    LEVEL = "CRITICAL"

    def setUp(self):
        self.basicEvent = Event(self.INFO, self.LEVEL)

    def test_has_dt(self):
        event = Event(self.INFO, self.LEVEL)
        self.assertIsNotNone(self.basicEvent.dt)

    def test_takes_arguments(self):
        given_dt = dt.datetime.now()
        formatter = ""
        event = Event(self.INFO, self.LEVEL, given_dt, formatter)
        self.assertEquals(event.dt, given_dt)
        self.assertEquals(event.info, self.INFO)
        self.assertEquals(event.level, self.LEVEL)
        self.assertEquals(event.formatter, formatter)

    def test_func_formatter(self):
        def quick_format(e):
            return "({level})({text})".format(level = e.level,
                                              text = e.info)
        event = Event(self.INFO, self.LEVEL, formatter=quick_format)

        self.assertEquals(event.formatted(), "({level})({text})".format(
            level = event.level, text = event.info))

        self.assertEquals(str(event), "({level})({text})".format(
            level=event.level, text=event.info))

        self.assertIs(event.formatter, quick_format)

        event.info = ""

        self.assertEquals(event.formatted(), "({level})({text})".format(
            level = event.level, text = event.info))

        self.assertEquals(str(event), "({level})({text})".format(
            level=event.level, text=event.info))

    def test_str_formatter(self):
        formatter = "({level})({info})"

        event = Event(self.INFO, self.LEVEL, formatter=formatter)

        self.assertEquals(event.formatted(), "({level})({text})".format(
            level=event.level, text=event.info))

        self.assertEquals(str(event), "({level})({text})".format(
            level=event.level, text=event.info))

        self.assertEquals(event.formatter, formatter)

        event.info = ""

        self.assertEquals(event.formatted(), "({level})({text})".format(
            level=event.level, text=event.info))

        self.assertEquals(str(event), "({level})({text})".format(
            level=event.level, text=event.info))

    def test_bad_formatter(self):
        formatter = 5
        with self.assertRaises(ValueError,
            msg="Could not identify formatter {}".format(formatter)):
            event = Event(self.INFO, self.LEVEL, formatter=formatter)

    def test_no_formatter(self):
        self.assertIsNone(self.basicEvent.formatter)

        with self.assertRaises(AttributeError,
            msg="Event instance has no attribute 'formatted'"):
            self.basicEvent.formatted()

        self.assertEquals(str(self.basicEvent), repr(self.basicEvent))

if __name__ == '__main__':
    unittest.main()
