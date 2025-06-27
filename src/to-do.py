to_do = []
def load_task():
	try:
		with open("tasks.txt","r") as file:
			for line in file:
				to_do.append(line.strip())
	except FileNotFoundError:
		pass
def save_task():
	with open("tasks.txt","w") as file:
		for tasks in to_do:
			file.write(tasks + "\n")
def add_task():
	tasks = input("\n What you wanna do?:").upper()
	if tasks:
		to_do.append(tasks)
		save_task()
		print("Task added! \n")
	else:
		print("\n It can't be empty \n")
def tasks():
	if not to_do:
		print("\nNothing to see here.\n")
	else:
		print("///TASKS\\\\")
		i = 1
		for task in to_do:
			print(f"{i}. {task}")
			i += 1
		print()
def task_done():
			if not to_do:
				print("there's nothing to remove.")
				print()
			else:
				tasks()
				a = int(input("Wut u wanna remove?:"))
				del to_do[a-1]
				save_task()
				print("Task removed!")
				

def wuttodo():
	lst = print("===Options=== \n"
	"1- Add a task \n"
	"2- View To-Do list \n"
	"3- Remove Tasks \n"
	"0- Quit \n")
	inpt = input("\n Enter:")
	if inpt == "1":
		add_task()
		wuttodo()
	elif inpt == "2":
		tasks()
		wuttodo()
	elif inpt == "3":
		task_done()
		wuttodo()
	elif inpt == "0":
		print("Bayes!")
		pass
	else:
		print("\n Enter a valid value retard! \n")
		wuttodo()
load_task()
wuttodo()
