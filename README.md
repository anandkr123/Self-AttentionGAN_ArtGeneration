# Self-AttentionGAN_ArtGeneration
Creative Art Generation using Self-Attention GAN's

## Application code
The code in all contains 6 files. Below is the explanation to all of the files used in the project.

### download.py
This file contains separate methods to download dataset from different sources. 
To run the project on a custom dataset, create a folder named 'dataset' and put the custom images folder inside it. Below is the folder architecture for the same.

For custom dataset, put images like this:dataset/DATASET_NAME/...........(all images)

### SAGAN.py
The file contains generator, discriminator, attention mechanism and the methods to build the model. All necessary steps related to training epochs such as model saving, model loading, saving images during training and test phase are implemented here.

### main.py
This is the file where all the arguments are passed and SAGAN.py file is executed using TensorFlow (library for neural network) session.

### utils.py
This file contains the image preprocessing functions like crop, transform. These functions can beused to prepare the image dataset for example to merge and visualizing the individual images generated during training and test phase , saving and resizing the images as needed by the user.  All the functions are available in the files which can be used as it or modified according to the requirement.

### ops.py
This file contains the functions for convolution layer, deconvolution layer, batch normalization, different loss functions and other TensorFlow built-in functions. User implemented functions such as spectral normalization, up-resblock and down-resblock functions are also there. So, any changed related to model operated on image can be done here. This file is not changed mostly as it contains the built-in functions of TensorFlow.

### data_pre_processing.py
All operations performed on image before training are done here. It is specific to the kaggle dataset used as it uses the dataset and .csv file to sort the images. This file contains two methods ‘sort_images’ and ‘prepare data’. At first, run the sort images function so as to arrange the data to user specific genre. And secondly run the ‘prepare_data’ method to resize the images, remove grayscale images  if any, as there were some gray scale images mixed when downloading it from kaggle and finally saving the images into a specific folder.

## Steps to train the model

1. Prepare your custom dataset folder with any name containing all the images and move it in a   folder called ‘dataset’.
You will have a dataset folder along with all the above required files mentioned above.

1. Start training your model

***python main.py --phase train(this tells the model that you want to train, but it starts to pick up the last saved model if it was interrupted before) --dataset ‘YOUR DATASET NAME’ --gan_type hinge( which type of loss function you want to use, different loss functions are implemented in ops.py ).***

During the training phase, the model after every 500 iterations( you can change the argument from the main.py) will be saved in a directory called checkpoint which is created by itself.

3. Start testing your model
Just replace the phase with the test itself. This generates the images based on the trained model. One can change the number of images generated from the arguments in the main.py file.

Example :- ***python main.py --phase test --dataset ‘YOUR DATASET NAME’ --gan_type hinge***

Notes:-
for saving each generated image individually(otherwise grid wise collection of images) during test or train phase uncomment the code in ‘utils.py’ under merge method.

for increasing the resolution to 256x256x3 uncomment the code in SAGAN.py in generator.

Art dataset of images -  https://www.kaggle.com/c/painter-by-numbers/data information for train image data in ‘train_info.csv’FIND MORE SOURCES TO THE ART DATASETS https://www.reddit.com/r/MachineLearning/comments/6ecfa2/d_art_datasets/


### Steps to connect to Google colab. 
1. open your google drive and Click on New→ More→ Connect More Apps
2. Add ‘Google Colaboratory’ to your drive.
3. Upload your complete Project on Google drive.
4. A folder though will already be created by the name ‘Colab Notebooks’
5. Go to colab.reaearch.google.com. Create New python .ipynb file.
6. You can start running the code from that .ipynb file itself.
7. To mount the google drive and start to run your code, the steps are as follows

In the untitled.ipynb file, run the below individual line as in a jupyter notebook
 
step 0:-At first change the HARDWARE ACCELERATOR TO GPU from runtime 

step 1:- from google.colab import drive 

