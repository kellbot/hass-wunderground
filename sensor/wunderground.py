"""Support for Wundeground weather service."""
from datetime import timedelta
import logging
import requests
from homeassistant.helpers.entity import Entity
from homeassistant.util import Throttle
from homeassistant.const import CONF_API_KEY

CONF_PWS_ID = 'pws_id'
_RESOURCE = 'https://api.wunderground.com/api/'
_LOGGER = logging.getLogger(__name__)

# Return cached results if last scan was less then this time ago.
MIN_TIME_BETWEEN_UPDATES = timedelta(seconds=300)


def setup_platform(hass, config, add_devices, discovery_info=None):
    """Setup the Wundeground sensor."""
    payload = config.get('payload', None)
    rest = WUndergroundData(_RESOURCE,
                            config.get(CONF_PWS_ID),
                            config.get(CONF_API_KEY),
                            payload)
    rest.update()
    add_devices([WUndergroundSensor(rest)])

class WUndergroundSensor(Entity):
    """A class for the PWS"""

    def __init__(self, rest):
        """Initialize the sensor."""
        self.rest = rest
        self._unit_of_measurement = "°F"
        self.update()
        self.weather = self.rest.data

    @property
    def name(self):
        """Return the name of the sensor."""
        return 'Weather Underground PWS'

    @property
    def state(self):
        """Return the state of the sensor."""
        self.weather = self.rest.data
        return self.weather['temp_f']

    @property
    def entity_picture(self):
        """Return the entity picture."""
        self.weather = self.rest.data
        return self.weather['icon_url']

    @property
    def device_state_attributes(self):
        """Return the state attributes."""
        return self.rest.data

    @property
    def unit_of_measurement(self):
        """Return the units of measurement."""
        return self._unit_of_measurement

#    @property
#    def temp_f(self):
#        self.weather = self.rest.data
#        return self.rest.data['temp_f']

    def update(self):
        """Update current conditions."""
        self.rest.update()
        self._state = self.rest.data

# pylint: disable=too-few-public-methods
class WUndergroundData(object):
    """Get data from Wundeground."""
    def __init__(self, resource, pws_id, api_key, data):
        """Initialize the data object."""
        self._resource = resource
        self._api_key = api_key
        self._pws_id = pws_id
        self.data = None

    @Throttle(MIN_TIME_BETWEEN_UPDATES)
    def update(self):
        """Get the latest data from wunderground"""
        try:
            result = requests.get(self._resource + self._api_key +
                                  '/conditions/q/pws:' + self._pws_id + '.json')
            self.data = result.json()['current_observation']
        except requests.exceptions.ConnectionError:
            _LOGGER.error("No route to host/endpoint: %s", self._resource)
            self.data = None
