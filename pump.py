
# from pandas import json_normalize
import pandas as pd
from decimal import Decimal, getcontext
from utils import get_data

# 设置精度
getcontext().prec = 20



def get_hot_list():
    # mint权限丢弃，非黑名单, top10持仓<30%
    # 持仓人数>
    min_holder_count = 300
    # 市值>
    min_marketcap = 80000

    data = get_data(f'https://gmgn.ai/defi/quotation/v1/rank/sol/swaps/1h?orderby=swaps&direction=desc&filters[]=renounced&filters[]=frozen&filters[]=distribed&min_marketcap={min_marketcap}&min_holder_count={min_holder_count}')
    # 将 JSON 字符串转换为 Python 对象
    
    # 转换为 DataFrame
    df = pd.DataFrame(data['rank'])
    # 小时买单最少数量
    buys = 1000
    df = df.loc[(df['buys']>df['sells']) & (df['buys']>buys)]
    # 小时买单>卖单15倍
    # print(df)
    res_list = []
    for index, item in df.iterrows():
        print(item['address'])
        data = get_data(f'https://gmgn.ai/defi/quotation/v1/tokens/top_holders/sol/{item["address"]}?limit=20&cost=20&tag=All&orderby=amount_percentage&direction=desc')
        # print(data)

        item_df = pd.DataFrame(data)
        top_df = item_df.head(50)
        # 获利地址小于多少个淘汰
        profit_df = top_df.loc[top_df['profit']>0]
        if len(profit_df) < 25:
            print('获利地址太少')
            continue

        # 接受外部转账钱包数量超过多少个淘汰
        bad_wallet_num = 0
        # 获利并且资金流出>50% 不超过数目
        flow_out_num = 0
        for i, row in top_df.iterrows():
            # 假如净资产大于(流入资产+总利润）*2
            if (Decimal(row['usd_value']) > (Decimal(row['netflow_usd']) + Decimal(row['profit'])) *2):
                bad_wallet_num = bad_wallet_num + 1
                if bad_wallet_num > 5:
                    print('庄家子账户太多')
                    break

            # 获利账户，并且资金流出超过50%
            if (-row['netflow_usd'])/row['profit'] > 0.5:
                flow_out_num = flow_out_num+1
                if flow_out_num > 5:
                    print('获利资金流出太多')
                    break

        if bad_wallet_num >5:
            continue 
        if flow_out_num >5:
            continue 

        res_list.append(item)

    res_df = pd.DataFrame(res_list)

    print(res_df['address'])
        


get_hot_list()



