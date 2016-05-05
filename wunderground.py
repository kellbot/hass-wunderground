"""
Support for Weather Underground Personal Weather Stations
Requires an wunderground API key from http://api.wunderground.com/weather/api

Enable in config as such:

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


"""
import logging
from datetime import timedelta

import requests

from homeassistant.helpers import validate_config
from homeassistant.helpers.event_decorators import \
    track_state_change, track_time_change

_LOGGER = logging.getLogger(__name__)
_RESOURCE = 'http://api.wunderground.com/api/'

DOMAIN = 'wunderground'

CONF_API_KEY = 'api_key'
CONF_PWS_ID = 'pws_id'
CONF_MONITORED_CONDITIONS = 'monitored_conditions'

def setup(hass, config):
    """Setup the WUnderground sensor."""

    if not validate_config(config, {DOMAIN: [CONF_API_KEY]}, _LOGGER):
        return False

    if not validate_config(config, {DOMAIN: [CONF_PWS_ID]}, _LOGGER):
        return False

    def handle_weather(call):

        raw_weather = []

        try:
            result = requests.get(_RESOURCE + config[DOMAIN].get(CONF_API_KEY, None) + '/conditions/q/pws:' + config[DOMAIN].get(CONF_PWS_ID, None) + '.json' )

            raw_weather.append(result.json()['current_observation'])

        except ValueError:
            _LOGGER.error(
                "Connection error "
                "Please check your settings for Weather Underground.")
            return False

        for condition in config[DOMAIN].get(CONF_MONITORED_CONDITIONS, None):
            hass.states.set('wunderground.' + condition, raw_weather[0][condition])

    hass.services.register(DOMAIN, 'refresh', handle_weather)
    hass.services.call(DOMAIN, 'refresh')

    return True

@track_time_change(minute=range(0, 60, 5), second=0)
def update_weather(hass, now):
    hass.services.call(DOMAIN, 'refresh')