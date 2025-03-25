# Ingenuity project 

## Introduction: Ingenuity as part of the Mars 2020 mission. 

Mars 2020 is a space mission that will deploy the Perseverance rover on the Martian surface to study its surface and collect soil samples. It is the first of a series of three missions whose ultimate aim is to return these samples to Earth for analysis. 

Ingenuity is a small helicopter developed by NASA, the US space agency. It is being used experimentally on the surface of Mars during the Mars 2020 mission.
The helicopter is on board the Perseverance rover. 

On April 19, 2021, for the first time in the history of the space age, a spacecraft makes a powered flight through the tenuous atmosphere of another planet. Ingenuity's objective is optical reconnaissance of the terrain, with the helicopter taking numerous aerial photos which are used by the pilots of the Perseverance astromobile to identify obstacles and promising sites (taking rock samples from the Martian soil). The tenuous atmosphere (only 1% of Earth's atmospheric pressure) offers very little lift, making it more difficult to develop an aerobot. 

Ingenuity is a 1.8 kg helicopter with 2 coaxial counter-rotating rotors. It draws its energy from 6 lithium-ion batteries recharged by solar cells. Its navigation system enables it to follow a pre-programmed route without human intervention. Its only payload is a camera. 

The mission recently came to an end (January 18, 2024) when a blade broke during the 72nd flight. 

Ingenuity has opened up new prospects for Mars exploration. NASA and ESA, in their Mars Sample Return mission, are now including 2 similar helicopters which will be responsible for collecting the tubes containing the Mars samples deposited by the Perseverance astromobile in the event of its failure. 

The Mars Sample Return mission will be Ingenuity's first operational use. Developed by NASA in collaboration with the European Space Agency, its aim is to return to Earth the Martian soil samples collected by the Perseverance astromobile. To achieve this objective, the mission plans to send a lander, Sample Retrieval Lander (SRL), carrying a remotely operated arm to retrieve the tubes containing the soil samples. If the soil samples are out of reach of the lander due to a failure of Perseverance, SRL has two Sample Recovery Helicopters, directly derived from the Ingenuity helicopter, equipped with a grabber to retrieve the tubes from where they were deposited.

## First look at the anatomy of the Martian helicopter

NASA's website with extensive information on Ingenuity: (https://mars.nasa.gov/technology/helicopter/#)


## Exploring helicopter operation

### Propulsion: 

The helicopter moves through the air thanks to two coaxial, two-bladed counter-rotating rotors. The rotational speed is between 2,400 and 2,900 rpm, ten times that of a helicopter main rotor on Earth, to be effective in the thin air of Mars. This is a condition we won't be able to meet. 

Understanding how helicopter propellers work helps us to overcome the first difficulties: we need small, coaxial, counter-rotating propellers, parts that we can't build ourselves (3D printing). One solution we've come up with is to use propellers taken from a remote-controlled helicopter. We'll dismantle the aircraft to keep only the propellers on the axis and the engines, and rebuild all the electronics according to our specifications. 

Aircraft type: the use of coaxial counter-rotating rotors saves space compared with the use of an anti-torque rotor. 

### Energy: 

Energy is the main limiting factor concerning the helicopter's capabilities. The energy required for propulsion, sensor operation (altimeter, camera), heating resistors (responsible for maintaining the various systems at a temperature compatible with the operating constraints during the Martian night), avionics, processors and the telecommunications system is supplied by six lithium-ion accumulators, with a capacity of 36 Watts-h recharged by photovoltaic cells (active surface area of 544 cm^2).

### Sensors: 

- a navigation camera
- 2 3-axis inertial units (acceleration and rotation speed)
- 2-axis inclinometer
- altimeter

### Telecommunications: 

Given the time taken for Mars-to-Earth communication (around ten minutes in favorable conditions), the helicopter flies autonomously, applying instructions transmitted beforehand. In flight, the helicopter does not receive, but transmits the data it has collected. 

### Avionics and processors:

The avionics are distributed over 5 circuit boards, 4 of which form the sides of the cubic fuselage and the fifth the inside. The on-board computer uses a Snapdragon microprocessor clocked at 2.26 GHz, with 2 GB RAM and 32 GB flash memory. The computer supports the navigation function and controls the rotors via two redundant microcontrollers. The software running on the microprocessor is supported by an FPGA-type integrated circuit, which handles functions such as altitiude control, I/O management of the inertial unit, altimeter and inclinometer, and telecommunications management. The FPGA is a militarized version of MicroSemi's ProASIC3L. The operating system is GNU/Linux. 



### Sources: 

https://mars.nasa.gov/technology/helicopter/#Tech-Specs

https://fr.wikipedia.org/wiki/Ingenuity_(hélicoptère)
