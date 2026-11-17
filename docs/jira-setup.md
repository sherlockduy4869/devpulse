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
