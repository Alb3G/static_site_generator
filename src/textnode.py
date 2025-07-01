from enum import Enum, unique
from typing import override

from htmlnode import LeafNode

@unique
class TextType(Enum):
	PLAIN = "plain"
	BOLD = "bold"
	ITALIC = "italic"
	CODE = "code"
	LINK = "link"
	IMAGE = "image"

def text_node_to_html_node(textNode: "TextNode") -> LeafNode:
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
				raise Exception("A link text node must contain valid url!.")

			return LeafNode("img", "", {"src": url, "alt": textNode.get_text()})

class TextNode:
	def __init__(self, text, text_type: TextType, url=None):
		self.__text = text
		self.__text_type = text_type
		self.__url = url
	
	def get_text(self):
		return self.__text
	
	def get_text_type(self):
		return self.__text_type
	
	def get_url(self):
		return self.__url
	
	def set_text(self, text):
		self.__text = text
	
	def set_text_type(self, text_type: TextType):
		self.__text_type = text_type
	
	def set_url(self, url):
		self.__url = url

	@override
	def __eq__(self, value: "TextNode") -> bool:
		if self.__text == value.__text and self.__text_type == value.__text_type and self.__url == value.__url:
			return True
		return False
	
	@override
	def __repr__(self) -> str:
		return f"TextNode({self.__text}, {self.__text_type.value}, {self.__url})"