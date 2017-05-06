# ATI - Flood Early Warning System
"A simple solution to a worlwide problem"

A team of the NASA Space Apps Challenge 2017.

---

[//]: # (Image References)
[ATI]: ./img/ATI%20logo%20copia.png

## THE CHALLENGE | BRING YOUR OWN SOLUTION
Follow your brain and your heart, and present a solution of your own choosing!

# ATI
<video>

### A Flood Early Warning System based on SMS messages

![ATI logo][ATI]

## Mission
This project looks forward to creating a system able to warn people in vulnerable situations on upcoming floods. This allows them to be prepared and act in advance. We are deeply motivated by the Sustainable Development Goal (SDG) 1.5, adopted by the United Nations General Assembly."By 2030, build the resilience of the poor and those in vulnerable situations and reduce their exposure and vulnerability to climate-related extreme events and other economic, social and environmental shocks and disasters."

On our first approach, we focused on the local city of Comodoro Rivadavia, Chubut, Argentina. This choice has been made as it was severely damaged by a huge flood last month. This has repeated over the last years. The topology of the surroundings and the climate change make this a vulnerable city.

## How it works
It's actually pretty simple. The system uses data from The Weather Company and the National Meteorological Service (SMN - Argentina) to run Machine Learning algorithms and forecast of the probability of floods in the next 12 hours. In particular, it takes in measurements of the temperature, barometric pressure, wind direction and speed and clouds shape to make predictions based on an Artificial Intelligence model trained with historical data of the region. When the output probability exceeds a predefined level the system fires an alert. This consists on broadcasting a warning SMS message to every cell phone connected to the antennas near the natural hazard.

## The message
The warning message provides information on shelter locations for people as well as livestock. It also gives critical advice on leaving their belongings at home and are the most dangerous zones:

```
IMMINENT FLOOD ALERT - 95% probability of flood within the next 12hs in your area.

Your nearest evacuation center is located in Av. San Martin 3944. Go to the center ASAP.

Send "1" for more info on how to protect your loved ones and possessions.

- ATI, your flood early warning system. 
```

## Resources
- NASA Worldview
- IBM Bluemix / The Weather Company API
- Keras
- Tensorflow
- Python
- Fruits and pizzas
- GitHub: https://github.com/Cschiff/MUZ

## Bibliography
- *Krzhizhanovskaya V. V., Shirshov G. S., Melnikova N. B., Belleman R. G., Rusadi F. I., Broekhuijsen B. J., Gouldby B. P., Lhomme J., Balis B., Bubak M., Pyayt A. L., Mokhov I. I., Ozhigin A. V., Lang B., Meijer R.J.,* "Flood early warning system: design, implementation and computational modules", Procedia Computer Science, Volume 4, ICCS 2011, p 106 - 115
- *Krzhizhanovskaya V.V.,* "A roadmap to multiscale modeling of flood defense systems: from sand grain to dike failure and inundation." Proc.of ASME 2010 Computers and Information in Engineering Conf. IDETC/CIE 2010, Montreal, Canada.
- "Flood early warning system - A warning mechanism for mitigating disasters during flood." Dep of Administrarive Reforms & Public Grievances Ministry of Personnel, India.