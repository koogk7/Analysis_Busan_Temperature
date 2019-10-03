import pandas as pd
import matplotlib.pyplot as plt

def preprocessing(data_name, mode='mean', groupby='day'):

    drop_result = None
    # skiprows를 통해 필요없는 row skip 가능
    dataframe = pd.read_csv(data_name, names=['day', 'hour', 'value'], skiprows=[0])
    # DataFrame은 groupby 함수를 통해 원하는 컬럼의 값들로 분류할 수 있다.
    data_groupby = dataframe.groupby(groupby)

    # 데이터 삭제
    # DataFrame.drop(labels=None, axis=0, index=None, columns=None, level=None, inplace=False, erros='raise')
    # axis 값에 따라서 특정 칼럼 또는 특정 행을 드롭,  0을 지정할 경우 lables에 오는 값을 인덱스로 간주, 1일 경우 칼럼명을 의미
    # inplace가 False이면 자기 자신의 DataFrame의 데이터는 삭제하지 않고, 삭제된 결과 DataFrame을 반환
    if mode == 'mean':
        drop_result = data_groupby.mean().drop(['hour'], axis=1, inplace=False)
    if mode == 'max':
        drop_result = data_groupby.max().drop(['hour'], axis=1, inplace=False)
    if mode == 'min':
        drop_result = data_groupby.min().drop(['hour'], axis=1, inplace=False)


    # groupby로 준 key값은 인덱스가 된다. 이 인덱스를 다시 컬럼으로 보내주기 위해서는 reset_index함수를 사용한다.
    return drop_result.reset_index(level=groupby, inplace=False)


fourteen_data = preprocessing('data/201408_month.csv', mode='max')
nineteen_data = preprocessing('data/201908_month.csv', mode='max')

# plt.plot([1, 2, 3, 4], [1, 4, 9, 16],  color='green', marker='o',\
#          linestyle='dashed',  linewidth=2, markersize=12,  alpha=.5)
plt.xlabel('Days')
plt.ylabel('Temperature')
plt.title("Max Temperature")



# plt.plot(ten_data['day'], ten_data['value'], alpha=0.3, c='blue', marker='o', label='2010')
plt.plot(fourteen_data['day'], fourteen_data['value'], alpha=0.3, c='blue', marker='o', label='2014')
plt.plot(nineteen_data['day'], nineteen_data['value'], alpha=0.3, c='red', marker='o', label='2019')
plt.bar(fourteen_data['day'], fourteen_data['value'], label='2014', alpha=0.4, color='b')
plt.bar(nineteen_data['day'], nineteen_data['value'], label='2019', alpha=0.4, color='red')
plt.legend()
plt.show()