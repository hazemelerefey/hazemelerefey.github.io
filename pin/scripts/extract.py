import zipfile
import json
import sys

def extract_layout(pbix_path, out_path):
    try:
        with zipfile.ZipFile(pbix_path, 'r') as z:
            # PBIX usually has 'Report/Layout'
            layout_data = z.read('Report/Layout')
            # It's typically UTF-16 LE encoded JSON file
            layout_text = layout_data.decode('utf-16-le')
            
            # Optionally parse and re-stringify to format it nicely
            parsed = json.loads(layout_text)
            
            with open(out_path, 'w', encoding='utf-8') as f:
                json.dump(parsed, f, indent=2)
            print(f"Successfully extracted {out_path}")
    except Exception as e:
        print(f"Error extracting from {pbix_path}: {e}")

if __name__ == '__main__':
    extract_layout(r"D:\MY Website\dashboards\HealthCare Wait list.pbix", r"D:\hazemelerefy website\my website\healthcare_layout.json")
    extract_layout(r"D:\MY Website\dashboards\Global Sales Dashboard.pbix", r"D:\hazemelerefy website\my website\globalsales_layout.json")
