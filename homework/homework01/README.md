# Savings Goal Tracker — Emergency Rent Fund

**Stage:** Problem Framing & Scoping (Stage 01)

## Problem Statement
I want to know whether my current rate of saving will let me build up a 6-month
emergency rent fund ($3,000/month × 6 months = $18,000) within a reasonable
timeframe, and if not, how much I need to save each month to hit that target.
This matters because having this buffer reduces financial risk if I lose income
or face unexpected expenses — right now I don't have a clear picture of my
savings trajectory or how sensitive it is to changes in monthly spending.

## Stakeholder & User
I am both the stakeholder (decision-maker: how much to save each month, whether
to cut spending in certain categories) and the user (the person reviewing the
analysis) — this is a personal finance project, so the two roles are the same
person. Decisions are reviewed on a monthly basis, after each month's bank
statement is available.

## Useful Answer & Decision
- **Type:** Primarily Predictive (projected time to reach $18,000 given current
  savings rate), supported by Descriptive analysis (monthly income/expense
  breakdown by category).
- **Metric:** Projected months remaining to reach the $18,000 goal.
- **Artifact:** A notebook/chart showing current savings trend, projected
  completion date, and a "what-if" comparison (e.g. how much sooner I'd reach
  the goal if I saved an extra $X/month).
- **Decision trigger:** If the projection shows I won't reach the goal within
  12 months, I'll revisit my monthly budget and cut discretionary spending.

## Assumptions & Constraints
- Data source: transaction history exported as CSV from my personal bank
  account (single account, no shared/joint expenses to separate out).
- Data availability: last 3 months of transaction history.
- Income is assumed relatively stable month to month (no major raises/job
  changes assumed during the analysis window).
- No investment returns considered — this is pure cash savings accumulation,
  not an investment projection.
- Analysis is manual/monthly cadence, not real-time.

## Known Unknowns / Risks
- Only 3 months of data may not capture seasonal spending variation (e.g.
  holidays, annual expenses like insurance renewals).
- Unexpected large expenses (medical, car repair, etc.) could disrupt the
  projection and aren't currently modeled.
- Income changes (raise, job change, reduced hours) would invalidate the
  stable-income assumption.
- Bank CSV export format may vary or require cleaning (e.g. inconsistent
  date formats, merged transaction descriptions).

## Lifecycle Mapping
Goal → Stage → Deliverable
- Understand current savings trajectory → Problem Framing & Scoping (Stage 01) → Scoping paragraph + repo skeleton
- Build monthly income/expense summary → Data Collection & Cleaning (later stage) → Cleaned transaction dataset
- Project time to reach $18,000 goal → Modeling/Analysis (later stage) → Savings projection chart + notebook

## Repo Plan
- `data/raw/` — original bank CSV exports (not pushed to GitHub if sensitive —
  add to .gitignore)
- `data/processed/` — cleaned/categorized transaction data
- `src/` — reusable functions (e.g. CSV parsing, categorization logic)
- `notebooks/` — exploration and analysis notebooks
- `docs/` — this project's stakeholder artifact
- Update cadence: monthly, after each new bank statement is available