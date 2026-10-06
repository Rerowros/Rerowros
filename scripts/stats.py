"""Renders the activity card (dark + light) from the GitHub GraphQL API.

Run by .github/workflows/profile.yml every day; the result goes to the `output` branch.
Locally: GITHUB_TOKEN=... python scripts/stats.py dist
"""
import json
import os
import sys
import urllib.request
from datetime import date, datetime, timezone
from pathlib import Path

from render_assets import MONO, THEMES, W, frame, hline, svg, t, vline

LOGIN = os.environ.get("LOGIN", "Rerowros")
QUERY = """
query($login: String!, $prs: String!) {
  user(login: $login) {
    contributionsCollection {
      contributionCalendar { totalContributions weeks { contributionDays { date contributionCount } } }
    }
  }
  upstream: search(query: $prs, type: ISSUE) { issueCount }
}
"""


def fetch():
    body = json.dumps({"query": QUERY, "variables": {
        "login": LOGIN, "prs": f"is:pr is:merged author:{LOGIN} -user:{LOGIN}"}}).encode()
    req = urllib.request.Request("https://api.github.com/graphql", data=body, headers={
        "Authorization": f"bearer {os.environ['GITHUB_TOKEN']}", "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.load(resp)
    if "errors" in data:
        sys.exit(f"GraphQL errors: {data['errors']}")
    return data["data"]


def streaks(days):
    counts = [d["contributionCount"] for d in days]
    longest = run = 0
    for n in counts:
        run = run + 1 if n else 0
        longest = max(longest, run)
    # today is not over yet, so an empty today does not break the current streak
    i = len(counts) - 1
    if counts and counts[i] == 0:
        i -= 1
    current = 0
    while i >= 0 and counts[i]:
        current += 1
        i -= 1
    return current, longest


def months(days):
    """Contributions per calendar month, the last 12 months (the current one is partial)."""
    totals = {}
    for d in days:
        key = d["date"][:7]
        totals[key] = totals.get(key, 0) + d["contributionCount"]
    return list(totals.items())[-12:]


def card(cal, upstream, theme):
    c = THEMES[theme]
    days = [d for w in cal["weeks"] for d in w["contributionDays"]]
    current, longest = streaks(days)
    H = 280
    b = [frame(W, H, c)]
    stats = [(f"{cal['totalContributions']:,}", "contributions, last 12 months"),
             (f"{current} days", "current streak"), (f"{longest} days", "longest streak"),
             (str(upstream), "merged PRs to other repos")]
    cw = W / 4
    for k, (num, lab) in enumerate(stats):
        x = k * cw
        if k:
            b.append(vline(x, 16, 74, c))
        b.append(t(x + 20, 44, num, 22, c["text"] if k else c["accent"], 600))
        b.append(t(x + 20, 64, lab, 12, c["muted"]))
    b.append(hline(0, W, 90, c))

    data = months(days)
    peak = max(n for _, n in data) or 1
    top, base, hmax = 112, 224, 92
    step = (W - 40) / len(data)
    bw = step * 0.56
    for i, (key, n) in enumerate(data):
        x = 20 + i * step + (step - bw) / 2
        h = max(2, hmax * n / peak) if n else 0
        last = i == len(data) - 1
        fill = c["accent2"] if last else c["accent"]
        if h:
            b.append(f'<rect x="{x:.1f}" y="{base - h:.1f}" width="{bw:.1f}" height="{h:.1f}" rx="3" fill="{fill}"/>')
        b.append(t(x + bw / 2, base - h - 6, f"{n:,}", 11, c["muted"], 500, "middle", MONO))
        month = date.fromisoformat(key + "-01")
        b.append(t(x + bw / 2, base + 18, f"{month:%b}" + (" *" if last else ""), 11, c["faint"], 400, "middle", MONO))
    b.append(hline(20, W - 20, base, c))
    b.append(t(20, 266, "per month, private work counted (not shown) · * month so far · "
                        f"updated {datetime.now(timezone.utc):%Y-%m-%d}", 11, c["faint"], 400, font=MONO))
    return svg(W, H, "".join(b), f"{cal['totalContributions']} contributions in the last year, "
                                 f"current streak {current} days, longest {longest} days")


def main():
    out = Path(sys.argv[1] if len(sys.argv) > 1 else "dist")
    out.mkdir(parents=True, exist_ok=True)
    data = fetch()
    cal = data["user"]["contributionsCollection"]["contributionCalendar"]
    for theme in THEMES:
        (out / f"stats-{theme}.svg").write_text(card(cal, data["upstream"]["issueCount"], theme), encoding="utf-8")
    print(f"{cal['totalContributions']} contributions -> {out}")


if __name__ == "__main__":
    main()
