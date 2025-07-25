from textnode import TextNode, TextType
from utils.extract_markdown_img_links.extract_markdown_img_links import extract_markdown_images

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
	new_nodes = []

	for node in old_nodes:
		if node.get_text_type() != TextType.PLAIN:
			new_nodes.append(node)
			continue
	
		text = node.get_text()

		images = extract_markdown_images(text)

		if len(images) == 0:
			new_nodes.append(node)
			continue
		
		for image in images:
			sections = text.split(f"![{image[0]}]({image[1]})", 1)
			
			if len(sections) != 2:
				raise ValueError("invalid markdown, image section not closed!")

			if sections[0] != "":
				new_nodes.append(TextNode(sections[0], TextType.PLAIN))

			new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))

			text = sections[1]

		if text != "":
			new_nodes.append(TextNode(text, TextType.PLAIN))

	return new_nodes