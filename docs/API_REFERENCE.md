# API Reference: HAG Build 2.1 Final

This document details the core classes, configuration, and shared values for HAG-2.1.

## 1. Core Configuration (`configs/bayesian_weights.json`)
The system behavior is governed by a central Bayesian configuration:
- **EKRLS**: Sigma (kernel width) and Q-threshold (integrity boundary).
- **Ribbon**: Global FPR (False Positive Rate) targets.
- **Q_Score_Weights**: Definitive weights for grounding, certainty, and coherence.

## 2. System Values (`src.core.values`)
### `SystemValues`
**Description:** Central repository for shared constants and Bayesian weight calculation.
- `get_aggregate_q_score(scores)`: Computes weighted truth score.

## 3. Learning Mechanisms (`src.agents`)
### `HolographicWeightEncoder`
**Description:** FFT-based weight distribution for 94%+ model resilience.
### `LieAugmenter`
**Description:** Discovers continuous symmetries for 40% data efficiency.
### `RecursiveDiffusionReasoning`
**Description:** Iterative "crystallization" of solutions.

## 4. Governance (`src.governor`)
### `HolographicGovernor`
**Description:** EKRLS-based integrity tracker. Now respects global `SystemValues`.

## 5. Agent Orchestration (`src.agents.native_recursive`)
### `NativelyRecursiveAgent`
**Description:** High-level orchestrator for 10M+ context tasks. Integrates Governor and Resilient Models.

## 6. CLI Entry Point
The system can be invoked via `hag-cli` or `python3 src/cli/main.py`.
