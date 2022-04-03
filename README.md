# Indoor Scene Recognition

## Final Web Application :
![finalimage](https://user-images.githubusercontent.com/61115039/161431485-8d36faaf-d31e-49e2-be50-037a918d068f.PNG)

## Web application Link of AZURE Cloud: https://indoorfound.azurewebsites.net/


## Description :
Indoor scene recognition is a challenging open problem in high level vision. Most scene recognition models that work well for outdoor scenes perform poorly in the indoor domain. The main difficulty is that while some indoor scenes (e.g. corridors) can be well characterized by global spatial properties, others (e.g., bookstores) are better characterized by the objects they contain. More generally, to address the indoor scenes recognition problem we need a model that can exploit local and global discriminative information.
The model used is Resnet101v2 and provide 86% accuracy.

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

### Model Details
![datamodel](https://user-images.githubusercontent.com/61115039/161432019-2db0fedf-3537-4f40-8f23-8e3f13ddb800.PNG)

### Training Results
![results](https://user-images.githubusercontent.com/61115039/161432067-4e79f238-8872-44f7-a57d-76c5809a67f5.PNG)

### Final Video of Classifier
https://user-images.githubusercontent.com/61115039/161432444-b8bc7768-b4aa-4098-820a-526b87a1f176.mp4

## References
A. Quattoni, and A.Torralba. Recognizing Indoor Scenes. IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2009.

## :heart: Owner
Made with :heart:&nbsp;  by [Aman Chauhan](https://github.com/amanchauhan71)

### How to reach me 📱
[<img target="_blank" src="https://img.icons8.com/cotton/64/000000/whatsapp--v4.png"/>](https://wa.me/919997600372)[<img target="_blank" src="https://img.icons8.com/doodle/64/000000/linkedin-circled.png"/>](https://www.linkedin.com/in/aman-chauhan-42bb9273/)

