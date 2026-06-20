#!/usr/bin/env python3
"""Create a compact figure showing representative executed artifacts."""

from __future__ import annotations

from pathlib import Path

import geopandas as gpd
import matplotlib

matplotlib.use("Agg")
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import rasterio


ROOT = Path(__file__).resolve().parents[3]
RUN = ROOT / "experiments/04_geo_faithfulness_evaluator/outputs/workflow_spec_execution/runs/qwen2.5-coder_32b/geoguard_exec_repair"
OUT = ROOT / "papers/geoguard_manuscript_source/Figure 2.png"


def vector_panel(ax, rel: str, title: str, column: str | None = None) -> None:
    gdf = gpd.read_file(RUN / rel)
    if len(gdf) > 800:
        gdf = gdf.sample(800, random_state=7)
    gdf.plot(ax=ax, column=column if column in gdf.columns else None, cmap="YlGnBu", linewidth=0.05, edgecolor="#222222")
    ax.set_title(title, fontsize=9)
    ax.set_axis_off()


def raster_panel(ax, rel: str, title: str) -> None:
    with rasterio.open(RUN / rel) as src:
        arr = src.read(1, masked=True)
    ax.imshow(arr, cmap="coolwarm")
    ax.set_title(title, fontsize=9)
    ax.set_axis_off()


def image_panel(ax, rel: str, title: str) -> None:
    img = mpimg.imread(RUN / rel)
    ax.imshow(img)
    ax.set_title(title, fontsize=9)
    ax.set_axis_off()


def main() -> None:
    fig, axes = plt.subplots(2, 3, figsize=(10.5, 7.2))
    vector_panel(axes[0, 0], "T001/T001_buffer_hospitals.gpkg", "T001 hospital buffers")
    vector_panel(axes[0, 1], "T007/T007_flood_tract_overlay_area.gpkg", "T007 flood overlay", "flood_area_m2")
    raster_panel(axes[0, 2], "T016/T016_temperature_clip.tif", "T016 raster clip")
    vector_panel(axes[1, 0], "T024/T024_temperature_school_join.gpkg", "T024 temp + schools", "temp_mean")
    image_panel(axes[1, 1], "T027/T027_school_density_choropleth.png", "T027 school density map")
    image_panel(axes[1, 2], "T030/T030_multivariate_risk_map.png", "T030 combined risk map")
    fig.tight_layout(pad=1.0)
    fig.savefig(OUT, dpi=220)
    print(OUT.relative_to(ROOT))


if __name__ == "__main__":
    main()
