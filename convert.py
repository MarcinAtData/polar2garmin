import xml.etree.ElementTree as ET
from pathlib import Path

INPUT_DIR = Path("input")
OUTPUT_DIR = Path("output")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def clean_tcx(input_file: Path, output_file: Path):
    tree = ET.parse(input_file)
    root = tree.getroot()


    def remove_elements_by_tag(tag_name):
        for parent in root.iter():
            for child in list(parent):
                if child.tag.endswith(tag_name):
                    parent.remove(child)


    remove_elements_by_tag("Author")
    remove_elements_by_tag("Creator")


    for parent in root.iter():
        for child in list(parent):
            if child.tag.endswith("Name") and child.text == "Polar Verity Sense":
                parent.remove(child)

    tree.write(output_file, encoding="utf-8", xml_declaration=True)


for tcx_file in list(INPUT_DIR.glob("*.tcx")) + list(INPUT_DIR.glob("*.TCX")):
    output_file = OUTPUT_DIR / tcx_file.name
    clean_tcx(tcx_file, output_file)
    print(f"✔ Processed: {tcx_file.name}")

print("✅ All TCX files processed.")
