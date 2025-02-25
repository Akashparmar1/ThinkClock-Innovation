import pandas as pd
import networkx as nx

def load_and_preprocess_data(file_path):
    df = pd.read_csv(file_path)
    df['email'] = df['email'].str.lower().str.strip()
    df['phone'] = df['phone'].astype(str).str.replace(r'\D', '', regex=True)
    df.fillna("", inplace=True)
    return df

def find_clusters(df):
    G = nx.Graph()
    for _, row in df.iterrows():
        G.add_node(row['id'], name=row['name'])
    for _, row in df.iterrows():
        for _, other_row in df.iterrows():
            if row['id'] != other_row['id']:
                if row['email'] == other_row['email'] or row['phone'] == other_row['phone']:
                    G.add_edge(row['id'], other_row['id'])
    return list(nx.connected_components(G))

def assign_unique_ids(clusters):
    customer_mapping = {}
    for cluster in clusters:
        main_id = min(cluster)
        for customer_id in cluster:
            customer_mapping[customer_id] = main_id
    return customer_mapping

def save_results(df, customer_mapping, output_file):
    df['unique_id'] = df['id'].map(customer_mapping)
    df.to_csv(output_file, index=False)
    print(f"Results saved to {output_file}")

# Run the full pipeline
if __name__ == "__main__":
    df = load_and_preprocess_data("customers.csv")
    clusters = find_clusters(df)
    customer_mapping = assign_unique_ids(clusters)
    save_results(df, customer_mapping, "resolved_customers.csv")
