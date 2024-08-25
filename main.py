import time

class Organelle:
    def __init__(self, name, function_description):
        self.name = name
        self.function_description = function_description
        self.active = False

    def perform_function(self):
        if self.active:
            self.visualize_action()

    def activate(self):
        self.active = True
        self.visualize_action()

    def deactivate(self):
        self.active = False

    def visualize_action(self):
        print(f"{self.name} is performing: {self.function_description}")

class EukaryoticCell:
    def __init__(self):
        self.nucleus = Organelle("Nucleus", "Controls cell activities")
        self.mitochondria = Organelle("Mitochondria", "Produces energy")
        self.ser = Organelle("Smooth ER", "Synthesizes lipids")
        self.golgi_app = Organelle("Golgi Apparatus", "Processes proteins")
        self.lysosome = Organelle("Lysosome", "Breaks down waste")
        self.ticks = 0
        self.cell_count = 1

    def tick(self):
        self.ticks += 1
        if self.ticks % 5 == 0:
            self.activate_protein_synthesis()
        if self.ticks % 10 == 0:
            self.activate_energy_production()
        if self.ticks % 15 == 0:
            self.activate_lysosome()
        if self.ticks % 20 == 0:
            self.activate_mitosis()

    def activate_protein_synthesis(self):
        self.nucleus.activate()
        self.ser.activate()
        self.golgi_app.activate()
        self.nucleus.perform_function()
        self.ser.perform_function()
        self.golgi_app.perform_function()

    def activate_energy_production(self):
        self.mitochondria.activate()
        self.mitochondria.perform_function()

    def activate_lysosome(self):
        self.lysosome.activate()
        self.lysosome.perform_function()

    def activate_mitosis(self):
        self.cell_count += 1
        print("Mitosis activated: New cell created.")
        self.create_organelles()

    def create_organelles(self):
        print(f"Creating organelles for new cell. Total cells: {self.cell_count}")

def main():
    cell = EukaryoticCell()
    while True:
        cell.tick()
        time.sleep(1)

if __name__ == "__main__":
    main()
