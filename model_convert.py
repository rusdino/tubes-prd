from ultralytics import YOLO

model = YOLO("C://Users//rusyd//Downloads//cobacoba1//best.pt")  # load a custom trained model

# Export the model
model.export(format="tflite")