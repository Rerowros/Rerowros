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

from render_assets import MONO, THEMES, frame, hline, kick, svg, t, vline

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


def card(cal, upstream, theme):
    c = THEMES[theme]
    weeks = cal["weeks"]
    days = [d for w in weeks for d in w["contributionDays"]]
    current, longest = streaks(days)
    W, H = 1200, 330
    b = [frame(W, H, c)]
    b.append(kick(40, 44, "Activity · last 12 months", c))
    b.append(t(1160, 44, f"updated {datetime.now(timezone.utc):%Y-%m-%d}", 13, c["faint"], 500, "end", MONO))
    b.append(hline(0, W, 66, c))
    stats = [(f"{cal['totalContributions']:,}", "contributions, incl. private"),
             (str(current), "days, current streak"), (str(longest), "days, longest streak"),
             (str(upstream), "merged PRs to other repos")]
    for k, (num, lab) in enumerate(stats):
        x = k * 300
        if k:
            b.append(vline(x, 66, 160, c))
        b.append(t(x + 40, 116, num, 36, c["text"], 600, extra='letter-spacing="-1"'))
        b.append(t(x + 40, 142, lab, 15, c["muted"]))
    b.append(hline(0, W, 160, c))

    # contributions per week
    totals = [sum(d["contributionCount"] for d in w["contributionDays"]) for w in weeks]
    peak = max(totals) or 1
    # one huge week would flatten the rest, so the axis tops out at 1.5x the 90th percentile and taller bars are clipped
    nz = sorted(n for n in totals if n)
    top = min(peak, nz[int(len(nz) * 0.9)] * 1.5) if nz else 1
    x0, x1, base, hmax = 40, 1160, 282, 72
    step = (x1 - x0) / len(weeks)
    bw = step * 0.62
    last_month = None
    for i, (w, n) in enumerate(zip(weeks, totals)):
        x = x0 + i * step
        h = max(2, hmax * min(n, top) / top) if n else 0
        if h:
            fill = c["text"] if i == len(weeks) - 1 else c["muted"]
            b.append(f'<rect x="{x:.1f}" y="{base - h:.1f}" width="{bw:.1f}" height="{h:.1f}" rx="1.5" fill="{fill}">'
                     f'<title>week of {w["contributionDays"][0]["date"]}: {n}</title></rect>')
        if n > top:
            b.append(t(x + bw / 2, base - hmax - 6, str(n), 11, c["muted"], 500, "middle", MONO))
        first = date.fromisoformat(w["contributionDays"][0]["date"])
        if first.month != last_month:
            if last_month is not None:
                b.append(t(x, base + 22, f"{first:%b}", 12, c["faint"], 500, font=MONO))
            last_month = first.month
    b.append(hline(x0, x1, base, c))
    b.append(t(40, 188, "contributions per week · private work is counted, not shown", 12, c["faint"], 500, font=MONO))
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
