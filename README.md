# Meta Graph Learning for Long-tail Recommendation

This repository is the official implementation of MGL.

## Requirements

To install requirements:

```setup
conda env create -f environment.yaml
```

## Data Process

To prepare the data for the model training:

```setup
python data_process.py
```

## Training

To train the model(s) in the paper:

```setup
python train.py
```
> Output: the file "model.tar"

## 改动：
用newenv.yaml构建，pip_install.sh中的pip运行一遍，剩下的运行时再安装：
1. 安装pytorch：
```shell
pip install torch==1.7.0 -f https://download.pytorch.org/whl/torch_stable.html
```
	
2. 安装pytorch对应版本的torch_sparse,torch_scatter
   ```shell
	pip install torch_sparse==0.6.9 -f https://pytorch-geometric.com/whl/torch-1.7.0%2Bcu110.html
    pip install torch_scatter==2.0.7 -f https://pytorch-geometric.com/whl/torch-1.7.0%2Bcu110.html
   ```
