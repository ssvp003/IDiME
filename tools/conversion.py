from pathlib import Path

input_path = Path("../out/IDiME for Meltype.tsv")
output_path = Path("../out/IDiME for Meltype.txt")

text = input_path.read_text(encoding="utf-8")
output_path.write_text(text, encoding="utf-8")
