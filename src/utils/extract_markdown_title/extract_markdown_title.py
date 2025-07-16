import re

def extract_title(markdown: str) -> str:
	h1: list[str] = re.findall(r"^\s*(#\s+.*)", markdown, re.MULTILINE)

	if len(h1) == 0:
		raise Exception("No h1 found in the markdown!")
	
	result = h1[0].strip()

	return result