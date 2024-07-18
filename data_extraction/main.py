import json

import pandas as pd
import requests


class BTCMapExtraction:

    def __init__(self):
        self.node_base_url = "https://api.btcmap.org/v2/elements/node:"
        self.elements_base_url = "https://static.btcmap.org/api/v2/elements.json"

    def request_node(self, node):
        node_req = requests.get(f"{self.node_base_url}{node}")

        if node_req.status_code == 200:
            node_dict = json.loads(node_req.content.decode())
        else:
            raise RuntimeError

        return node_dict

    def request_elements(self):

        elements_req = requests.get(self.elements_base_url)

        if elements_req.status_code == 200:
            elements_dict = json.loads(elements_req.content.decode())
        else:
            raise RuntimeError

        return elements_dict

    def individual_df(self, node_dict):

        individual_keys = {
            "type": node_dict.get("osm_json").get("type"),
            "id": node_dict.get("osm_json").get("id"),
            "lat": node_dict.get("osm_json").get("lat"),
            "lon": node_dict.get("osm_json").get("lon"),
            "user": node_dict.get("osm_json").get("user"),
            "created_at": node_dict.get("created_at"),
            "updated_at": node_dict.get("updated_at"),
            "deleted_at": node_dict.get("deleted_at"),
        }

        keys_df = pd.DataFrame.from_dict([individual_keys], orient="columns")

        osm_json_tags = node_dict.get("osm_json").get("tags")

        if osm_json_tags is not None:

            tags_df = pd.DataFrame.from_dict([osm_json_tags], orient="columns")

            tags_df.columns = "tags_" + tags_df.columns
        else:
            tags_df = pd.DataFrame()

        ret_df = pd.concat([keys_df, tags_df], axis=1)

        ret_df.dropna(axis=1, inplace=True)

        return ret_df

    def elements_df(self, list_elements):

        list_dfs = [self.individual_df(x) for x in list_elements]

        ret_df = pd.concat(list_dfs, axis=0, ignore_index=True)

        return ret_df
