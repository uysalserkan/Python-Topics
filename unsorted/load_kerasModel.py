from keras.models import load_model
import tensorflow as tf
import numpy as np
import datetime
# import h5py
start = datetime.datetime.now()
model = load_model('trained_model.h5')


print(model.summary())
end = datetime.datetime.now()
print("Gecen zaman: {}".format(end - start))

# ! Numpy problem solution is
""" pip install --upgrade --force-reinstall numpy """
# ! H5Py error correction
""" pip install --upgrade h5py """
