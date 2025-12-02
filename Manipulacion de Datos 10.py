import pandas as pd

df_members = pd.read_csv('/datasets/new_members.csv')
df_orders = pd.read_csv('/datasets/recent_orders.csv')

df_merged = df_members.merge(df_orders,
                             left_on='id',
                             right_on='user_id',
                             suffixes=('_member', '_order'))

# elimina la columna user_id
df_merged = df_merged.drop('user_id', axis='columns')


print(df_merged)

# resultado :
#   id_member      username  ...    service_id      order_timestamp
# 0       9836  watermelon89  ...  XMD8nVShpINn  2021-06-22Z18:32:59
# 1       9836  watermelon89  ...  PXAQ9MiP7BvW  2021-06-22Z18:32:59
# 2       9837       SUPERXD  ...  R2GA1xIVXK1o  2021-06-22Z18:39:12
# 3       9839    NotHotDog2  ...  NvwWjzW7FydE  2021-06-22Z18:36:21
# 4       9840      starrats  ...  9KyrlovWf2nH  2021-06-22Z18:34:00
# 5       9841     beat1box2  ...  fCobsButtJD7  2021-06-22Z18:36:55

# [6 rows x 6 columns]

# guia : Llama a drop() en df_merged e incluye axis='columns' para eliminar la columna 'user_id'. Vuelve a asignar el resultado a df_merged.
