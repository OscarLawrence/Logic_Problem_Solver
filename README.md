# Universal Problem Solver (Safe Rewrite Preparation)

## Status: Python Implementation Removed
All previous Python code has been deleted due to inability to guarantee runtime immutability and logical safety (see `SYSTEM_STATUS_BRUTAL_HONESTY.md`).

## Next Steps
- Reimplement the system in a language with strong safety and immutability guarantees (Rust or Haskell recommended).
- See `MIGRATION.md` for rationale and migration plan.
- All new code must meet 100% logical and runtime safety requirements.

## Documentation
- `SYSTEM_STATUS_BRUTAL_HONESTY.md`: Full safety and coherence requirements
- `MIGRATION.md`: Migration rationale and next steps
- `docs/`: Place all new design and system documentation here

## Directory Structure
- `src/` — New source code (Rust/Haskell only)
- `docs/` — Documentation
- `tests/` — Future test cases

**No problem-solving code will be implemented until all safety requirements are provably met.**