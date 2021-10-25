FROM jupyter/datascience-notebook:python-3.9.6
LABEL maintainer="cansav09@gmail.com"

USER root

# Create the environment:
COPY environment.yml .
RUN conda env create -f environment.yml

# Activate the environment, and make sure it's activated:
RUN conda activate reproducible-python
