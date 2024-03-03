# Porject Title : Image Processing Using Transfer learning on Brain MRI Data 

Brain Tumors are complex. There are a lot of abnormalities in the sizes and location of the brain tumor(s). This makes it really difficult for complete understanding of the nature of the tumor. Also, a professional Neurosurgeon is required for MRI analysis. Often times in developing countries the lack of skillful doctors and lack of knowledge about tumors makes it really challenging and time-consuming to generate reports from MRI’. So an automated system on Cloud can solve this problem.

More information about this Project.

1. Problem Statement-
    To Detect and Classify Brain Tumor using CNN and Transfer Learning ; as an asset of Deep Learning and to examine the tumor.

2. Sources:
   (a) Date:    3rd Mar 2024. (Project Date)

3. Dataset-

    data that can be downloaded at:
https://www.kaggle.com/datasets/sartajbhuvaji/brain-tumor-classification-mri


4. Techniques and Algorithms used -

     1. Model - Used a bottleneck feature of pretrained VGG-16 Network with Fully Connected layers and initialized all the weights with Imagenet trained weights.

5. Conclusions-
    1. Model_1:
        1. Got validation accuracy of 0.70 after 100 epochs.
        2. the variance of the validation accuracy is fairly high, because accuracy is a high-variance metric and because we only use few sample images.
        4. A good validation strategy in such cases would be to do k-fold cross-validation, but this would require training k models for every evaluation round.



         

