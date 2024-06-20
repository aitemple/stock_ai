from langchain_core.tools import tool
import akshare as ak
from langchain.pydantic_v1 import BaseModel, Field
import pandas as pd
from langchain_core.tools import BaseTool
import json


class StockHistory(BaseModel):
    symbol: str = Field(..., title="股票代码", description="股票代码")
    period: str = Field(..., title="周期", description="周期")
    start_date: str = Field(..., title="开始日期", description="开始日期(yyyyMMDD)")
    end_date: str = Field(..., title="结束日期", description="结束日期(yyyyMMDD)")


@tool("stock_history", args_schema=StockHistory, return_direct=True)
def stock_history(
    symbol: str, period: str, start_date: str, end_date: str
) -> json:
    """
    获取股票历史数据
    :param symbol: 股票代码
    :param period: 周期
    :param start_date: 开始日期
    :param end_date: 结束日期
    :return: 股票历史数据
    """
    match period:
        case "daily":
            period = "daily"
        case "weekly":
            period = "weekly"
        case "monthly":
            period = "monthly"
        case _:
            period = "daily"

    stock_history_df = ak.stock_zh_a_hist(
        symbol=symbol, period=period, start_date=start_date, end_date=end_date
    ).to_json(orient="records")
    return stock_history_df


class StockSzseSummary(BaseModel):
    date: str = Field(..., title="日期", description="日期(yyyyMMDD)")


@tool("stock_szse_summary", args_schema=StockSzseSummary, return_direct=True)
def stock_szse_summary(
    date: str
) -> json:
    """
    获取深证证券交易所交易概况
    :param date: 日期
    :return: 深证证券交易所交易概况
    """
    stock_szse_summary_df = ak.stock_szse_summary(
        date=date).to_json(orient="records")
    return stock_szse_summary_df


class StockIndividualInfoEm(BaseModel):
    symbol: str = Field(..., title="股票代码", description="股票代码")


@tool("stock_individual_info_em", args_schema=StockIndividualInfoEm, return_direct=True)
def stock_individual_info_em(
    symbol: str
) -> json:
    """
    获取股票个股资金流向
    :param symbol: 股票代码
    :return: 股票个股资金流向
    """
    stock_individual_info_em_df = ak.stock_individual_info_em(
        symbol=symbol).to_json(orient="records")
    return stock_individual_info_em_df


class StockNewsEm(BaseModel):
    symbol: str = Field(..., title="股票代码", description="股票代码")


@tool("stock_news_em", args_schema=StockNewsEm, return_direct=True)
def stock_news_em(
    symbol: str
) -> json:
    """
    获取股票新闻
    :param symbol: 股票代码
    :return: 股票新闻
    """
    stock_news_em_df = ak.stock_news_em(
        symbol=symbol).to_json(orient="records")
    return stock_news_em_df
