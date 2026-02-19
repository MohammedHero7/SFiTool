#!/usr/bin/env python3
"""Arabic shaping helper for bitmap-font pipelines.

Converts Arabic text into Arabic Presentation Forms so engines that do not
implement Arabic shaping can render connected glyphs from a font image.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass


@dataclass(frozen=True)
class Forms:
    isolated: str
    final: str | None = None
    initial: str | None = None
    medial: str | None = None


# Arabic Presentation Forms-B glyph mapping.
FORMS: dict[str, Forms] = {
    "\u0621": Forms("\uFE80"),
    "\u0622": Forms("\uFE81", "\uFE82"),
    "\u0623": Forms("\uFE83", "\uFE84"),
    "\u0624": Forms("\uFE85", "\uFE86"),
    "\u0625": Forms("\uFE87", "\uFE88"),
    "\u0626": Forms("\uFE89", "\uFE8A", "\uFE8B", "\uFE8C"),
    "\u0627": Forms("\uFE8D", "\uFE8E"),
    "\u0628": Forms("\uFE8F", "\uFE90", "\uFE91", "\uFE92"),
    "\u0629": Forms("\uFE93", "\uFE94"),
    "\u062A": Forms("\uFE95", "\uFE96", "\uFE97", "\uFE98"),
    "\u062B": Forms("\uFE99", "\uFE9A", "\uFE9B", "\uFE9C"),
    "\u062C": Forms("\uFE9D", "\uFE9E", "\uFE9F", "\uFEA0"),
    "\u062D": Forms("\uFEA1", "\uFEA2", "\uFEA3", "\uFEA4"),
    "\u062E": Forms("\uFEA5", "\uFEA6", "\uFEA7", "\uFEA8"),
    "\u062F": Forms("\uFEA9", "\uFEAA"),
    "\u0630": Forms("\uFEAB", "\uFEAC"),
    "\u0631": Forms("\uFEAD", "\uFEAE"),
    "\u0632": Forms("\uFEAF", "\uFEB0"),
    "\u0633": Forms("\uFEB1", "\uFEB2", "\uFEB3", "\uFEB4"),
    "\u0634": Forms("\uFEB5", "\uFEB6", "\uFEB7", "\uFEB8"),
    "\u0635": Forms("\uFEB9", "\uFEBA", "\uFEBB", "\uFEBC"),
    "\u0636": Forms("\uFEBD", "\uFEBE", "\uFEBF", "\uFEC0"),
    "\u0637": Forms("\uFEC1", "\uFEC2", "\uFEC3", "\uFEC4"),
    "\u0638": Forms("\uFEC5", "\uFEC6", "\uFEC7", "\uFEC8"),
    "\u0639": Forms("\uFEC9", "\uFECA", "\uFECB", "\uFECC"),
    "\u063A": Forms("\uFECD", "\uFECE", "\uFECF", "\uFED0"),
    "\u0641": Forms("\uFED1", "\uFED2", "\uFED3", "\uFED4"),
    "\u0642": Forms("\uFED5", "\uFED6", "\uFED7", "\uFED8"),
    "\u0643": Forms("\uFED9", "\uFEDA", "\uFEDB", "\uFEDC"),
    "\u0644": Forms("\uFEDD", "\uFEDE", "\uFEDF", "\uFEE0"),
    "\u0645": Forms("\uFEE1", "\uFEE2", "\uFEE3", "\uFEE4"),
    "\u0646": Forms("\uFEE5", "\uFEE6", "\uFEE7", "\uFEE8"),
    "\u0647": Forms("\uFEE9", "\uFEEA", "\uFEEB", "\uFEEC"),
    "\u0648": Forms("\uFEED", "\uFEEE"),
    "\u0649": Forms("\uFEEF", "\uFEF0"),
    "\u064A": Forms("\uFEF1", "\uFEF2", "\uFEF3", "\uFEF4"),
}

NON_JOINING_LEFT = {
    "\u0621", "\u0622", "\u0623", "\u0624", "\u0625", "\u0627", "\u0629", "\u062F", "\u0630", "\u0631", "\u0632", "\u0648", "\u0649"
}

LAM_ALEF_LIGATURES = {
    "\u0622": ("\uFEF5", "\uFEF6"),
    "\u0623": ("\uFEF7", "\uFEF8"),
    "\u0625": ("\uFEF9", "\uFEFA"),
    "\u0627": ("\uFEFB", "\uFEFC"),
}

TATWEEL = "\u0640"


def is_arabic_char(ch: str) -> bool:
    code = ord(ch)
    return (
        0x0600 <= code <= 0x06FF
        or 0x0750 <= code <= 0x077F
        or 0x08A0 <= code <= 0x08FF
        or 0xFB50 <= code <= 0xFDFF
        or 0xFE70 <= code <= 0xFEFF
    )


def can_connect_left(ch: str) -> bool:
    return ch in FORMS and ch not in NON_JOINING_LEFT


def can_connect_right(ch: str) -> bool:
    return ch in FORMS


def tighten_arabic_spacing(text: str) -> str:
    """Remove accidental spaces between Arabic letters while keeping word spaces."""
    chars = list(text)
    out: list[str] = []
    for i, ch in enumerate(chars):
        if ch != " ":
            out.append(ch)
            continue

        prev_ch = chars[i - 1] if i > 0 else ""
        next_ch = chars[i + 1] if i + 1 < len(chars) else ""

        # If the space is between two Arabic letters, treat it as accidental gap.
        if is_arabic_char(prev_ch) and is_arabic_char(next_ch):
            continue

        if not out or out[-1] == " ":
            continue

        out.append(" ")

    return "".join(out).strip()


def shape_arabic(text: str) -> str:
    chars = list(text)
    out: list[str] = []

    i = 0
    while i < len(chars):
        ch = chars[i]

        # Lam-alef ligatures.
        if ch == "\u0644" and i + 1 < len(chars) and chars[i + 1] in LAM_ALEF_LIGATURES:
            prev_ch = chars[i - 1] if i > 0 else ""
            isolated, final = LAM_ALEF_LIGATURES[chars[i + 1]]
            out.append(final if can_connect_left(prev_ch) else isolated)
            i += 2
            continue

        forms = FORMS.get(ch)
        if not forms:
            out.append(ch)
            i += 1
            continue

        prev_ch = chars[i - 1] if i > 0 else ""
        next_ch = chars[i + 1] if i + 1 < len(chars) else ""

        join_prev = can_connect_left(prev_ch) and can_connect_right(ch)
        join_next = can_connect_left(ch) and can_connect_right(next_ch)

        if join_prev and join_next and forms.medial:
            out.append(forms.medial)
        elif join_prev and forms.final:
            out.append(forms.final)
        elif join_next and forms.initial:
            out.append(forms.initial)
        else:
            out.append(forms.isolated)
        i += 1

    return "".join(out)


def normalize_spacing(text: str) -> str:
    compact = " ".join(part for part in text.split())
    compact = compact.replace("_", TATWEEL)
    return tighten_arabic_spacing(compact)


def main() -> None:
    parser = argparse.ArgumentParser(description="Shape Arabic text for bitmap fonts")
    parser.add_argument("text", nargs="+", help="Arabic text")
    args = parser.parse_args()

    normalized = normalize_spacing(" ".join(args.text))
    print(shape_arabic(normalized))


if __name__ == "__main__":
    main()
