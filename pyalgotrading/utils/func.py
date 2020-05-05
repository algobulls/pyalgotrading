import enum

counter = 0


class PlotType(enum.Enum):
    OHLC = 'OHLC'
    LINEBREAK = 'Linebreak'
    RENKO = 'Renko'
    HEIKINASHI = 'HeikinAshi'
    QUANDL_OHLC = 'Quandl OHLC'


def import_with_install(package_import_name, package_install_name=None):
    """
    Helps import 'package'. If its not present, it will be installed using 'pip' and a re-import will be attempted, which should succeed if the package was imported correctly

    :param package_import_name: name of package to be installed using pip, str
    :param package_install_name: name of package to be imported. Default is None, which means package can be imported with the same name as used for installation. If not, this parameter can be used to specify a different import name.
    :return: imported package
    """
    package_install_name = package_install_name if package_install_name is not None else package_import_name
    try:
        return __import__(package_import_name)
    except ImportError:
        print(f"Installing package {package_import_name} via pip...")
        import subprocess
        import sys
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package_install_name])
        return __import__(package_import_name)


def plot_candlestick_chart(data, plot_type, caption='', hide_missing_dates=False, show=True, indicators=None, plot_indicators_separately=False, plot_height=500, plot_width=1000):
    make_subplots = import_with_install('plotly').subplots.make_subplots
    go = import_with_install('plotly').graph_objects

    # Sanity checks
    if not isinstance(plot_type, PlotType):
        print(f'Error: plot_type should be an instance of {PlotType.__class__}')
        return

    # Plot
    if plot_type is PlotType.QUANDL_OHLC:
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
    if (indicators is not None) and (plot_indicators_separately is True):
        fig = make_subplots(rows=3, cols=1, vertical_spacing=0.05, shared_xaxes=True, specs=[[{"rowspan": 2}], [{}], [{}]])
        indicator_subplot_row_index = 3
        indicator_subplot_col_index = 1
    else:
        fig = make_subplots(rows=1, cols=1, vertical_spacing=0.05, shared_xaxes=True)
        indicator_subplot_row_index = 1
        indicator_subplot_col_index = 1

    if plot_type in [PlotType.OHLC, PlotType.HEIKINASHI]:
        fig.append_trace(go.Candlestick(x=timestamps, open=data['open'], high=data['high'], low=data['low'], close=data['close'], name='Historical Data'), row=candlesticks_data_subplot_row_index, col=candlesticks_data_subplot_col_index)
    elif plot_type == PlotType.LINEBREAK:
        fig = go.Figure(data=[go.Candlestick(x=timestamps, open=data['open'], high=data[["open", "close"]].max(axis=1), low=data[["open", "close"]].min(axis=1), close=data['close'], name='Historical Data')], row=candlesticks_data_subplot_row_index,
                        col=candlesticks_data_subplot_col_index)
    elif plot_type == PlotType.RENKO:
        fig = go.Figure(data=[go.Candlestick(x=timestamps, open=data['open'], high=data[["open", "close"]].max(axis=1), low=data[["open", "close"]].min(axis=1), close=data['close'], name='Historical Data')], row=candlesticks_data_subplot_row_index,
                        col=candlesticks_data_subplot_col_index)
    elif plot_type == PlotType.QUANDL_OHLC:
        fig = go.Figure(data=[go.Candlestick(x=timestamps, open=data['Open'], high=data['High'], low=data['Low'], close=data['Close'], name='Historical Data')], row=candlesticks_data_subplot_row_index, col=candlesticks_data_subplot_col_index)
    else:
        print(f'Error: plot_type ({plot_type}) is not implemented yet')
        return

    for indicator in indicators:
        indicator_name = indicator['name']
        indicator_data = indicator['data']
        extra = indicator['extra'] if 'extra' in indicator else {}
        fig.add_trace(go.Scatter(x=timestamps, y=indicator_data, name=indicator_name, **extra), row=indicator_subplot_row_index, col=1)

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
        global counter
        fig.write_image(f'fig_{counter}.pdf')
        counter += 1
