import re
from textnode import TextNode, TextType

def split_nodes_image(old_nodes: list[TextNode]):
	new_nodes = []
	for node in old_nodes:
		matches = re.findall(r"\[(.*?)\]\((.*?)\)", node.get_text())
		for text_match in matches:
			new_nodes.append(TextNode(text_match[0], TextType.IMAGE))
			new_nodes.append(TextNode(text_match[1], TextType.IMAGE))
