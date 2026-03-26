## BOLT'S JOURNAL - PERFORMANCE OPTIMIZATIONS

## 2025-05-22 - [EKRLS Scaling & Vectorization]
**Learning:** Found a dimensionality bug in the EKRLS Governor where Q/alpha weren't expanding, and kernel computations were O(N) with high Python overhead.
**Action:** Always verify matrix expansion logic in recursive filters; use vectorized broadcasting for distance metrics.

## 2025-05-22 - [Amortized Storage & Norm Expansion]
**Learning:** Even with vectorization, O(N^2) memory reallocations and repeated subtraction/squaring in distance metrics create bottlenecks as N grows.
**Action:** Use block-growing pre-allocated arrays and the A^2 + B^2 - 2AB trick for distance metrics in high-frequency recursive filters.
