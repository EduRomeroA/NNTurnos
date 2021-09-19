import tensorflow as tf
import numpy as np
import psycopg2
from datetime import datetime, timedelta
from datetime import date


usuarios = [['Eduardo','Kevin','Maria','Edu','Maga','Amanda','Natalia','Joe','Josu','Edison'],
            [0.15,0.45,1,0.95,0,0.55,0.25,1,0.1,0.75,0.85,0.35],
            [20201205,20201205,20201205,20201205,20201205,20201205,20201205,
             20201205,20201205,20201205,20201205,20201205]]
avanc = np.array(usuarios[1], dtype=int)
avance = np.array(usuarios[2], dtype=int)
print(usuarios)
result = np.array([20201207,20201210,20201215,20201214,20201206,20201211,20201207,20201215,
                   20201206,20201213,20201214,20201208], dtype= int)


capa = tf.keras.layers.Dense(units =1, input_shape=[1])
modelo = tf.keras.Sequential([capa])
oculta1 = tf.keras.layers.Dense(units=10, input_shape=([1]))
oculta2 = tf.keras.layers.Dense(units=9)
oculta3 = tf.keras.layers.Dense(units=8)
oculta4 = tf.keras.layers.Dense(units=7)
oculta5 = tf.keras.layers.Dense(units=6)
oculta6 = tf.keras.layers.Dense(units=4)
salida = tf.keras.layers.Dense(units=1)
modelo = tf.keras.Sequential([oculta1, oculta2,oculta3 ,oculta4, oculta5,oculta6, salida])


modelo.compile(
    optimizer= tf.keras.optimizers.Adam(0.01),
    loss = 'mean_squared_error'
)


print("comienzo entrenamientos...")
historial = modelo.fit(avance,result, epochs=1000, verbose=False)
print("modelo etrenado")

def int2date(argdate: int) -> date:
    """
    If you have date as an integer, use this method to obtain a datetime.date object.

    Parameters
    ----------
    argdate : int
      Date as a regular integer value (example: 20160618)

    Returns
    -------
    dateandtime.date
      A date object which corresponds to the given value `argdate`.
    """
    year = int(argdate / 10000)
    month = int((argdate % 10000) / 100)
    day = int(argdate % 100)

    return date(year, month, day)
