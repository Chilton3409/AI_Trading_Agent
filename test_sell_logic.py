#!/usr/bin/env python3
#New file created
from alpaca.trading import TradingClient
import alpacabot
from dotenv import load_dotenv
import asyncio
import os
load_dotenv()
import time
import datetime
import asyncio
import logging
from decimal import Decimal
import ast
import re
from ai_trading_system import AITradingSystem
async def main():
    ai_trading_system = AITradingSystem()
    account = await ai_trading_system.get_account()
    
    await ai_trading_system.sell_logic()
    

    
    
        
    
if __name__ == '__main__':
    asyncio.run(main())