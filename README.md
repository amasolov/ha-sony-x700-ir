# Sony X700 Infrared for Home Assistant

[![HACS](https://img.shields.io/badge/HACS-Custom-41BDF5.svg)](https://github.com/hacs/integration)
[![Validate](https://github.com/amasolov/ha-sony-x700-ir/actions/workflows/validate.yml/badge.svg)](https://github.com/amasolov/ha-sony-x700-ir/actions/workflows/validate.yml)

Control a **Sony UBP-X700** (and compatible Sony Blu-ray players) over infrared
using Home Assistant's native [infrared entity platform](https://www.home-assistant.io/integrations/infrared/) (HA 2026.4+).

The integration sends raw IR commands through any ESPHome-based IR emitter,
giving you a proper **media player** entity and **24 button** entities for every
key on the RMT-VB201D remote.

## Requirements

| Requirement | Version |
|---|---|
| Home Assistant | 2026.4 or later |
| ESPHome IR emitter | Exposes an `infrared` entity (IR proxy) |

Your ESPHome device must have the new infrared proxy component configured so
that Home Assistant discovers it as an infrared emitter.

## Installation

### HACS (recommended)

1. Open **HACS &rarr; Integrations &rarr; Explore & Download Repositories**
2. Search for **Sony X700 Infrared**
3. Click **Download**
4. Restart Home Assistant

### Manual

Copy `custom_components/sony_x700_ir/` into your Home Assistant
`config/custom_components/` directory and restart.

## Setup

1. Go to **Settings &rarr; Devices & Services &rarr; Add Integration**
2. Search for **Sony X700 Infrared**
3. Select the infrared emitter entity that points at your Blu-ray player
4. Done &mdash; a **Sony UBP-X700** device appears with all entities

## Entities

### Media player

| Feature | IR code |
|---|---|
| Turn on | Power toggle (SIRC20 command 21) |
| Turn off | Power toggle (SIRC20 command 21) |
| Play / Pause / Stop | SIRC20 |
| Previous / Next track | Chapter skip (SIRC20) |

The media player uses **assumed state** &mdash; IR is one-way so the player's
actual state cannot be read back.

### Buttons (24)

| Button | Button | Button |
|---|---|---|
| Power | Open/Close | Play |
| Pause | Stop | Rewind |
| Fast Forward | Previous | Next |
| Home | Top Menu | Pop-up Menu |
| Options | Return | Up |
| Down | Left | Right |
| Select | Subtitle | Audio |
| Display | Favourite | Netflix |

## IR codes

All codes use the Sony SIRC20 protocol (20-bit variant, device 26,
extended 226). The carrier frequency is **40 kHz** and each command is
transmitted **3 times** with a 45 ms start-to-start period, matching the
SIRC repeat convention.

The **Power** button sends a toggle command (SIRC20 command 21), matching
the green power key on the physical remote. The media player's turn on/off
both use this toggle since the Sony SIRC protocol does not define discrete
on/off codes for this device.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Submit a pull request

To add support for additional Sony devices, add a new `Enum` in `ir_codes.py`
with the raw captures and register buttons/media-player mappings in the
corresponding platform files.

## License

MIT
