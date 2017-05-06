# =========================================================================== #
# ATI
# A Flood Early Warning System
# Buenos Aires People's Choice Winner.
#
# Team members:
# - Taboh, Joaquín
# - Schiffmacher, Christian
# - Sampayo, Sebastián  Lucas
# - Fosco, Camilo
#
# * NASA Space Apps Challenge 2017 *
# =========================================================================== #

import numpy as np
import math
from keras.models import Sequential, Model
from keras.layers import Input, GlobalAveragePooling2D, Cropping2D
from keras.layers.core import Dense, Activation, Flatten, Dropout, Merge, Lambda
from keras.layers.convolutional import Convolution2D
from keras.layers.pooling import MaxPooling2D
from keras.models import load_model


# User functions, models and configuration parameters
from params import *
from utils import *
from models import *


# =========================================================================== #
# Model based on paper
def my_model():
  model = Sequential()

  # Normalize to (-1, 1)
  model.add(Lambda(normalize_image), input_shape=in_shape, name='input'))

  model.add(Convolution2D(3, 1, 1, border_mode='same', activation='elu'))
  # model.add(Dropout(0.5))

  model.add(Convolution2D(3, 5, 5, border_mode='same', activation='elu'))
  model.add(Convolution2D(3, 5, 5, border_mode='same', activation='elu'))
  model.add(MaxPooling2D((2, 2)))
  model.add(Dropout(0.5))

  model.add(Convolution2D(24, 5, 5, border_mode='same',activation='elu'))
  model.add(Convolution2D(24, 5, 5, border_mode='same',activation='elu'))
  model.add(MaxPooling2D((2, 2)))

  model.add(Flatten())
  model.add(Dropout(0.5))
  model.add(Dense(10, activation='elu'))
  model.add(Dense(1,name='output'))
  
  return model
  
# =========================================================================== #
# Loads model filename ".h5" file and make trainable only the last layer for feature extraction
def loaded_model(filename='model.h5'):
  print()
  print('Loading model...')
  model = load_model(filename)
  # Set every layer to be not trainable
  for layer in model.layers:
    layer.trainable = False
  # Set to trainable only the last layer
  model.layers[-1].trainable = True
  print('Model loaded.')
  print()
  return model
  
# ----------------------------------------------------------------------------
model = loaded_model()

# ----------------------------------------------------------------------------
# Get the number of samples in the csv
n_train_samples = count_rows(train_log_file)
print('Number of training samples: ', n_train_samples)  
# Augment number of training samples by increasing samples per epoch  
n_train_samples *= augmentation_factor
# Make it multiple of BATCH_SIZE
n_train_samples -= (n_train_samples % BATCH_SIZE)
n_validation_samples = math.floor(n_train_samples * validation_factor)
print('New number of training samples: ', n_train_samples)
print('New number of validation samples: ', n_validation_samples)

# ----------------------------------------------------------------------------
# Configures the learning process and metrics
model.compile(optimizer=optimizer, loss=loss)

# Train the model
if (validation_mode == True):
  print('With validation')
  model.fit_generator(generate_arrays_from_file(train_log_file, BATCH_SIZE),
        samples_per_epoch=n_train_samples, nb_epoch=EPOCHS, 
        validation_data=generate_arrays_from_file(validation_log_file, BATCH_SIZE),
        nb_val_samples=n_validation_samples)
else:
  print('No validation')
  model.fit_generator(generate_arrays_from_file(train_log_file, BATCH_SIZE),
        samples_per_epoch=n_train_samples, nb_epoch=EPOCHS)
  
# ----------------------------------------------------------------------------
# Predictions on test cases
if (predict_mode == True):
    print('Predicting...')
    predictions = model.predict_generator(generate_arrays_from_file(train_log_file, BATCH_SIZE, predict=True), val_samples=n_train_samples)
    print('Output: ', predictions)
    print('Done')
    i = 0
    y = []
    for item in generate_arrays_from_file(train_log_file, BATCH_SIZE):
      j = 0
      for output in item:
        if j == 0:
          j += 1
          continue
        y.append(output)
        j += 1
      i += 1
      if i == 3:
        break

# ----------------------------------------------------------------------------
# Save the model
if (save_mode == True ):
    print('Saving model...')
    model_filename = 'model.h5'
    model.save(model_filename)  # creates a HDF5 file 'model.h5'
    print('Model saved.')

# =========================================================================== #
def VGG16_pretrained():
  # Input layer + preprocessing
  input_tensor = Input(shape=img_shape)
  input_tensor = Lambda(resize,input_shape=img_shape)(input_tensor)
  input_layer = Lambda(normalize_image) (input_tensor)

  # Base model - VGG16
  from keras.applications.vgg16 import VGG16
  base_model = VGG16(input_tensor=input_layer, weights='imagenet', include_top=False)
  
  # Output model
  x = base_model.output
  x = Flatten()(x)
  x = Dropout(0.5) (x)
  output_model = Dense(1, name='output')(x)  

  # this is the model we will train
  model = Model(input=base_model.input, output=output_model)
  # model = Model(input=mid_model.input, output=output_model)

  # first: train only the top layers (which were randomly initialized)
  # i.e. freeze all convolutional InceptionV3 layers
  for layer in base_model.layers:
      layer.trainable = False
      
  return model