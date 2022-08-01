from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def start():
  return render_template('receitas.html')

@app.route('/<receita>')
def receitas(receita):
  opcoes_receitas = [
    'Bolo de Chocolate: INGREDIENTES: - 4 ovos. - 4 colheres (sopa) de chocolate em po.- 2 colheres (sopa) de manteiga.- 3 xicaras (cha) de farinha de trigo. - 2 xicaras (cha) de acucar.- 2 colheres (sopa) de fermento.- 1 xicara (cha) de leite.                                                        CALDA: - 7 colheres (sopa) de chocolate em po. - 2 lat as de creme de leite com soro. - 3 colheres (sopa) de acucar.                                                      Modo de preparo: PARA A MASSA:                                                        1) Em um liquidificador adicione os ovos, o chocolate em po, a manteiga, a farinha de trigo, o acucar e o leite, depois bata por 5 minutos. 2) Adicione o fermento e misture com uma espatula delicadamente.  3) Em uma forma untada, despeje a massa e asse em forno medio (180 C) preaquecido por cerca de 40 minutos. Nao se esqueca de usar uma forma alta para essa receita: como leva duas colheres de fermento, ela cresce bastante! Outra solucao pode ser colocar apenas uma colher de fermento e manter a sua receita em uma forma pequena.                                        PARA A CALDA:                                                                         4) Em uma panela, aqueca a manteiga e misture o chocolate em po ate que esteja homogeneo. 5) Acrescente o creme de leite e misture bem ate obter uma consistencia cremosa.      6) Desligue o fogo e acrescente o acucar.', 
                     'Bolo de milho: INGREDIENTES:        - 1 lata de milho verde. - 1 lata de oleo (medida da lata de milho). - 1 lata de acucar (medida da lata de milho).  - 1 lata de fuba (medida da lata de milho). - 4 ovos.  - 2 colheres (sopa) de farinha de trigo.   - 2 colheres (sopa) de coco ralado.  - 1 e 1/2 colher (cha) de fermento em po.                                                      MODO DE PREPARO:            1) Em um liquidificador, adicione o milho verde, o oleo, o acucar, o fuba, os ovos e a farinha de trigo, depois bata ate obter uma consistencia cremosa.         2) Depois, acrescente o coco ralado e o fermento, misture novamente.             3) Despeje a massa em uma assadeira untada e leve para assar, em um forno com temperatura media a 180C, preaquecido por 40 minutos.',
    'Panquecas: INGREDIENTES: -1 e 1/4 xicara (cha) de farinha de trigo - 1 colher (sopa) de acucar. - 3 colheres (cha) de fermento em po. - 2 ovos levemente batidos. - 1 xicara (cha) de leite. - 2 colheres (sopa) de manteiga derretida. - pitada de sal. - oleo MODO DE PREPARO: 1)Misture em um recipiente: a farinha, o acucar, o fermento e o sal. 2) Em outro recipiente, misture os ovos, o leite e a manteiga. 3) Acrescente os liquidos aos secos, sem misturar em excesso. 4)  O ponto da massa não deve ser muito liquido, deve escorrer lentamente. 5) Aqueca e unte a frigideira com oleo, coloque a massa no centro, cerca de 1/4 xicara por panqueca. 6) Vire a massa para assar do outro lado e esta pronto!',
                     'Pao de Queijo: INGREDIENTES:    - 2 copos americanos de leite.  - 1 copo americano de agua.   - 1/3 de copo americano de oleo.  - 1 colher de sopa de sal.     - 500 g de polvilho doce.    - Queijo ralado a gosto.   - 3 ovos inteiros.                                                                  MODO DE PREPARO:   1) Ferva o leite com a agua e o oleo.  2) Em uma vasilha misture o polvilho e o sal.   3) Jogue o liquido fervido e misture com uma colher grande.    4) Espere esfriar e despeje o queijo ralado e os ovos.   5) Misture a massa com a mão amassando bem ate virar uma cola caseira dura.     6) Faca bolinhas do tamanho que preferir.  7) Asse em forno bem quente ate dourar.  8) Sirva quentinho. ']
  
  receita = int(receita)

  return jsonify({'receita':opcoes_receitas[receita-1]})

app.run(host='0.0.0.0')

  


    

  

  

  

  


  
  

