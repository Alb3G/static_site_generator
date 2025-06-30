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
	
	def __repr__(self) -> str:
		return f"HtmlNode({self.get_tag()}, {self.get_value()}, {self.get_children()}, {self.get_props()})"

class LeafNode(HtmlNode):
	def __init__(self, tag: str, value: str, props: dict[str, str] = {}) -> None:
		super().__init__(tag=tag, value=value, props=props)

	def to_html(self):
		if self.get_value() is None:
			raise ValueError("All leaf nodes must have a value!.")
		
		if self.get_tag() is None:
			return self.get_value()
		
		props_string = self.props_to_html()

		html_result = f'<{self.get_tag()}{props_string if props_string != None else ''}>{self.get_value()}</{self.get_tag()}>'
	
		return html_result