# CiS2021-hackathon
Materials for the Hackathon at the 2021 Crops in Silico Symposium &amp; Workshop

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/cropsinsilico/CiS2021-hackathon/HEAD)

References:

["Plant-2"](https://sketchfab.com/3d-models/plants-2-f4636a80dcec4ca9a29f52fa32182721) by [FALCON](https://sketchfab.com/qewr1324) is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), converted into .obj format with texture and grouping removed.

## Running Notebook Locally

### Download:

```
git clone https://github.com/cropsinsilico/CiS2021-hackathon.git
cd CiS2021-hackathon
```

### Set up environment:

```
conda env create -f environment.yml
conda activate CiS2021-hackathon-environment
```

### Finish Installing yggdrasil (linux/mac):

```
source postBuild
```

### Finish Installing yggdrasil (windows):

```
call postBuild.bat
```

### Run notebook:

```
jupyter notebook
```
