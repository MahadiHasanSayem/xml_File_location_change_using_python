import os
import shutil

# Source directory containing XML files
source_dir = r'C:\Users\Mahadi Saym\Desktop\imran\xml'

# Destination directory where you want to move the XML files
destination_dir = r'F:\after delete place it here\Replacedxml files'

# List of specific XML file names you want to move
xml_files_to_move = [
    "s_second2 (637).xml",
    "s_second2 (505).xml",
    "s_second2 (454).xml",
    "s_second2 (334).xml",
    "s_second2 (336).xml",
    "s_second2 (714).xml",
    "s_second2 (854).xml",
    "s_second2 (252).xml",
    "s_second2 (297).xml",
    "s_second2 (367).xml",
    "s_second2 (459).xml",
    "s_second2 (638).xml",
    "s_second2 (186).xml",
    "s_second2 (889).xml",
    "s_second2 (975).xml",
    "Vehicle1071.xml",
    "Vehicle1683.xml",
    "Vehicle1708.xml",
    "Vehicle1704.xml",
    "Vehicle706.xml",
    "Vehicle852.xml",
    "Vehicle975.xml",
    # Add more file names here
]

# Iterate through the list of specific XML files and move them to the destination directory
for xml_file in xml_files_to_move:
    source_path = os.path.join(source_dir, xml_file)
    destination_path = os.path.join(destination_dir, xml_file)
    
    try:
        # Move the XML file to the destination directory
        shutil.move(source_path, destination_path)
        print(f"Moved {xml_file} to {destination_dir}")
    except Exception as e:
        print(f"Failed to move {xml_file}: {str(e)}")

print("Done")
