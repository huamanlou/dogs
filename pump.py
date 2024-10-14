
# from pandas import json_normalize
import pandas as pd

from utils import get_data

def get_hot_list():
    # mint权限丢弃，非黑名单, top10持仓<30%
    # 持仓人数>
    min_holder_count = 300
    # 市值>
    min_marketcap = 40000

    data = get_data(f'https://gmgn.ai/defi/quotation/v1/rank/sol/swaps/1h?orderby=swaps&direction=desc&filters[]=renounced&filters[]=frozen&filters[]=distribed&min_marketcap={min_marketcap}&min_holder_count={min_holder_count}')
    # 将 JSON 字符串转换为 Python 对象
    
    # 转换为 DataFrame
    df = pd.DataFrame(data['rank'])
    # print(df['buys'])
    # 小时买单最少数量
    buys = 1000
    df = df.loc[(df['buys']>df['sells']) & (df['buys']>500)]
    # print(df)
    res_list = []
    for index, item in df.iterrows():
        print(item['address'])
        data = get_data(f'https://gmgn.ai/defi/quotation/v1/tokens/top_holders/sol/{item["address"]}?limit=20&cost=20&tag=All&orderby=amount_percentage&direction=desc')
        print(data)

        item_df = pd.DataFrame(data)
        top_df = item_df.head(50)
        # 野钱包数量超过多少个淘汰
        netflow_df = top_df.loc[top_df['netflow_usd']<10]
        if len(netflow_df) > 5:
            continue

        # 获利地址小于多少个淘汰
        profit_df = top_df.loc[top_df['profit']>0]
        print('llll', len(profit_df))
        if len(profit_df) < 25:
            continue

        # 获利并且资金流出>50% 不超过数目
        flow_out_num = 0
        for i, row in profit_df.iterrows():
            if (-row['netflow_usd'])/row['profit'] >0.5:
                flow_out_num = flow_out_num+1
                if flow_out_num>=5:
                    break
        
        if flow_out_num >=5:
            continue 

        res_list.append(item)

    res_df = pd.DataFrame(res_list)

    print(res_df['address'])
        


get_hot_list()



