easyLIFX
=====
Lucas Childers, 2017

A Python 3 library used to **easily** interact with LIFX lights.

# Setup

1. Head to [LIFX Cloud](https://cloud.lifx.com/settings) and generate a new token. This is used as an argument when creating a new easyLIFX object.

---

# Methods

## init
`lifx = easyLIFX(os.environ["LIFX_KEY"])`

Creates a new easyLIFX object.

_The init method takes the LIFX API key as a required argument. The best way
to handle this is by setting the key as an environment variable._

---

## togglePower
`togglePower()`

Toggles the power of specified lights on or off.

_All values are optional, below are defaults._

* `lights="all"`
  * Use comma separated names of lights

```[python]
togglePower(lights="Bed,Desk")
```

---
## setState
`setState()`

Set the state of specified lights, such as color or brightness.

_All values are optional, below are defaults._

* `state="on"`
  * on
  * off
<br><br>
* `brightness="1.0"`
  * Between 0 and 1
<br><br>
* `duration="1"`
  * Fade on or off duration in seconds
<br><br>
* `color="kelvin:4500"`
  * TODO: Simplify color selection
  * `blue saturation=0.5`
<br><br>
* `lights="all"`
  * Use comma separated names of lights

```[python]
setState(state="off", lights="Bed,Desk")
```

---
## listLightsInfo
`listLightsInfo()`  

Displays all lights connected to your LIFX account.

```     
     Name: Bed
       ID: 00000000000
    State: off
Brighness: 1
```
