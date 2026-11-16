"""Timestamp helpers shared by all source connectors.

Project rule: every timestamp is stored and compared in UTC.
"""

from datetime import UTC, datetime


def parse_api_timestamp(value: str) -> datetime:
    """Parse an ISO-8601 timestamp from Jira or GitHub and return it in UTC.

    Examples:
        GitHub: "2026-11-16T09:00:00Z"
        Jira:   "2026-11-16T10:00:00.000+0100"

    Raises:
        ValueError: if the value has no timezone, because such a timestamp is ambiguous.
    """
    parsed = datetime.fromisoformat(value)
    if parsed.tzinfo is None:
        raise ValueError(f"Timestamp without timezone is ambiguous: {value!r}")
    return parsed.astimezone(UTC)
