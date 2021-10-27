# Reproducible analysis example - Python

This is an example project repository to illustrate what a reproducible analysis might look like as discussed in more detail in the [Reproducibility in Cancer Informatics course](https://github.com/jhudsl/Reproducibility_in_Cancer_Informatics).  
It can be used as a template or otherwise borrowed from.

_This example analysis:_  

- Downloads [data from refine.bio](https://www.refine.bio/experiments/SRP070849/combination-targeted-therapy-to-disrupt-aberrant-oncogenic-signaling-and-reverse-epigenetic-dysfunction-in-idh2-and-tet2-mutant-acute-myeloid-leukemia-rna-seq) using the [refine.bio python API client](https://github.com/AlexsLemonade/refinebio-py).
- Identifies the top 90th percentile variant genes from the set.
- Creates and saves a heatmap from those genes.

It also has its own Docker image and GitHub actions to aid reproducibility.

## Requirements

To run this analysis you will need [`git`](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and [`Docker`](https://docs.docker.com/get-docker/) installed on your computer.
These are two platforms that are very useful for reproducibility so they will be useful for you far beyond this repository.

## How to run the analysis

To re-run this analysis within its Docker image, open up your Terminal/Command Prompt.

1. First you can obtain a local copy of this repository by `git clone`-ing it.
```
git clone https://github.com/jhudsl/reproducible-python-example.git
```
2. Now navigate to the top of this repository.
```
cd reproducible-python-example
```
3. Use the following command to run the analysis:  
```
docker run \
--mount type=bind,target=/home/jovyan/work,source=$PWD \
  jhudsl/reproducible-python \
  jupyter nbconvert --execute work/make_heatmap.ipynb --to notebook --inplace
```

## make_heatmap.ipynb

## Input

The [dataset used by this analysis](https://www.refine.bio/experiments/SRP070849) is downloaded already [processed and quantile normalized](http://docs.refine.bio/en/latest/main_text.html#refine-bio-processed-refinebio-processedibadge) from refine.bio using their API.
It is RNA-seq data from 19 acute myeloid leukemia (AML) mice models.

## Output

Two directories are created by this analysis and hold the output:  

`plots/` - contains the heatmap png: `aml_heatmap.png`
`results/` - contains the TSV file list of most variant genes: `top_90_var_genes.tsv`

## Docker

### Running the Python docker image for development purposes

With your current directory being the top of this repository, run this command in your Terminal:
```
docker run --rm -v $(pwd):/home/jovyan/work -e JUPYTER_ENABLE_LAB=yes -p 8888:8888 jhudsl/reproducible-python
```
Then navigate to the port that the output tells you (you may have to try both links, sometimes only one of them works).
This command will pull the most recent docker image from Dockerhub if you do not have it locally.

### Rebuilding the docker image locally

If you prefer to build the image locally, or have otherwise modified the Dockerfile and want to test if it builds, you can run this command from the top of the repository:
```
docker build -f docker/Dockerfile . -t jhudsl/reproducible-python
```
Running `docker ps` should show you the `jhudsl/reproducible-python` listed with your images

## Github actions

There are two main GitHub actions in this repository:  

- `docker-management.yml` - Tests the building of the docker image upon changes to the `Dockerfile` being added to a pull request.
- `run-py-notebook.yml` - Re-runs the analysis by running `make_heatmap.ipynb` within the docker image (using the [command described above](#how-to-run-the-analysis)).

Both GitHub actions have the option [to be run manually](https://docs.github.com/en/actions/managing-workflow-runs/manually-running-a-workflow).
The Docker management GitHub actions also has the option to push the re-built Docker image to Dockerhub by setting `dockerhubpush` to `true`.
