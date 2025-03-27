import tkinter as tk
from tkinter import ttk, messagebox
import random
from gtts import gTTS
import pygame
import os

pygame.mixer.init()

scenarios = {
    "pyramid construction": {
        "years": range(-2630, -2600),
        "locations": ["Giza Plateau", "Saqqara", "The Nile Banks"],
        "weather": ["humid hot summer", "dusty dry afternoon", "scorching midday sun"],
        "activities": [
            "huge blocks of limestone being dragged by ropes",
            "workers chanting rhythmic work songs",
            "overseers shouting commands in ancient tongues",
            "sledges grinding against the sand",
            "a sudden dust storm sweeping the site"
        ],
        "historical_figures": ["Imhotep", "Pharaoh Khufu", "High Priest Hemiunu"],
        "details": [
            "a cracked water jug spills onto the sand",
            "a child runs with a basket of bread for the workers",
            "vultures circle overhead in the shimmering heat",
            "a distant roar of the Nile’s flooding waters"
        ]
    },
    "david and goliath": {
        "years": range(-1020, -1000),
        "locations": ["Valley of Elah", "Philistine Camp", "Israelite Ridge"],
        "weather": ["clear morning haze", "dusty afternoon wind", "cool evening shadows"],
        "activities": [
            "Goliath bellows a challenge across the valley",
            "Israelite soldiers murmur in fear behind their lines",
            "David selects smooth stones from the brook",
            "the sling whirs as David steps forward",
            "Philistines roar as their champion falls"
        ],
        "historical_figures": ["David", "Goliath", "King Saul"],
        "details": [
            "a shepherd’s staff lies discarded in the dust",
            "bronze armor glints under the sun",
            "vultures gather on the hilltops",
            "a distant cheer rises from the Israelite camp"
        ]
    }
}

class TimeTravelPortal:
    def __init__(self, root):
        self.root = root
        self.root.title("Time Travel Portal")
        self.root.geometry("600x400")
        self.root.configure(bg="#1a1a1a")

        self.style = ttk.Style()
        self.style.configure("TButton", font=("Arial", 12, "bold"), background="#00ffcc", foreground="black")
        self.style.configure("TLabel", font=("Arial", 10), background="#1a1a1a", foreground="#00ffcc")
        self.style.configure("TEntry", font=("Arial", 10))

        self.frame = ttk.Frame(root, padding="10")
        self.frame.pack(fill="both", expand=True)

        ttk.Label(self.frame, text="Step Into the Time Portal", font=("Arial", 16, "bold"), foreground="#00ffcc").pack(pady=10)

        ttk.Label(self.frame, text="Historical Scenario (e.g., 'during pyramid construction'):").pack()
        self.scenario_entry = ttk.Entry(self.frame, width=40)
        self.scenario_entry.pack(pady=5)
        self.scenario_entry.insert(0, "during pyramid construction")

        ttk.Label(self.frame, text="Duration (hours):").pack()
        self.duration_entry = ttk.Entry(self.frame, width=10)
        self.duration_entry.pack(pady=5)
        self.duration_entry.insert(0, "5")

        ttk.Button(self.frame, text="Generate Timeline", command=self.generate_timeline).pack(pady=10)

        self.output_text = tk.Text(self.frame, height=10, width=60, bg="#333333", fg="#00ffcc", font=("Arial", 10))
        self.output_text.pack(pady=10)

        self.play_button = ttk.Button(self.frame, text="Play", command=self.play_audio, state="disabled")
        self.play_button.pack(side="left", padx=5)
        self.pause_button = ttk.Button(self.frame, text="Pause", command=self.pause_audio, state="disabled")
        self.pause_button.pack(side="left", padx=5)

        self.audio_file = None

    def generate_timeline(self):
        scenario = self.scenario_entry.get()
        try:
            duration_hours = float(self.duration_entry.get())
            if duration_hours <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Invalid duration! Using 5 hours.")
            duration_hours = 5

        self.output_text.delete(1.0, tk.END)
        scenario_key = None
        scenario_lower = scenario.lower()

        if "pyramid construction" in scenario_lower:
            scenario_key = "pyramid construction"
        elif "david" in scenario_lower or "goliath" in scenario_lower:
            scenario_key = "david and goliath"
        else:
            self.output_text.insert(tk.END, "Scenario not recognized! Defaulting to 'during pyramid construction'.\n\n")
            scenario_key = "pyramid construction"

        data = scenarios[scenario_key]
        year = random.choice(data["years"])
        location = random.choice(data["locations"])
        weather = random.choice(data["weather"])

        if scenario_key == "david and goliath":
            philistines = random.randint(5000, 10000)
            israelites = random.randint(4000, 8000)
            intro = (f"Year: {year} BCE\nLocation: {location}\nConditions: {weather}\n"
                     f"On Site: {philistines} Philistine warriors face {israelites} Israelites across the valley.\n\n")
        else:
            elephants = random.randint(800, 1500)
            bulls = random.randint(3000, 4000)
            humans = random.randint(4000, 6000)
            intro = (f"Year: {year} BCE\nLocation: {location}\nConditions: {weather}\n"
                     f"On Site: {elephants} elephants, {bulls} bulls, {humans} humans at the construction site.\n\n")

        timeline = intro + "=== Your Imaginary Timeline ===\n"
        hours = int(duration_hours)
        events_per_hour = 3
        for hour in range(hours):
            timeline += f"\nHour {hour + 1}:\n"
            for _ in range(events_per_hour):
                activity = random.choice(data["activities"])
                detail = random.choice(data["details"])
                if random.random() < 0.3:
                    figure = random.choice(data["historical_figures"])
                    timeline += f" - {activity}. {figure} stands nearby, observing silently. {detail}.\n"
                else:
                    timeline += f" - {activity}. {detail}.\n"

        self.output_text.insert(tk.END, timeline)
        self.audio_file = "time_travel_experience.mp3"
        tts = gTTS(text=timeline, lang="en", slow=False)
        tts.save(self.audio_file)
        pygame.mixer.music.load(self.audio_file)
        self.play_button.config(state="normal")
        self.pause_button.config(state="normal")

    def play_audio(self):
        if self.audio_file and os.path.exists(self.audio_file):
            pygame.mixer.music.play()

    def pause_audio(self):
        pygame.mixer.music.pause()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    portal = TimeTravelPortal(root)
    portal.run()
