# Jira setup

- **Site:** `https://<your-site>.atlassian.net` (Jira Free plan)
- **Space:** DevPulse, key `DP`, Kanban template, team-managed

## Work types
| Work type | Purpose |
|---|---|
| Story / Task | Planned work, linked to Git branches (`feature/DP-12-...`) |
| Bug | Defects found before production |
| Incident | Production problems; feeds change fail rate and failed deployment recovery time |

## Incident fields
| Field | Type | Notes |
|---|---|---|
| Severity | Dropdown: SEV1, SEV2, SEV3 | SEV1 = most severe |
| Caused by deployment | Short text | Commit SHA of the deployment that caused the incident |

## Design rules
- DevPulse logic relies on **status categories** (To Do / In Progress / Done), never on status names.
- Recovery time is computed from the **changelog** (transition to a Done-category status).
- Incremental loads use the `updated` field as watermark.

## API access
- **Auth:** HTTP Basic (`email:token`) with a **scoped, read-only** API token (`read:jira-work`, `read:jira-user`), 90-day expiry.
- **Base URL:** scoped tokens go through `https://api.atlassian.com/ex/jira/{cloudId}`; cloudId from `https://<site>.atlassian.net/_edge/tenant_info`.
- **Config:** all values live in `.env` (see `.env.example`); custom field IDs are site-specific.

| Endpoint | Purpose | Pagination |
|---|---|---|
| `GET /rest/api/3/myself` | Auth check | none |
| `GET /rest/api/3/field` | Discover custom field IDs | none |
| `GET /rest/api/3/search/jql` | Search work items by JQL (`fields` must be explicit) | `nextPageToken` / `isLast` |
| `GET /rest/api/3/issue/{key}/changelog` | Field change history | `startAt` / `isLast` |
