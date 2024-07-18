import pandas as pd

from data_extraction.main import BTCMapExtraction

btcmap = BTCMapExtraction()

elements_dict = btcmap.request_elements()

n_runs = int(elements_dict.__len__() / 1000) + 1

all_elements_df = pd.DataFrame()

for i in range(0, n_runs):
    print(f"Range from {i*1000} to {(i+1)*1000}")
    elements_inter = btcmap.elements_df(elements_dict[i * 1000 : (i + 1) * 1000])

    all_elements_df = pd.concat(
        [all_elements_df, elements_inter], axis=0, ignore_index=True
    )

# all_elements_df

all_elements_df.to_csv("all_elements_df.csv", index=False)

# individual_node = btcmap.request_node(node=11089175599)

# btcmap.individual_df(individual_node)
