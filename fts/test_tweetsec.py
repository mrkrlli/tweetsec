from tests import FunctionalTest, tweetsec_eval_url

import requests

class TestTweetSec(FunctionalTest):
    
    def test_tweetsec_response_code(self):
        #test that the tweetsec URL for checking the tweet password exists
        r = requests.get(tweetsec_eval_url)
        self.assertEqual(r.status_code, 200)
      