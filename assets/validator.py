import os
import sys
import io
from lxml import etree

def validate_xml_with_dtd(xml_file, dtd_file):
    try:
        with open(xml_file, 'rb') as f:
            xml_content = f.read()
            
        with open(dtd_file, 'rb') as f:
            dtd_content = f.read()
        print("read File dtd file")
        
        dtd = etree.DTD(file=io.BytesIO(dtd_content))
        print("dtd etree")
        print(dtd)
        parser = etree.XMLParser(dtd_validation=True)
        print(parser)
        etree.fromstring(xml_content, parser)
        print(etree.fromstring(xml_content))
        if dtd.validate(etree.fromstring(xml_content)):
            print("Validation successful")
            return True
        else:
            print("Validation failed")
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python validator.py <xml_file> <dtd_file>")
        sys.exit(1)
    
    xml_file = sys.argv[1]
    dtd_file = sys.argv[2]

    if not os.path.exists(xml_file):
        print("XML file not found")
        sys.exit(1)

    if not os.path.exists(dtd_file):
        print("DTD file not found")
        sys.exit(1)
    print("call fct")
    if not validate_xml_with_dtd(xml_file, dtd_file):
        sys.exit(1)
