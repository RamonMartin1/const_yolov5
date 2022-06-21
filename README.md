# YOLOv5 GCP Training and deployment

   
<p>
   
   <img width="850" src="https://github.com/RamonMartin1/const_yolov5/blob/ab0309651d66d88ad636f225f5b5dc61a877c932/YOLOv5%20GCP%20Flowchart.png"></a>
</p>

## In GCP
<br>

### Command line for creating instance
gcloud compute instances create <VM_NAME> --project=<PROJECT_NAME> --zone=<ZONE> --machine-type=n1-standard-8 --network-interface=network-tier=PREMIUM,subnet=default --maintenance-policy=TERMINATE --provisioning-model=STANDARD --service-account=<SERVICE-ACC> --scopes=https://www.googleapis.com/auth/cloud-platform --accelerator=count=1,type=nvidia-tesla-p100 --tags=http-server,https-server --create-disk=auto-delete=yes,boot=yes,device-name=<VM_NAME>,image=projects/ubuntu-os-cloud/global/images/ubuntu-2004-focal-v20220610,mode=rw,size=200,type=projects/<PROJECT_NAME>/zones/<ZONE>/diskTypes/pd-ssd --no-shielded-secure-boot --shielded-vtpm --shielded-integrity-monitoring --reservation-affinity=any

<br>   
### Recreating image from snapshot
gcloud compute instances create <VM_NAME> --project=<PROJECT_NAME> --zone=<ZONE> --machine-type=n1-highmem-8 --network-interface=network-tier=PREMIUM,subnet=default --maintenance-policy=TERMINATE --provisioning-model=STANDARD --service-account=<SERVICE-ACC> --scopes=https://www.googleapis.com/auth/cloud-platform --accelerator=count=1,type=nvidia-tesla-v100 --tags=http-server,https-server --create-disk=auto-delete=yes,boot=yes,device-name=<VM_NAME>,mode=rw,size=200,source-snapshot=projects/<PROJECT_NAME>/global/snapshots/<SNAPSHOT_NAME>,type=projects/<PROJECT_NAME>/zones/<ZONE>/diskTypes/pd-ssd --reservation-affinity=any

 <br>  
### Cloud shell jupyter
gcloud compute ssh \
    --project <PROJECT_NAME>\
    --zone <zone> \
    <VM_NAME> \
    -- -L 8081:localhost:8081

       <br>
#### FIREWALL RULE
Provide appropriate name. Set Target to “All instances in the network”, 
source filter as “IP ranges” and Source IP ranges as “0.0.0.0/0”. 
Enable the tcp checkbox and set the value as 8080. Click on Create.

<br>       
### INSTALL CONDA & JUPYTER
ssh into vm       
sudo apt update
sudo apt install python3-pip
cd /
cd /tmp
curl https://repo.anaconda.com/archive/Anaconda3-2021.11-Linux-x86_64.sh --output anaconda.sh
sha256sum anaconda.sh
export PATH="$HOME/.local/bin:$PATH"
bash anaconda.sh
source ~/.bashrc
conda list

jupyter lab --generate-config
cd to config file
nano jupyter_lab_config.py
    add these lines to config file
        c.ServerApp.allow_origin = '*'
        c.ServerApp.allow_remote_access = True
        c.ServerApp.ip = '*'
        c.LabApp.app_dir = 'home/'
jupyter lab password:
    enter password
    confirm password

jupyter lab --allow-root --port 8081 
go-to <VM external IP>:8081
       
<br>
### REPO
git clone https://github.com/ultralytics/yolov5
cd yolov5
pip install -r requirements.txt
wget https://scut-scet-academic.oss-cn-guangzhou.aliyuncs.com/SODA/2022.2/VOCv1.zip
       
<br>
### UNZIP data
need to use 7zip to unzip cause unzip doesnt work on larger files
sudo apt install p7zip-full p7zip-rar
7z x VOCv1.zip (e extracts files without folders, x extracts files with nested subfolder)
       
<br>
### RENAMING
delete weird symbols from following file names
['annotations/hptm2969¸Ä.xml',   
 'annotations/hptm2970¸Ä.xml',
 'annotations/hptm2967¸Ä.xml']   
['images/hptm2967¸Ä.jpg',
 'images/hptm2969¸Ä.jpg',
 'images/hptm2970¸Ä.jpg',]

delete 'annotations/README.md'
rename annotations folder to labels
       
<br>
### Convert the labels and do test/train split
All code for converting .xml labels to .txt is in YOLOv5.ipynb
run python train.py with all the arguments to train model 
       
 <br>    
### Creating swap memory to -cache large data
sudo swapoff /swapfile  #clear existing swap
sudo fallocate -l 16G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
free -h  # check memory
       
<br>
### FINALLY A WORKING FIX to the libstdc++.so.6: version GLIBCXX_3.4.26' not found 
Confirm GLIBCXX_3.4.26 is missing
cd /usr/lib/x86_64-linux-gnu/
strings libstdc++.so.6 | grep GLIBCXX
       

To fix run 
wget https://repo.anaconda.com/archive/Anaconda3-2019.07-Linux-x86_64.sh
sh Anaconda3-2019.07-Linux-x86_64.sh 
cp anaconda3/lib/libstdc++.so.6.0.26 /usr/lib/x86_64-linux-gnu/
rm /usr/lib/x86_64-linux-gnu/libstdc++.so.6
ln -s /usr/lib/x86_64-linux-gnu/libstdc++.so.6.0.26 /usr/lib/x86_64-linux-gnu/libstdc++.so.6
       
 <br>      
### Trained Model
For trained model go to terraform subfolder the main.py has all the code to run the model. 
Model itself is best.pt 
   
 <br>     
### ML Ops
Deploy model to Cloud Functions using Terraform
Setup trigger for Cloud Function to run on data being uploaded to ingestion bucket
Set daily BigQuerry data transfer from export bucket
       

       
       
