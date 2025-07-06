from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType):
	"""
		node = TextNode("This is text with a `code block` word", TextType.TEXT)
		new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
		
		Output
		[
    		TextNode("This is text with a ", TextType.TEXT),
    		TextNode("code block", TextType.CODE),
    		TextNode(" word", TextType.TEXT),
		]
	"""
	new_nodes_list = []
	for node in old_nodes:
		if node.get_text_type() != TextType.PLAIN:
			new_nodes_list.append(node)
		else:
			if node.get_text().count(delimiter) % 2 == 1:
				raise ValueError("Unmatched delimiters in string")
			
			node_text_parts = node.get_text().split(delimiter)

			for i, node_text in enumerate(node_text_parts):
				if node_text == "":
					continue

				if i % 2 == 0:
					new_nodes_list.append(TextNode(node_text, TextType.PLAIN))
				else:
					new_nodes_list.append(TextNode(node_text, text_type))
	
	return new_nodes_list





			
			
			
				

