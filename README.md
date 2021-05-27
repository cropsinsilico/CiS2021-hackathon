# CiS2021-hackathon
Materials for the Hackathon at the 2021 Crops in Silico Symposium &amp; Workshop

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/cropsinsilico/CiS2021-hackathon/HEAD)

## Getting Started

All of the materials for the 2021 Crops in Silico Hackathon can be found in [this repository](https://github.com/cropsinsilico/CiS2021-hackathon).

### Requirements

- Browser (tested on Google Chrome, Safari, Firefox)
- Github Account

### Preparing for the hackathon

- Check that you can sign-in to Github, creating an account as necessary. We will be using Github Issues to track problems encountered during the hackathon.
- Try launching a mybinder instance by clicking on this [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/cropsinsilico/CiS2021-hackathon/HEAD) icon (or the link below). It may take a few moments to initialize. If you encounter an error, open an issue and try with another browser. If you still cannot launch the binder, follow the instruction [here](https://github.com/cropsinsilico/CiS2021-hackathon#running-notebook-locally) for downloading and installing the materials locally.

[https://mybinder.org/v2/gh/cropsinsilico/CiS2021-hackathon/HEAD](https://mybinder.org/v2/gh/cropsinsilico/CiS2021-hackathon/HEAD)

## Useful links

- [Hackathon Repository](https://github.com/cropsinsilico/CiS2021-hackathon)
- [yggdrasil Repository](https://github.com/cropsinsilico/yggdrasil)
- [yggdrasil Documentation](https://cropsinsilico.github.io/yggdrasil/index.html)
- [Additional Examples](https://github.com/cropsinsilico/yggdrasil/tree/main/yggdrasil/examples)
- [Debugging Tips & Documented Errors](https://cropsinsilico.github.io/yggdrasil/debugging.html)

## Running Notebook Locally

### Install Miniconda:

Complete the instruction installing Miniconda for your operating system [here](https://docs.conda.io/en/latest/miniconda.html). Select an installer for Python >=3 (i.e. not 2.7; the installation will still work if you install the 2.7 version, but it will probably be slower).

NOTE: On Windows machines the following commands should be executed from a conda command prompt.

### Download this repository:

```
git clone https://github.com/cropsinsilico/CiS2021-hackathon.git
cd CiS2021-hackathon
```

If you do not have git installed, you can either:

- Install it using conda (`conda install git`) or
- Install it using an OS specific package manager (e.g. apt, homebrew, choco) or
- Download the repo as a ZIP file via the repository webpage (click the green "Code" button and select "Download ZIP")

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

References:

["Plant-2"](https://sketchfab.com/3d-models/plants-2-f4636a80dcec4ca9a29f52fa32182721) by [FALCON](https://sketchfab.com/qewr1324) is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), converted into .obj format with texture and grouping removed.
