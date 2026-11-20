# GitHub API setup

- **Auth:** fine-grained PAT, repository `devpulse` only, read-only:
  Metadata, Contents, Pull requests, Deployments, Actions. 90-day expiry.
- **API version:** always send `X-GitHub-Api-Version: 2026-03-10` (pinned in code).
- **Env vars:** `GH_API_*` prefix (`GITHUB_` is reserved by GitHub Actions; `GH_TOKEN` is read by `gh` CLI).

| Endpoint | Purpose |
|---|---|
| `GET /rate_limit` | Quota check (`resources.core`), not counted |
| `GET /repos/{o}/{r}/commits?sha=main` | Commits on main |
| `GET /repos/{o}/{r}/pulls?state=closed` | PRs; `head.ref` carries type + Jira key |
| `GET /repos/{o}/{r}/pulls/{n}/commits` | Original PR commits (lead time start) |
| `GET /repos/{o}/{r}/commits/{sha}/pulls` | Map a main commit back to its PR |
| `GET /repos/{o}/{r}/deployments` + `/{id}/statuses` | Deployments; deploy time = `success` status |

## Rate limits
- Primary: 5,000 requests/hour (headers `x-ratelimit-*`).
- Secondary: max 100 concurrent requests, 900 points/minute → HTTP 429 + `Retry-After`.
- DevPulse uses at most 10 parallel workers.

## Pagination
`Link` response header; follow `rel="next"` until absent. `per_page` max 100.
