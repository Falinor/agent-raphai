from pydantic import BaseModel, Field
from enum import Enum
from typing import List, Dict, Optional, Any, Literal


class VisualizationType(str, Enum):
    """Type of visualization to use for data presentation."""

    LINE_CHART = "line_chart"
    BAR_CHART = "bar_chart"
    PIE_CHART = "pie_chart"
    SCATTER_CHART = "scatter_chart"
    RADAR_CHART = "radar_chart"
    TEXT = "text"
    TABLE = "table"


class BaseVisualization(BaseModel):
    """Base class for all visualization schemas."""

    type: VisualizationType = Field(
        ..., description="The type of visualization to render"
    )
    title: str = Field(..., description="Title for the visualization")
    description: str = Field(..., description="Description or explanation of the data")
    sql_query: Optional[str] = Field(
        None, description="The SQL query that generated this data"
    )


class LineChartVisualization(BaseVisualization):
    """Schema for line chart visualization data."""

    type: Literal[VisualizationType.LINE_CHART] = VisualizationType.LINE_CHART
    x_values: List[Any] = Field(
        ..., description="Values for the x-axis in the language of the user if needed"
    )
    y_values: List[float] = Field(..., description="Values for the y-axis")
    x_label: str = Field(
        ..., description="Label for x-axis in the language of the user"
    )
    y_label: str = Field(
        ..., description="Label for y-axis in the language of the user"
    )
    series_label: Optional[str] = Field(
        None, description="Label for the data series in the language of the user"
    )


class BarChartVisualization(BaseVisualization):
    """Schema for bar chart visualization data."""

    type: Literal[VisualizationType.BAR_CHART] = VisualizationType.BAR_CHART
    categories: List[str] = Field(..., description="Categories for the bars (x-axis)")
    values: List[float] = Field(..., description="Values for the bars (y-axis)")
    x_label: str = Field(..., description="Label for x-axis")
    y_label: str = Field(..., description="Label for y-axis")
    series_label: Optional[str] = Field(None, description="Label for the data series")


class PieChartVisualization(BaseVisualization):
    """Schema for pie chart visualization data."""

    type: Literal[VisualizationType.PIE_CHART] = VisualizationType.PIE_CHART
    labels: List[str] = Field(
        ..., description="Labels for the pie slices in the language of the user"
    )
    values: List[float] = Field(..., description="Values for the pie slices")


class ScatterChartPoint(BaseModel):
    """Schema for a single point in a scatter chart."""

    x: float = Field(..., description="X coordinate")
    y: float = Field(..., description="Y coordinate")
    z: Optional[float] = Field(None, description="Z coordinate (optional)")
    label: Optional[str] = Field(
        None, description="Point label (optional) in the language of the user"
    )


class ScatterChartVisualization(BaseVisualization):
    """Schema for scatter chart visualization data."""

    type: Literal[VisualizationType.SCATTER_CHART] = VisualizationType.SCATTER_CHART
    points: List[ScatterChartPoint] = Field(..., description="Points to plot")
    x_label: str = Field(
        ..., description="Label for x-axis in the language of the user"
    )
    y_label: str = Field(
        ..., description="Label for y-axis in the language of the user"
    )
    z_label: Optional[str] = Field(
        None, description="Label for z-axis (optional) in the language of the user"
    )


class RadarChartDataPoint(BaseModel):
    """Schema for a single data point in a radar chart."""

    subject: str = Field(..., description="Subject name in the language of the user")
    values: Dict[str, float] = Field(..., description="Values for each axis")


class RadarChartVisualization(BaseVisualization):
    """Schema for radar chart visualization data."""

    type: Literal[VisualizationType.RADAR_CHART] = VisualizationType.RADAR_CHART
    data: List[RadarChartDataPoint] = Field(
        ..., description="Data points for the radar chart"
    )
    keys: List[str] = Field(..., description="Keys/axes for the radar chart")


class TableVisualization(BaseVisualization):
    """Schema for table visualization data."""

    type: Literal[VisualizationType.TABLE] = VisualizationType.TABLE
    columns: List[str] = Field(
        ..., description="Column names in the language of the user"
    )
    data: List[List[Any]] = Field(..., description="Table data as rows of values")
    markdown: Optional[str] = Field(
        None, description="Markdown representation of the table"
    )


class TextVisualization(BaseVisualization):
    """Schema for text visualization (explanations, descriptions, etc.)."""

    type: Literal[VisualizationType.TEXT] = VisualizationType.TEXT
    content: str = Field(..., description="The text content to display")
    markdown: Optional[str] = Field(
        None, description="Markdown formatted content (if available)"
    )


# Functions to create visualizations from dataframes
