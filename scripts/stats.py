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

from render_assets import MONO, THEMES, frame, svg, t

LOGIN = os.environ.get("LOGIN", "Rerowros")
LEVELS = {
    "dark": ["#161b22", "#22306b", "#2f6bff", "#8b3dff", "#e81cff"],
    "light": ["#ebedf0", "#c7d4ff", "#2f6bff", "#8b3dff", "#e81cff"],
}
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


def thresholds(days):
    nz = sorted(d["contributionCount"] for d in days if d["contributionCount"])
    if not nz:
        return [1, 1, 1]
    return [nz[int(len(nz) * q)] for q in (0.25, 0.5, 0.75)]


def level(n, th):
    if n == 0:
        return 0
    return 1 + sum(n > x for x in th)


def card(cal, upstream, theme):
    c, lv = THEMES[theme], LEVELS[theme]
    weeks = cal["weeks"]
    days = [d for w in weeks for d in w["contributionDays"]]
    current, longest = streaks(days)
    th = thresholds(days)
    W, H = 1200, 360
    b = [frame(W, H, c)]
    b.append(t(56, 58, "ACTIVITY · LAST 12 MONTHS", 15, "url(#g)", 700, font=MONO, extra='letter-spacing="1.5"'))
    b.append(t(1144, 58, f"updated {datetime.now(timezone.utc):%Y-%m-%d}", 13, c["faint"], 500, "end", MONO))
    stats = [(f"{cal['totalContributions']:,}", "contributions, incl. private"),
             (str(current), "days, current streak"), (str(longest), "days, longest streak"),
             (str(upstream), "merged PRs to other repos")]
    for k, (num, lab) in enumerate(stats):
        x = 56 + k * 272
        b.append(t(x, 108, num, 38, "url(#g)", 700))
        b.append(t(x, 134, lab, 16, c["muted"]))

    cell, gap = 14, 4
    x0 = (W - len(weeks) * (cell + gap) + gap) / 2
    y0 = 186
    last_month = None
    for wi, w in enumerate(weeks):
        x = x0 + wi * (cell + gap)
        first = date.fromisoformat(w["contributionDays"][0]["date"])
        if first.month != last_month and wi < len(weeks) - 2:
            if last_month is not None or first.day <= 7:
                b.append(t(x, y0 - 10, f"{first:%b}", 12, c["faint"], 500, font=MONO))
            last_month = first.month
        for d in w["contributionDays"]:
            wd = (date.fromisoformat(d["date"]).weekday() + 1) % 7  # Sunday first, like GitHub
            n = d["contributionCount"]
            b.append(f'<rect x="{x:.1f}" y="{y0 + wd * (cell + gap)}" width="{cell}" height="{cell}" rx="3" '
                     f'fill="{lv[level(n, th)]}"><title>{d["date"]}: {n}</title></rect>')

    ly = y0 + 7 * (cell + gap) + 22
    b.append(t(56, ly + 11, "Private work shows as counts only · rendered daily by GitHub Actions", 13, c["faint"]))
    lx = 1144 - 5 * (cell + gap) - 40
    b.append(t(lx - 8, ly + 11, "less", 12, c["faint"], 500, "end", MONO))
    for k in range(5):
        b.append(f'<rect x="{lx + k * (cell + gap)}" y="{ly}" width="{cell}" height="{cell}" rx="3" fill="{lv[k]}"/>')
    b.append(t(lx + 5 * (cell + gap) + 4, ly + 11, "more", 12, c["faint"], 500, font=MONO))
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
