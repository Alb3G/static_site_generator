from textnode import TextNode, TextType
from htmlnode import LeafNode

def text_node_to_html_node(textNode: TextNode) -> LeafNode:
	if textNode.get_text_type() not in TextType:
		raise Exception(f"TextType: {textNode.get_text_type()} is not allowed!")

	match textNode.get_text_type():
		case TextType.PLAIN:
			return LeafNode(None, textNode.get_text())
		case TextType.BOLD:
			return LeafNode("b", textNode.get_text())
		case TextType.ITALIC:
			return LeafNode("i", textNode.get_text())
		case TextType.CODE:
			return LeafNode("code", textNode.get_text())
		case TextType.LINK:
			url = textNode.get_url()

			if url is None:
				raise Exception("A link text node must contain valid url!.")

			return LeafNode("a", textNode.get_text(), {"href": url})
		case TextType.IMAGE:
			url = textNode.get_url()

			if url is None:
				raise Exception("An image node must contain valid url!.")

			return LeafNode("img", textNode.get_text(), {"src": url, "alt": textNode.get_text()})