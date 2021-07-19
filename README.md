[![](http://github-actions.40ants.com/USGS-Astrogeology/PyHAT_Point_Spectra_GUI/matrix.svg)](https://github.com/USGS-Astrogeology/PyHAT_Point_Spectra_GUI)
<img src="https://raw.githubusercontent.com/USGS-Astrogeology/PyHAT_Point_Spectra_GUI/master/images/splash.png" width=500>

## Installation


### 1. Install Anaconda (Skip to step 2 if you have Anaconda/Miniconda)

Install <a href="https://www.anaconda.com/download/">Anaconda</a>. Be sure to choose the Python 3.x version!


### 2. Open a terminal (on Windows, use the Anaconda prompt that gets installed with Anaconda) and type:

```bash
conda config --add channels conda-forge #This ensures that your conda is connected to the conda-forge channel where many pagkages live
conda create -n pyhat_gui # This creates a new environment named pyhat_gui. Substitute your preferred name if desired.
conda activate pyhat_gui #this activates the environment
conda install -c usgs-astrogeology ppsg # This installs the PyHAT Point Spectra GUI (ppsg) package from Anaconda
```

### 3. Done! How to use point_spectra_gui
From the terminal type:

```bash
conda activate pyhat_gui  # This activates the environment where the tool is installed
python -m point_spectra_gui # This runs the GUI
```

### 4. Update an existing installation

If you already have an earlier version of the PyHAT Point Spectra GUI installed as described above and you want to wipe it and update to the latest version, just do:

```bash
conda env remove -n pyhat_gui #removes the environment
conda clean -a #removes old cached versions of packages
```
And then follow the instructions above to install a fresh version.

### Bugs

Run into bugs or features that are missing? Let us know by reporting an issue!

- The UI's backend is designed and created in Python with the QT framework
