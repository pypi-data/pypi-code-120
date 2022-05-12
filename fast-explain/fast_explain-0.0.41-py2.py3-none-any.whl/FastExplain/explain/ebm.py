from typing import List, Optional, Union

import pandas as pd

from FastExplain.utils import (
    COLOURS,
    bin_columns,
    check_all_numeric,
    clean_dict_text,
    clean_text,
    cycle_colours,
    get_upper_lower_bound_traces,
    ifnone,
    merge_multi_df,
    plot_upper_lower_bound_traces,
    try_convert_numeric,
)


def ebm_explain(
    m: (Union[List[type], type]),
    xs: (Union[List[pd.DataFrame], pd.DataFrame]),
    col: str,
    standardize_values: bool = True,
    dp: int = 2,
    percentage: bool = False,
    condense_last: bool = True,
    index_mapping: Optional[dict] = None,
    model_names: Optional[List[str]] = None,
):
    """
    Calculate EBM values for a predictor feature in a model

    Args:
        m (Union[List[type], type]):
            Trained EBM model that uses feature as a predictor. Can supply a list of models with the same feature and dependent variable to create a cross-comparison
        xs (Union[List[pd.DataFrame], pd.DataFrame]):
            Dataframe used by model to predict. Can supply a list of dataframes with the same features to create a cross-comparison
        col (str):
            Name of predictor feature to use for EBM Explain
        standardize_values (bool, optional):
            Whether to standardize the first bin as 0. Defaults to True.
        dp (int, optional):
            Decimal points to format. Defaults to 2.
        percentage (bool, optional):
            Whether to format bins as percentages. Defaults to False.
        condense_last (bool, optional):
            Whether to bin last value with a greater than. Defaults to True.
        index_mapping (Optional[dict], optional):
            Dictionary mapping the values to display on the x-axis. Defaults to None.
        model_names (Optional[List[str]], optional):
            Name of models to use as columns if supplying multiple models. Defaults to None.
    """

    if isinstance(m, (list, tuple)):
        model_names = ifnone(model_names, [f"Model {i}" for i in range(len(m))])
        ebms = []
        for count, ale_info in enumerate(zip(m, xs)):
            model, x_values = ale_info
            if count == len(m) - 1:
                ebms.append(
                    _clean_ebm_explain(
                        m=model,
                        xs=x_values,
                        col=col,
                        standardize_values=standardize_values,
                        dp=dp,
                        percentage=percentage,
                        condense_last=condense_last,
                        index_mapping=index_mapping,
                    )[["eff", "size"]]
                )
            else:
                ebms.append(
                    _clean_ebm_explain(
                        m=model,
                        xs=x_values,
                        col=col,
                        standardize_values=standardize_values,
                        dp=dp,
                        percentage=percentage,
                        condense_last=condense_last,
                        index_mapping=index_mapping,
                    )[["eff"]]
                )

        output = merge_multi_df(ebms, left_index=True, right_index=True)
        output.columns = model_names + ["size"]
        return output
    else:
        return _clean_ebm_explain(
            m,
            xs,
            col,
            standardize_values=standardize_values,
            dp=dp,
            percentage=percentage,
            condense_last=condense_last,
            index_mapping=index_mapping,
        )


def plot_ebm_explain(
    m: (Union[List[type], type]),
    xs: (Union[List[pd.DataFrame], pd.DataFrame]),
    col: str,
    standardize_values: bool = True,
    dp: int = 2,
    percentage: bool = False,
    condense_last: bool = True,
    index_mapping: Optional[dict] = None,
    model_names: Optional[List[str]] = None,
    dep_name=None,
    feature_name=None,
    plot_title=None,
    plotsize=None,
):

    """
    Plot EBM values for a predictor feature in a model

    Args:
        m (Union[List[type], type]):
            Trained EBM model that uses feature as a predictor. Can supply a list of models with the same feature and dependent variable to create a cross-comparison
        xs (Union[List[pd.DataFrame], pd.DataFrame]):
            Dataframe used by model to predict. Can supply a list of dataframes with the same features to create a cross-comparison
        col (str):
            Name of predictor feature to use for EBM Explain
        standardize_values (bool, optional):
            Whether to standardize the first bin as 0. Defaults to True.
        dp (int, optional):
            Decimal points to format. Defaults to 2.
        percentage (bool, optional):
            Whether to format bins as percentages. Defaults to False.
        condense_last (bool, optional):
            Whether to bin last value with a greater than. Defaults to True.
        index_mapping (Optional[dict], optional):
            Dictionary mapping the values to display on the x-axis. Defaults to None.
        model_names (Optional[List[str]], optional):
            Name of models to use as columns if supplying multiple models. Defaults to None.
        dep_name (Optional[str], optional):
            Custom name to use for dependent variable on plot. Defaults to None.
        feature_names (Optional[str], optional):
            Custom names to use for predictor variable on plot. Defaults to None.
        plot_title (Optional[str], optional):
            Custom name to use for title of plot. Defaults to None.
        plotsize (Optional[List[int]], optional):
            Custom plotsize supplied as (width, height). Defaults to None.
    """

    feature_name = ifnone(feature_name, clean_text(col))

    if isinstance(m, list):
        model_names = (
            model_names if model_names else [f"Model {i}" for i in range(len(m))]
        )
        for count, ale_info in enumerate(zip(m, xs, model_names, cycle_colours())):
            model, x_values, model_name, color = ale_info
            if count == 0:
                traces, x, size = _get_ebm_explain_traces(
                    m=model,
                    xs=x_values,
                    col=col,
                    model_name=model_name,
                    color=color,
                    return_index_size=True,
                    standardize_values=standardize_values,
                    dp=dp,
                    percentage=percentage,
                    condense_last=condense_last,
                    index_mapping=index_mapping,
                )
            else:
                traces.extend(
                    _get_ebm_explain_traces(
                        m=model,
                        xs=x_values,
                        col=col,
                        model_name=model_name,
                        color=color,
                        return_index_size=False,
                        standardize_values=standardize_values,
                        dp=dp,
                        percentage=percentage,
                        condense_last=condense_last,
                        index_mapping=index_mapping,
                    )
                )
    else:
        traces, x, size = _get_ebm_explain_traces(
            m=m,
            xs=xs,
            col=col,
            model_name=feature_name,
            color=COLOURS["blue"],
            return_index_size=True,
            standardize_values=standardize_values,
            dp=dp,
            percentage=percentage,
            condense_last=condense_last,
            index_mapping=index_mapping,
        )

    title = (
        f"EBM {feature_name} vs {clean_text(dep_name)}"
        if dep_name
        else f"EBM {feature_name}"
    )
    plot_title = ifnone(plot_title, title)

    fig = plot_upper_lower_bound_traces(
        traces=traces,
        x=x,
        size=size,
        x_axis_title=feature_name,
        y_axis_title=dep_name,
        plotsize=plotsize,
        plot_title=plot_title,
    )
    return fig


class EbmExplain:
    def __init__(self, m, xs, dep_var=None, cat_mapping=None):
        self.m = m
        self.xs = xs
        self.dep_var = dep_var
        self.cat_mapping = cat_mapping

    def ebm_explain(
        self,
        col: str,
        standardize_values: bool = True,
        dp: int = 2,
        percentage: bool = False,
        condense_last: bool = True,
        index_mapping: Optional[dict] = None,
    ):
        """
        Calculate EBM values for a predictor feature in a model

        Args:
            col (str):
                Name of predictor feature to use for EBM Explain
            standardize_values (bool, optional):
                Whether to standardize the first bin as 0. Defaults to True.
            dp (int, optional):
                Decimal points to format. Defaults to 2.
            percentage (bool, optional):
                Whether to format bins as percentages. Defaults to False.
            condense_last (bool, optional):
                Whether to bin last value with a greater than. Defaults to True.
            index_mapping (Optional[dict], optional):
                Dictionary mapping the values to display on the x-axis. Defaults to None.
        """
        index_mapping = ifnone(
            index_mapping,
            clean_dict_text(self.cat_mapping[col]) if col in self.cat_mapping else None,
        )
        return ebm_explain(
            m=self.m,
            xs=self.xs,
            col=col,
            standardize_values=standardize_values,
            dp=dp,
            percentage=percentage,
            condense_last=condense_last,
            index_mapping=index_mapping,
        )

    def plot_ebm_explain(
        self,
        col: str,
        standardize_values: bool = True,
        dp: int = 2,
        percentage: bool = False,
        condense_last: bool = True,
        index_mapping: Optional[dict] = None,
        dep_name=None,
        feature_name=None,
        plot_title=None,
        plotsize=None,
    ):

        """
        Plot EBM values for a predictor feature in a model

        Args:
            col (str):
                Name of predictor feature to use for EBM Explain
            standardize_values (bool, optional):
                Whether to standardize the first bin as 0. Defaults to True.
            dp (int, optional):
                Decimal points to format. Defaults to 2.
            percentage (bool, optional):
                Whether to format bins as percentages. Defaults to False.
            condense_last (bool, optional):
                Whether to bin last value with a greater than. Defaults to True.
            index_mapping (Optional[dict], optional):
                Dictionary mapping the values to display on the x-axis. Defaults to None.
            dep_name (Optional[str], optional):
                Custom name to use for dependent variable on plot. Defaults to None.
            feature_names (Optional[str], optional):
                Custom names to use for predictor variable on plot. Defaults to None.
            plot_title (Optional[str], optional):
                Custom name to use for title of plot. Defaults to None.
            plotsize (Optional[List[int]], optional):
                Custom plotsize supplied as (width, height). Defaults to None.
        """
        dep_name = ifnone(dep_name, self.dep_var)
        index_mapping = ifnone(
            index_mapping,
            clean_dict_text(self.cat_mapping[col]) if col in self.cat_mapping else None,
        )
        return plot_ebm_explain(
            m=self.m,
            xs=self.xs,
            col=col,
            standardize_values=standardize_values,
            dp=dp,
            percentage=percentage,
            condense_last=condense_last,
            index_mapping=index_mapping,
            dep_name=dep_name,
            feature_name=feature_name,
            plot_title=plot_title,
            plotsize=plotsize,
        )


def _get_ebm_index(m, col):
    """Get index of feature from EBM"""
    ebm_global = m.explain_global()
    col_dict = {i: count for count, i in enumerate(ebm_global.data()["names"])}
    return col_dict[col]


def _clean_ebm_explain(
    m,
    xs,
    col,
    standardize_values=True,
    dp=2,
    percentage=False,
    condense_last=True,
    index_mapping: Optional[dict] = None,
):
    """Base function for cleaning EBM"""
    ebm_global = m.explain_global()
    index = _get_ebm_index(m, col)
    numeric = check_all_numeric(ebm_global.data(index)["names"])
    binned = (
        pd.cut(xs[col], ebm_global.data(index)["names"], include_lowest=True)
        if numeric
        else xs[col]
    )
    binned_count = list(binned.groupby(binned).count())
    df = pd.DataFrame(
        {
            "eff": ebm_global.data(index)["scores"],
            "upper": ebm_global.data(index)["upper_bounds"],
            "lower": ebm_global.data(index)["lower_bounds"],
            "size": binned_count,
        },
        index=bin_columns(
            ebm_global.data(index)["names"],
            dp=dp,
            percentage=percentage,
            condense_last=condense_last,
        )
        if numeric
        else ebm_global.data(index)["names"],
    )
    df = df[~df.index.duplicated(keep="last")]
    if standardize_values:
        adjust = -1 * df.iloc[0]["eff"]
        df["eff"] += adjust
        df["lower"] += adjust
        df["upper"] += adjust
    if index_mapping is not None and numeric is False:
        df.index = try_convert_numeric(df.index)
        df.index = df.index.map(index_mapping)
    return df


def _get_ebm_explain_traces(
    m,
    xs,
    col,
    model_name,
    color,
    return_index_size=True,
    standardize_values: bool = True,
    dp=2,
    percentage=False,
    condense_last=True,
    index_mapping: Optional[dict] = None,
):
    """Base function for plotting EBM"""
    df = ebm_explain(
        m,
        xs,
        col,
        standardize_values=standardize_values,
        dp=dp,
        percentage=percentage,
        condense_last=condense_last,
        index_mapping=index_mapping,
    )
    x = df.index
    y = df["eff"]
    size = df["size"]
    y_lower = df["lower"]
    y_upper = df["upper"]
    return get_upper_lower_bound_traces(
        x=x,
        y=y,
        y_lower=y_lower,
        y_upper=y_upper,
        size=size,
        color=color,
        line_name=model_name,
        return_index_size=return_index_size,
    )
