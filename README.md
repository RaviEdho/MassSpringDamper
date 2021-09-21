# MassSpringDamper
Small program built to simulate a mass-spring-damper model on Python.

Originally made as Modelling and Simulation task.

## Usage
The program was specifically built to simulate and iterate the deviation of the object from the equilibrium in a mass-spring-damper model as seen on Figure 1


![Figure 1](/resources/Figure1.png)<br />*Figure 1*

For example, the program was fed with the following parameters:
| Parameter  | Value |
| ------------- | ------------- |
| Massa Objek  | 1100  |
| Konstanta Pegas  | 1200000  |
| Koefisien Peredaman  | 13000  |
| Simpangan awal  | 0.2  |
| Waktu pengamatan | 3  |
| Jumlah pengamatan  | 60  |

Program then calculate the iteration of deviation 60 times, distributed evenly on the span of 3 seconds.

And then produces following result.

| No |   t  |  Simpangan  |
| ------------- | ----- | ------------- |
|  0 | 0.00 |  0.20000000 |
|  1 | 0.05 |  0.01899130 |
|  2 | 0.10 | -0.11229050 |
|  3 | 0.15 | -0.00149627 |
|  4 | 0.20 |  0.06230934 |
|  5 | 0.25 | -0.00417734 |
|  6 | 0.30 | -0.03417277 |
|  7 | 0.35 |  0.00505899 |
|  8 | 0.40 |  0.01851924 |
|  9 | 0.45 | -0.00428965 |
| 10 | 0.50 | -0.00991176 |
| . | . |  . |
| . | . |  . |
| 58 | 2.90 |  0.00000001 |
| 59 | 2.95 |  0.00000000 |
| 60 | 3.00 | -0.00000000 |

It also pops up another window of image that shows the plot of deviation of object from equilibrium against time, as seen on Figure 2.

![Figure 2](/resources/Figure2.png)<br />*Figure 2*
