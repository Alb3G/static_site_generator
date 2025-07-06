from textnode import TextNode, TextType
from utils.split_nodes_delimiter.split_nodes_delimiter import split_nodes_delimiter
from utils.split_nodes_image.split_nodes_image import split_nodes_image
from utils.split_nodes_link.split_nodes_link import split_nodes_link

def text_to_textnodes(text) -> list[TextNode]:
	text_node = TextNode(text, TextType.PLAIN)
	new_nodes = split_nodes_delimiter([text_node], "**", TextType.BOLD)
	new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
	new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)
	new_nodes = split_nodes_image(new_nodes)
	new_nodes = split_nodes_link(new_nodes)
	return new_nodes