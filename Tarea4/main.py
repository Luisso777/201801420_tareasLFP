import webbrowser

nombres=['Nery','jose','barrientos','edwin','hernandez','damaris', 'paola','amparo','dulce','paz']
edad=['20','70','27','29','82','31','41','38','33','30']
saldo=['20120.1','15645531.5','51455.25','4545635.13','4645153.1','554845.04','4545312.66','9845135.15','5455454.4','48455.6']
activo=['False','False','False','False','True','True','True','False','False','Fasle']

atributos=["nombre","edad","activo","saldo"]

def html(atributos):
    print('Cargando Html...')
    cabeza = '<!DOCTYPE html>\n' + '<html lang="en">\n' + '<head>\n' + '<meta charset="utf-8">\n' + '<title>Reporte</title>\n'+ '<link rel="stylesheet"  href="estilo.css">\n'
    cabeza = cabeza + '</head>\n' + '<body>\n' + '<div id="main-container">\n' + '<table>\n' + '<thead>\n' + '<tr>\n'
    for elemento in atributos:
        timer = '<th>' + elemento + '</th>'
        cabeza = cabeza + timer
    cabeza = cabeza + '\n</tr>' + '\n</thead>\n'
    for a in range(10):
        label = '<tr>\n'
        label = label + '<td>' + nombres[a] + '</td><td>' + edad[a] + '</td><td>' + \
                saldo[a] + '</td><td>' + activo[a] + '</td>'

        label =label + '\n</tr>\n'
        cabeza = cabeza + label
    cabeza = cabeza + '</table>\n' + '</div>\n' + '</body>\n' + '</html>'
    doc = open("tarea4.html", "w")
    doc.write(cabeza)
    doc.close()

    webbrowser.open_new_tab('tarea4.html')
html(atributos)