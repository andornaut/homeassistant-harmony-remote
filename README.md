# homeassistant-harmony-remote

[![Test](https://github.com/andornaut/homeassistant-harmony-remote/actions/workflows/test.yml/badge.svg)](https://github.com/andornaut/homeassistant-harmony-remote/actions/workflows/test.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/license/MIT)

- [v1](./v1/)

Physical remote control for Home Assistant

Inspiration: [The Everything Remote](https://www.thestockpot.net/videos/theeverythingremote)

- [Overview (video)](https://www.youtube.com/watch?v=Pe_ozZkrRAw)
- [Build instructions (video)](https://www.youtube.com/watch?v=JU_7mb1ue7o&t=2059s)
- [3D models (.3mf and .step)](https://www.printables.com/model/1281626-everything-remote-esp32-powered-universal-remote)
- [Order PCB from PCBWay](https://www.pcbway.com/project/shareproject/The_Everything_Remote_The_Stock_Pot_ff1fe6b5.html)

## Bill of materials (BOM)

| Item                                                                                                                                          | Quantity | Description                                                                                                                                                     |
| --------------------------------------------------------------------------------------------------------------------------------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Lithium Ion Battery - 1500mAh](https://www.sparkfun.com/lithium-ion-battery-1500mah-iec62133-certified.html)                                 | 1        | 3.7V at 1500 mAh                                                                                                                                                |
| [Mill-Max 315-43-116-41-001000](https://www.digikey.ca/en/products/detail/mill-max-manufacturing-corp/315-43-116-41-001000/4455239)           | 2        | [315 series](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/2481/310%2C%20311%2C%20315%20Series%20%28in.%29.pdf) "very low profile" 16-pin socket |
| [Mill-max 3320-0-00-15-00-00-03-0](https://www.digikey.ca/en/products/detail/mill-max-manufacturing-corp/3320-0-00-15-00-00-03-0/4147392)     | 32       | Pins to connec the microcontroller to the sockets                                                                                                               |
| [Vishay Dale CRCW120610K0FKEAC](https://www.digikey.ca/en/products/detail/vishay-dale/CRCW120610K0FKEAC/7928405)                              | 2        | 10 kΩ pull-up resistors                                                                                                                                         |
| [SCHURTER tactile switches](https://www.digikey.ca/en/products/detail/schurter-inc/1301-9315-24/2643953?so=92547316&content=productdetail_CA) | 24       | 6x6x0.5mm, 0.5A 12v                                                                                                                                             |
| [SparkFun Thing Plus - ESP32 WROOM (USB-C)](https://www.sparkfun.com/sparkfun-thing-plus-esp32-wroom-usb-c.html)                              | 1        | Microcontroller                                                                                                                                                 |
