from textnode import TextNode, TextType
from utils.extract_markdown_img_links.extract_markdown_img_links import extract_markdown_links


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
	new_nodes = []

	for node in old_nodes:
		if node.get_text_type() != TextType.PLAIN:
			new_nodes.append(node)
			continue
	
		text = node.get_text()

		links = extract_markdown_links(text)

		if len(links) == 0:
			new_nodes.append(node)
			continue
		
		for link in links:
			sections = text.split(f"[{link[0]}]({link[1]})", 1)
			
			if len(sections) != 2:
				raise ValueError("invalid markdown, link section not closed!")

			if sections[0] != "":
				new_nodes.append(TextNode(sections[0], TextType.PLAIN))

			new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))

			text = sections[1]

		if text != "":
			new_nodes.append(TextNode(text, TextType.PLAIN))

	return new_nodes