FROM jupyter/minimal-notebook
MAINTAINER cansav09@gmail.com

COPY environment.yml .
RUN conda env create -f environment.yml

# Pull the environment name out of the environment.yml
RUN echo "source activate $(head -1 environment.yml | cut -d' ' -f2)" > ~/.bashrc
ENV PATH /opt/conda/envs/$(head -1 environment.yml | cut -d' ' -f2)/bin:$PATH
