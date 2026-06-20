# GeoGuard Experiment Package

This package contains the code, benchmark inputs, processed Los Angeles County data, and lightweight result artifacts used for the GeoGuard workflow-spec planning experiments.

Main paths:

- `experiments/04_geo_faithfulness_evaluator/scripts/`: benchmark, scoring, repair, execution, bootstrap, and sensitivity scripts.
- `experiments/04_geo_faithfulness_evaluator/inputs/`: task list and local benchmark configuration with relative data paths.
- `experiments/04_geo_faithfulness_evaluator/outputs/`: generated workflow specs, summary tables, statistical tests, and artifact audit summaries. Large runtime artifact folders were excluded from this zip.
- `data/raw/geoguard/geoguard/data/`: processed geospatial inputs required by the benchmark.

Typical commands from the repository root:

```bash
python3 experiments/04_geo_faithfulness_evaluator/scripts/score_workflow_specs.py
python3 experiments/04_geo_faithfulness_evaluator/scripts/execute_workflow_specs.py
python3 experiments/04_geo_faithfulness_evaluator/scripts/bootstrap_workflow_stats.py
python3 experiments/04_geo_faithfulness_evaluator/scripts/metric_sensitivity_analysis.py
```

The included outputs are intended to document the reported experiment state without storing large generated execution artifacts.
