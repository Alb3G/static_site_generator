def markdown_to_blocks(markdown: str) -> list[str]:
	result = []
	for markdown_part in markdown.split("\n\n"):
		if markdown_part.strip() != '':
			# Eliminar espacios al inicio y final del bloque
			block = markdown_part.strip()
			# Dividir en líneas y eliminar la indentación de cada línea
			lines = block.split('\n')
			cleaned_lines = []
			for line in lines:
				cleaned_lines.append(line.strip())
			# Reconstruir el bloque
			result.append('\n'.join(cleaned_lines))

	return result