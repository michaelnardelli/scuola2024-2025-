import time
import sys
from datetime import datetime
from blessed import Terminal

term = Terminal()

class RaceRenderer:
    def __init__(self, race):
        self.race = race
        self.selected_driver = 0
        self.last_update = datetime.now()

    def draw_track(self):
        track = ""
        track_width = 40
        track_height = 10

        for i in range(track_height):
            if i == 0 or i == track_height - 1:
                track += term.blue("═" * track_width) + "\n"
            else:
                track += term.blue("║") + " " * (track_width - 2) + term.blue("║") + "\n"
        return track

    def draw_sidebar(self):
        selected_entry = self.race.piloti[self.selected_driver]
        sidebar = f"""
{term.bold("🏁 LIVE TIMING")} (Lap {self.race.current_lap}/{self.race.laps})
🏎️ {selected_entry['driver'].nome}
⛽ Carburante: {selected_entry['car'].fuel:.1f}%
💥 Danni: {selected_entry['car'].damage:.1f}%
        """
        return sidebar

    def render(self):
        print(term.clear)
        print(self.draw_track())
        print(self.draw_sidebar())
        print(term.dim("[P] Pausa  [←→] Cambia pilota  [Q] Esci"))

class Gara:
    def __init__(self, nome: str, laps: int = 60):
        self.nome = nome
        self.laps = laps
        self.current_lap = 0
        self.piloti = []

    def add_driver(self, driver):
        self.piloti.append({"driver": driver, "car": driver.auto})

    def simulate_race(self):
        renderer = RaceRenderer(self)
        
        while self.current_lap < self.laps:
            renderer.render()
            key = term.inkey(timeout=0.1)
            
            if key == "q":
                break
            if key == "p":
                self.handle_pause()
            if key.name == "KEY_RIGHT":
                renderer.selected_driver = (renderer.selected_driver + 1) % len(self.piloti)
            if key.name == "KEY_LEFT":
                renderer.selected_driver = (renderer.selected_driver - 1) % len(self.piloti)

            self.current_lap += 1
            time.sleep(0.1)

    def handle_pause(self):
        print(term.clear + term.bold_red("⏸ GARA IN PAUSA [C] Continua  [Q] Esci"))
        while True:
            key = term.inkey()
            if key == "c":
                break
            if key == "q":
                sys.exit()

class Pilota:
    def __init__(self, nome, squadra):
        self.nome = nome
        self.squadra = squadra
        self.auto = Car()

class Car:
    def __init__(self):
        self.fuel = 100
        self.damage = 0

def main():
    piloti = [
        Pilota("Mario Rossi", "Ferrari"),
        Pilota("Luigi Bianchi", "Mercedes"),
        Pilota("Andrea Verdi", "Red Bull")
    ]
    
    gara = Gara("Gran Premio d'Italia", laps=30)
    for p in piloti:
        gara.add_driver(p)

    gara.simulate_race()

    print(term.clear + term.bold("🏁 RISULTATI FINALI 🏁"))
    print(term.bold_green("Gara completata!"))
    time.sleep(2)

if __name__ == "__main__":
    main()
