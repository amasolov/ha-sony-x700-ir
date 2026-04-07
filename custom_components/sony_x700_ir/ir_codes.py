"""Sony SIRC20 IR codes for the UBP-X700 Blu-ray player (RMT-VB201D remote).

Protocol
  Sony SIRC, 20-bit variant.  Each frame is:
    header mark (2400 µs) + header space (600 µs)
    then 20 data bits LSB-first:
      7 command bits + 5 device bits + 8 extended-device bits
    bit encoding: mark 1200 µs = '1', mark 600 µs = '0'; space always 600 µs
  Carrier: 40 kHz.
  Frames are repeated with a 45 ms start-to-start period (SIRC standard).

Device address
  device = 26, extended = 226  (Sony BD-player family).

Power
  The media player ``turn_on`` / ``turn_off`` both send the power toggle
  command (21), matching the green power key on the physical remote.
"""

from __future__ import annotations

from enum import Enum
from typing import override

from infrared_protocols import Command, Timing

# --- SIRC20 timing constants (µs) -------------------------------------------
HEADER_MARK_US = 2400
HEADER_SPACE_US = 600
ONE_MARK_US = 1200
ZERO_MARK_US = 600
BIT_SPACE_US = 600

# --- Transmission parameters -------------------------------------------------
CARRIER_FREQ_HZ = 40_000
FRAME_REPEAT = 3  # total frames per press (SIRC minimum is 3)
FRAME_PERIOD_US = 45_000  # start-to-start, per Sony spec

# --- Device address (shared by every button) ---------------------------------
DEVICE = 26
EXTENDED = 226

class SonyX700Code(Enum):
    """SIRC20 command numbers for the Sony UBP-X700 remote."""

    POWER = 21
    OPEN_CLOSE = 22
    PLAY = 26
    PAUSE = 25
    STOP = 24
    REWIND = 27
    FAST_FORWARD = 28
    PREVIOUS = 87
    NEXT = 86
    HOME = 66
    TOP_MENU = 44
    MENU = 41
    OPTIONS = 63
    RETURN = 67
    UP = 57
    DOWN = 58
    LEFT = 59
    RIGHT = 60
    SELECT = 61
    SUBTITLE = 99
    AUDIO = 100
    DISPLAY = 65
    FAVOURITE = 94
    NETFLIX = 75


def _sirc20_frame(command: int, device: int, extended: int) -> list[Timing]:
    """Build one SIRC20 frame with ideal timing."""
    timings: list[Timing] = [Timing(high_us=HEADER_MARK_US, low_us=HEADER_SPACE_US)]

    data = command | (device << 7) | (extended << 12)
    for _ in range(20):
        mark = ONE_MARK_US if (data & 1) else ZERO_MARK_US
        timings.append(Timing(high_us=mark, low_us=BIT_SPACE_US))
        data >>= 1

    last = timings[-1]
    timings[-1] = Timing(high_us=last.high_us, low_us=0)
    return timings


class SonyX700Command(Command):
    """SIRC20 IR command for a Sony UBP-X700 remote button."""

    def __init__(self, code: SonyX700Code) -> None:
        super().__init__(modulation=CARRIER_FREQ_HZ, repeat_count=FRAME_REPEAT)
        self._frame = _sirc20_frame(code.value, DEVICE, EXTENDED)
        frame_duration = sum(t.high_us + t.low_us for t in self._frame)
        self._inter_frame_gap = max(0, FRAME_PERIOD_US - frame_duration)

    @override
    def get_raw_timings(self) -> list[Timing]:
        timings = list(self._frame)
        for _ in range(self.repeat_count - 1):
            last = timings[-1]
            timings[-1] = Timing(high_us=last.high_us, low_us=self._inter_frame_gap)
            timings.extend(self._frame)
        return timings
