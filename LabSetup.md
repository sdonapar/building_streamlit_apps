# Lab Setup instructions

</br>

### It is highly recommend to create a virtual environment and install the dependencies.

</br>

### Please install [miniconda](https://docs.conda.io/en/latest/miniconda.html) if you don't have conda installer already

</br>

### if you are using other virtual env tools, please install Python 3.8.10 and use `requirements.txt` file for creating the virtual environment.

</br>

## Instructions - installing using conda:

</br>

1.  Please chnage the following line at the end of the environment.yaml file to the path
where the virtual env should be created

</br>

```
prefix: /home/<user>/miniconda3/envs/pyconws
```

</br>


2. Create virtual environment

</br>

```
conda create -f ./environment.yaml
```
</br>

3. Activate conda environment

</br>

```
conda activate pyconws
```

4. Download Spacy language models

</br>

```
python -m spacy download en_core_web_sm
```
Above language model is a small one
if you have enough bandwidth download other medium and large language models also

</br>

```
python -m spacy download en_core_web_md
```

</br>


```
python -m spacy download en_core_web_lg
```


### I will be using **visual studio code** IDE for the workshop
### You can install the same or your preferred choice of IDE

</br>

[Home](./README.md)
