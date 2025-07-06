import unittest
from textnode import TextNode, TextType
from utils.split_nodes_link.split_nodes_link import split_nodes_link

class TestSplitNodesLink(unittest.TestCase):
	def test_split_node_link_OK(self):
		node = TextNode("This is text with an [link](https://i.imgur.com/zjjcJKZ.png)", TextType.PLAIN)
		new_nodes = split_nodes_link([node])
		self.assertListEqual(
			[
				TextNode("This is text with an ", TextType.PLAIN),
				TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png")
			],
			new_nodes
		)
	
	def test_split_link_single(self):
		node = TextNode(
			"[link](https://www.example.COM/IMAGE.PNG)",
			TextType.PLAIN,
        )
		new_nodes = split_nodes_link([node])
		self.assertListEqual(
			[
				TextNode("link", TextType.LINK, "https://www.example.COM/IMAGE.PNG"),
			],
			new_nodes,
		)

	def test_split_links(self):
		node = TextNode(
			"This is text with an [link](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png)",
			TextType.PLAIN,
        )
		new_nodes = split_nodes_link([node])
		self.assertListEqual(
			[
				TextNode("This is text with an ", TextType.PLAIN),
				TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
				TextNode(" and another ", TextType.PLAIN),
				TextNode(
					"second link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
				),
			],
			new_nodes,
		)

if __name__ == "__main__":
	unittest.main()