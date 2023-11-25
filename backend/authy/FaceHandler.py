import random
import string
from pathlib import Path
from uuid import uuid4

import torch
from PIL import Image
from transformers import DetrImageProcessor, DetrForObjectDetection


def detect_face(imgPath):
    image = Image.open(imgPath).convert("RGB")

    processor = DetrImageProcessor.from_pretrained(
        "facebook/detr-resnet-50", revision="no_timm")
    model = DetrForObjectDetection.from_pretrained(
        "facebook/detr-resnet-50", revision="no_timm")

    inputs = processor(images=image, return_tensors="pt")
    outputs = model(**inputs)

    target_sizes = torch.tensor([image.size[::-1]])
    results = processor.post_process_object_detection(outputs,
                                                      target_sizes=target_sizes,
                                                      threshold=0.9)[0]

    box = []
    for score, label, box in zip(results["scores"], results["labels"],
                                 results["boxes"]):
        box = [round(i, 2) for i in box.tolist()]
        print(
            f"Detected {model.config.id2label[label.item()]} with confidence "
            f"{round(score.item(), 3)} at location {box}"
        )
    photo = image.crop(box)
    rand_strings = ''.join(random.choice(string.ascii_lowercase
                                         + string.digits
                                         + string.ascii_uppercase)
                           for i in range(5))
    file_name = f"{rand_strings}{uuid4().hex}.jpg"
    BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
    path = f'{BASE_DIR}\\media\\faces\\{file_name}'
    photo.save(path)

    return path
