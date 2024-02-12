def run_user_code():
    user_code = input("Enter your Python code: ")
    try:
        exec(user_code)
    except Exception as e:
        print(f"Error executing the code: {e}")

# Example usage
run_user_code()