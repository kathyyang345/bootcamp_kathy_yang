# Data Storage Utilities — Sample Price Data

**Stage:** Data Storage (Stage 05)

## Objective
Implement a reproducible storage layer for a sample dataset: save to two
formats (CSV and Parquet), reload and validate the data, and abstract the
save/load logic into reusable utility functions — all driven by environment
variables rather than hardcoded paths.

## Data Storage

### Folder Structure
- `data/raw/` — original data as first saved, in CSV format. Treated as the
  immutable source; new versions get new timestamped filenames rather than
  overwriting.
- `data/processed/` — the same data re-saved in Parquet format, representing
  an analysis-ready version with preserved dtypes.

### Formats Used and Why
- **CSV** (`data/raw/`) — human-readable, easy to diff in git, and universally
  supported. Used for the raw layer since transparency matters more than
  performance at this stage.
- **Parquet** (`data/processed/`) — columnar, compressed, and preserves data
  types (e.g. dates stay dates instead of turning into text on reload).
  Requires the `pyarrow` engine, installed via `pip install pyarrow` in the
  `bootcamp_env` conda environment.

### Environment-Driven Paths
Paths are never hardcoded. A `.env` file (not committed to git — listed in
`.gitignore`) defines: 
```
DATA_DIR_RAW=data/raw
DATA_DIR_PROCESSED=data/processed
```

The notebook loads these with `python-dotenv`:
```python
from dotenv import load_dotenv
load_dotenv()
RAW = pathlib.Path(os.getenv('DATA_DIR_RAW', 'data/raw'))
PROC = pathlib.Path(os.getenv('DATA_DIR_PROCESSED', 'data/processed'))
```
`.env.example` is committed as a template so anyone cloning the repo knows
what variables to set locally.

### Utility Functions
`write_df(df, path)` and `read_df(path)` route by file suffix (`.csv` vs
`.parquet`), auto-create missing parent directories, and raise a clear
`RuntimeError` if the Parquet engine is unavailable, instead of failing with
an unclear low-level error.

### Validation
After every save, the file is reloaded and checked with `validate_loaded()`:
shape must match the original, and the `date`/`price` columns must keep their
expected dtypes (datetime and numeric respectively). Both the CSV and Parquet
round trips passed all checks.

### Assumptions
- Sample data is synthetic (20 days of simulated AAPL prices), not real
  financial data, so no privacy/sensitivity handling was needed for this
  stage's dataset.
- Timestamped filenames (`sample_YYYYMMDD-HHMMSS.csv`) are used instead of
  fixed names, so repeated runs don't overwrite prior outputs.