# MUZ
"We know what we are doing, we love what we are doing and we believe in what we are doing"

A team of the NASA Space Apps Challenge 2017.

---

[//]: # (Image References)
[ATI]: './img/ATI logo copia.png'

## THE CHALLENGE | BRING YOUR OWN SOLUTION
Follow your brain and your heart, and present a solution of your own choosing!

# ATI
<video>

### A Flood Early Warning System based on SMS messages

![ATI logo][ATI]

## Mission
This project looks forward to creating a system able to warn people in vulnerable situations on upcoming floods so that they can act in advance.
We are deeply motivated by the [Sustainable Development Goal (SDG) 1.5, adopted by the United Nations General Assembly](https://sustainabledevelopment.un.org/post2015/transformingourworld).
On our first approach, we focused on the local city of Comodoro Rivadavia, Chubut, Argentina. This choice has been made as it was severely damaged by a huge flood last month. This has repeated over the last years. The topology of the surroundings and the rainfall increase make this a vulnerable city.

## How it works
It's actually pretty simple. The system uses data from The Weather Company and runs Machine Learning algorithms to make a forecast of the probability of floods in the next 12 hours. In particular, it takes in measurements of the temperature, barometric pressure, wind direction and speed and clouds shape to make predictions based on an Artificial Intelligence model trained with historical data of the region. When the output probability exceeds a predefined level the system fires an alert. This consists on broadcasting a warning SMS message to every cell phone connected to the antennas near the natural hazard.

## The message
The warning message provides information on shelter locations for people as well as livestock. It also gives critical advice on leaving their belongings at home and danger zones:

```
IMMINENT FLOOD ALERT - 95% probability of flood within the next 12hs in your area.

Your nearest evacuation center is located in Av. San Martin 3944. Go to the center ASAP.

Send 1 for more info on how to protect your loved ones and possessions.

- ATI, your flood early warning system.
```

## Resources
- IBM Bluemix / The Weather Company API
- Keras
- Tensorflow
- Python
- Wisdom