import pandas as pd
import fileinput

df = pd.read_json('tweet_spider_by_user_id_20240306164811.jsonl',lines = True)

count1 = len(df[(df['reposts_count'] == 0) & (df['comments_count'] == 0) & (df['attitudes_count'] == 0)])
print("没有转发、评论和点赞的会话条数：",count1)

"""count2 = len(df[(df['user'].apply(lambda x: x.get('verified', True)) == True) &
               (df['reposts_count'] == 0) &
               (df['comments_count'] == 0) &
               (df['attitudes_count'] == 0)])
print("其中verified为True的数据条数：", count2)

count3 = len(df[(df['user'].apply(lambda x: x.get('verified', True)) == True) &
                (df['reposts_count'] == 0) &
                (df['comments_count'] == 0) &
                (df['attitudes_count'] == 0) &
                (df['pic_urls'].apply(lambda x: len(x)) > 0)])
print("verified为True且没有转发、评论和点赞，且pic_urls列表不为空的数据条数：", count3)

    # 筛选满足条件的数据
filtered_df = df[(df['user'].apply(lambda x: x.get('verified', True)) == True) &
                     (df['reposts_count'] == 0) &
                     (df['comments_count'] == 0) &
                     (df['attitudes_count'] == 0)]"""




    # 提取 mblogid 值
mblogid_values = filtered_df['mblogid'].tolist()

    # 写入新文件
with open('mblogid_list.txt', 'w') as f:
    for mblogid in mblogid_values:
        f.write("%s\n" % mblogid)

print("提取的 mblogid 值已保存到 mblogid_list.txt 文件中。")

