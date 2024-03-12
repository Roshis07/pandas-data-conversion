import pandas as pd

def infer_and_convert_data_types(df):
    for col in df.columns:
        # Attempt to convert to numeric
        try:
            numeric_values = pd.to_numeric(df[col], errors='coerce')
            if not numeric_values.isna().all():
                df[col] = numeric_values
                continue
        except ValueError:
            pass
        
        # Attempt to convert to datetime
        try:
            datetime_values = pd.to_datetime(df[col], errors='coerce')
            if not datetime_values.isna().all():
                df[col] = datetime_values
                continue
        except ValueError:
            pass

        # Check for mixed data types
        if df[col].apply(lambda x: isinstance(x, str)).all():
            # If all values are strings, consider converting to categorical
            if len(df[col].unique()) / len(df[col]) < 0.5:
                df[col] = pd.Categorical(df[col])
            else:
                # If not suitable for categorical, leave as object dtype
                continue
        
        # If none of the above conditions are met, leave as object dtype
    return df
   

# The rest of the code remains the same...

def read_and_infer_data_types(file_path, chunksize=10000):
    # Determine file type based on extension
    if file_path.endswith('.csv'):
        reader = pd.read_csv(file_path, chunksize=chunksize)
    elif file_path.endswith('.xlsx') or file_path.endswith('.xls'):
        reader = pd.read_excel(file_path, chunksize=chunksize)
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


# def main():
#     file_path = input("Enter the path to the CSV or Excel file: ")
#     try:
#         df = read_and_infer_data_types(file_path)
#         print("\nData types after inference:")
#         print(df.dtypes)
#     except Exception as e:
#         print("An error occurred:", str(e))


