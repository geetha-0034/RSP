import customtkinter as ctk
import random
from PIL import Image

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class RockPaperScissorsGame(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Rock Paper Scissors Pro")
        self.geometry("600x650")
        self.resizable(False, False)

        # Game State
        self.player_score = 0
        self.cpu_score = 0
        self.choices = ['Rock', 'Paper', 'Scissors']
        self.emojis = {'Rock': '🪨', 'Paper': '📄', 'Scissors': '✂️'}

        # UI Setup
        self.setup_ui()

    def setup_ui(self):
        # Header
        self.header_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.header_frame.pack(pady=20, padx=20, fill="x")
        
        self.title_label = ctk.CTkLabel(self.header_frame, text="Ultimate RPS Challenge", font=ctk.CTkFont(size=32, weight="bold"))
        self.title_label.pack(pady=(10, 5))
        
        self.subtitle_label = ctk.CTkLabel(self.header_frame, text="Player vs CPU", font=ctk.CTkFont(size=16, slant="italic"), text_color="gray")
        self.subtitle_label.pack()

        # Score Board
        self.score_frame = ctk.CTkFrame(self, corner_radius=15, fg_color="#1E1E1E", border_width=2, border_color="#3A3A3A")
        self.score_frame.pack(pady=20, padx=40, fill="x")

        self.player_score_label = ctk.CTkLabel(self.score_frame, text="Player: 0", font=ctk.CTkFont(size=24, weight="bold"), text_color="#00D2FF")
        self.player_score_label.pack(side="left", padx=30, pady=20)
        
        self.vs_label = ctk.CTkLabel(self.score_frame, text="VS", font=ctk.CTkFont(size=20, weight="bold"), text_color="#FF4B4B")
        self.vs_label.pack(side="left", expand=True)

        self.cpu_score_label = ctk.CTkLabel(self.score_frame, text="CPU: 0", font=ctk.CTkFont(size=24, weight="bold"), text_color="#FF007A")
        self.cpu_score_label.pack(side="right", padx=30, pady=20)

        # Main Play Area
        self.play_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.play_frame.pack(pady=10, expand=True, fill="both")

        # Result Display Area
        self.result_label = ctk.CTkLabel(
            self.play_frame, 
            text="Make your move!", 
            font=ctk.CTkFont(size=26, weight="bold")
        )
        self.result_label.pack(pady=(10, 20))
        
        self.move_display_label = ctk.CTkLabel(
            self.play_frame,
            text="👤 ?   vs   🖥️ ?",
            font=ctk.CTkFont(size=36)
        )
        self.move_display_label.pack(pady=10)

        # Buttons Frame
        self.buttons_frame = ctk.CTkFrame(self.play_frame, fg_color="transparent")
        self.buttons_frame.pack(pady=30)

        # Buttons
        self.btn_rock = self.create_choice_button("Rock", self.buttons_frame)
        self.btn_rock.grid(row=0, column=0, padx=15)
        
        self.btn_paper = self.create_choice_button("Paper", self.buttons_frame)
        self.btn_paper.grid(row=0, column=1, padx=15)

        self.btn_scissors = self.create_choice_button("Scissors", self.buttons_frame)
        self.btn_scissors.grid(row=0, column=2, padx=15)

        # Reset button
        self.reset_btn = ctk.CTkButton(
            self, 
            text="Reset Game", 
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color="#333333",
            hover_color="#555555",
            command=self.reset_game
        )
        self.reset_btn.pack(pady=20)

    def create_choice_button(self, choice, parent):
        return ctk.CTkButton(
            parent,
            text=f"{self.emojis[choice]}\n{choice}",
            font=ctk.CTkFont(size=20, weight="bold"),
            width=120,
            height=120,
            corner_radius=20,
            fg_color="#2B2B2B",
            hover_color="#3A86FF",
            command=lambda: self.play(choice)
        )

    def play(self, player_choice):
        self.animate_choice()
        cpu_choice = random.choice(self.choices)
        
        # Determine winner
        result = self.check_winner(player_choice, cpu_choice)
        
        # Update UI
        self.move_display_label.configure(
            text=f"👤 {self.emojis[player_choice]}   vs   🖥️ {self.emojis[cpu_choice]}"
        )
        
        if result == "win":
            self.player_score += 1
            self.result_label.configure(text=f"You win! {player_choice} beats {cpu_choice}", text_color="#00D2FF")
        elif result == "lose":
            self.cpu_score += 1
            self.result_label.configure(text=f"You lost! {cpu_choice} beats {player_choice}", text_color="#FF007A")
        else:
            self.result_label.configure(text="It's a Tie!", text_color="white")

        self.update_scores()

    def check_winner(self, player, cpu):
        if player == cpu:
            return "tie"
        elif (player == 'Rock' and cpu == 'Scissors') or \
             (player == 'Paper' and cpu == 'Rock') or \
             (player == 'Scissors' and cpu == 'Paper'):
            return "win"
        else:
            return "lose"

    def update_scores(self):
        self.player_score_label.configure(text=f"Player: {self.player_score}")
        self.cpu_score_label.configure(text=f"CPU: {self.cpu_score}")

    def animate_choice(self):
        # A simple little trick to provide a basic gamifying "flash" feel before revealing
        self.result_label.configure(text="Rock... Paper... Scissors...", text_color="yellow")
        self.update()
        self.after(200)

    def reset_game(self):
        self.player_score = 0
        self.cpu_score = 0
        self.update_scores()
        self.result_label.configure(text="Make your move!", text_color="white")
        self.move_display_label.configure(text="👤 ?   vs   🖥️ ?")

if __name__ == "__main__":
    app = RockPaperScissorsGame()
    app.mainloop()
