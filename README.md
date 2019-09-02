# Facial Detector
- Wanted a simple way to sort my personal photos and detect whether faces were present in each of them (as I wanted to contribute most photos without faces through google photos/maps)
  - This is based on machine learning so cannot expect the sorting to be 100% accurate!
- Simple script/application/wrapper based on the package [opencv-python](https://github.com/skvark/opencv-python)
  - This package saves all the trouble for installing opencv and the dependencies separately. Simply just do a pip install: ```pip install opencv-python```, and it should work
  - Doesn't even need tweaking any settings and it seemed to work well! 
  (previously played with this and had settings scale_factor=1.1, min_neighbors=8 that seemed to work ok
  - Noticed that it doesn't detect rotated photos for now

