import unittest
from constants import MARKDOWN_TEXT, MARKDOWN_TEXT_INDENTED
from utils.extract_markdown_title.extract_markdown_title import extract_title

class TestExtractMarkdownTitle(unittest.TestCase):
	def test_extract_title(self):
		h1_from_markdown = "# Título principal";
		h1_result = extract_title(MARKDOWN_TEXT);
		self.assertEqual(h1_from_markdown, h1_result);
	
	def test_extract_title_with_indentation(self):
		h1_from_markdown = "# Título principal";
		h1_result = extract_title(MARKDOWN_TEXT_INDENTED);
		self.assertEqual(h1_from_markdown, h1_result);