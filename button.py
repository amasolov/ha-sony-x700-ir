"""Button platform for Sony Blu-ray IR integration."""

from __future__ import annotations

from dataclasses import dataclass

from homeassistant.components.button import ButtonEntity, ButtonEntityDescription
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback

from .const import CONF_INFRARED_ENTITY_ID
from .entity import SonyBlurayIrEntity
from .ir_codes import SonyBlurayCode

PARALLEL_UPDATES = 1


@dataclass(frozen=True, kw_only=True)
class SonyBlurayButtonDescription(ButtonEntityDescription):
    """Describes a Sony Blu-ray IR button entity."""

    command_code: SonyBlurayCode


BUTTON_DESCRIPTIONS: tuple[SonyBlurayButtonDescription, ...] = (
    SonyBlurayButtonDescription(
        key="power",
        translation_key="power",
        command_code=SonyBlurayCode.POWER,
    ),
    SonyBlurayButtonDescription(
        key="power_on",
        translation_key="power_on",
        command_code=SonyBlurayCode.POWER_ON,
    ),
    SonyBlurayButtonDescription(
        key="power_off",
        translation_key="power_off",
        command_code=SonyBlurayCode.POWER_OFF,
    ),
    SonyBlurayButtonDescription(
        key="open_close",
        translation_key="open_close",
        command_code=SonyBlurayCode.OPEN_CLOSE,
    ),
    SonyBlurayButtonDescription(
        key="play",
        translation_key="play",
        command_code=SonyBlurayCode.PLAY,
    ),
    SonyBlurayButtonDescription(
        key="pause",
        translation_key="pause",
        command_code=SonyBlurayCode.PAUSE,
    ),
    SonyBlurayButtonDescription(
        key="stop",
        translation_key="stop",
        command_code=SonyBlurayCode.STOP,
    ),
    SonyBlurayButtonDescription(
        key="rewind",
        translation_key="rewind",
        command_code=SonyBlurayCode.REWIND,
    ),
    SonyBlurayButtonDescription(
        key="fast_forward",
        translation_key="fast_forward",
        command_code=SonyBlurayCode.FAST_FORWARD,
    ),
    SonyBlurayButtonDescription(
        key="previous",
        translation_key="previous",
        command_code=SonyBlurayCode.PREVIOUS,
    ),
    SonyBlurayButtonDescription(
        key="next",
        translation_key="next",
        command_code=SonyBlurayCode.NEXT,
    ),
    SonyBlurayButtonDescription(
        key="home",
        translation_key="home",
        command_code=SonyBlurayCode.HOME,
    ),
    SonyBlurayButtonDescription(
        key="top_menu",
        translation_key="top_menu",
        command_code=SonyBlurayCode.TOP_MENU,
    ),
    SonyBlurayButtonDescription(
        key="menu",
        translation_key="menu",
        command_code=SonyBlurayCode.MENU,
    ),
    SonyBlurayButtonDescription(
        key="options",
        translation_key="options",
        command_code=SonyBlurayCode.OPTIONS,
    ),
    SonyBlurayButtonDescription(
        key="return",
        translation_key="return",
        command_code=SonyBlurayCode.RETURN,
    ),
    SonyBlurayButtonDescription(
        key="up",
        translation_key="up",
        command_code=SonyBlurayCode.UP,
    ),
    SonyBlurayButtonDescription(
        key="down",
        translation_key="down",
        command_code=SonyBlurayCode.DOWN,
    ),
    SonyBlurayButtonDescription(
        key="left",
        translation_key="left",
        command_code=SonyBlurayCode.LEFT,
    ),
    SonyBlurayButtonDescription(
        key="right",
        translation_key="right",
        command_code=SonyBlurayCode.RIGHT,
    ),
    SonyBlurayButtonDescription(
        key="select",
        translation_key="select",
        command_code=SonyBlurayCode.SELECT,
    ),
    SonyBlurayButtonDescription(
        key="subtitle",
        translation_key="subtitle",
        command_code=SonyBlurayCode.SUBTITLE,
    ),
    SonyBlurayButtonDescription(
        key="audio",
        translation_key="audio",
        command_code=SonyBlurayCode.AUDIO,
    ),
    SonyBlurayButtonDescription(
        key="display",
        translation_key="display",
        command_code=SonyBlurayCode.DISPLAY,
    ),
    SonyBlurayButtonDescription(
        key="favourite",
        translation_key="favourite",
        command_code=SonyBlurayCode.FAVOURITE,
    ),
    SonyBlurayButtonDescription(
        key="netflix",
        translation_key="netflix",
        command_code=SonyBlurayCode.NETFLIX,
    ),
)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddConfigEntryEntitiesCallback,
) -> None:
    """Set up Sony Blu-ray IR buttons from config entry."""
    infrared_entity_id = entry.data[CONF_INFRARED_ENTITY_ID]
    async_add_entities(
        SonyBlurayButton(entry, infrared_entity_id, desc)
        for desc in BUTTON_DESCRIPTIONS
    )


class SonyBlurayButton(SonyBlurayIrEntity, ButtonEntity):
    """Sony Blu-ray IR button entity."""

    entity_description: SonyBlurayButtonDescription

    def __init__(
        self,
        entry: ConfigEntry,
        infrared_entity_id: str,
        description: SonyBlurayButtonDescription,
    ) -> None:
        super().__init__(entry, infrared_entity_id, unique_id_suffix=description.key)
        self.entity_description = description

    async def async_press(self) -> None:
        """Press the button."""
        await self._send_command(self.entity_description.command_code)
