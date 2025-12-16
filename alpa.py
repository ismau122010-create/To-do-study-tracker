import json
from pathlib import Path

file = Path("data2.json")

def load_data():
    if file.exists():
        data= json.loads(file.read_text(encoding="utf-8"))
            # Ensure required keys exist
        data.setdefault("task", [])
        data.setdefault("subject", [])
        return data
    return {"task": [],
            "subject": []
    }

def save_data(data):
    file.write_text(json.dumps(data, indent=2), encoding="utf-8")

# Load file
data = load_data()
To_Do_data = data["task"]
study_session_data = data["subject"]



     
def add():
    user_task = input("add task: ").strip()
    user_status = input("type status (done/not yet): ").strip().lower()

    # STRICT string validation (letters only)
    if not user_task.isalpha():
        raise ValueError("Error: task must contain letters only (no numbers, spaces, or symbols)")

    if user_status not in ("done", "not yet"):
        raise ValueError("Error: status must be 'done' or 'not yet'")

    # Update existing task
    for item in To_Do_data:
        if item["task"].lower() == user_task.lower():
            item["status"] = user_status
            save_data(data)
            return To_Do_data

    # Add new task
    To_Do_data.append({"task": user_task.lower(), "status": user_status})
    save_data(data)
    return To_Do_data


def delete(): # create the delete function
     user = input("Enter delete all or delete task: ").lower().strip()
   
     if user == "delete all":   # this will delte evertyhing in the data list
        To_Do_data.clear()
        study_session_data.clear()   
        save_data(data)
     elif user == "delete task":       # this will delete only specific task choosen by the user. 
        user_delete_task = input("Enter task to be deleleted: ").lower().strip()
        To_Do_data[:] = [
     item for item in To_Do_data
     if item["task"].lower() != user_delete_task
]       
        save_data(data)
     return To_Do_data 


def view():
     return To_Do_data                # this will view everything in the data list. 
 
    

def mark_task():
    user_mark_input = input("type task: ").strip().lower()
    user_mark_input2 = input("type done/not yet: ").strip().lower()

    # validate status FIRST
    if user_mark_input2 not in ("done", "not yet"):
        raise ValueError("Error: status must be 'done' or 'not yet'")

    for item in To_Do_data:
        if item["task"].lower() == user_mark_input:       # if the same input entered, update the task status with                                             
            item["status"] = user_mark_input2                 # new user input
            save_data(data)
            return To_Do_data

    print("task not found")
    return To_Do_data

def study_session():
    user_subject = input("Enter subject: ").strip()
    user_subject_duration = int(input("Enter duration: ").strip())

    # Validate subject (letters only)
    if not user_subject.isalpha():
        raise ValueError("Error: subject must contain letters only (no numbers, spaces, or symbols)")

    # If subject exists → update duration
    for session in study_session_data:
        if session["subject"].lower() == user_subject.lower():
            session["duration"] += user_subject_duration
            save_data(data)
            return study_session_data   # ✅ STOP — no append

    # If subject not found → add new
    study_session_data.append({
        "subject": user_subject,
        "duration": user_subject_duration
    })

    save_data(data)
    return study_session_data



def study_report():
    save_data(data)
    return study_session_data


def quit_program():
   return "End programme"


def final_result():                 
   
  while True:
    user_delta = input(
        "\nChoose add / view / mark task / delete / study session / study report / exit: "
    ).strip().lower()

    try:
        if user_delta == "add":
            print(add())

        elif user_delta == "view":
            print(view())

        elif user_delta == "mark task":
            print(mark_task())

        elif user_delta == "delete":
            print(delete())

        elif user_delta == "study session":
            print(study_session())

        elif user_delta == "study report":
            print(study_report())

        elif user_delta == "exit":
            print("End programme 👋")
            break   # ← EXIT the loop

        else:
            print("Wrong input. Please try again.")

    except ValueError as e:
        print(e)

final_result()