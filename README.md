# Facial Detector
- Simple script/application/wrapper to classify whether photos have faces or not
    - Based on the package [opencv-python](https://github.com/skvark/opencv-python)
- Based on machine learning so cannot expect the sorting to be 100% accurate!
- Note: it doesn't detect rotated photos (yet!)

# How to use
## Install
- Download this package (to be published on pip, but for now cd into where this package has been downloaded)
- Install with ```pip install facialdetector```
## Run
- Run with ```python app.py -i /path/to/folder/to/analyse -n 8```
    - This will run with 8 parallel processes (quicker) and analyse a folder of interest