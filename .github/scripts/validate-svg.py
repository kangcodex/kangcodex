import sys
import xml.etree.ElementTree as ET

path = sys.argv[1]
try:
    root = ET.parse(path).getroot()
except (ET.ParseError, OSError) as error:
    print(f"Invalid SVG {path}: {error}", file=sys.stderr)
    raise SystemExit(1)

if root.tag != "{http://www.w3.org/2000/svg}svg":
    print(f"Invalid SVG {path}: root element is not SVG", file=sys.stderr)
    raise SystemExit(1)
