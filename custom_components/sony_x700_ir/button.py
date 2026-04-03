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
        translation_key="power",
        command_code=SonyX700Code.POWER,
    ),
    SonyX700ButtonDescription(
        key="power_on",
        translation_key="power_on",
        command_code=SonyX700Code.POWER_ON,
    ),
    SonyX700ButtonDescription(
        key="power_off",
        translation_key="power_off",
        command_code=SonyX700Code.POWER_OFF,
    ),
    SonyX700ButtonDescription(
        key="open_close",
        translation_key="open_close",
        command_code=SonyX700Code.OPEN_CLOSE,
    ),
    SonyX700ButtonDescription(
        key="play",
        translation_key="play",
        command_code=SonyX700Code.PLAY,
    ),
    SonyX700ButtonDescription(
        key="pause",
        translation_key="pause",
        command_code=SonyX700Code.PAUSE,
    ),
    SonyX700ButtonDescription(
        key="stop",
        translation_key="stop",
        command_code=SonyX700Code.STOP,
    ),
    SonyX700ButtonDescription(
        key="rewind",
        translation_key="rewind",
        command_code=SonyX700Code.REWIND,
    ),
    SonyX700ButtonDescription(
        key="fast_forward",
        translation_key="fast_forward",
        command_code=SonyX700Code.FAST_FORWARD,
    ),
    SonyX700ButtonDescription(
        key="previous",
        translation_key="previous",
        command_code=SonyX700Code.PREVIOUS,
    ),
    SonyX700ButtonDescription(
        key="next",
        translation_key="next",
        command_code=SonyX700Code.NEXT,
    ),
    SonyX700ButtonDescription(
        key="home",
        translation_key="home",
        command_code=SonyX700Code.HOME,
    ),
    SonyX700ButtonDescription(
        key="top_menu",
        translation_key="top_menu",
        command_code=SonyX700Code.TOP_MENU,
    ),
    SonyX700ButtonDescription(
        key="menu",
        translation_key="menu",
        command_code=SonyX700Code.MENU,
    ),
    SonyX700ButtonDescription(
        key="options",
        translation_key="options",
        command_code=SonyX700Code.OPTIONS,
    ),
    SonyX700ButtonDescription(
        key="return",
        translation_key="return",
        command_code=SonyX700Code.RETURN,
    ),
    SonyX700ButtonDescription(
        key="up",
        translation_key="up",
        command_code=SonyX700Code.UP,
    ),
    SonyX700ButtonDescription(
        key="down",
        translation_key="down",
        command_code=SonyX700Code.DOWN,
    ),
    SonyX700ButtonDescription(
        key="left",
        translation_key="left",
        command_code=SonyX700Code.LEFT,
    ),
    SonyX700ButtonDescription(
        key="right",
        translation_key="right",
        command_code=SonyX700Code.RIGHT,
    ),
    SonyX700ButtonDescription(
        key="select",
        translation_key="select",
        command_code=SonyX700Code.SELECT,
    ),
    SonyX700ButtonDescription(
        key="subtitle",
        translation_key="subtitle",
        command_code=SonyX700Code.SUBTITLE,
    ),
    SonyX700ButtonDescription(
        key="audio",
        translation_key="audio",
        command_code=SonyX700Code.AUDIO,
    ),
    SonyX700ButtonDescription(
        key="display",
        translation_key="display",
        command_code=SonyX700Code.DISPLAY,
    ),
    SonyX700ButtonDescription(
        key="favourite",
        translation_key="favourite",
        command_code=SonyX700Code.FAVOURITE,
    ),
    SonyX700ButtonDescription(
        key="netflix",
        translation_key="netflix",
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
