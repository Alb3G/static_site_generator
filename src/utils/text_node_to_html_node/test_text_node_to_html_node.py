import unittest
from textnode import TextNode, TextType
from utils.text_node_to_html_node.text_node_to_html_node import text_node_to_html_node

class TestTextNodeToHtmlNode(unittest.TestCase):
	def test_plain_text_OK(self):
		node = TextNode("This is a text node", TextType.PLAIN)
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.get_tag(), None)
		self.assertEqual(html_node.get_value(), "This is a text node")
	
	def test_bold_text_OK(self):
		node = TextNode("This is a bold text node", TextType.BOLD)
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.get_tag(), "b")
		self.assertEqual(html_node.get_value(), "This is a bold text node")
	
	def test_italic_text_OK(self):
		node = TextNode("This is a italic text node", TextType.ITALIC)
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.get_tag(), "i")
		self.assertEqual(html_node.get_value(), "This is a italic text node")
	
	def test_code_node_OK(self):
		node = TextNode("This is a code node", TextType.CODE)
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.get_tag(), "code")
		self.assertEqual(html_node.get_value(), "This is a code node")
	
	def test_link_node_OK(self):
		node = TextNode("This is a link node", TextType.LINK, "url")
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.get_tag(), "a")
		self.assertEqual(html_node.get_value(), "This is a link node")
	
	def test_image_node(self):
		node = TextNode("This is an image node", TextType.IMAGE, "picsum")
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.get_tag(), "img")
		self.assertEqual(html_node.get_value(), "This is an image node")

if __name__ == "__main__":
	unittest.main()