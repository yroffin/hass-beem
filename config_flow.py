"""Config flow for BeemApp."""

from __future__ import annotations

from typing import Any

import voluptuous as vol

from homeassistant.config_entries import ConfigFlow, ConfigFlowResult
from homeassistant.const import CONF_IP_ADDRESS

from .const import DOMAIN

# https://alecthomas.github.io/voluptuous/docs/_build/html/index.html
CONFIG_SCHEMA = vol.Schema(
    {vol.Required("user", default="jhon doe"): str}
)

class BeemAppConfigFlow(ConfigFlow, domain=DOMAIN):
    """The configuration flow for a BeemApp system."""

    # The schema version of the entries that it creates
    # Home Assistant will call your migrate method if the version changes
    VERSION = 1
    MINOR_VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Ask the user information on its beem system."""
        errors = {
            "TEST": "TEST"
        }

        if user_input:
            return self.async_create_entry(
                title="BeemApp",
                data=user_input,
            )
    
        return self.async_show_form(
                step_id="user", data_schema=CONFIG_SCHEMA, errors=errors
            )
