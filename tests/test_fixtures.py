from functions.fixtures import *

def test_sum(sample_list):
	assert sum(sample_list) == 15

def test_len(sample_list):
	assert len(sample_list) == 5
