## Motor microsteps counter for Star slots
Python script running on RaspberryPi which calculates:
1. ```Gap Start```(motor current position in microsteps): optical sensor changes its state from 0 (light off) to 1 (light on)
2. ```Gap End```(motor current position in microsteps): optical sensor changes its state from 1 (light on) to 0 (light off)
3. ```Gap```(microsteps): ```Gap End - Gap Start``` for each Star slot

#### Setup
* Connect optical sensor to RaspberryPi GPIO pin. To see your pinout run ```piout``` command in RaspberryPi terminal:

    ```3V3  (1) (2)  5V    
     GPIO2  (3) (4)  5V    
     GPIO3  (5) (6)  GND   
     GPIO4  (7) (8)  GPIO14
       GND  (9) (10) GPIO15
    GPIO17 (11) (12) GPIO18
    GPIO27 (13) (14) GND   
    GPIO22 (15) (16) GPIO23
       3V3 (17) (18) GPIO24
    GPIO10 (19) (20) GND   
     GPIO9 (21) (22) GPIO25
    GPIO11 (23) (24) GPIO8 
       GND (25) (26) GPIO7 
     GPIO0 (27) (28) GPIO1 
     GPIO5 (29) (30) GND   
     GPIO6 (31) (32) GPIO12
    GPIO13 (33) (34) GND   
    GPIO19 (35) (36) GPIO16
    GPIO26 (37) (38) GPIO20
       GND (39) (40) GPIO21
    ```

    In our case the sensor was connected to physical pin ```29``` which corresponds to ```GPIO5```.
    
    Another option to check RaspberryPi's pins state is to run ```gpio readall``` command. Check pin ```29``` in ```Physical``` column (for our case) which corresponded to ```21``` in ```wPi``` column and ```5``` in ```BCM``` column (```5``` is the value which needs to be set in ```config/gap_counter_setting.txt``` config file for ```opto_sensor_pin``` property).
    
    BCM| wPi| Name    | Mode | V | Physical
    ---|----| --------|------|---|---------
    5  | 21 | GPIO.21 | IN   | 0 | 29

* Make sure you will be tracking the correct pin. If your pin is ```5 BCM / 29 Physical``` like in our case, ```V``` column value from the abobe table will be changing from 0 --> 1 --> 0 once the sensor state is changed. Sensor state changes can be also tracked by running ```gpio read <pin_number>``` command.

#### Run
* Run gap_counter.py script ```python3 gap_counter.py```
* Motor will be initialised with the properties from ```config/gap_counter_settings.txt``` config file. Below are the values used for our run:

    - starting_speed: 0
    - max_speed: 348000
    - max_accel: 848000
    - max_decel: 848000
    - step_mode: 8
    - current_limit: 672
    - decay_mode: fast                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
    - initial_position: 0
    - opto_sensor_pin: 5
    - target_position: 6400
* The Star will make a 360 degree turn which corresponds to ```target_position: 6400```. Once the motor makes 6400 microsteps and all 9 slots will pass the sensor, the script will output the results and the motor will be deenergized. 

#### Output
The following table will be printed at the end of the run:
```Tic was initialised!
    Tic is running!
    1. Gap Start: 278. Gap End: 300. Gap: 22
    2. Gap Start: 988. Gap End: 1010. Gap: 22
    3. Gap Start: 1701. Gap End: 1722. Gap: 21
    4. Gap Start: 2410. Gap End: 2431. Gap: 21
    5. Gap Start: 3117. Gap End: 3140. Gap: 23
    6. Gap Start: 3830. Gap End: 3853. Gap: 23
    7. Gap Start: 4550. Gap End: 4569. Gap: 19
    8. Gap Start: 5257. Gap End: 5281. Gap: 24
    9. Gap Start: 5967. Gap End: 5988. Gap: 21
    Tic was deenergized!
 ```
Same table will be appended to ```output/gap_results.csv``` with each new run.
