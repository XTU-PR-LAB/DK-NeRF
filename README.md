# Overview

We present a dynamic kernel-based deblurring method for Neural Radiance Fields (NeRF), aimed at overcoming the limitations of previous methods that use fixed blur kernels. While prior works successfully address blur caused by camera motion or defocus, they can be inaccurate when blur intensity varies across different scenes and regions. To resolve this issue, the proposed method employs a Mask Convolutional Neural Network to dynamically adjust the blur kernel size for each pixel, allowing for more accurate handling of varying blur speeds and areas. By modifying the kernel size and utilizing weighted aggregation, this approach achieves superior results in reconstructing sharp, detailed 3D scenes from blurred images.

# Training & Evaluation

## 1. Environment
```
pip install -r requirements.txt
```
<details>
  <summary> Dependencies (click to expand) </summary>
  <li>numpy
  <li>scikit-image
  <li>torch>=1.8
  <li>torchvision>=0.9.1
  <li>imageio
  <li>imageio-ffmpeg
  <li>matplotlib
  <li>configargparse
  <li>tensorboardX>=2.0
  <li>opencv-python
  <li>einops
  <li>tensorboard
</details>


## 2. Download dataset
We use the dataset from [Deblur-NeRF](https://github.com/limacv/Deblur-NeRF) to train the DP-NERF. Download the dataset from [here](https://drive.google.com/drive/folders/1_TkpcJnw504ZOWmgVTD7vWqPdzbk9Wx_?usp=sharing). 

There are total of 31 scenes used in the paper, 5 synthetic scene and 10 real-world scene for each blur type: camera-motion blur, defocus blur.

Note that, quantitative evaluation of the `bush` scene in real-defocus dataset is excluded in the paper since there are no clean ground truth image to evaluate.

## 3. Train
For example, to train `blurpool` scene, 
```
python run_nerf.py --config ./configs/blurpool/tx_blurpool_dpnerf.txt --expname $experiment_name
```
The training and tensorboard results will be save in `<basedir>/<expname>` and `<tbdir>`.

## 5. Evaluation

Evaluation is automatically executed every `--i_testset` iterations.
Please refer the other logging options in `run_nerf.py` to adjust save and print the results.

After the training, execute the evaluation results following command.
For example, to evaluate `blurpool` scene after 200000 iteration,
```
python run_nerf.py --config ./configs/blurpool/tx_blurpool_dpnerf.txt --expname $dir_to_log --ft_path ./<basedir>/<expname>/200000.tar --render_only --render_test
```

# Visualization
You can render or save the results after 200000 iteration of training following process.

## 1. Visualization of trained model

### Visualize the trained model as videos of spiral-path.
Results will be saved in `./<basedir>/<dir_to_log>/renderonly_path_199999`.

```
python run_nerf.py --config ./configs/blurpool/tx_blurpool_dpnerf.txt --expname $dir_to_log --ft_path ./<basedir>/<expname>/200000.tar --render_only 
```

### Visualize the trained model as images of training views in datasets.
Results will be saved in `./<basedir>/<dir_to_log>/renderonly_test_199999`

```
python run_nerf.py --config ./configs/blurpool/tx_blurpool_dpnerf.txt --expname $dir_to_log --ft_path ./<basedir>/<expname>/200000.tar --render_only  --render_test
```

## 2. Save the warped poses and images

Results will be saved in `./<basedir>/<dir_to_log>/warped_ray_img_path_199999`

```
python run_nerf.py --config ./configs/blurpool/tx_blurpool_dpnerf.txt --expname $dir_to_log --ft_path ./<basedir>/<expname>/200000.tar --save_warped_ray_img
```

# Notes

## GPU memory 

Training requires progressively large memory as the number of rigid motion increases. 
This is the same drawback as the baseline.
If you have not enough memory to train on your single GPU, set `N_rand` to a smaller value, or use multiple GPUs.

## Multi-GPUs training

To train the DP-NeRF with multiple gpus, please set `num_gpu=<num_gpu>`.

## Original NeRF training

To train original NeRf, set `blur_model_type = none`.

## Acknowledgement

We sincerely thank the authors of [DP-NeRF](https://github.com/dogyoonlee/DP-NeRF) for their excellent foundational research and open-source implementation, which provided valuable inspiration and support for our improvements.
