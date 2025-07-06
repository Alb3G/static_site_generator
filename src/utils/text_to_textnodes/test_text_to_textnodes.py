import unittest
from textnode import TextNode, TextType
from utils.text_to_textnodes.text_to_textnodes import text_to_textnodes

class TestTextToTextNodes(unittest.TestCase):
	def test_all_node_types_OK(self):
		input = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
		new_nodes = text_to_textnodes(input)
		self.assertListEqual(
			[
				TextNode("This is ", TextType.PLAIN),
				TextNode("text", TextType.BOLD),
				TextNode(" with an ", TextType.PLAIN),
				TextNode("italic", TextType.ITALIC),
				TextNode(" word and a ", TextType.PLAIN),
				TextNode("code block", TextType.CODE),
				TextNode(" and an ", TextType.PLAIN),
				TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
				TextNode(" and a ", TextType.PLAIN),
				TextNode("link", TextType.LINK, "https://boot.dev"),
			],
			new_nodes
		)