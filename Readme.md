# Home Assistant Custom Component for WUnderground Personal Weather Stations

Requires a WUnderground API key from http://api.wunderground.com/weather/api

Enable in config as such:

```yaml
sensor:
  platform: wunderground
  api_key: xxxxxxxxxx
  pws_id: XXXXXXXX
```

Refreshes every 5 minutes

Individual attributes can be added to the display by using sensor templates (thanks @rpitera for providing the example:

```yaml
sensor:
   platform: template
   sensors:
     pws_stationid:
       value_template: '{{ states.sensor.weather_underground_pws.attributes.station_id }}'
     pws_location:
       value_template: '{{ states.sensor.weather_underground_pws.attributes.display_location.full }}'
     pws_elevation:
       value_template: '{{ states.sensor.weather_underground_pws.attributes.observation_location.elevation }}'
     pws_forecast_period_0_text:
       value_template: '{{ states.sensor.weather_underground_pws.attributes.txt_forecast.forecastday.0.fcttext }}'
```

The list of attributes can be found in the API docs at https://www.wunderground.com/weather/api/d/docs?d=data/conditions

These sensors can then be customized using groups, custom icons, etc. Sample configurations can be found at https://community.home-assistant.io/t/is-anyone-doing-anything-with-weather-underground/763/72

## Installation

Place sensor/wunderground.py in the /custom_components/sensor/ directory (you may need to create it) wherever your hass config file lies. Restart hass.


## To-Do

This component would be improved by a number of features, but what we really need is a generic weather component for HA first.
