# Thesis File Structure

## Overview
This repository contains files and results from the thesis research on fine-tuning object detection models for FDM additive manufacturing. The structure is divided into three main sections:

1. **Final Model and Python Code for Local Run** – Contains the final implementation and trained model (See their respective **ReadMe.md** files inside folder).
2. **ML Algorithm Comparison** – Stores performance comparisons of different models .pynb file where we can see all training code and result inside it.
3. **YOLO Fine-Tuning** – Includes fine-tuning experiments on small and large datasets.

**Refer inside the thesis folder for the High-Level File Organization Chart.**
---

## 1. Final Model and Python Code for Local Run
This section includes all necessary files to execute the final trained model locally. 
To run our model locally, only this folder is required; the rest are experiments and comparisons. 

### **Python Code for Locally Run**
- `V11s/`
  - `alarm.mp3` – Audio notification file.
  - `best.pt` – Final trained YOLO model.
  - `main.py` – Python script to run the trained model.
  - `ReadMe.txt` – Additional instructions for execution.
- `.idea/` – Project-specific settings for IDE.

### **Training Code (.ipynb)**
- `In_process_defect_monitoring_Using_Computer_Vision_for_FDM_Additive_Manufacturing.ipynb` – Notebook containing the final training procedure with last optimized hyperparameters.

### **Live DEMO Vidio file link** 
---

## 2. ML Algorithm Comparison
This section evaluates different machine learning models for object detection to identify the best one for real-time detection, which is most preferable in our case.
We chose this model from many available options based on our requirements.

- `Baseline_YOLOv11s_0.855.ipynb` – YOLO baseline model results.
- `Faster R-cnn_ResNet50_Detectron 2_0.828.ipynb` – Faster R-CNN model implementation.
- `Rtdetr_50vd_COCO_0.730.ipynb` – Results from RT-DETR model.
- `SSD_movilenet_v2_0.791.ipynb` – Results from SSD MobileNetV2 model.

Each file contains model training code, validation, and performance metrics for evaluation.

---

## 3. YOLO Fine-Tuning
Fine-tuning experiments conducted on different datasets to optimize hyperparameters.

### **3.1 Small Dataset**
- `20 Tuning to fine optimal hyperparameter/`
  - `20 iteration Tuner Initialized Tuner instance wi.txt` – Log of tuning iterations.
  - Various `.png` and `.txt` files – Hyperparameter performance at different iterations.

### **3.2 Big Dataset**
- **Fine-Tuning_All_Experiments/** – Results from large dataset experiments.
  - `Map0.50 comparison of all model.xlsx` – Performance comparison of all models.
  - Multiple result `.csv` files for each tuning experiment.
  - Various `.png` files showing graphical performance insights.

Each subfolder contains results from experiments with different hyperparameter sets, sorted by performance.


## Authors & Acknowledgments
This research was conducted using open-source model and tools. Special thanks to:

- **YOLO** - Open-source object detection framework Developed by Ultralytics.
- **Detectron2** - Facebook AI's object detection library.
- **SSD MobileNet** - A lightweight detection model from Tenserflow API.
- **RT-DETR** - Real-time detection transformer developed by Baidu Research.

Dataset collection from TC campus, Which also avalible on request.
All contributions and open-source resources are greatly appreciated.


