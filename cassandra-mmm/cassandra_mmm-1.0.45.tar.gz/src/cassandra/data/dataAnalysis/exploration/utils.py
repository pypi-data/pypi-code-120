from cassandra.data.dataAnalysis.correlation import *
from cassandra.data.dataAnalysis.plot import *
import pandas as pd


# Example how create a dict_columns_aggregate dict_columns_aggregate = { 'keywords_impressions' : [
# 'adopta_albero_impressions', 'regalar_arbol_impressions', 'regala_arbol_impressions', 'plantar_arbol_impressions',
# 'treedom_impressions'] }
def create_df(df, dict_columns_aggregate={}):
    for key, value in dict_columns_aggregate.items():
        # Aggregate columns into one for each key
        df[key] = df[value].sum(axis=1)

        # Drop un-used columns
        df.drop(value, axis=1, inplace=True)
        df.fillna(value=0)

    return df


def define_features(df, media_split=True):
    media = [col for col in df.columns if '_spend' in col]

    organic = [col for col in df.columns if '_org' in col]

    seasonality = []
    if 'trend' in df.columns:
        seasonality.append('trend')
    if 'holidays' in df.columns:
        seasonality.append('holidays')
    if 'yearly' in df.columns:
        seasonality.append('yearly')
    if 'monthly' in df.columns:
        seasonality.append('monthly')
    if 'weekly' in df.columns:
        seasonality.append('weekly')
    if 'daily' in df.columns:
        seasonality.append('daily')

    price = [col for col in df.columns if 'avg' in col]

    media_google = [col for col in media if col.startswith('g_')]

    media_fb = [col for col in media if col.startswith('fb_')]

    #media_am = [col for col in media if col.startswith('am_')]

    media_others = [col for col in media if not col.startswith('g_') if not col.startswith('fb_')]

    everything = media + organic + price + seasonality
    no_price = media + organic + seasonality
    no_seasonality = media + organic + seasonality
    no_organic = media + price + seasonality
    no_media = organic + price + seasonality

    if media_split:
        return everything, media, organic, price, seasonality, no_media, no_organic, no_price, no_seasonality, media_google, media_fb, media_others
    else:
        return everything, media, organic, price, seasonality, no_media, no_organic, no_price, no_seasonality


def show_media(df, name_date_column, name_target_column, media, media_google=[], media_fb=[], media_others=[]):
    if media_google:
        #Google media graph
        display(Markdown(f"# Google media"))
        display(Markdown(f"### Google media over time"))
        fig_media_google = px.line(df, x=name_date_column, y=media_google)
        fig_media_google.show()
        display(Markdown(f"### Google media trendline"))
        show_trendline_curves(media_google, df, name_target_column)

    if media_fb:
        #Facebook media graph
        display(Markdown(f"# Facebook media"))
        display(Markdown(f"### Facebook media over time"))
        fig_media_fb = px.line(df, x=name_date_column, y=media_fb)
        fig_media_fb.show()
        display(Markdown(f"### Facebook media trendline"))
        show_trendline_curves(media_fb, df, name_target_column)

    if media_others:
        #Others media graph
        display(Markdown(f"# Others media"))
        display(Markdown(f"### Others media over time"))
        fig_media_others = px.line(df, x=name_date_column, y=media_others)
        fig_media_others.show()
        display(Markdown(f"### Others media trendline"))
        show_trendline_curves(media_others, df, name_target_column)


    #Target vs media
    display(Markdown(f"# Time serie: media and {name_target_column}"))
    show_target_vs_media_spent_graph(df, name_date_column, name_target_column, media)


def show_no_media(df, name_date_column, name_target_column, organic=[], price=[], seasonality=[]):
    if organic:
        # Organic graph
        display(Markdown(f"# Organic"))
        display(Markdown(f"### Organic over time"))
        fig_organic = px.line(df, x=name_date_column, y=organic)
        fig_organic.show()
        display(Markdown(f"### Organic trendline"))
        show_trendline_curves(organic, df, name_target_column)
        # Target vs organic
        display(Markdown(f"# Time serie: organic and {name_target_column}"))
        show_target_vs_media_spent_graph(df, name_date_column, name_target_column, organic)

    if price:
        # Organic graph
        display(Markdown(f"# Price"))
        display(Markdown(f"### Price over time"))
        fig_price = px.line(df, x=name_date_column, y=price)
        fig_price.show()
        display(Markdown(f"### Price trendline"))
        show_trendline_curves(price, df, name_target_column)
        # Target vs price
        display(Markdown(f"# Time serie: price and {name_target_column}"))
        show_target_vs_media_spent_graph(df, name_date_column, name_target_column, price)

    if seasonality:
        # Seasonality graph
        display(Markdown(f"# Seasonality"))
        display(Markdown(f"### Seasonality over time"))
        fig_seasonality = px.line(df, x=name_date_column, y=seasonality)
        fig_seasonality.show()
        display(Markdown(f"### Seasonality trendline"))
        show_trendline_curves(seasonality, df, name_target_column)
        # Target vs seasonality
        display(Markdown(f"# Time serie: seasonality and {name_target_column}"))
        show_target_vs_media_spent_graph(df, name_date_column, name_target_column, seasonality)


