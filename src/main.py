from htmlnode import HtmlNode
from textnode import TextNode, TextType

def main():
	html_node = HtmlNode("<p>", "Lorem ipsum dolor sit amet")
	print(html_node.__repr__())

if __name__ == "__main__":
	main()