import pytest
import tkinter as tk
from unittest.mock import patch
from ACEest_Fitness import FitnessTrackerApp  # ✅ Match your actual file name (no .py)

@pytest.fixture
def app_instance():
    root = tk.Tk()
    root.withdraw()  # Hide the GUI during tests
    app = FitnessTrackerApp(root)
    return app

def test_add_valid_workout(app_instance):
    # Simulate user input
    app_instance.workout_entry.insert(0, "Squats")
    app_instance.duration_entry.insert(0, "45")

    with patch("tkinter.messagebox.showinfo") as mock_info:
        app_instance.add_workout()

        assert len(app_instance.workouts) == 1
        assert app_instance.workouts[0]["workout"] == "Squats"
        assert app_instance.workouts[0]["duration"] == 45
        mock_info.assert_called_once_with("Success", "'Squats' added successfully!")

def test_add_empty_workout(app_instance):
    with patch("tkinter.messagebox.showerror") as mock_error:
        app_instance.add_workout()

        assert len(app_instance.workouts) == 0
        mock_error.assert_called_once_with("Error", "Please enter both workout and duration.")

def test_add_invalid_duration(app_instance):
    app_instance.workout_entry.insert(0, "Pushups")
    app_instance.duration_entry.insert(0, "abc")

    with patch("tkinter.messagebox.showerror") as mock_error:
        app_instance.add_workout()

        assert len(app_instance.workouts) == 0
        mock_error.assert_called_once_with("Error", "Duration must be a number.")
