FROM nvidia/cuda:9.0-cudnn7-devel

RUN apt update
RUN apt upgrade -y
RUN apt install -y python3 python3-pip
RUN pip3 install --upgrade pip
RUN pip3 install tensorflow-gpu keras scikit-learn pillow
COPY . /code