# MIGRATION.md

## Python Implementation Removed

All Python proof and safety-critical code has been deleted. This is due to the inability of Python to guarantee runtime immutability, interface consistency, and logical safety as required by the system's core principles (see SYSTEM_STATUS_BRUTAL_HONESTY.md).

## Next Steps
- Reimplement the core logic in a language with strong immutability and safety guarantees (Rust or Haskell recommended).
- Use the `src/` directory for new source code.
- Place all documentation in `docs/`.
- Place all future tests in `tests/`.

## Requirements
- 100% logical and runtime safety
- No partial or unsafe implementations
- All code must be provably safe and coherent

See SYSTEM_STATUS_BRUTAL_HONESTY.md for full requirements and rationale.
