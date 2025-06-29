import unittest
from textnode import TextNode, TextType

class TestTexNode(unittest.TestCase):
	def test_eq_OK(self):
		node = TextNode("This is a text node", TextType.BOLD)
		node2 = TextNode("This is a text node", TextType.BOLD)
		self.assertEqual(node, node2)

	def _eq_url_KO(self):
		node = TextNode("This is a text node", TextType.BOLD)
		self.assertIsNotNone(node.get_url())
	
	def test_eq_url_OK(self):
		node = TextNode("This is a text node", TextType.BOLD, "https://localhost:8080")
		self.assertIsNotNone(node.get_url())
		
	def _eq_KO(self):
		node = TextNode("This is a text node", TextType.BOLD)
		node2 = TextNode("This is a text node", TextType.BOLD)
		self.assertNotEqual(node, node2)
	
	def test_eq_Diff_OK(self):
		node = TextNode("This is a text node", TextType.LINK)
		node2 = TextNode("This is a text node", TextType.BOLD)
		self.assertNotEqual(node, node2)
	

if __name__ == "__main__":
	unittest.main()