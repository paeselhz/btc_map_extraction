from data_extraction.main import BTCMapExtraction

btcmap = BTCMapExtraction()

elements_dict = btcmap.request_elements()

elements_dict.__len__()

all_elements_df = btcmap.elements_df(elements_dict)
all_elements_df

all_elements_df.to_csv('all_elements_df.csv', index=False)

# individual_node = btcmap.request_node(node=11089175599)

# btcmap.individual_df(individual_node)
