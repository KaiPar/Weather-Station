from flask import Flask, Markup, render_template
import dbdata

app = Flask(__name__)

colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]

@app.route('/all')
def up_all():
    idd, labels, values, humvals = dbdata.get_db_allsensordata()
    all_labels = labels
    all_values = values
    index = len(all_labels)-1
    curr_temp = all_values[index]
    curr_hum = humvals[index]

    return render_template('allchart.html',
                            max=41,
                            labels=all_labels,
                            values=all_values,
                            set=zip(values, labels, colors),
                            title="Welcome to Weather station",
                            temp=(str(curr_temp) + " degrees celsius"),
                            hum=(str(curr_hum ) + "%"))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
