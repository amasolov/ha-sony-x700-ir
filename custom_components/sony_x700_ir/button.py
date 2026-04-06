"""Button platform for Sony X700 IR integration."""

from __future__ import annotations

from dataclasses import dataclass

from homeassistant.components.button import ButtonEntity, ButtonEntityDescription
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback

from .const import CONF_INFRARED_ENTITY_ID
from .entity import SonyX700IrEntity
from .ir_codes import SonyX700Code

PARALLEL_UPDATES = 1


@dataclass(frozen=True, kw_only=True)
class SonyX700ButtonDescription(ButtonEntityDescription):
    """Describes a Sony X700 IR button entity."""

    command_code: SonyX700Code


BUTTON_DESCRIPTIONS: tuple[SonyX700ButtonDescription, ...] = (
    SonyX700ButtonDescription(
        key="power",
        name="Power",
        command_code=SonyX700Code.POWER,
    ),
    SonyX700ButtonDescription(
        key="power_on",
        name="Power on",
        command_code=SonyX700Code.POWER_ON,
    ),
    SonyX700ButtonDescription(
        key="power_off",
        name="Power off",
        command_code=SonyX700Code.POWER_OFF,
    ),
    SonyX700ButtonDescription(
        key="open_close",
        name="Open/Close",
        command_code=SonyX700Code.OPEN_CLOSE,
    ),
    SonyX700ButtonDescription(
        key="play",
        name="Play",
        command_code=SonyX700Code.PLAY,
    ),
    SonyX700ButtonDescription(
        key="pause",
        name="Pause",
        command_code=SonyX700Code.PAUSE,
    ),
    SonyX700ButtonDescription(
        key="stop",
        name="Stop",
        command_code=SonyX700Code.STOP,
    ),
    SonyX700ButtonDescription(
        key="rewind",
        name="Rewind",
        command_code=SonyX700Code.REWIND,
    ),
    SonyX700ButtonDescription(
        key="fast_forward",
        name="Fast forward",
        command_code=SonyX700Code.FAST_FORWARD,
    ),
    SonyX700ButtonDescription(
        key="previous",
        name="Previous",
        command_code=SonyX700Code.PREVIOUS,
    ),
    SonyX700ButtonDescription(
        key="next",
        name="Next",
        command_code=SonyX700Code.NEXT,
    ),
    SonyX700ButtonDescription(
        key="home",
        name="Home",
        command_code=SonyX700Code.HOME,
    ),
    SonyX700ButtonDescription(
        key="top_menu",
        name="Top menu",
        command_code=SonyX700Code.TOP_MENU,
    ),
    SonyX700ButtonDescription(
        key="menu",
        name="Pop-up menu",
        command_code=SonyX700Code.MENU,
    ),
    SonyX700ButtonDescription(
        key="options",
        name="Options",
        command_code=SonyX700Code.OPTIONS,
    ),
    SonyX700ButtonDescription(
        key="return",
        name="Return",
        command_code=SonyX700Code.RETURN,
    ),
    SonyX700ButtonDescription(
        key="up",
        name="Up",
        command_code=SonyX700Code.UP,
    ),
    SonyX700ButtonDescription(
        key="down",
        name="Down",
        command_code=SonyX700Code.DOWN,
    ),
    SonyX700ButtonDescription(
        key="left",
        name="Left",
        command_code=SonyX700Code.LEFT,
    ),
    SonyX700ButtonDescription(
        key="right",
        name="Right",
        command_code=SonyX700Code.RIGHT,
    ),
    SonyX700ButtonDescription(
        key="select",
        name="Select",
        command_code=SonyX700Code.SELECT,
    ),
    SonyX700ButtonDescription(
        key="subtitle",
        name="Subtitle",
        command_code=SonyX700Code.SUBTITLE,
    ),
    SonyX700ButtonDescription(
        key="audio",
        name="Audio",
        command_code=SonyX700Code.AUDIO,
    ),
    SonyX700ButtonDescription(
        key="display",
        name="Display",
        command_code=SonyX700Code.DISPLAY,
    ),
    SonyX700ButtonDescription(
        key="favourite",
        name="Favourite",
        command_code=SonyX700Code.FAVOURITE,
    ),
    SonyX700ButtonDescription(
        key="netflix",
        name="Netflix",
        command_code=SonyX700Code.NETFLIX,
    ),
)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddConfigEntryEntitiesCallback,
) -> None:
    """Set up Sony X700 IR buttons from config entry."""
    infrared_entity_id = entry.data[CONF_INFRARED_ENTITY_ID]
    async_add_entities(
        SonyX700Button(entry, infrared_entity_id, desc)
        for desc in BUTTON_DESCRIPTIONS
    )


class SonyX700Button(SonyX700IrEntity, ButtonEntity):
    """Sony X700 IR button entity."""

    entity_description: SonyX700ButtonDescription

    def __init__(
        self,
        entry: ConfigEntry,
        infrared_entity_id: str,
        description: SonyX700ButtonDescription,
    ) -> None:
        super().__init__(entry, infrared_entity_id, unique_id_suffix=description.key)
        self.entity_description = description

    async def async_press(self) -> None:
        """Press the button."""
        await self._send_command(self.entity_description.command_code)
