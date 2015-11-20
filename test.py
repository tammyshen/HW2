import hw1
import unittest
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TestlookForKeyword(unittest.TestCase):

    def test_mediaapi(self):

        trump = hw1.lookForKeyword('Trump')
        assert trump['count'] == 34800


        logger.info('finish!')

if __name__ == "__main__":
    unittest.main()
