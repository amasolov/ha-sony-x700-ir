"""Media player platform for Sony X700 IR integration."""

from __future__ import annotations

from homeassistant.components.media_player import (
    MediaPlayerDeviceClass,
    MediaPlayerEntity,
    MediaPlayerEntityFeature,
    MediaPlayerState,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback

from .const import CONF_INFRARED_ENTITY_ID
from .entity import SonyX700IrEntity
from .ir_codes import SonyX700Code

PARALLEL_UPDATES = 1


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddConfigEntryEntitiesCallback,
) -> None:
    """Set up Sony X700 IR media player from config entry."""
    infrared_entity_id = entry.data[CONF_INFRARED_ENTITY_ID]
    async_add_entities([SonyX700MediaPlayer(entry, infrared_entity_id)])


class SonyX700MediaPlayer(SonyX700IrEntity, MediaPlayerEntity):
    """Sony X700 Blu-ray player controlled via IR."""

    _attr_name = None
    _attr_assumed_state = True
    _attr_device_class = MediaPlayerDeviceClass.RECEIVER
    _attr_supported_features = (
        MediaPlayerEntityFeature.TURN_ON
        | MediaPlayerEntityFeature.TURN_OFF
        | MediaPlayerEntityFeature.PLAY
        | MediaPlayerEntityFeature.PAUSE
        | MediaPlayerEntityFeature.STOP
        | MediaPlayerEntityFeature.PREVIOUS_TRACK
        | MediaPlayerEntityFeature.NEXT_TRACK
    )

    def __init__(self, entry: ConfigEntry, infrared_entity_id: str) -> None:
        super().__init__(entry, infrared_entity_id, unique_id_suffix="media_player")
        self._attr_state = MediaPlayerState.ON

    async def async_turn_on(self) -> None:
        """Turn on the player."""
        await self._send_command(SonyX700Code.POWER_ON)

    async def async_turn_off(self) -> None:
        """Turn off the player."""
        await self._send_command(SonyX700Code.POWER_OFF)

    async def async_media_play(self) -> None:
        """Send play command."""
        await self._send_command(SonyX700Code.PLAY)

    async def async_media_pause(self) -> None:
        """Send pause command."""
        await self._send_command(SonyX700Code.PAUSE)

    async def async_media_stop(self) -> None:
        """Send stop command."""
        await self._send_command(SonyX700Code.STOP)

    async def async_media_previous_track(self) -> None:
        """Send previous chapter command."""
        await self._send_command(SonyX700Code.PREVIOUS)

    async def async_media_next_track(self) -> None:
        """Send next chapter command."""
        await self._send_command(SonyX700Code.NEXT)
