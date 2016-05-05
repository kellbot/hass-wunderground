# Home Assistant Custom Compoent for WUnderground Personal Weather Stations

Requires an wunderground API key from http://api.wunderground.com/weather/api

Enable in config as such:

```yaml
wunderground:
  api_key: xxxxxxxxxx
  pws_id: XXXXXXXX
  monitored_conditions:
    - station_id
    - observation_time
    - weather
    - temperature_string
    - temp_f
    - temp_c
    - relative_humidity
    - wind_string
    - wind_dir
    - wind_degrees
    - wind_mph
    - wind_gust_mph
    - wind_kph
    - wind_gust_kph
    - pressure_mb
    - pressure_in
    - pressure_trend
    - dewpoint_string
    - dewpoint_f
    - dewpoint_c
    - heat_index_string
    - heat_index_f
    - heat_index_c
    - windchill_string
    - windchill_f
    - windchill_c
    - feelslike_string
    - feelslike_f
    - feelslike_c
    - visibility_mi
    - visibility_km
    - solarradiation
    - UV
    - precip_1hr_string
    - precip_1hr_in
    - precip_1hr_metric
    - precip_today_string
    - precip_today_in
    - precip_today_metric
    - icon
```

Refreshes every 5 minutes

## Installation

Place wunderground.py in the /custom_components directory (you may need to create it) wherever your hass config file lies. Restart hass.

## To-Do

This component would be improved by a number of features, including (but not limited to):
- Configurable refresh intervals
- Friendlier labels
- Use the weather icons provided by wunderground
- graphs