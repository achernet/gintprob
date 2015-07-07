import unittest2
import call_logger


class TestCallLogger(unittest2.TestCase):

    def test_call_logging(self):

        @call_logger.logCall()
        def loggedAdd(a, b):
            return a + b

        @call_logger.logCall
        def loggedSub(a, b):
            return a - b

        firstResult = loggedAdd(0, len(self.__dict__))
        secondResult = loggedSub(firstResult, len(self.__dict__))
        self.assertEquals(0, secondResult)



if __name__ == '__main__':  # pragma: no cover
    unittest2.main()
