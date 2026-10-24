## October 24, 2026 — QAOA training, sampling, and noise sweep

- Ran the notebook locally in VS Code using the project environment.
- Verified that classical enumeration finds two optimal generator
  selections: (0, 1, 1, 0) and (1, 0, 0, 1), both with cost 11.
- Checked agreement between the penalty expression, expanded QUBO,
  and Ising expression across all 256 encoded assignments.
- Built and trained an eight-qubit p = 1 QAOA circuit with COBYLA,
  using starting seeds 42, 43, and 44.
- Selected seed 44 by its lowest observed expected penalized objective:
  approximately 516.45.
- Ran 4,096 ideal measurement shots and saved the counts.
- Evaluated five gate-noise strengths with the trained angles fixed.
- Saved training and noise figures, numerical results, and noise settings.
- Observed that noise reduced feasibility and optimal encoded probability,
  while optimal generator probability moved toward its random baseline.
