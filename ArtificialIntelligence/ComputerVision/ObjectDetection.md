# R-CNN

Rich Feature Hierarchies for Accurate Object Detection and Semantic Segmentation

论文地址：https://www.cv-foundation.org/openaccess/content_cvpr_2014/html/Girshick_Rich_Feature_Hierarchies_2014_CVPR_paper.html

根据图像局部特征划分出子图，最后通过卷积网络（AlexNet）输出，每个子图都会蒸馏出一个特征向量，为 4096 维，最后通过 SVM 进行分类

![image-20250705145408164](../../assets/image-20250705145408164.png)
