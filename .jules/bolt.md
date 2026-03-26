## BOLT'S JOURNAL - PERFORMANCE OPTIMIZATIONS

## 2025-05-22 - [EKRLS Scaling & Vectorization]
**Learning:** Found a dimensionality bug in the EKRLS Governor where Q/alpha weren't expanding, and kernel computations were O(N) with high Python overhead.
**Action:** Always verify matrix expansion logic in recursive filters; use vectorized broadcasting for distance metrics.
