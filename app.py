import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render

#Options
ui.page_opts(title="Baby's First App (I'm Baby)", fillable= True)

with ui.sidebar():
    "THIS IS THE SIDEBAR"
    ui.input_slider("n", "Number of Bins", 5, 50, 25)
    ui.input_numeric("seed","Histogram Seed",476784,)
    


@render.plot(alt="A histogram")
def histogram():
    np.random.seed(input.seed())
    hist_data_array = 100 + 15 * np.random.randn(437)
    plt.hist(hist_data_array, input.n(), density=True)
