#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests
import sys


def get_details(url):
	r = requests.get(url)
	web_content = r.content
	insert_line = '\n-------------------------------------------------------\n'
	page = BeautifulSoup(web_content)
	players_info={}
	question_header = page.find('div', id='question-header').get_text()
	question_block = page.find('div', class_='question', id='question')
	question_description = question_block.find('div', class_='post-text').get_text()
	question_tag_block = question_block.find('div', class_='post-taglist')
	question_tags = question_tag_block.find_all('a')
	question_tags = [question_tag.get_text() for question_tag in question_tags]
	vote_count = question_block.find('span', class_='vote-count-post').get_text()
	question_owner_user = question_block.find('td', class_='post-signature owner')
	user_block = question_owner_user.find('div', class_='user-details')
	questioned_user = user_block.find('a').get_text()

	answer_blocks = page.find('div', id='answers')
	accepted_answers = answer_blocks.find('div', class_='answer accepted-answer')
	answer_table = accepted_answers.find_next('table')
	answer_vote_block = answer_table.find('td', class_='votecell')

	answer_vote_count = answer_vote_block.find('span', class_='vote-count-post ').get_text()

	answer_cell_block = answer_table.find('td', class_='answercell')
	# import pdb
	# pdb.set_trace()
	answer_description = answer_cell_block.find('code').get_text()
	answer_owner_user = answer_blocks.find('td', class_='post-signature')
	user_block = answer_owner_user.find('div', class_='user-details')
	answered_user = user_block.find('a').get_text()
	print insert_line
	print 'Question Header:%s%s' % (question_header, insert_line)
	print 'Question Description:%s%s' % (question_description, insert_line)
	print 'Question Tags:%s%s' % (question_tags, insert_line)
	print 'Question Vote Count:%s%s' % (vote_count, insert_line)
	print 'Question Owner:%s%s' % (questioned_user, insert_line)

	print 'Answer Description:%s%s' % (answer_description, insert_line)
	print 'Answer Vote Count:%s%s' % (answer_vote_count, insert_line)
	print 'Answer Owner:%s%s' % (answered_user, insert_line)

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print "Enter stackoverflow url"
		exit(0)
	
	url = sys.argv[1]
	print url
	get_details(url)
	