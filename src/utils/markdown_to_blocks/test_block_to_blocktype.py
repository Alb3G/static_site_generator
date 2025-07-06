import unittest
from utils.markdown_to_blocks.block_to_blocktype import block_to_blocktype, BlockType

class TestBlockToBlockType(unittest.TestCase):
	
	def test_paragraph_block_OK(self):
		"""Test para bloques de párrafo normales"""
		markdown = "This is a simple paragraph"
		block_type = block_to_blocktype(markdown)
		self.assertEqual(block_type, BlockType.PARAGRAPH)
	
	def test_paragraph_with_formatting_OK(self):
		"""Test para párrafos con formato pero sin indicadores de bloque"""
		markdown = "This is a paragraph with **bold** and _italic_ text"
		block_type = block_to_blocktype(markdown)
		self.assertEqual(block_type, BlockType.PARAGRAPH)
	
	def test_heading_h1_OK(self):
		"""Test para encabezados H1"""
		markdown = "# This is a heading"
		block_type = block_to_blocktype(markdown)
		self.assertEqual(block_type, BlockType.HEADING)
	
	def test_heading_h2_OK(self):
		"""Test para encabezados H2"""
		markdown = "## This is a heading"
		block_type = block_to_blocktype(markdown)
		self.assertEqual(block_type, BlockType.HEADING)
	
	def test_heading_h6_OK(self):
		"""Test para encabezados H6"""
		markdown = "###### This is a heading"
		block_type = block_to_blocktype(markdown)
		self.assertEqual(block_type, BlockType.HEADING)
	
	def test_heading_with_content_OK(self):
		"""Test para encabezados con contenido adicional"""
		markdown = "# This is a heading with **bold** text"
		block_type = block_to_blocktype(markdown)
		self.assertEqual(block_type, BlockType.HEADING)
	
	def test_code_block_OK(self):
		"""Test para bloques de código"""
		markdown = "```\nprint('Hello, World!')\n```"
		block_type = block_to_blocktype(markdown)
		self.assertEqual(block_type, BlockType.CODE)
	
	def test_code_block_with_language_OK(self):
		"""Test para bloques de código con especificación de lenguaje"""
		markdown = "```python\nprint('Hello, World!')\n```"
		block_type = block_to_blocktype(markdown)
		self.assertEqual(block_type, BlockType.CODE)
	
	def test_code_block_with_content_OK(self):
		"""Test para bloques de código con contenido complejo"""
		markdown = "```\ndef hello():\n    return 'Hello, World!'\n```"
		block_type = block_to_blocktype(markdown)
		self.assertEqual(block_type, BlockType.CODE)
	
	def test_quote_block_OK(self):
		"""Test para bloques de cita"""
		markdown = "> This is a quote"
		block_type = block_to_blocktype(markdown)
		self.assertEqual(block_type, BlockType.QUOTE)
	
	def test_quote_block_multiline_OK(self):
		"""Test para bloques de cita multilínea"""
		markdown = "> This is a quote\n> with multiple lines"
		block_type = block_to_blocktype(markdown)
		self.assertEqual(block_type, BlockType.QUOTE)
	
	def test_quote_block_with_formatting_OK(self):
		"""Test para bloques de cita con formato"""
		markdown = "> This is a **bold** quote with _italic_ text"
		block_type = block_to_blocktype(markdown)
		self.assertEqual(block_type, BlockType.QUOTE)
	
	def test_unordered_list_single_item_OK(self):
		"""Test para listas desordenadas con un elemento"""
		markdown = "- This is a list item"
		block_type = block_to_blocktype(markdown)
		self.assertEqual(block_type, BlockType.UNORDERED_LIST)
	
	def test_unordered_list_multiple_items_OK(self):
		"""Test para listas desordenadas con múltiples elementos"""
		markdown = "- First item\n- Second item\n- Third item"
		block_type = block_to_blocktype(markdown)
		self.assertEqual(block_type, BlockType.UNORDERED_LIST)
	
	def test_unordered_list_with_formatting_OK(self):
		"""Test para listas desordenadas con formato"""
		markdown = "- **Bold** item\n- _Italic_ item"
		block_type = block_to_blocktype(markdown)
		self.assertEqual(block_type, BlockType.UNORDERED_LIST)
	
	def test_ordered_list_single_item_OK(self):
		"""Test para listas ordenadas con un elemento"""
		markdown = "1. This is a list item"
		block_type = block_to_blocktype(markdown)
		self.assertEqual(block_type, BlockType.ORDERED_LIST)
	
	def test_ordered_list_multiple_items_OK(self):
		"""Test para listas ordenadas con múltiples elementos"""
		markdown = "1. First item\n2. Second item\n3. Third item"
		block_type = block_to_blocktype(markdown)
		self.assertEqual(block_type, BlockType.ORDERED_LIST)
	
	def test_ordered_list_with_formatting_OK(self):
		"""Test para listas ordenadas con formato"""
		markdown = "1. **Bold** item\n2. _Italic_ item"
		block_type = block_to_blocktype(markdown)
		self.assertEqual(block_type, BlockType.ORDERED_LIST)
	
	def test_ordered_list_double_digits_OK(self):
		"""Test para listas ordenadas con números de dos dígitos"""
		markdown = "10. Tenth item\n11. Eleventh item"
		block_type = block_to_blocktype(markdown)
		self.assertEqual(block_type, BlockType.ORDERED_LIST)
	
	def test_edge_case_dash_in_text_OK(self):
		"""Test para texto con guiones que no es una lista"""
		markdown = "This text has a dash - but it's not a list"
		block_type = block_to_blocktype(markdown)
		self.assertEqual(block_type, BlockType.PARAGRAPH)
	
	def test_edge_case_number_in_text_OK(self):
		"""Test para texto con números que no es una lista"""
		markdown = "This text has a number 1. but it's not a list"
		block_type = block_to_blocktype(markdown)
		self.assertEqual(block_type, BlockType.PARAGRAPH)
	
	def test_edge_case_hash_in_text_OK(self):
		"""Test para texto con # que no es un encabezado"""
		markdown = "This text has a # symbol but it's not a heading"
		block_type = block_to_blocktype(markdown)
		self.assertEqual(block_type, BlockType.PARAGRAPH)
	
	def test_edge_case_backticks_in_text_OK(self):
		"""Test para texto con backticks que no es un bloque de código"""
		markdown = "This text has `inline code` but it's not a code block"
		block_type = block_to_blocktype(markdown)
		self.assertEqual(block_type, BlockType.PARAGRAPH)
	
	def test_edge_case_greater_than_in_text_OK(self):
		"""Test para texto con > que no es una cita"""
		markdown = "This text has > symbol but it's not a quote"
		block_type = block_to_blocktype(markdown)
		self.assertEqual(block_type, BlockType.PARAGRAPH)
	
	def test_empty_string_OK(self):
		"""Test para string vacío"""
		markdown = ""
		block_type = block_to_blocktype(markdown)
		self.assertEqual(block_type, BlockType.PARAGRAPH)
	
	def test_whitespace_only_OK(self):
		"""Test para string con solo espacios"""
		markdown = "   \n\t  "
		block_type = block_to_blocktype(markdown)
		self.assertEqual(block_type, BlockType.PARAGRAPH)

if __name__ == "__main__":
	unittest.main() 