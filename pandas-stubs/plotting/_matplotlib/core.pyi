from __future__ import annotations

class MPLPlot:
    orientation: str | None = ...
    data = ...
    by = ...
    kind = ...
    sort_columns = ...
    subplots = ...
    sharex: bool = ...
    sharey = ...
    figsize = ...
    layout = ...
    xticks = ...
    yticks = ...
    xlim = ...
    ylim = ...
    title = ...
    use_index = ...
    fontsize = ...
    rot = ...
    grid = ...
    legend = ...
    legend_handles = ...
    legend_labels = ...
    ax = ...
    fig = ...
    axes = ...
    errors = ...
    secondary_y = ...
    colormap = ...
    table = ...
    include_bool = ...
    kwds = ...
    def __init__(
        self,
        data,
        kind=...,
        by=...,
        subplots: bool = ...,
        sharex=...,
        sharey: bool = ...,
        use_index: bool = ...,
        figsize=...,
        grid=...,
        legend: bool = ...,
        rot=...,
        ax=...,
        fig=...,
        title=...,
        xlim=...,
        ylim=...,
        xticks=...,
        yticks=...,
        sort_columns: bool = ...,
        fontsize=...,
        secondary_y: bool = ...,
        colormap=...,
        table: bool = ...,
        layout=...,
        include_bool: bool = ...,
        **kwds,
    ) -> None: ...
    @property
    def nseries(self): ...
    def draw(self) -> None: ...
    def generate(self) -> None: ...
    @property
    def result(self): ...
    @property
    def legend_title(self): ...
    def plt(self): ...
    @classmethod
    def get_default_ax(cls, ax) -> None: ...
    def on_right(self, i): ...

class PlanePlot(MPLPlot):
    x = ...
    y = ...
    def __init__(self, data, x, y, **kwargs) -> None: ...
    @property
    def nseries(self): ...

class ScatterPlot(PlanePlot):
    c = ...
    def __init__(self, data, x, y, s=..., c=..., **kwargs) -> None: ...

class HexBinPlot(PlanePlot):
    C = ...
    def __init__(self, data, x, y, C=..., **kwargs) -> None: ...

class LinePlot(MPLPlot):
    orientation: str = ...
    data = ...
    x_compat = ...
    def __init__(self, data, **kwargs) -> None: ...

class AreaPlot(LinePlot):
    def __init__(self, data, **kwargs) -> None: ...

class BarPlot(MPLPlot):
    orientation: str = ...
    bar_width = ...
    tick_pos = ...
    bottom = ...
    left = ...
    log = ...
    tickoffset = ...
    lim_offset = ...
    ax_pos = ...
    def __init__(self, data, **kwargs) -> None: ...

class BarhPlot(BarPlot):
    orientation: str = ...

class PiePlot(MPLPlot):
    def __init__(self, data, kind=..., **kwargs) -> None: ...
