_STROKE_SVG = (
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" '
    'stroke="{{color}}" stroke-width="{width}" stroke-linecap="round" '
    'stroke-linejoin="round">{body}</svg>'
)


def _stroke(body: str, width: float = 1.8) -> str:
    return _STROKE_SVG.format(body=body, width=width)


LOGO_SVG = (
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none">'
    '<path d="M4.48 14.74 A8 8 0 0 1 13.39 4.12" stroke="#3B82F6" '
    'stroke-width="3.4" stroke-linecap="round"/>'
    '<path d="M19.52 9.26 A8 8 0 0 1 10.61 19.88" stroke="#F59E0B" '
    'stroke-width="3.4" stroke-linecap="round"/>'
    '<circle cx="12" cy="12" r="2.2" fill="#FFFFFF"/>'
    '</svg>'
)

ICONS = {
    "monitor": _stroke(
        '<rect width="20" height="14" x="2" y="3" rx="2"/>'
        '<path d="M8 21h8M12 17v4"/>'
    ),
    "settings": _stroke(
        '<path d="M12.22 2h-.44a2 2 0 0 0-2 2v.18a2 2 0 0 1-1 1.73l-.43.25a2 2 0 '
        '0 1-2 0l-.15-.08a2 2 0 0 0-2.73.73l-.22.38a2 2 0 0 0 .73 2.73l.15.1a2 2 '
        '0 0 1 1 1.72v.51a2 2 0 0 1-1 1.74l-.15.09a2 2 0 0 0-.73 2.73l.22.38a2 2 '
        '0 0 0 2.73.73l.15-.08a2 2 0 0 1 2 0l.43.25a2 2 0 0 1 1 1.73V20a2 2 0 0 '
        '0 2 2h.44a2 2 0 0 0 2-2v-.18a2 2 0 0 1 1-1.73l.43-.25a2 2 0 0 1 2 '
        '0l.15.08a2 2 0 0 0 2.73-.73l.22-.39a2 2 0 0 0-.73-2.73l-.15-.08a2 2 0 '
        '0 1-1-1.74v-.5a2 2 0 0 1 1-1.74l.15-.09a2 2 0 0 0 .73-2.73l-.22-.38a2 2 '
        '0 0 0-2.73-.73l-.15.08a2 2 0 0 1-2 0l-.43-.25a2 2 0 0 1-1-1.73V4a2 2 0 '
        '0 0-2-2z"/><circle cx="12" cy="12" r="3"/>'
    ),
    "info": _stroke(
        '<circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><path d="M12 8h.01"/>'
    ),
    "user": _stroke(
        '<path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/>'
        '<circle cx="12" cy="7" r="4"/>'
    ),
    "copy": _stroke(
        '<rect width="14" height="14" x="8" y="8" rx="2" ry="2"/>'
        '<path d="M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2"/>'
    ),
    "check": _stroke('<path d="M20 6 9 17l-5-5"/>', 2.2),
    "eye": _stroke(
        '<path d="M2.06 12.35a1 1 0 0 1 0-.7 10.75 10.75 0 0 1 19.88 0 1 1 0 0 1 '
        '0 .7 10.75 10.75 0 0 1-19.88 0"/><circle cx="12" cy="12" r="3"/>'
    ),
    "eye_off": _stroke(
        '<path d="M10.73 5.08a10.74 10.74 0 0 1 11.2 6.57 1 1 0 0 1 0 .7 10.75 '
        '10.75 0 0 1-1.44 2.49"/><path d="M14.08 14.16a3 3 0 0 1-4.24-4.24"/>'
        '<path d="M17.48 17.5a10.75 10.75 0 0 1-15.42-5.15 1 1 0 0 1 0-.7 10.75 '
        '10.75 0 0 1 4.45-5.14"/><path d="m2 2 20 20"/>'
    ),
    "refresh": _stroke(
        '<path d="M21 12a9 9 0 1 1-9-9c2.52 0 4.93 1 6.74 2.74L21 8"/>'
        '<path d="M21 3v5h-5"/>'
    ),
    "chevron_down": _stroke('<path d="m6 9 6 6 6-6"/>', 2),
    "clock": _stroke(
        '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>', 1.6
    ),
    "minimize": _stroke('<path d="M5 12h14"/>', 1.6),
    "maximize": _stroke('<rect width="14" height="14" x="5" y="5" rx="2"/>', 1.6),
    "restore": _stroke(
        '<rect width="11" height="11" x="4" y="9" rx="2"/>'
        '<path d="M9 9V6a2 2 0 0 1 2-2h7a2 2 0 0 1 2 2v7a2 2 0 0 1-2 2h-3"/>',
        1.6,
    ),
    "close": _stroke('<path d="M18 6 6 18M6 6l12 12"/>', 1.6),
}