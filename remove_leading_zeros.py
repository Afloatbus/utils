import pandas as pd

def remove_leading_zeros(input_file, output_file, column_name):
    """removes leading zeros from a csv file 

    Args:
        input_file (string): the file to remove zeroes from
        output_file (string): the output file
        column_name (string): the colum to remove the zeroes from
    """
    
    df = pd.read_csv(input_file)
    df[column_name] = df[column_name]astype(str).str.lstrip('0')
    df.to_csv(output_file, index=False)


if __name__ == "__main__":
    input_csv_file = "input_csv_file.csv"
    output_csv_file = "output_csv_file.csv"
    column_to_modify =  "column_to_modify.csv"
    remove_leading_zeros(input_csv_file, output_csv_file, column_to_modify)
