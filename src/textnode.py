from cgitb import text
from enum import Enum
from typing import override

class TextType(Enum):
	PLAIN = "plain"
	BOLD = "bold"
	ITALIC = "italic"
	CODE = "code"
	LINK = "link"
	IMAGE = "image"


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