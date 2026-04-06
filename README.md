# Sony X700 Infrared for Home Assistant

[![HACS](https://img.shields.io/badge/HACS-Default-41BDF5.svg)](https://github.com/hacs/integration)
[![Validate](https://github.com/amasolov/ha-sony-x700-ir/actions/workflows/validate.yml/badge.svg)](https://github.com/amasolov/ha-sony-x700-ir/actions/workflows/validate.yml)

Control a **Sony UBP-X700** (and compatible Sony Blu-ray players) over infrared
using Home Assistant's native [infrared entity platform](https://www.home-assistant.io/integrations/infrared/) (HA 2026.4+).

The integration sends raw IR commands through any ESPHome-based IR emitter,
giving you a proper **media player** entity and **26 button** entities for every
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
| Turn on | Same learned burst as Power (toggle) until discrete on is captured |
| Turn off | Same learned burst as Power (toggle) until discrete off is captured |
| Play / Pause / Stop | Captured raw |
| Previous / Next track | Chapter skip |

The media player uses **assumed state** &mdash; IR is one-way so the player's
actual state cannot be read back.

### Buttons (26)

| Button | Button | Button |
|---|---|---|
| Power | Power On | Power Off |
| Open/Close | Play | Pause |
| Stop | Rewind | Fast Forward |
| Previous | Next | Home |
| Top Menu | Pop-up Menu | Options |
| Return | Up | Down |
| Left | Right | Select |
| Subtitle | Audio | Display |
| Favourite | Netflix | |

## IR codes

All codes were captured from a genuine Sony RMT-VB201D remote using an
ESPHome `remote_receiver` on an M5Stack ATOM S3 Lite. The carrier frequency
is **40 kHz** (Sony SIRC standard). Each command is transmitted **3 times**
with a 25 ms inter-frame gap, matching the SIRC repeat convention.

**Power**, **Power On**, and **Power Off** all use the same learned raw burst (the
green power key) until you capture discrete SIRC on/off codes from your remote and
replace `POWER_ON` / `POWER_OFF` in `ir_codes.py`. The media player’s turn on/off
then matches that behaviour.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Submit a pull request

To add support for additional Sony devices, add a new `Enum` in `ir_codes.py`
with the raw captures and register buttons/media-player mappings in the
corresponding platform files.

## License

MIT
