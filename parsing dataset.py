import xml.etree.ElementTree as ET
from pathlib import Path

# Load and parse the XML file
tree = ET.parse("C://Users//rusyd//Downloads//annotations.xml")
root = tree.getroot()

# Image dimensions from metadata
image_width = 480
image_height = 864
class_id = 0  # Assuming class "RedBlock" has ID 0

# Prepare dictionary to hold YOLO formatted data per frame
frame_data = {}

# Iterate over each <image> tag
for image in root.findall("image"):
    frame_name = image.attrib["name"]
    frame_number = int(image.attrib["id"])
    txt_filename = f"{frame_name}.txt"

    for box in image.findall("box"):
        xtl = float(box.attrib["xtl"])
        ytl = float(box.attrib["ytl"])
        xbr = float(box.attrib["xbr"])
        ybr = float(box.attrib["ybr"])

        # Convert to YOLO format
        x_center = (xtl + xbr) / 2.0 / image_width
        y_center = (ytl + ybr) / 2.0 / image_height
        width = (xbr - xtl) / image_width
        height = (ybr - ytl) / image_height

        line = f"{class_id} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}"

        if txt_filename not in frame_data:
            frame_data[txt_filename] = []
        frame_data[txt_filename].append(line)

# Save each frame to corresponding text file
output_dir = "C://Users//rusyd//Downloads//tubes-prd//prd_labeled_data//obj_train_data"

for filename, lines in frame_data.items():
    with open(f"{output_dir}/{filename}", "w") as f:
        f.write("\n".join(lines))

len(frame_data)  # Return number of frames processed
