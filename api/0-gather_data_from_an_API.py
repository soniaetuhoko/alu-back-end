#!/usr/bin/python3
"""
Script to fetch and display an employee's TODO list progress using the intranet API.
"""

import requests
import sys

def get_employee_todo_progress(employee_id):
    """
    Fetches and displays the TODO list progress for a given employee ID.
    """
    # Base URL for the intranet API (replace with the actual base URL)
    base_url = "https://intranet.example.com"

    # Fetch employee details
    user_url = f"{base_url}/users/{employee_id}"
    response = requests.get(user_url)
    if response.status_code != 200:
        print(f"Error: Unable to fetch employee details for ID {employee_id}.")
        return
    employee_name = response.json().get("name")  # Ensure this is the correct key

    # Fetch employee TODO list
    todos_url = f"{base_url}/users/{employee_id}/todos"
    response = requests.get(todos_url)
    if response.status_code != 200:
        print(f"Error: Unable to fetch TODO list for employee ID {employee_id}.")
        return
    todos = response.json()

    # Filter completed tasks
    completed_tasks = [todo for todo in todos if todo.get("completed")]
    total_tasks = len(todos)
    num_completed_tasks = len(completed_tasks)

    # Display the output
    print(f"Employee {employee_name} is done with tasks({num_completed_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task.get('title')}")  # 1 tab and 1 space before the title

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Error: Employee ID must be an integer.")
