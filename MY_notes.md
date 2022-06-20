# GCP

### Cloud shell jupyter
gcloud compute ssh \
    --project yolo52\
    --zone us-west1-b \
    deeplearning-1-vm \
    -- -L 8080:localhost:8080

    (Web Preview on port 8080.)(replace deeplearnivng-1 with other instance names)

### REPO
git clone https://github.com/ultralytics/yolov5
cd yolov5
pip install -r requirements.txt
wget https://scut-scet-academic.oss-cn-guangzhou.aliyuncs.com/SODA/2022.2/VOCv1.zip

### 7zip
need to use 7zip to unzip cause unzip doesnt work on larger files
sudo apt install p7zip-full p7zip-rar
7z x VOCv1.zip (e extracts files without folders, x extracts files with nested subfolder)

### VOC viles need renaming
['annotations/hptm2969¸Ä.xml',   
 'annotations/hptm2970¸Ä.xml',
 'annotations/hptm2967¸Ä.xml']   
['images/hptm2967¸Ä.jpg',
 'images/hptm2969¸Ä.jpg',
 'images/hptm2970¸Ä.jpg',]

  'annotations/README.md' delete

### File folders
rename annotations to labels

### 