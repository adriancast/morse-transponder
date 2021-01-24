# morse-transponder
UIB exercice to build a client-server app to translate and play morse text

This repository was tested in macOS Big Sur. If you have problems playing the sounds maybe its because you do not have installed the proper audio player. In macOS execute the following command:
```
pip install -U PyObjC
```
# How to use it

1. Create a virtualenv with python 3.6 and install the dependencies
2. Start the morse transponder server
```
python server.py
```
3. Launch a client
```
python client.py
```

If you want to check the result without running the code, check the demo.mov file 😉

