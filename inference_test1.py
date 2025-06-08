from ultralytics import YOLO

# Load a model
model = YOLO("C://Users//rusyd//Downloads//cobacoba1//best.pt")
# Run batched inference on a list of images
model.predict("http://192.168.26.184:81/stream", show = True)