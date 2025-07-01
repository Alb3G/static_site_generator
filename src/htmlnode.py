from typing import override


class HtmlNode:
	def __init__(self, tag=None, value=None, children: list["HtmlNode"]=[], props: dict[str,str]={}) -> None:
		self.__tag = tag
		self.__value = value
		self.__children = children
		self.__props = props
	
	# Getters
	def get_tag(self) -> str | None:
		return self.__tag
		
	def get_value(self) -> str | None:
		return self.__value
		
	def get_children(self) -> list["HtmlNode"]:
		return self.__children
		
	def get_props(self) -> dict[str, str]:
		return self.__props
		
	# Setters
	def set_tag(self, tag: str | None) -> None:
		self.__tag = tag
		
	def set_value(self, value: str | None) -> None:
		self.__value = value
		
	def set_children(self, children: list["HtmlNode"]) -> None:
		self.__children = children
		
	def set_props(self, props: dict[str, str]) -> None:
		self.__props = props

	def to_html(self):
		raise NotImplementedError
	
	def props_to_html(self):
		result = ''
		
		for prop_tuple in self.get_props().items():
			result += f' {prop_tuple[0]}="{prop_tuple[1]}"'
		
		return result
	
	@override
	def __repr__(self) -> str:
		return f"HtmlNode({self.get_tag()}, {self.get_value()}, {self.get_children()}, {self.get_props()})"

class LeafNode(HtmlNode):
	def __init__(self, tag: str | None, value: str, props: dict[str, str] = {}) -> None:
		super().__init__(tag=tag, value=value, props=props)

	def to_html(self):
		if self.get_value() is None:
			raise ValueError("All leaf nodes must have a value!.")
		
		if self.get_tag() is None:
			return self.get_value()
		
		props_string = self.props_to_html()

		html_result = f'<{self.get_tag()}{props_string if props_string != None else ''}>{self.get_value()}</{self.get_tag()}>'
	
		return html_result

class ParentNode(HtmlNode):
	def __init__(self, tag, children: list["HtmlNode"], props: dict[str, str] = {}) -> None:
		super().__init__(tag=tag, children=children, props=props)
	
	def to_html(self):
		if self.get_tag() == None:
			raise ValueError("Node must have a tag!.")
		
		if len(self.get_children()) == 0 or self.get_children() is None:
			raise ValueError("You must use children nodes in this class!.")
		
		html_string = f'<{self.get_tag()}>'

		for child in self.get_children():
			html_string += child.to_html()

		html_string += f'</{self.get_tag()}>'

		return html_string
	
	@override
	def __repr__(self):
		return f"ParentNode({self.get_tag()}, children: {self.get_children()}, {self.get_props()})"