class Industry666:
    def __init__(self):
        self.vision = "A convergence of technology and biology in Industry 6.6.6"
        self.pillars = ["Classical Computing", "Quantum Computing", "Biological Computing"]
        self.applications = ["DNA data storage", "Living cellular components", "Synthetic organisms for eco-friendly production"]
    
    def display_vision(self):
        print(self.vision)

    def display_pillars(self):
        print("The three pillars of Industry 6.6.6 are:")
        for pillar in self.pillars:
            print(pillar)

    def display_applications(self):
        print("Remarkable applications on the horizon:")
        for app in self.applications:
            print(app)

if __name__ == "__main__":
    industry = Industry666()
    industry.display_vision()
    industry.display_pillars()
    industry.display_applications()
