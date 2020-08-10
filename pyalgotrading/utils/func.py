"""
A module for plotting candlesticks
"""
import pandas as pd

from pyalgotrading.constants import PlotType


def import_with_install(package_import_name, package_install_name=None, dependancies=()):
    """
    Helps import 'package' even if its not installed.

    If package is installed, it will be imported and returned.
    If its not installed, it will be installed using 'pip' and a re-import will be attempted, which should succeed if the package was imported correctly.

    Args:
        package_import_name: name of package to be installed using pip, str
        package_install_name: name of package to be imported. Default is None, which means package can be imported with the same name as used for installation. If not, this parameter can be used to specify a different import name.
        dependancies: list of python packages to be installed as additional dependencies'

    Returns:
        The imported package
    """

    package_install_name = package_install_name if package_install_name is not None else package_import_name

    try:
        return __import__(package_import_name)
    except ImportError:
        print(f"Installing package {package_import_name} via pip. This may take a while...")
        import subprocess
        import sys
        cmd_list = [sys.executable, '-m', 'pip', 'install', package_install_name]
        if dependancies:
            cmd_list.extend(dependancies)
        subprocess.check_call(cmd_list)
        return __import__(package_import_name)


def plot_candlestick_chart(data: pd.DataFrame, plot_type: PlotType, caption: str = '', hide_missing_dates: bool = False, show: bool = True, indicators: tuple = (), plot_indicators_separately: bool = False, plot_height: int = 500,
                           plot_width: int = 1000):
    """
    Function to create charts for various candlesticks pattern data -
        - Japanese
        - Heikin-Ashi
        - Linebreak
        - Renko
        - Japanese for Quandl data

    Support for displaying indicator data (on top of candlesticks pattern data or separately).

    Args:
        data: Pandas DataFrame with columns `timestamp`, `open`, 'high`, 'low`, `close`
        plot_type: Enum of type PlotType
        caption: Caption for the chart
        hide_missing_dates: If True, missing dates in the `data` (say due to no data over weekend) will be hidden and a continuous plot will be shown.
                            If False, gaps would be shown for missing dates. However, the date formatting on the x-axis is better here, so prefer this when there are no date gaps.
        show: If True, figure will be shown. Useful for displaying figures inline while using Jupyter Notebooks
        indicators: Indicator data to be displayed
        plot_indicators_separately: If True, indicator data would be plotted in a different subplot. Use this when indicator data range coincides with the historical data range.
                                    If False, it will be plotted in the same subplot as the historical data. Use this when indicator data range does not coincide with the historical data range
        plot_height: Plot height in pixels
        plot_width: Plot width in pixels
    """
    import_with_install(package_import_name='plotly', package_install_name='plotly==4.9.0', dependancies=['notebook>=5.3', 'ipywidgets==7.5', 'psutil'])
    # Plotly requirements taken from here: https://pypi.org/project/plotly/
    from plotly.subplots import make_subplots
    from plotly import graph_objects as go

    # Sanity checks
    if not isinstance(plot_type, PlotType):
        print(f'Error: plot_type should be an instance of {PlotType.__class__}')
        return

    # Plot
    if plot_type is PlotType.QUANDL_JAPANESE:
        data['timestamp'] = data.index

    if hide_missing_dates:
        # Plotly has a limitation where if the timestamp are DateTime.DateTime objects which are not continuous,
        # it will plot the missing dates as empty space, which makes the curve look unnatural. The below code gives
        # custom timestamp formatting, which will be the x-axis ticks
        format_timestamp = lambda x: x.strftime("%d/%m %H:%M")
        timestamps = data['timestamp'].apply(format_timestamp)
    else:
        timestamps = data['timestamp']

    candlesticks_data_subplot_row_index = 1
    candlesticks_data_subplot_col_index = 1
    if indicators and (plot_indicators_separately is True):
        fig = make_subplots(rows=3, cols=1, vertical_spacing=0.05, shared_xaxes=True, specs=[[{"rowspan": 2}], [{}], [{}]])
        indicator_subplot_row_index = 3
        indicator_subplot_col_index = 1
    else:
        fig = make_subplots(rows=1, cols=1, vertical_spacing=0.05, shared_xaxes=True)
        indicator_subplot_row_index = 1
        indicator_subplot_col_index = 1

    if plot_type in [PlotType.JAPANESE, PlotType.HEIKINASHI]:
        fig.append_trace(go.Candlestick(x=timestamps, open=data['open'], high=data['high'], low=data['low'], close=data['close'], name='Historical Data'), row=candlesticks_data_subplot_row_index, col=candlesticks_data_subplot_col_index)
    elif plot_type == PlotType.LINEBREAK:
        fig = go.Figure(data=[go.Candlestick(x=timestamps, open=data['open'], high=data[["open", "close"]].max(axis=1), low=data[["open", "close"]].min(axis=1), close=data['close'], name='Historical Data')])
    elif plot_type == PlotType.RENKO:
        fig = go.Figure(data=[go.Candlestick(x=timestamps, open=data['open'], high=data[["open", "close"]].max(axis=1), low=data[["open", "close"]].min(axis=1), close=data['close'], name='Historical Data')])
    elif plot_type == PlotType.QUANDL_JAPANESE:
        fig = go.Figure(data=[go.Candlestick(x=timestamps, open=data['Open'], high=data['High'], low=data['Low'], close=data['Close'], name='Historical Data')])
    else:
        print(f'Error: plot_type ({plot_type}) is not implemented yet')
        return

    for indicator in indicators:
        indicator_name = indicator['name']
        indicator_data = indicator['data']
        extra = indicator['extra'] if 'extra' in indicator else {}
        fig.add_trace(go.Scatter(x=timestamps, y=indicator_data, name=indicator_name, **extra), row=indicator_subplot_row_index, col=indicator_subplot_col_index)

    # Plot customization
    if hide_missing_dates:
        # Plotly has a limitation where if the timestamp are DateTime.DateTime objects which are not continuous,
        # it will plot the missing dates as empty space, which makes the curve look unnatural. Hence, the below fix
        fig.layout.xaxis.type = 'category'

    fig.update(layout_xaxis_rangeslider_visible=False)
    fig.update_layout(title={'text': caption, 'y': 0.9, 'x': 0.5, 'xanchor': 'center', 'yanchor': 'bottom'}, height=plot_height, width=plot_width)

    # Show the plot
    if show:
        fig.show()
