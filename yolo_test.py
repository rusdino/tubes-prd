from ultralytics import YOLO

# Load a model
def main():
    model = YOLO("yolo11n.yaml")  # build a new model from YAML
    model = YOLO("yolo11n.pt")  # load a pretrained model (recommended for training)
    model = YOLO("yolo11n.yaml").load("yolo11n.pt")  # build from YAML and transfer weights
    results = model.train(data="C://Users//rusyd//Downloads//tubes-prd//prd_labeled_data//data.yaml", epochs=3000, imgsz=640)

# Train the model
if __name__ == "__main__":
    main()
    # model.train(data="coco128.yaml", epochs=3)  # train the model
    # model.val()  # evaluate the model on the validation set
    # model.export(format="onnx")  # export the model to ONNX format
    # model.predict(source="https://ultralytics.com/images/bus.jpg", show=True)  # predict with the model