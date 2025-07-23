import tkinter as tk
import webbrowser


def run_command(event=None):
    command = entry.get().strip().lower()

    result = "My Terminal"

    # Define custom command logic
    if command == "clear":
        output_text.delete(1.0, tk.END)
        entry.delete(0, tk.END)
        return

    elif command == "--help":
        result = (
            "Hello, Welcome to my own terminal.\n"
            ">> Available Commands:\n"
            "--> info → For my information\n"
            "--> disc → my discription\n"
            "--> down_resume → Download Resume\n"
            "--> clear → Clear the screen\n"
            "--> experience → Work Experience\n"
            "--> hobbies → Show my Hobbies\n"
            "--> certificate → Show my certificates\n"
            "--> education → Show my Education\n"
            "--> skill → Show my skill\n"
            "--> contect → Show my Contects\n"
            "--> social_med → Show my Social media account\n"
            "--> --help → Show this help message\n"
            
        )

    elif command == "info":
        result = "- My name is Mohd Arif 😊\n- D.O.B : 17/03/2002\n- Address : Kanpur\n- Marital status : ummarried\n"

    elif command == "disc":
        result = "- Detail-oriented and analytical professional transitioning from customer service to data science. Equipped with hands-on experience in Python, Pandas, SQL, and machine learning. Adept at translating business needs into data-driven solutions with strong communication and stakeholder collaboration skills for previous clientfacing experience."

    elif command == "down_resume":
        result = "- uploading soon....................\n"
    
    elif command == "experience":
        result = "- 1. Linear Regration => lr\n"
    
    elif command == "lr":
        webbrowser.open("https://github.com/mohdarif1234/Learning-Linear-Regression-My-First-Machine-Learning-Project/blob/main/shoes_linearRegration.ipynb")
        result = "- Opening https://github.com...\n"

    elif command == "hobbies":
        result = (
            "- Travling\n- Cooking\n"
        )

    elif command == "certificate":
        result = (
            "- APNA COLLEGE : JAVA with DSA\n"
        )

    elif command == "education":
        result = (
            ">> Class 12th\n"
            "  - Aligarh Muslim University\n"
            "  - 1st Division\n"
            ">> Bachelor of Technology in Computer Science\n"
            "  - Khwaja moin uddin chisti language university\n"
            "  - CGPS : 8.25\n"
        )

    elif command == "skill":
        result = (
            "- languages : Python, SQL, HTML, CSS, JavaScript\n"
            "- Libraries : Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, Streamlit, Tkinter(basic)\n"
            "- Tools : VS Code Editor, Jupyter Notebook, git\n"
            "- Soft Skill : Communication, Problem Solving, TeamWork, Client Interaction\n"
            "- Ubuntu : (basic for interacting with Git), Windows\n"
        )

    elif command == "contect":
        result = (
            "-Mob No: +91 8573991870\n"
            "-Email Id: mohammadarif5761@gmail.com"
        )
    
    elif command == "social_med":
        result = (
            "-github : Command -> github\n"
            "-Linkdin: Command -> linkdin\n"
        )

    elif command == "github":
        webbrowser.open("https://github.com/mohdarif1234")
        result = "- Opening https://github.com...\n"
            
    elif command == "linkdin":
        webbrowser.open("https://www.linkedin.com/in/arifmohd5761/")
        result = "- Opening https://linkdin.com...\n"


    elif command == "lang":
        result = (
            "- Hindi\n"
            "- English\n"
            "- Urdu\n"
        )

    else:
        result = f"Unknown command: {command}\nType --help to see available commands."

    # Show output
    output_text.insert(tk.END, f"> {command}\n{result}\n\n")
    entry.delete(0, tk.END)

# GUI setup
root = tk.Tk()
root.title("Custom Terminal")
root.geometry("1500x900")
root.configure(bg="black")

header = tk.Label(root, text="Welcome to Arif's Terminal  ||  Type --help for commands",
                  bg="black", fg="yellow", font=("Consolas", 18))
header.pack(fill=tk.X)

output_text = tk.Text(root, bg="black", fg="red", insertbackground="green", font=("Consolas", 20))
output_text.pack(expand=True, fill=tk.BOTH)

header = tk.Label(root, text="↓ write commands ↓",
                  bg="black", fg="blue", font=("Consolas", 22))
header.pack(fill=tk.X)

entry = tk.Entry(root, bg="black", fg="white", insertbackground="white", font=("Consolas", 20))
entry.pack(fill=tk.X)
entry.bind("<Return>", run_command)
entry.focus()

root.mainloop()
