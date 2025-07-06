import re
from constants import MARKDOWN_TEXT
from utils.markdown_to_blocks.markdown_to_blocks import markdown_to_blocks

def main():
	md = MARKDOWN_TEXT
	print(re.findall(r"`{3}", md))

if __name__ == "__main__":
	main()