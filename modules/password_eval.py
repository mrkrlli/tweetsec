# -*- coding: utf-8 -*-
import re
import enchant

def numerical_strength_value(password):
	replacement_password = replace_english_words(password)
	char_types = find_char_types(replacement_password)
	
	return char_types * len(replacement_password)

def find_char_types(password):
	total_count = 0

	if re.search(r'[a-zA-Z]', password):
		total_count += 1

	if re.search(r'[\d]', password):
		total_count += 1	

	if re.search(r'[\s]', password):
		total_count += 1	

	if re.search(r'[^a-zA-Z\d\s]', password):
		total_count += 1

	return total_count


def replace_english_words(password):
	#find chunks of 1 or more alphabet letters, and replace if they fit various conditions
	password_with_replacement = re.sub(r'[a-zA-Z]+', check_letters, password)

	return password_with_replacement


def check_letters(matchobj):
	#check the letters in the substring for various conditions, and replace accordingly
	#we will be replacing whole english words with the lower letter "p" (this will be the letter we replace that satisfies the Tweetsec condiction)
	
	d = enchant.Dict("en_US")
	if d.check(matchobj.group(0)):
		#if whole substring is an english word, replace with "p"
		return "p"
	else:
		#if whole substring is NOT an english word, see if there's a part of this substring that IS an english word
		#start off by including 1 less than the total number of characters in the substring, and then go smaller if you still don't find anything (so prefence will be given to longer english word matches)
		#end this at 1 character length (b/c this would be equivalent to replacing it with character "p" for tweetsec purposes)
		substring_len = len(matchobj.group(0))

		for x in range(substring_len-1, 1, -1):
			char_offset = 0

			while char_offset + x <= substring_len:

				if d.check(matchobj.group(0)[char_offset:char_offset+x]):
					#if it matches, replace the matched part with "p"
					replaced_string = matchobj.group(0)[0:char_offset] + "p" + matchobj.group(0)[char_offset+x: substring_len]
					return replaced_string
				else:
					#if it doesn't match, move the starting char offset up
					char_offset += 1

			'''
			if d.check(matchobj.group(0)[char_offset:char_offset+x]):
				#if it matches, replace the matched part with "p"
				replaced_string = matchobj.group(0)[0:char_offset] + "p" + matchobj.group(0)[char_offset+x: substring_len]
				return replaced_string

			else:
				#if it doesn't match, move the starting char offset up (until the smaller substring reaches the end of the whole substring)
				char_
			'''

		return matchobj.group(0)

