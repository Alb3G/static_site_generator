import re
from enum import Enum, unique

@unique
class BlockType(Enum):
	PARAGRAPH = "paragraph"
	HEADING = "heading"
	CODE = "code"
	QUOTE = "quote"
	UNORDERED_LIST = "unordered_list"
	ORDERED_LIST = "ordereded_list"

def block_to_blocktype(markdown: str) -> BlockType:
	if len(re.findall(r"^#{1,6}", markdown, re.MULTILINE)) > 0:
		return BlockType.HEADING
	if len(re.findall(r"^`{3}", markdown, re.MULTILINE)) > 0:
		return BlockType.CODE
	if len(re.findall(r"^>", markdown, re.MULTILINE)) > 0:
		return BlockType.QUOTE
	if len(re.findall(r"^-", markdown, re.MULTILINE)) > 0:
		return BlockType.UNORDERED_LIST
	if len(re.findall(r"^\d+.", markdown, re.MULTILINE)) > 0:
		return BlockType.ORDERED_LIST

	return BlockType.PARAGRAPH