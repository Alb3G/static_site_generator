import unittest
from htmlnode import HtmlNode, LeafNode

class TestHtmlNode(unittest.TestCase):

	def test_to_html_OK(self):
		props = {
			"href": "https://www.google.com",
			"target": "_blank",
		}
		
		html_node = HtmlNode("<a>", "Lorem ipsum dolor", props=props)

		with self.assertRaises(NotImplementedError):
			html_node.to_html()
	
	def test_props_to_html_OK(self):
		props = {
			"href": "https://www.google.com",
			"target": "_blank",
		}

		html_node = HtmlNode("<a>", "Lorem ipsum dolor", props=props)
		props_string = ' href="https://www.google.com" target="_blank"'

		self.assertEqual(html_node.props_to_html(), props_string)

	def test__repr__OK(self):
		result = "HtmlNode(<p>, Lorem ipsum dolor sit amet, [], {})"
		html_node = HtmlNode("<p>", "Lorem ipsum dolor sit amet")

		self.assertEqual(result, html_node.__repr__())
	
	def test_leaf_to_html_p(self):
		node = LeafNode("p", "Hello, world!")
		self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
	
	def test_leaf_to_html_a(self):
		node = LeafNode("a", "Google", {"href": "https://google.com", "target": "_blank"})
		self.assertEqual(node.to_html(), '<a href="https://google.com" target="_blank">Google</a>')


if __name__ == "__main__":
	unittest.main()