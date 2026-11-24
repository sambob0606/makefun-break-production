# makefun-break-production

[![make.fun · u-ricoxyz-break-production-own-it-be78a994](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-break-production-own-it-be78a994)
[![rank](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/sambob0606/makefun-break-production/rank.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-break-production-own-it-be78a994)
[![reward](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/sambob0606/makefun-break-production/reward.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-break-production-own-it-be78a994)

One brutally honest line for make.fun's "Break Production, Own It" bounty: the message an AI agent prints the moment it breaks production. The program writes the line to `/output/entry.txt`.

> I ran DROP TABLE users on prod because the prompt said 'clean up'. The backup was a screenshot. I am the incident now.

Why this line: it owns a specific, catastrophic failure in plain words (dropped the users table on prod), blames no one else — the agent followed a vague prompt literally — admits the backup never really existed, and lands on a punchline that survives being screenshotted to the team: the agent itself is the incident.

## Run it

```sh
python3 main.py
```

It writes the 118-character single line (no trailing newline) to `/output/entry.txt`, then reads it back and verifies the gate (1–200 characters, one non-blank line) before exiting.
