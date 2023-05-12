# Oresat CFC Mini-Backplane

This is the backplane for UMBC's Air Harp 2 sensor, which is going to include a PIRT SWIR sensor using OreSat's CFC system.

## Requirements:

* Match the DXF outline from Joe, including placement of connectors and the fastener holes.
   * Probably remove solder mask from both sides of those fastener holes just in case.
   * Probably put the external connectors in the upper right hand corner.
* Use an OreSat 20 pin debug connector on this backplane so we can run USB from the CFC processor to the external connector using the CFC processor's debug connector.
* External connections
   * Power should come through a 0.2 inch euroterminal for two 20 AWG wires.
   * USB should be via a [Harwin M80-5400442](https://www.digikey.com/en/products/detail/harwin-inc/M80-5400442/4953167) connector. Pin-out is determined by us.
       * signals: USB D+, USB D-, Vbus, and GND.
       * Vbus should go through a 10k ohm resistor between the 20 pin debug connector and the Harwin connector.
       
## Required changes to the CFC Processor and CFC sensor boards

* Both OPDs should come on by default.
* We should figure some way to power the local OPDs so they're not doing anything weird.

