from bokeh.plotting import figure, output_file, show
import csv

if __name__ == '__main__':
    output_file("fig.html")
    fig = figure()
    
    total_values = int(input('How many values do you graph?'))
    x_values = list(range(total_values))
    y_values = []
    
    for x in x_values:
        value = int(input(f"Y value for {x} value"))
        y_values.append(value)
    
    fig.line(x_values,y_values, line_width = 2 )
    show(fig)
    
    
    
    
    