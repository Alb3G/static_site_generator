import re

def extract_markdown_images_and_links(text: str) -> list[tuple[str, str]]:
    # \[(.*?)\] -> brackets
	# \((.*?)\) -> Parenthesis
	matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
	return matches
