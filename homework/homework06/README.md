# Stage 6 — Data Preprocessing

## Overview
This homework implements three reusable data-cleaning functions in
`src/cleaning.py` and applies them to `data/raw/sample_data.csv`,
producing `data/processed/sample_data_cleaned.csv`.

## Cleaning Strategy & Assumptions

### 1. Fill missing values with median (`fill_missing_median`)
Applied to: `age`, `income`, `score`.

**Assumption:** Missingness in these numeric columns is MCAR/MAR — i.e.,
not systematically tied to the missing value itself. Median is used
instead of mean because it is robust to outliers and skewed
distributions.

### 2. Drop high-missingness columns (`drop_missing`, threshold=0.5)
Applied to: all columns; only `extra_data` (71% missing) was dropped.

**Assumption:** A column missing more than 50% of its values carries too
little reliable signal to impute confidently, and is treated as
non-essential. Tradeoff: if `extra_data` actually contained a rare but
important signal, this strategy discards it — a stricter/looser
threshold could be revisited depending on domain context.

### 3. Normalize to [0, 1] (`normalize_data`, min-max scaling)
Applied to: `age`, `income`, `score` (after filling missing values).

**Assumption:** The observed min/max values are representative of the
true range of each feature (not extreme outliers or data-entry errors).
Min-max scaling was chosen over StandardScaler because the dataset is
small and we did not verify a normal distribution assumption.

## Before vs After Summary
- Original shape: 7 rows × 6 columns, with missing values in `age`,
  `income`, `score`, and `extra_data`.
- Cleaned shape: 7 rows × 5 columns, zero missing values, numeric
  columns rescaled to [0, 1].

## Reproducibility
All cleaning logic lives in `src/cleaning.py` as modular, documented
functions so it can be reapplied to future datasets with the same
structure.