![Screenshot 2023-04-19 074732](https://github.com/Rex123774/Face-frontalization-using-TP-GAN/assets/77051661/8e7a9fb5-2f8e-4aab-847c-ec1552817b41)
# Face-frontalization-using-TP-GAN
Face frontalization is the process of synthesizing frontal views of faces from non-frontal images. 
TP-GAN, or Temporal Prior GAN, is an approach that utilizes temporal information to improve the quality of face frontalization.
For this project NVIDIA Super RTX 2070/60 model is used because this project uses 16GB GPU storage(8GB is used for users of gpu and another 8GB is used for Nvidia)
Steps for processing the project
Step1:- Download the repository
Step2:- Download anaconda 2019 version because if we use other type of version then this project will not work
Step3:-Step up GPU with the anaconda 2019 version
Step4:-Use the environmental file from my repository
Step5:-Run multipie_gen.py
Step6:-Run Tpgan.py and then Run Train.py
3200 epochs is used to train the model which means two weeks is required to fully train the project
If the project is not working upto 3200 epochs then we have reduce the batch size limit to less than 2
As we increase the size of the epoch then image quality gets increased , but the flaws of this project is as follows
A)As I have mention the storage of the gpu above this model compeletely needs 16GB empty GPU storage because this project is having verry high depricated memory and if use only 8GB GPU storage(4GB is used for users of gpu and another 4GB is used for Nvidia) then this project will completely get crashed because of the depricated memory(Please read this note carefully)
B)As we know 3200 epochs = higher quality improvement but this model still needs an improvement and for that I have used Super Resolution model , Image Toonification model and Stable Diffusion model(To use these models then you have to use my previous repositories)
C)This model generates random frontal images so in order to check the distance between the images we have used lpips model 
[Link Text]https://drive.google.com/drive/uc?id=12FZpvPKc5XEIv26mYH40GXvQYKKHxjXD?&export=download
This the google drive link to download main things of the project
