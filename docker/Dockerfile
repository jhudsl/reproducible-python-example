FROM ubuntu:21.04
RUN apt-get update -qq && apt-get -y --no-install-recommends install \
    git \
    wget

RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh --no-check-certificate
RUN bash Miniconda3-latest-Linux-x86_64.sh -b -p /miniconda
ENV PATH=/miniconda/bin:$PATH


# Attach environment as a kernel in jupyter
COPY environment.yml .
RUN conda env update -f environment.yml

# Install jupyter and its extensions
RUN pip install \
  jupyter \
  jupyter_contrib_nbextensions \
  jupyter_nbextensions_configurator \
  ipywidgets

# Some stuff to get it show up
RUN jupyter kernelspec remove -f python3
RUN python -m ipykernel install --name python3 --display-name "reproducible-python"

RUN rm -rf packages
RUN rm Miniconda3-latest-Linux-x86_64.sh

# enable jupyter extensions
RUN jupyter contrib nbextension install
RUN jupyter nbextensions_configurator enable

# turn on extensions
RUN jupyter nbextension enable collapsible_headings/main
RUN jupyter nbextension enable rubberband/main
RUN jupyter nbextension enable toc2/main
RUN jupyter nbextension enable codefolding/main
RUN jupyter nbextension enable scratchpad/main
RUN jupyter nbextension enable --py widgetsnbextension

ENV NB_USER pythoner
ENV NB_UID 1000

RUN useradd -m -s /bin/bash -N -u $NB_UID $NB_USER

WORKDIR /home/${NB_USER}
USER $NB_USER

EXPOSE 8888
ENTRYPOINT ["jupyter", "notebook", "--no-browser", "--ip=0.0.0.0","--NotebookApp.token=''", "--NotebookApp.password=''"]
