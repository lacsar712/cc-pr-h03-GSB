"""Blank cyan in list/projection while detail keeps value."""

BLANK_LIST_CYAN = True
ZERO_OUT_PARAM = True


def project_list_row(row: dict) -> dict:
    out = dict(row)
    if BLANK_LIST_CYAN:
        out["cyan_mm"] = ""
    return out


def map_out(row: dict) -> dict:
    out = dict(row)
    if ZERO_OUT_PARAM:
        out["cyan_mm"] = 0
    return out


def template_cyan(value):
    return "" if BLANK_LIST_CYAN else value


def keep_detail(row: dict) -> dict:
    return dict(row)


def reason_placeholder() -> str:
    return ""
