from perfect import flow,task
import pandas as pd

@task
def extract_csv(file_path: str) -> pd.DataFrame:
    return pd.read_csv(file_path)

@task
def transform_to_json(df: pd.DataFrame) -> str:
    return df.to_json(orient='records', indent=2)

@task
def save_json(json_data: str, output_path: str):
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(json_data)

@flow
def simple_pipeline(csv_path: str, json_path: str):
    df = extract_csv(file_path=csv_path)
    json_data = transform_to_json(df)
    save_json(json_data, output_path=json_path)

# Example usage:
# simple_pipeline('input.csv', 'output.json')
