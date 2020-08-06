import os
import numpy as np
import tensorflow as tf
from tensorflow import keras

print(tf.version.VERSION)


test_input = np.random.random((128, 16))
test_target = np.random.random((128, 1))


def create_model():
    model = tf.keras.models.Sequential(
        [keras.layers.Dense(1, activation="relu", input_shape=(16,))]
    )

    model.compile(
        optimizer="adam",
        loss=tf.losses.SparseCategoricalCrossentropy(from_logits=True),
        metrics=["accuracy"],
    )

    return model


# Create a basic model instance
model = create_model()

# Display the model's architecture
model.summary()

checkpoint_path = "model/training_1/cp.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)


cp_callback = tf.keras.callbacks.ModelCheckpoint(
    filepath=checkpoint_path, save_weights_only=True, verbose=1
)


model.fit(test_input, test_target, epochs=10, callbacks=[cp_callback])


model.save("model/my_model")
