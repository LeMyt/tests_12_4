import logging
import unittest
from rt_with_exceptions import Runner

logging.basicConfig(level=logging.INFO, filemode='w', encoding='utf-8', filename='runner_tests.log',
                        format="%(asctime)s | %(levelname)s | %(message)s")

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            r2 = Runner(1)
            r2.walk()
            logging.info('"test_walk" выполнен успешно')
        except TypeError as err:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    def test_run(self):
        try:
            r1 = Runner("Runner", -5)
            r1.run()
            logging.info('"test_run" выполнен успешно')
        except ValueError as e:
            logging.warning('Неверная скорость для Runner', exc_info=True)


if __name__ == "__main__":
    unittest.main()

