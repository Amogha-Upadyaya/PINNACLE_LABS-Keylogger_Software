def write_to_version2_log(file_path, content):
    try:
        with open(file_path, 'a') as f:
            f.write(content)
    except Exception as e:
        print(f"Error writing to log file: {e}")
