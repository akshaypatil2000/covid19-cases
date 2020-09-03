from flask import Flask,render_template,request,jsonify,abort
import requests
#import COVID19Py
#covid19 = COVID19Py.COVID19()
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/data',methods=['GET','POST'])
def data():
        if request.method == 'POST':
            name = request.form['name']
            try:
                #data = covid.get_status_by_country_name_(name)
                url = "https://coronavirus-19-api.herokuapp.com/countries/{}"
                #https://coronavirus-19-api.herokuapp.com/countries/{countryName}
                r =requests.get(url.format(name)).json()
                #print(r)
                country=r['country']
                confirmed=r['cases']
                active=r['active']
                deaths=r['deaths']

                #print(country)
                '''covid= {
                        'country':r['country'],
                        'confirmed': r['cases'],
                        'recovered': r['recovered'],
                        'critical': r['critical'],
                        'deaths': r['deaths'],
                        'todayCases': r['todayCases'],
                        'todayDeaths': r['todayDeaths'],
                        'active': r['active'],
                        'totalTests': r['totalTests'],
                    }
                print(covid)'''
                #print(data)

                return render_template('index.html',country=country,confirmed=confirmed,active=active,deaths=deaths )

            except:
                abort(404)
        else:
               return render_template('index.html')


if __name__=='__main__':
    app.run(debug=True)