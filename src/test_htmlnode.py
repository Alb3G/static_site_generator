import unittest
from htmlnode import HtmlNode, LeafNode, ParentNode

class TestHtmlNode(unittest.TestCase):

	# Html nodes test cases
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
	
	# Leaf nodes test cases
	def test_leaf_to_html_p(self):
		node = LeafNode("p", "Hello, world!")
		self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
	
	def test_leaf_to_html_a(self):
		node = LeafNode("a", "Google", {"href": "https://google.com", "target": "_blank"})
		self.assertEqual(node.to_html(), '<a href="https://google.com" target="_blank">Google</a>')
	
	# Parent node test cases
	def test_to_html_with_children_OK(self):
		child_node = LeafNode("span", "child")
		parent_node = ParentNode("div", [child_node])
		self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

	def test_to_html_with_grandchildren_OK(self):
		grandchild_node = LeafNode("b", "grandchild")
		child_node = ParentNode("span", [grandchild_node])
		parent_node = ParentNode("div", [child_node])
		self.assertEqual(
			parent_node.to_html(),
			"<div><span><b>grandchild</b></span></div>",
		)
	
	def test_to_html_with_grandchildren_props_OK(self):
		grandchild_node = LeafNode("a", "Link", {"href": "https://google.com", "target": "_blank"})
		child_node = ParentNode("span", [grandchild_node])
		parent_node = ParentNode("div", [child_node])
		self.assertEqual(
			parent_node.to_html(),
			'<div><span><a href="https://google.com" target="_blank">Link</a></span></div>',
		)


if __name__ == "__main__":
	unittest.main()