import unittest
from textnode import TextNode, TextType
from utils.split_nodes_image.split_nodes_image import split_nodes_image

class TestSplitNodesImage(unittest.TestCase):
	def test_split_node_image_OK(self):
		node = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)", TextType.PLAIN)
		new_nodes = split_nodes_image([node])
		self.assertListEqual(
			[
				TextNode("This is text with an ", TextType.PLAIN),
				TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png")
			],
			new_nodes
		)
	
	def test_split_image_single(self):
		node = TextNode(
			"![image](https://www.example.COM/IMAGE.PNG)",
			TextType.PLAIN,
        )
		new_nodes = split_nodes_image([node])
		self.assertListEqual(
			[
				TextNode("image", TextType.IMAGE, "https://www.example.COM/IMAGE.PNG"),
			],
			new_nodes,
		)

	def test_split_images(self):
		node = TextNode(
			"This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
			TextType.PLAIN,
        )
		new_nodes = split_nodes_image([node])
		self.assertListEqual(
			[
				TextNode("This is text with an ", TextType.PLAIN),
				TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
				TextNode(" and another ", TextType.PLAIN),
				TextNode(
					"second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
				),
			],
			new_nodes,
		)

if __name__ == "__main__":
	unittest.main()