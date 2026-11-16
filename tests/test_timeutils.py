from datetime import UTC, datetime

import pytest

from devpulse.common.timeutils import parse_api_timestamp


def test_github_timestamp_with_z_suffix():
    assert parse_api_timestamp("2026-11-16T09:00:00Z") == datetime(2026, 11, 16, 9, 0, tzinfo=UTC)


def test_jira_timestamp_is_converted_to_utc():
    result = parse_api_timestamp("2026-11-16T10:00:00.000+0100")
    assert result == datetime(2026, 11, 16, 9, 0, tzinfo=UTC)
    assert result.utcoffset().total_seconds() == 0


def test_naive_timestamp_is_rejected():
    with pytest.raises(ValueError, match="ambiguous"):
        parse_api_timestamp("2026-11-16T10:00:00")
