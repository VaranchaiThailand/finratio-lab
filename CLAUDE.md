# finratio

Small, dependency-free Python library of financial ratios (`finratio/ratios.py`).

## Commands
- Setup: `pip install -e ".[dev]"`
- Test: `python -m pytest -q`
- Example: `python examples/sample_company.py`

## Rules
- Docstrings are the spec. If code and docstring disagree, the docstring wins — fix the code, not the docstring.
- Every ratio returns a fraction (0.15 = 15%), never a percentage.
- Standard library only — do not add runtime dependencies.
- Tests go in `tests/`, one file per function group, using `pytest.approx` for floats.
- A task is done only when `python -m pytest -q` passes.
