import QUANTAXIS as QA
# from QAStrategy.qastockbase_ext import QAStrategyStockBaseExt



class strategy2(QAStrategyStockBaseExt):
    def on_bar(self, data):
        # print(data)
        # print(self.get_positions('000001'))
        # print(self.market_data)
        
        code = data.name[1]
        # print('---------------under is 当前全市场的market_data --------------')
        
        # print(self.get_current_marketdata())
        # print('---------------under is 当前品种的market_data --------------')
        # print(self.get_code_marketdata(code))
        # print("step...")
        print(code)
        #print(self.running_time)
        # input()

if __name__ == '__main__':
    s = strategy2(code=['000001', '000002'], frequence='day', start='2019-01-01', end='2019-02-01', strategy_id='x')
    s.run_sim()
#     s.run_backtest()