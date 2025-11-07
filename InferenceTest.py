import torch, cv2, numpy as np, matplotlib.pyplot as plt
from torchvision.models.detection import fasterrcnn_resnet50_fpn
from torchvision.transforms import functional as F

# Carga de modelo
def get_model(num_classes):
    model = fasterrcnn_resnet50_fpn(weights=None)
    in_features = model.roi_heads.box_predictor.cls_score.in_features
    from torchvision.models.detection.faster_rcnn import FastRCNNPredictor
    model.roi_heads.box_predictor = FastRCNNPredictor(in_features, num_classes)
    return model

# Cargar los pesos ya entrenados
NUM_CLASSES = 4  # ['rump', 'udder'] + background = 3
model = get_model(NUM_CLASSES)
model.load_state_dict(torch.load("best_fasterrcnn_cowparts.pth", map_location='cpu'))
model.eval()
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)
print("Model loaded and ready for inference.")

filename = "WhatsApp Image 2025-11-06 at 14.03.17.jpeg"
image_path = filename
image = cv2.imread(image_path)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
img_tensor = F.to_tensor(image_rgb).to(device)

    # Inferencia
with torch.no_grad():
    outputs = model([img_tensor])

outputs = [{k: v.to('cpu') for k, v in t.items()} for t in outputs]
boxes = outputs[0]['boxes'].numpy()
scores = outputs[0]['scores'].numpy()
labels = outputs[0]['labels'].numpy()

    # Visualización de resultados
CLASS_NAMES = ['__background__', 'cow', 'rump', 'udder']  # cambiar acorde al dataset
conf_thresh = 0.75
for box, score, label in zip(boxes, scores, labels):
    if score < conf_thresh:
        continue
    x1, y1, x2, y2 = map(int, box)
    name = CLASS_NAMES[label]
    color = (0, 255, 0) if name == 'udder' else (255, 0, 0)
    cv2.rectangle(image_rgb, (x1, y1), (x2, y2), color, 2)
    cv2.putText(image_rgb, f"{name} {score:.2f}", (x1, y1 - 5),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

plt.figure(figsize=(10,10))
plt.imshow(image_rgb)
plt.axis('off')
plt.show()
