import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_analisi(self, e):
        calorie=self._view.txtcalorie.value
        if calorie=="":
            self._view.create_alert("Inserire un valore numerico per le calorie")
            return
        grafo = self._model.creaGrafo( int(calorie))
        self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato."))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene "
                                                      f"{self._model.getNumNodes()} nodi."))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene {self._model.getNumEdges()} archi."))
        porzioni=grafo.nodes()
        for porzione in porzioni:
            self._view.ddporzione.options.append(ft.dropdown.Option(
                text=porzione))
        self._view.update_page()
    def handle_correlate(self, e):
        porzione=self._view.ddporzione.value
        if porzione is None:
            self._view.create_alert("Selezionare un tipo di porzione")
            return
        dizio=self._model.analisi(porzione)
        for porzione in dizio.keys():
            self._view.txt_result.controls.append(ft.Text(f"{porzione} con peso {dizio[porzione]}"))
        self._view.update_page()

    def handle_cammino(self, e):
        passi = self._view.txtpassi.value
        if passi == "":
            self._view.create_alert("Inserire un passo")
            return
        soluzione,peso=self._model.getBestPath(int(passi),self._view.ddporzione.value)
        self._view.txt_result.controls.append(ft.Text(f"Il cammino migliore ha un peso pari a {peso}"))
        for nodo in soluzione:
            self._view.txt_result.controls.append(ft.Text(f"{nodo}"))
        self._view.update_page()
