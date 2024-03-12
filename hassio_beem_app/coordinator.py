"""Contains the shared Coordinator for Beem systems."""

from __future__ import annotations

import asyncio
from dataclasses import dataclass
from datetime import timedelta
import logging

from homeassistant.core import HomeAssistant
from homeassistant.exceptions import HomeAssistantError
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

_LOGGER = logging.getLogger(__name__)

@dataclass
class BeemAppData:
    """Contains data pulled from the Beem system."""

    location: None

class BeemAppUpdateCoordinator(DataUpdateCoordinator[BeemAppData]):
    """Coordinates updates between all entries defined in this file."""

    def __init__(self, hass: HomeAssistant, name: str) -> None:
        """Initialize an UpdateCoordinator for a group of sensors."""

        super().__init__(
            hass,
            _LOGGER,
            name=name,
            update_interval=timedelta(seconds=5),
        )

    async def _async_update_data(self) -> BeemAppData:
        async with asyncio.timeout(4):
            try:
                location = await self.hass.async_add_executor_job(
                    "test", self.channel_context
                )
                return BeemAppData(location)
            except Exception as exc:
                raise UpdateFailed from exc
