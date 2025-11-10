# Faster R-CNN for Cow Part Detection - TC3007C

This project trains a Faster R-CNN (ResNet-50-FPN backbone) to detect cow body parts using COCO-style datasets. 

It includes dataset splitting, COCO evaluation (mAP/mAR), early stopping, and training/validation curve plotting to monitor overfitting.

Drive link for all the files: [Link Text](https://drive.google.com/drive/folders/1oglVJM3iefNnJLqC83uX7Pv36KOWyGIb?usp=sharing)

## Model Architecture

**Model**: Faster R-CNN with ResNet-50 FPN backbone
**Framework**: PyTorch
**Pretrained weights**: COCO (ImageNet backbone)

After training completes, the outputs are:

- best_fasterrcnn_cowparts.pth → best checkpoint (highest validation mAP)
- FiftyEpochs_fasterrcnn_cowparts_restored.pth → final model restored from best checkpoint
- prediction.jpg → annotated prediction sample
- Training logs printed to console (epoch loss, mAP, mAR)

COCO evaluation provides:

- mAP (mean Average Precision): Average detection precision across IoU thresholds (0.50:0.95)
- mAR (mean Average Recall): Average recall across IoU thresholds (0.50:0.95)
- The script uses pycocotools to summarize these metrics each validation epoch.

## Features 

- COCO-format dataset loader (CowDataset)
- Automatic train/val/test split creation (80/10/10)
- Supports .zip Roboflow COCO exports or existing directories
- Early stopping based on validation mAP
- COCO evaluation using pycocotools
- Visualization of model predictions on sample images
- Training vs Validation curves:
  - Loss (train)
  - mAP & mAR (validation IoU=0.50:0.95)

## Project Structure

train_fasterrcnn_cowparts.py ----------------  # Main training script

cow_dataset/ --------------------------------  # Dataset folder (images + COCO annotations)

best_fasterrcnn_cowparts.pth ----------------  # Best model checkpoint (by validation mAP)

FiftyEpochs_fasterrcnn_cowparts_restored.pth - # Restored best weights

prediction.jpg ------------------------------- # Sample inference visualization

## Requirements:
- Install dependencies

  ```
  pip install torch torchvision pycocotools matplotlib pillow numpy opencv-python
  ```
  
-Optional (for ZIP dataset extraction, which is what i used):

  ```
  pip install zipfile36
  ```

## Usage:

- Option 1 (which is what i used):
  
  ```
  python train_fasterrcnn_cowparts.py --zip vacas.v1i.coco.zip --epochs 50
  ```

  On VCS command prompt:
  
  ```
  >conda activate .\.conda
  >python InferenceTest.py
  ```

- Option 2: Using an existing data directory:
  ```
  python train_fasterrcnn_cowparts.py --data_dir ./cow_dataset --epochs 50
  ```

| Argument         | Description                                      | Default       |
| ---------------- | ------------------------------------------------ | ------------- |
| `--zip`          | Path to COCO-format ZIP dataset                  | `None`        |
| `--data_dir`     | Path to images + annotations folder              | `cow_dataset` |
| `--epochs`       | Maximum number of epochs                         | `50`          |
| `--batch_size`   | Batch size for DataLoader                        | `2`           |
| `--lr`           | Learning rate                                    | `5e-4`        |
| `--patience`     | Early stopping patience                          | `5`           |
| `--score_thresh` | Detection confidence threshold for visualization | `0.3`         |
| `--show`         | Display final prediction image                   | `False`       |

