from __future__ import annotations

from matplotlib.axes import Axes as PlotAxes
from pandas.core.base import PandasObject as PandasObject
from pandas.core.frame import DataFrame

def hist_series(
    self,
    by=...,
    ax=...,
    grid: bool = ...,
    xlabelsize=...,
    xrot=...,
    ylabelsize=...,
    yrot=...,
    figsize=...,
    bins: int = ...,
    backend=...,
    **kwargs,
): ...
def hist_frame(
    data,
    column=...,
    by=...,
    grid: bool = ...,
    xlabelsize=...,
    xrot=...,
    ylabelsize=...,
    yrot=...,
    ax=...,
    sharex: bool = ...,
    sharey: bool = ...,
    figsize=...,
    layout=...,
    bins: int = ...,
    backend=...,
    **kwargs,
): ...
def boxplot(
    data: DataFrame,
    column: str | list[str] | None = ...,
    by: str | list[str] | None = ...,
    ax: PlotAxes | None = ...,
    fontsize: float | str | None = ...,
    rot: float = ...,
    grid: bool = ...,
    figsize: tuple[float, float] | None = ...,
    layout: tuple[int, int] | None = ...,
    return_type: str | None = ...,
): ...
def boxplot_frame(
    self,
    column=...,
    by=...,
    ax=...,
    fontsize=...,
    rot: int = ...,
    grid: bool = ...,
    figsize=...,
    layout=...,
    return_type=...,
    backend=...,
    **kwargs,
): ...
def boxplot_frame_groupby(
    grouped,
    subplots: bool = ...,
    column=...,
    fontsize=...,
    rot: int = ...,
    grid: bool = ...,
    ax=...,
    figsize=...,
    layout=...,
    sharex: bool = ...,
    sharey: bool = ...,
    backend=...,
    **kwargs,
): ...

class PlotAccessor(PandasObject):
    def __init__(self, data) -> None: ...
    def __call__(self, *args, **kwargs): ...
    def line(self, x=..., y=..., **kwargs) -> PlotAccessor: ...
    def bar(self, x=..., y=..., **kwargs) -> PlotAccessor: ...
    def barh(self, x=..., y=..., **kwargs) -> PlotAccessor: ...
    def box(self, by=..., **kwargs) -> PlotAccessor: ...
    def hist(self, by=..., bins: int = ..., **kwargs) -> PlotAccessor: ...
    def kde(self, bw_method=..., ind=..., **kwargs) -> PlotAccessor: ...
    density = ...
    def area(self, x=..., y=..., **kwargs) -> PlotAccessor: ...
    def pie(self, **kwargs) -> PlotAccessor: ...
    def scatter(self, x, y, s=..., c=..., **kwargs) -> PlotAccessor: ...
    def hexbin(
        self, x, y, C=..., reduce_C_function=..., gridsize=..., **kwargs
    ) -> PlotAccessor: ...
