import tensorflow as tf
import numpy as np
# import h5py
from keras.models import load_model
model = load_model('trained_model.h5')


print(tf.__version__)


# ! Numpy problem solution is
""" pip install --upgrade --force-reinstall numpy """
# ! H5Py error correction
""" pip install --upgrade h5py """
