import unittest
from textnode import TextNode, TextType
from utils.split_nodes_delimiter.split_nodes_delimiter import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
	def test_split_nodes_by_delimiter(self):
		node = TextNode("This is text with a `code block` word", TextType.PLAIN)
		new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
		success_results = [
    		TextNode("This is text with a ", TextType.PLAIN),
    		TextNode("code block", TextType.CODE),
    		TextNode(" word", TextType.PLAIN),
		]
		self.assertListEqual(new_nodes, success_results)

if __name__ == "__main__":
	unittest.main()