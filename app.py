from flask import Flask, render_template
from database import execute_query

app = Flask(__name__)
app.debug = True

@app.route('/')
@app.route('/home')
def home():    
    return render_template("principal.html")

@app.route('/query1')
def query1():
    artistas = execute_query("SELECT SUM(streams), songs.id_artist, artistas.artist_Name FROM `songs`, artistas WHERE songs.id_artist = artistas.artist_ID AND YEAR(songs.release_date) = 2023 GROUP BY songs.id_artist ORDER BY SUM(streams) DESC LIMIT 10;")
    return render_template("query1.html", artistas = artistas)

@app.route('/query2')
def query2():
    artistas = execute_query("SELECT songs.name, artistas.artist_Name, songs.streams FROM `songs`, artistas WHERE songs.id_artist = artistas.artist_ID ORDER BY streams DESC LIMIT 20;")
    return render_template("query2.html",artistas = artistas)

@app.route('/query3')
def query3():
    artistas  = execute_query("SELECT COUNT(usuarios.ID), countries.country_name FROM usuarios, countries WHERE usuarios.Pais = countries.country_ID GROUP BY countries.country_ID ORDER BY COUNT(usuarios.ID) DESC LIMIT 10;")
    return render_template("query3.html", artistas = artistas)

@app.route('/query4')
def query4():
    artistas = execute_query("SELECT artistas.artist_Name, COUNT(songs.id_artist) FROM artistas, songs WHERE artistas.artist_ID = songs.id_artist GROUP BY artistas.artist_ID ORDER BY COUNT(songs.id_artist) DESC LIMIT 20;")
    return render_template("query4.html", artistas= artistas)

@app.route('/query5')
def query5():
    artistas = execute_query("SELECT DAT.H, (DAT.H*100/DAT.T) AS POR_HOM,DAT.M, (DAT.M*100/DAT.T) AS POR_MUJ, DAT.T FROM( SELECT( SELECT COUNT(*) FROM `usuarios` WHERE sexo = 0 ) AS M, ( SELECT COUNT(*) FROM `usuarios` WHERE sexo = 1 ) AS H, ( SELECT COUNT(*) FROM `usuarios` ) AS T ) DAT;")
    return render_template("query5.html", artistas = artistas)

@app.route('/query6')
def query6():
    artistas = execute_query("SELECT DAT.FREE AS FREE, (DAT.FREE*100/DAT.T) AS Por_Free,DAT.PREM AS Premium, (DAT.PREM*100/DAT.T) AS Por_Prem, DAT.T AS TOTAL FROM( SELECT( SELECT COUNT(*) FROM `usuarios` WHERE usuarios.Tipo_Cuenta = 0 ) AS FREE, ( SELECT COUNT(*) FROM `usuarios` WHERE usuarios.Tipo_Cuenta = 1 ) AS PREM, ( SELECT COUNT(*) FROM `usuarios` ) AS T ) DAT;")
    return render_template("query6.html", artistas = artistas)

if __name__ == '__main__':
    app.run()

