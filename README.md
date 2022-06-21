# YOLOv5 GCP Training and deployment

   
<p>
   
   <img width="850" src="https://github.com/RamonMartin1/const_yolov5/blob/ab0309651d66d88ad636f225f5b5dc61a877c932/YOLOv5%20GCP%20Flowchart.png"></a>
</p>

## In GCP

### Command line for creating instance
<p> gcloud compute instances create <VM_NAME> --project=<PROJECT_NAME> --zone=<ZONE> --machine-type=n1-standard-8 --network-interface=network-tier=PREMIUM,subnet=default --maintenance-policy=TERMINATE --provisioning-model=STANDARD --service-account=<SERVICE-ACC> --scopes=https://www.googleapis.com/auth/cloud-platform --accelerator=count=1,type=nvidia-tesla-p100 --tags=http-server,https-server --create-disk=auto-delete=yes,boot=yes,device-name=<VM_NAME>,image=projects/ubuntu-os-cloud/global/images/ubuntu-2004-focal-v20220610,mode=rw,size=200,type=projects/<PROJECT_NAME>/zones/<ZONE>/diskTypes/pd-ssd --no-shielded-secure-boot --shielded-vtpm --shielded-integrity-monitoring --reservation-affinity=any </p> 

 
   
### Recreating image from snapshot
<p> gcloud compute instances create <VM_NAME> --project=<PROJECT_NAME> --zone=<ZONE> --machine-type=n1-highmem-8 --network-interface=network-tier=PREMIUM,subnet=default --maintenance-policy=TERMINATE --provisioning-model=STANDARD --service-account=<SERVICE-ACC> --scopes=https://www.googleapis.com/auth/cloud-platform --accelerator=count=1,type=nvidia-tesla-v100 --tags=http-server,https-server --create-disk=auto-delete=yes,boot=yes,device-name=<VM_NAME>,mode=rw,size=200,source-snapshot=projects/<PROJECT_NAME>/global/snapshots/<SNAPSHOT_NAME>,type=projects/<PROJECT_NAME>/zones/<ZONE>/diskTypes/pd-ssd --reservation-affinity=any </p> 


   
### CLOUD SHELL JUPYER
<p> if enabled preinstalled jupyter lab from GCP run:  
gcloud compute ssh --project <PROJECT_NAME> --zone <zone> <VM_NAME> -- -L 8081:localhost:8081 </p> 

   

#### FIREWALL RULE
<p> Provide appropriate name. Set Target to “All instances in the network”, <br>  
source filter as “IP ranges” and Source IP ranges as “0.0.0.0/0”. <br>  
Enable the tcp checkbox and set the value as 8080. Click on Create. </p> 


   
### INSTALL CONDA & JUPYTER
<p> ssh into vm  <br>     
sudo apt update <br>  
sudo apt install python3-pip <br>  
cd / <br>  
cd /tmp <br>  
curl https://repo.anaconda.com/archive/Anaconda3-2021.11-Linux-x86_64.sh --output anaconda.sh <br>  
sha256sum anaconda.sh  <br>  
export PATH="$HOME/.local/bin:$PATH" <br>  
bash anaconda.sh <br>  
source ~/.bashrc <br>  
conda list </p> 

<p> jupyter lab --generate-config <br>  
cd to config file <br>  
nano jupyter_lab_config.py <br>  
add these lines to config file <br>  
  c.ServerApp.allow_origin = '*' <br>  
  c.ServerApp.allow_remote_access = True <br>  
  c.ServerApp.ip = '*' <br>  
  c.LabApp.app_dir = 'home/' <br>  
jupyter lab password:  <br>  
    enter password  <br>  
    confirm password  <br>  
jupyter lab --allow-root --port 8081 <br>  
go-to <VM external IP>:8081 </p> 
       

   
### REPO
<p> git clone https://github.com/ultralytics/yolov5 <br>  
cd yolov5  <br>  
pip install -r requirements.txt <br>  
wget https://scut-scet-academic.oss-cn-guangzhou.aliyuncs.com/SODA/2022.2/VOCv1.zip </p> 
       

   
### UNZIP data
<p> need to use 7zip to unzip cause unzip doesnt work on larger files  <br>  
sudo apt install p7zip-full p7zip-rar <br>  
7z x VOCv1.zip (e extracts files without folders, x extracts files with nested subfolder) </p> 
       

   
### RENAMING
<p> delete weird symbols from following file names  <br>  
['annotations/hptm2969¸Ä.xml', <br>  
 'annotations/hptm2970¸Ä.xml', <br>  
 'annotations/hptm2967¸Ä.xml']  <br>  
['images/hptm2967¸Ä.jpg', <br>  
 'images/hptm2969¸Ä.jpg', <br>  
 'images/hptm2970¸Ä.jpg',]  <br>  
delete 'annotations/README.md' <br>  
rename annotations folder to labels </p> 
       

   
### CONVERT & SPLIT
<p> All code for converting .xml labels to .txt is in YOLOv5.ipynb <br>  
run python train.py with all the arguments to train model  </p> 
       

   
### CREATE CACHE
<p> Creating swap memory to -cache large data <br>  
sudo swapoff /swapfile  #clear existing swap <br>  
sudo fallocate -l 16G /swapfile <br>  
sudo chmod 600 /swapfile <br>  
sudo mkswap /swapfile <br>  
sudo swapon /swapfile <br>  
free -h  # check memory </p> 
       

   
### GLIBCXX_3.4.26 ERROR
<p> FINALLY A WORKING FIX to the libstdc++.so.6: version GLIBCXX_3.4.26' not found  <br>  
Confirm GLIBCXX_3.4.26 is missing <br>  
cd /usr/lib/x86_64-linux-gnu/ <br>  
strings libstdc++.so.6 | grep GLIBCXX </p> 
       

<p> To fix run 
wget https://repo.anaconda.com/archive/Anaconda3-2019.07-Linux-x86_64.sh <br>  
sh Anaconda3-2019.07-Linux-x86_64.sh  <br>  
cp anaconda3/lib/libstdc++.so.6.0.26 /usr/lib/x86_64-linux-gnu/ <br>  
rm /usr/lib/x86_64-linux-gnu/libstdc++.so.6 <br>  
ln -s /usr/lib/x86_64-linux-gnu/libstdc++.so.6.0.26 /usr/lib/x86_64-linux-gnu/libstdc++.so.6 </p> 
       

   
### TRAINED MODEL
<p> For trained model go to terraform subfolder the main.py has all the code to run the model.  <br>  
Model itself is best.pt  </p> 
   

   
### ML Ops
<p> Deploy model to Cloud Functions using Terraform <br>  
Setup trigger for Cloud Function to run on data being uploaded to ingestion bucket <br>  
Set daily BigQuerry data transfer from export bucket </p> 
       

       
       
