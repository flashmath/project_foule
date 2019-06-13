class Observable:
    def __init__(self):
        self.observateurs = []

    def attach_observateur(self,observateur):
        self.observateurs.append(observateur)

    def notifier(self):
        for o in self.observateurs:
            o.mise_a_jour()