from tests import FunctionalTest, tweetsec_eval_url

import requests
import password_eval


class TestTweetSec(FunctionalTest):

    def test_tweetsec_response_code(self):
        #test that the tweetsec URL for checking the tweet password exists
        r = requests.get(tweetsec_eval_url)
        self.assertEqual(r.status_code, 200)

class TestTweetSecNumericalStrengthValue(FunctionalTest):

    def test_tweetsec_numerical_strength(self):
        #test that password_eval module function numerical_strength_value returns the proper value,
        numerical_strength_value = password_eval.numerical_strength_value("password1")
        self.assertEqual(numerical_strength_value, 4)

        numerical_strength_value = password_eval.numerical_strength_value("goat m4n")
        self.assertEqual(numerical_strength_value, 15)

        numerical_strength_value = password_eval.numerical_strength_value("s0_0per 5nak3")
        self.assertEqual(numerical_strength_value, 44)


class TestTweetSecFindCharTypes(FunctionalTest):
    def test_tweetsec_find_char_types(self):
        #test that password_eval module function find_char_types, will properly find the number of char types according to Tweetsec conditions
        number_char_types = password_eval.find_char_types("aa0 #")
        self.assertEqual(number_char_types, 4)

        number_char_types = password_eval.find_char_types("aabbbA")
        self.assertEqual(number_char_types, 1)

        number_char_types = password_eval.find_char_types("$$&&++@@")
        self.assertEqual(number_char_types, 1)

        number_char_types = password_eval.find_char_types("       ")
        self.assertEqual(number_char_types, 1)

        number_char_types = password_eval.find_char_types("123456123234")
        self.assertEqual(number_char_types, 1)


class TestTweetSecWordReplacement(FunctionalTest):
    
    def test_tweetsec_replace_english_words(self):
        #test that password_eval module function replace_english_words, will replace any complete English words in the text with any lower-case letter
        #this will prefer longer replacements
        replace_pw = password_eval.replace_english_words("12password34")
        self.assertEqual(replace_pw, "12p34")

    def test_tweetsec_replace_foreign_words(self):
        #test that password_eval module function replace_english_words, will NOT replace foreign words
        replace_pw = password_eval.replace_english_words("12roja34")
        self.assertEqual(replace_pw, "12roja34")

    def test_tweetsec_replace_only_english_words(self):
        #test that password_eval module function replace_english_words, will ONLY replace real english words
        replace_pw = password_eval.replace_english_words("1tttt34")
        self.assertEqual(replace_pw, "1tttt34")

    def test_tweetsec_replace_smaller_substring_english_words(self):
        #test that password_eval module function replace_english_words, will replace smaller substrings if it's an english word (doesn't have to be the whole substring)
        replace_pw = password_eval.replace_english_words("1boxttt34")
        self.assertEqual(replace_pw, "1pttt34")

    def test_tweetsec_replace_smaller_substring_english_words_greater_than_zero_index(self):
        #test that password_eval module function replace_english_words, will replace smaller substrings if it's an english word, if the smaller substring does NOT start at the beginning of the bigger string (index>0)
        replace_pw = password_eval.replace_english_words("1sssboxttt34")
        self.assertEqual(replace_pw, "1ssspttt34")
    
    def test_tweetsec_replace_prefer_longer_english_substring_words(self):
        #test that password_eval module function replace_english_words, will prefer LONGER english substring words (when whole substring is not a word itself like "password")
        replace_pw = password_eval.replace_english_words("1zboyztable34")
        self.assertEqual(replace_pw, "1zboyzp34")

    