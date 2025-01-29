# Personal Fitness Tracker System 🏋️‍♂️

# Lists to store fitness data
workouts = []  # To store workout types and durations
calories = []  # To store calorie intake for meals

# Variables for daily goals
workout_goal = 0  # Daily workout goal in minutes
calorie_goal = 0  # Daily calorie intake goal


def log_workout(workout_type, duration):
    """
    Log a workout.
    - Append the workout type and duration to the workouts list.
    - Print a confirmation message.
    """
    workouts.append((workout_type, duration))
    print(f"Workout logged: {workout_type} for {duration} minutes")

def log_calorie_intake(calories_consumed):
    """
    Log calorie intake for a meal.
    - Append the calorie amount to the calories list.
    - Print a confirmation message.
    """
    calories.append(int(calories_consumed))
    print(f"Calorie intake logged: {calories_consumed} kcal")

def view_progress():
    """
    Display a summary of the user's progress for the day.
    - Calculate the total workout time and total calories.
    - Print motivational feedback.
    """
    total_workout = sum(duration for _, duration in workouts)
    total_calories = sum(calories)
    print("\nDaily Progress: ")
    print(f"Total workout time: {total_workout} minutes")
    print(f"Total calorie intake: {total_calories} kcal")
    encouragement_system(total_calories, total_workout)

def reset_progress():
    """
    Clear all data from the workouts and calories lists.
    - Print a confirmation message.
    """
    workouts.clear()
    calories.clear()
    print("\nProgress has been reset!")

def set_daily_goals(workout_minutes, calorie_limit):
    """
    Set daily goals for workout time and calorie intake.
    - Update the global variables workout_goal and calorie_goal.
    - Print a confirmation message.
    """
    global workout_goal, calorie_goal
    workout_goal = workout_minutes
    calorie_goal = calorie_limit
    print(f"Daily goals set at {workout_goal} minutes of workout and {calorie_goal} kcal.")

def encouragement_system(total_calories, total_workout):
    """
    Provide motivational feedback based on progress and goals.
    - Compare current totals to the daily goals.
    - Print encouragement messages.
    """
    print("\nMotivational Feedback:")
    if total_workout >= workout_goal:
        print("Great job on meeting your workout goal! Keep pushing!")
    else:
        print("You're getting there! Keep moving to reach your workout goal.")

    if total_calories <= calorie_goal:
        print("Well done on staying within your calorie goal!")
    else:
        print("Watch your calorie intake! Try to balance it with exercise.")


def main():
    """
    Main function to interact with the user.
    """
    print("Welcome to the Personal Fitness Tracker System 🏋️‍♂️\n")

    while True:
        # Display menu options
        print("1. Log Workout")
        print("2. Log Calorie Intake")
        print("3. View Progress")
        print("4. Reset Progress")
        print("5. Set Daily Goals")
        print("6. Exit")

        # Prompt user for their choice
        choice = input("\nEnter your choice: ")

        if choice == '1':
            # Prompt for workout type and duration
            workout_type = input("Enter workout type: ")
            duration = input("Enter duration in minutes: ")
            log_workout(workout_type, duration)

        elif choice == '2':
            # Prompt for calories consumed
            calories_consumed = input("Enter calories consumed in kcal: ")
            log_calorie_intake(calories_consumed)

        elif choice == '3':
            # Call view_progress function
            view_progress()

        elif choice == '4':
            # Call reset_progress function
            reset_progress()

        elif choice == '5':
            # Prompt for daily goals
            workout_minutes = int(input("Enter your daily workout goal in minutes: "))
            calorie_limit = int(input("Enter your daily calorie intake limit in kcal: "))
            set_daily_goals(workout_minutes, calorie_limit)

        elif choice == '6':
            # Print a goodbye message and break the loop
            print("Thank you for using the Fitness Tracker. Stay healthy! 💪")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()