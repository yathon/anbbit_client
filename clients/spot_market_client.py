#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .base_client import AnbbitClient
from .constants import ANBBIT_MARKET_HOST, SPOT_MARKET_PATH_PUB


class AnbbitSpotMarketClient(AnbbitClient):

    def __init__(self, public_url_base=None):
        public_url_base = public_url_base or ANBBIT_MARKET_HOST + SPOT_MARKET_PATH_PUB
        super(AnbbitSpotMarketClient, self).__init__(None, public_url_base, api_key=None, api_secret=None)

    def market_orderbook(self, symbol, limit=None):
        path = f'/depth'
        url = self.public_url_base + path
        params = {
            'symbol': symbol
        }
        if limit:
            params['limit'] = limit
        return self.send_request(url, params=params, method='GET')

    def market_aggregate_trade(self, symbol, limit=None):
        path = f'/aggTrades'
        url = self.public_url_base + path
        params = {
            'symbol': symbol
        }
        if limit:
            params['limit'] = limit
        return self.send_request(url, params=params, method='GET')

    def market_ticker_24hr(self, symbol=None):
        path = f'/ticker/24hr'
        url = self.public_url_base + path
        params = {
        }
        if symbol:
            params['symbol'] = symbol
        return self.send_request(url, params=params, method='GET')

    def market_kline(self, symbol, interval, limit=None, start_tm_ms=None, end_tm_ms=None):
        path = f'/klines'
        url = self.public_url_base + path
        params = {
            'symbol': symbol,
            'interval': interval
        }
        if limit:
            params['limit'] = limit
        if start_tm_ms:
            params['startTime'] = start_tm_ms
        if end_tm_ms:
            params['endTime'] = end_tm_ms
        return self.send_request(url, params=params, method='GET')
