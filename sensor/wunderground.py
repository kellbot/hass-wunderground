from homeassistant.helpers.entity import Entity
from homeassistant.util import Throttle
from homeassistant.const import CONF_API_KEY
import requests
from datetime import timedelta

CONF_PWS_ID = 'pws_id'
_RESOURCE = 'http://api.wunderground.com/api/'

# Return cached results if last scan was less then this time ago.
MIN_TIME_BETWEEN_UPDATES = timedelta(seconds=300)


def setup_platform(hass, config, add_devices, discovery_info=None):
    rest = WUndergroundData(_RESOURCE, config.get(CONF_PWS_ID), config.get(CONF_API_KEY))
    add_devices([WUndergroundSensor(rest)])

class WUndergroundSensor(Entity):
    """A class for the PWS"""

    def __init__(self, rest):
        self.rest = rest
        self._unit_of_measurement = "degrees F"
        self.update()
        self.weather = self.rest.data

    @property
    def name(self):
        return 'Weather Underground PWS'

    @property
    def state(self):
        return self.weather['temp_f']

    @property
    def entity_picture(self):
        return self.weather['icon_url']

    @property
    def device_state_attributes(self):
        return self.weather

    @property
    def unit_of_measurement(self):
        return self._unit_of_measurement

    @property
    def temp_f(self):
        return self.weather['temp_f']

    def update(self):
        """Update current conditios"""

        self.rest.update()

 

class WUndergroundData(object):

    def __init__(self, resource, pws_id, api_key):
        self._resource = resource
        self._api_key = api_key
        self._pws_id = pws_id

        self.data = dict()

    @Throttle(MIN_TIME_BETWEEN_UPDATES)
    def update(self):
        """Get the latest data from wunderground"""
        try:
            result = requests.get(self._resource + self._api_key + '/conditions/q/pws:' + self._pws_id + '.json' )
            self.data =  result.json()['current_observation']
        except requests.exceptions.ConnectionError:
            _LOGGER.error("No route to host/endpoint: %s", self._resource)
            self.data = None
        
        
