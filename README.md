# Indoor Scene Recognition

## Final Web Application :
![finalimage](https://user-images.githubusercontent.com/61115039/161431485-8d36faaf-d31e-49e2-be50-037a918d068f.PNG)

## Web application Link of AZURE Cloud : https://indoorfound.azurewebsites.net/


## Description :
Indoor scene recognition is a challenging open problem in high level vision. Most scene recognition models that work well for outdoor scenes perform poorly in the indoor domain. The main difficulty is that while some indoor scenes (e.g. corridors) can be well characterized by global spatial properties, others (e.g., bookstores) are better characterized by the objects they contain. More generally, to address the indoor scenes recognition problem we need a model that can exploit local and global discriminative information.

## Database :
The database contains 67 Indoor categories, and a total of 15620 images. The number of images varies across categories, but there are at least 100 images per category. All images are in jpg format. The images provided here are for research purposes only.
https://web.mit.edu/torralba/www/indoor.html

## Pre-Requisites
- NumPy
- Pandas
- Scikit-image
- IPython
- Matplotlib
- Tensorflow 2.X
- Keras
- AZURE Cloud

### Installation
**Dependencies:**
```
# With Tensorflow CPU
git clone <repository name> 
pip install -r requirements.txt

# With Tensorflow GPU
pip install -r requirements-gpu.txt
```
**Nvidia Driver (For GPU, if you haven't set it up already):**
```
# Ubuntu 20.04
sudo apt-add-repository -r ppa:graphics-drivers/ppa
sudo apt install nvidia-driver-430

# Windows/Other
https://www.nvidia.com/Download/index.aspx
![example images](https://i.imgur.com/Mp2Te2Y.png)

```
## Approach
### Data Augmentation
Data augmentation is done through the following techniques:
- Rescaling (1./255)
- Shear Transformation (0.2)
- Zoom (0.2)
- Horizontal Flipping
- Rotation (20)
- Width Shifting (0.2)
- Height Shifting (0.2)

