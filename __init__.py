"""Sony Blu-ray IR integration for Home Assistant."""

from __future__ import annotations

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant

PLATFORMS = [Platform.BUTTON, Platform.MEDIA_PLAYER]


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Sony Blu-ray IR from a config entry."""
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a Sony Blu-ray IR config entry."""
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
