import pandas as pd

def infer_and_convert_data_types(df):
    for col in df.columns:
        try:
            numeric_values = pd.to_numeric(df[col], errors='coerce')
            if not numeric_values.isna().all():
                df[col] = numeric_values
                continue
        except ValueError:
            pass
        try:
            datetime_values = pd.to_datetime(df[col], errors='coerce')
            if not datetime_values.isna().all():
                df[col] = datetime_values
                continue
        except ValueError:
            pass
        if df[col].apply(lambda x: isinstance(x, str)).all():
            if len(df[col].unique()) / len(df[col]) < 0.5:
                df[col] = pd.Categorical(df[col])
            else:
                continue
    return df

def read_and_infer_data_types(file, chunksize=10000):
    if file.content_type == 'text/csv':
        reader = pd.read_csv(file, chunksize=chunksize)
    elif file.content_type in ['application/vnd.ms-excel', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet']:
        reader = pd.read_excel(file, chunksize=chunksize)
    else:
        raise ValueError("Unsupported file format. Only CSV and Excel files are supported.")

    # Initialize an empty DataFrame to store the results
    df_list = []

    # Iterate over chunks and infer data types
    for chunk in reader:
        chunk = infer_and_convert_data_types(chunk)
        df_list.append(chunk)

    # Concatenate all chunks into a single DataFrame
    df = pd.concat(df_list)

    return df