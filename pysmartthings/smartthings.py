"""Define the SmartThings Cloud API."""

from .api import API
from .app import App
from .device import Device
from .location import Location


class SmartThings:
    """Define a class for interacting with the SmartThings Cloud API."""

    def __init__(self, token):
        """
        Initialize the API.

        :param token: The personal access token used to authenticate to the API
        :type token: str
        """
        self._api = API(token)

    def locations(self):
        """Retrieve SmartThings locations."""
        resp = self._api.get_locations()
        return [Location(self._api, entity) for entity in resp["items"]]

    def devices(self):
        """Retrieve SmartThings devices."""
        resp = self._api.get_devices()
        return [Device(self._api, entity) for entity in resp["items"]]

    def apps(self):
        """Retrieve list of apps."""
        resp = self._api.get_apps()
        return [App(self._api, entity) for entity in resp["items"]]

    def create_app(self) -> App:
        """Create a new app."""
        return App(self._api, None)

    def delete_app(self, app_id: str):
        """Delete an app."""
        return self._api.delete_app(app_id)
