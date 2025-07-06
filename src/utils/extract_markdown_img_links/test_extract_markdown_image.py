import unittest
from .extract_markdown_img_links import (
	extract_markdown_images,
	extract_markdown_links
)

class TestExtractMarkDown(unittest.TestCase):
	def test_extract_markdown_images_OK(self):
		matches = extract_markdown_images(
			"This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
		)
		self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
	
	def test_extract_markdown_links_OK(self):
		matches = extract_markdown_links(
			"This is text with an [image](https://i.imgur.com/zjjcJKZ.png)"
		)
		self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

if __name__ == "__main__":
	unittest.main()