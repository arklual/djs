import matplotlib.pyplot as plt
import numpy as np
import imgkit
import os

html = '''
<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="diagram.css">
        <link href="https://fonts.cdnfonts.com/css/gilroy-bold" rel="stylesheet">
        <style>
            * {{
                font-family: 'Gilroy-Bold', sans-serif;
            }}
            .row {{
                display: flex;
                flex-direction: row;
                justify-content: center;
                align-items: center;
            }}
            .column {{
                display: flex;
                flex-direction: column;
                margin: 10px;
                width: 300px;
                text-align: center;
            }}
            .sport {{
                background-color: #E69F00;
            }}
            .family {{
                background-color: #56B4E9;
            }}
            .friends {{
                background-color: #009E73;
            }}
            .work {{
                background-color: #F0E442;
            }}
            .hobby {{
                background-color: #0072B2;
            }}
            .money {{
                background-color: #D55E00;
            }}
            .selfedu {{
                background-color: #D55EFF;
            }}
        </style>
    </head>
    <body>
        <h1 style="text-align: center;">&#1050;&#1054;&#1051;&#1045;&#1057;&#1054; &#1046;&#1048;&#1047;&#1053;&#1045;&#1053;&#1053;&#1054;&#1043;&#1054; &#1041;&#1040;&#1051;&#1040;&#1053;&#1057;&#1040;</h1>
        <div class="row">
            <div class="column">
                <h1 class="friends">&#1044;&#1088;&#1091;&#1079;&#1100;&#1103;</h1>
                <h1 class="work">&#1056;&#1072;&#1073;&#1086;&#1090;&#1072;</h1>
                <h1 class="hobby">&#1061;&#1086;&#1073;&#1073;&#1080;</h1>
                <h1 class="money">&#1060;&#1080;&#1085;&#1072;&#1085;&#1089;&#1099;</h1>
            </div >
            <img style="width: 50%;" src="{}">
            <div class="column">
                <h1 class="family">&#1057;&#1077;&#1084;&#1100;&#1103;</h1>
                <h1 class="sport">&#1057;&#1087;&#1086;&#1088;&#1090; &#1080; &#1079;&#1076;&#1086;&#1088;&#1086;&#1074;&#1100;&#1077;</h1>
                <h1 class="selfedu">&#1057;&#1072;&#1084;&#1086;&#1088;&#1072;&#1079;&#1074;&#1080;&#1090;&#1080;&#1077;</h1>
            </div>
        </div>
    </body>
</html>
'''

def generate(data):
    # цвета для каждой категории
    colors = ['#E69F00', '#56B4E9', '#009E73', '#F0E442', '#0072B2', '#D55E00', '#D55EFF']

    # углы направлений гистограммы
    angles = [n / float(len(data)) * 2 * 3.14159 for n in range(len(data))]
    angles += angles[:1]

    # создание радиального графика
    fig = plt.figure(figsize=(10, 10), dpi=100)
    ax = plt.subplot(111, polar=True)

    # удаление линий сетки
    ax.grid(True)

    # ограничение осей
    plt.ylim([0, 10])

    # создание радиальной шкалы
    #ticks = np.linspace(start=0, stop=10, num=11)
    #ax.set_yticks(ticks)
    #ax.set_yticklabels(ticks, fontsize=12, fontweight='bold', color='gray')

    # построение гистограммы
    plt.xticks(angles[:-1], data.values(), color='black', size=18, fontweight='bold')

    for color, angle, label, value in zip(colors, angles, data.keys(), data.values()):
        count = 0.1
        for i in range(1, value + 1):
            ax.bar(
                x=angle, 
                height=i, 
                width=(2*3.14159)/len(data), 
                color=color, 
                alpha=count  
            )
            count += 0.1

    for color, angle, label, value in zip(colors, angles, data.keys(), data.values()):
        ax.bar(
                x=angle + 0.0871966666666666/2+0.4, 
                height=i, 
                width=0.01, 
                color="#000", 
                alpha=1  
            )



    # отключение рамки графика
    ax.spines['polar'].set_visible(True)

    # отображение графика
    #plt.show()
    plt.savefig('main/static/main/diagram.png')
    imgkit.from_string(html.format(os.path.abspath('main/static/main/diagram.png')), 'main/static/main/diagram.png', options={'format':'png', "enable-local-file-access": None, 'quality': 100, 'width': 2000, 'height':1000})