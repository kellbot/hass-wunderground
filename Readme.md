# Home Assistant Custom Compoent for WUnderground Personal Weather Stations

Requires an wunderground API key from http://api.wunderground.com/weather/api

Enable in config as such:

```yaml
sensor:
  platform: wunderground
  api_key: xxxxxxxxxx
  pws_id: XXXXXXXX

Refreshes every 5 minutes

## Installation

Place sensor/wunderground.py in the /custom_components/sensor/ directory (you may need to create it) wherever your hass config file lies. Restart hass.


## To-Do

This component would be improved by a number of features, but what we really need is a generic weather component for HA first.
