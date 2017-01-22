# coding=utf-8
from flask_pymongo import MongoClient
import cyrtranslit
from slugify import slugify
from tqdm import tqdm
import csv


# Instantiate mongo client
mongo = MongoClient()

# Create mongo database instance
db = mongo['datacentar']
collection = 'izbori2'
class Izbori2DataImporter(object):
    def get_political_parties(self, kandidat_name=None):
        data = []
        # year 2000
        data.append({
            'slug': "demokratska-opozicija-srbije",
            "name": "Демократска опозиција Србије",
            "color": "#AA8E39"
        })
        data.append({
            'slug': "socijalisticka-partija-srbije",
            "name": "Социјалистичка партија Србије",
            "color": "#2E4372"
        })
        data.append({
            'slug': "srpska-radikalna-stranka",
            "name": "Српска радикална странка",
            "color": "#29526D"
        })
        data.append({
            'slug': "stranka-srpskog-jedinstva",
            "name": "Странка Српског јединства",
            "color": "#A3A838"
        })
        data.append({
            'slug': "srpski-pokret-obnove",
            "name": "Српски покрет обнове",
            "color": "#6B9A33"
        })
        data.append({
            'slug': "demokratska-socijalisticka-partija",
            "name": "Демократска социјалистичка партија",
            "color": "#05a6f0"
        })
        data.append({
            'slug': "srpska-socijal-demokratska-partija",
            "name": "Српска социјал-демократска партија",
            "color": "#852C62"
        })
        data.append({
            'slug': "jugoslovenska-levica",
            "name": "Југословенска левица",
            "color": "#81bc06"
        })
        # end of 2000
        data.append({
            'slug': "",
            "name": "ЦРНОГОРСКА ПАРТИЈА - ЈОСИП БРОЗ",
            "color": "#AA8E39"
        })
        data.append({
            'slug': "",
            "name": "ЛИСТА НАЦИОНАЛНИХ ЗАЈЕДНИЦА - ЕМИР ЕЛФИЋ",
            "color": "#2E4372"
        })
        data.append({
            'slug': "",
            "name": "ДОСТА ЈЕ БИЛО - САША РАДУЛОВИЋ",
            "color": "#29526D"
        })

        data.append({
            'slug': "",
            "name": "ГРУПА ГРАЂАНА ПАТРИОТСКИ ФРОНТ",
            "color": "#A3A838"
        })
        data.append({
            'slug': "",
            "name": "РУСКА СТРАНКА - СЛОБОДАН НИКОЛИЋ",
            "color": "#6B9A33"
        })
        data.append({
            'slug': "partija-za-demokratsko-delovanje-riza-halimi",
            "name": "ПАРТИЈА ЗА ДЕМОКРАТСКО ДЕЛОВАЊЕ - РИЗА ХАЛИМИ",
            "color": "#412F74"
        })
        data.append({
            'slug': "aleksandar-vucic-sns-sdps-ns-spo-ps",
            "name": "АЛЕКСАНДАР ВУЧИЋ - СНС, СДПС, НС, СПО, ПС",
            "color": "#00441b"
        })
        data.append({
            'slug': "",
            "name": "АЛЕКСАНДАР ВУЧИЋ – БУДУЋНОСТ У КОЈУ ВЕРУЈЕМО (Српска напредна странка Сцијалдемократска партија Србије, Нова Србија, Српски покрет обнове, Покрет социјалиста)",
            "color": "#05a6f0"
        })

        data.append({
            'slug': "",
            "name": "ДЕМОКРАТСКА СТРАНКА СРБИЈЕ - ВОЈИСЛАВ КОШТИНИЦА",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "ЧЕДОМИР ЈОВАНОВИЋ - ЛДП, БДЗС, СДУ",
            "color": "#313695"
        })
        data.append({
            'slug': "savez-vojvodanskih-madara-istvan-pastor",
            "name": "САВЕЗ ВОЈВОЂАНСКИХ МАЂАРА - ИШТВАН ПАСТОР",
            "color": "#7fbc41"
        })

        data.append({
            'slug': "ujedinjeni-regioni-srbije-mladan-dinkic",
            "name": "УЈЕДИЊЕНИ РЕГИОНИ СРБИЈЕ - МЛАЂАН ДИНКИЋ",
            "color": "#74add1"
        })
        data.append({
            'slug': "",
            "name": "СА ДЕМОКРАТСКОМ СТРАНКОМ ЗА ДЕМОКРАТСКУ СРБИЈУ",
            "color": "#5aae61"
        })
        data.append({
            'slug': "",
            "name": "ДВЕРИ - БОШКО ОБРАДОВИЋ",
            "color": "#4575b4"
        })

        data.append({
            'slug': "",
            "name": "БОРИС ТАДИЋ - НДС, ЛСВ, ЗЗС, ВМДК, ЗЗВ, ДЛР",
            "color": "#a6dba0"
        })
        data.append({
            'slug': "",
            "name": "ТРЕЋА СРБИЈА - ЗА СВЕ ВРЕДНЕ ЉУДЕ",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "МУАМЕР ЗУКОРЛИЋ / MUAMER ZUKORLIĆ - БОШЊАЧКА ДЕМОКРАТСКА ЗАЈЕДНИЦА САНЏАКА / BOŠNJAČKA DEMOKRATSKA ZAJEDNICA SANDŽAKA",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "SDA Sandžaka – Dr. Sulejman Ugljanin СДА Санџака – Др Сулејман Угљанин",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "За слободну Србију – ЗАВЕТНИЦИ – Милица Ђурђевић",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Група грађана ЗА ПРЕПОРОД СРБИЈЕ – ПРОФ. ДР СЛОБОДАН КОМАЗЕЦ",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Републиканска странка – Republikánus párt – Никола Сандуловић",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "СРПСКО РУСКИ ПОКРЕТ – СЛОБОДАН ДИМИТРИЈЕВИЋ",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Борко Стефановић – Србија за све нас",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "ДИЈАЛОГ – МЛАДИ СА СТАВОМ – СТАНКО ДЕБЕЉАКОВИЋ",
            "color": "#852C62"
        })
        data.append({
            'slug': "dosta-je-bilo-sasa-radulovic",
            "name": "ДОСТА ЈЕ БИЛО – САША РАДУЛОВИЋ",
            "color": "#852C62"
        })
        data.append({
            'slug': "partija-za-demokratsko-delovanje-ardita-sinani",
            "name": "ПАРТИЈА ЗА ДЕМОКРАТСКО ДЕЛОВАЊЕ – АРДИТА СИНАНИ PARTIA PËR VEPRIM DEMOKRATIK – ARDITA SINANI",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "ЗЕЛЕНА СТРАНКА",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "У ИНАТ – СЛОЖНО ЗА СРБИЈУ – НАРОДНИ САВЕЗ",
            "color": "#852C62"
        })
        data.append({
            'slug': "aleksandar-vucic-srbija-pobeduje",
            "name": "АЛЕКСАНДАР ВУЧИЋ - СРБИЈА ПОБЕЂУЈЕ",
            "color": "#05a6f0"
        })
        data.append({
            'slug': "",
            "name": "ЗА ПРАВЕДНУ СРБИЈУ - ДЕМОКРАТСКА СТРАНКА (НОВА, ДСХВ, ЗЗС)",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "ИВИЦА ДАЧИЋ -\"Социјалистичка партија Србије (СПС), Јединствена Србија (ЈС) - Драган Марковић Палма\"",
            "color": "#81bc06"
        })
        data.append({
            'slug': "dr-vojislav-seselj-srpska-radikalna-stranka",
            "name": "Др ВОЈИСЛАВ ШЕШЕЉ - СРПСКА РАДИКАЛНА СТРАНКА",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "ДВЕРИ - ДЕМОКРАТСКА СТРАНКА СРБИЈЕ - САНДА РАШКОВИЋ ИВИЋ - БОШКО ОБРАДОВИЋ",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Vajdasági Magyar Szövetség-Pásztor István - Савез војвођанских Мађара-Иштван Пастор",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "БОРИС ТАДИЋ, ЧЕДОМИР ЈОВАНОВИЋ - САВЕЗ ЗА БОЉУ СРБИЈУ - Либерално демократска партија, Лига социјалдемократа Војводине, Социјалдемократска странка",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Иштван Пастор",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Маријан Ристичевић",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Чедомир Јовановић",
            "color": "#852C62"
        })
        data.append({
            'slug': "milutin-mrkonjic",
            "name": "Милутин Мркоњић",
            "color": "#99d8c9"
        })
        data.append({
            'slug': "marijan-risti-cevic",
            "name": "Маријан Ристи-чевић",
            "color": "#2ca25f"
        })

        data.append({
            'slug': "",
            "name": "Југослав Добричанин",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Велимир Илић",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Вук Драшковић",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Велимир-Бата Живојиновић",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Проф. Др Бранислав-Бане Ивковић",
            "color": "#852C62"
        })

        data.append({
            'slug': "",
            "name": "Др Мирољуб Лабус",
            "color": "#D4D469"
        })
        data.append({
            'slug': "",
            "name": "Др Томислав Лалошевић",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Др Вук Обрадовић",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Небојша Павковић",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Проф. Борислав Пелевић",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Др Драган Раденовић",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Др Војислав Шешељ",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Војислав Коштуница",
            "color": "#659933"
        })
        data.append({
            'slug': "",
            "name": "Борислав Пелевић",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Радослав Авлијаш",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Проф. Др Драгољуб Мићуновић",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Марјан Ристичевић",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Драган С. Томић",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Љиљана Аранђеловић",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Владан Батић",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Ивица Дачић",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Милован Дрецун",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Драган Ђорђевић",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Проф. Др Бранислав Бане Ивковић",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Мирко Јовић",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Јелисавета Карађорђевић",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Богољуб Карић",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Драган Маршићанин",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Зоран Милинковић",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Проф. Др Зоран Станковић",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Владан Глишић",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Проф. Др Зоран Драгишић",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Јадранка Шешељ",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Муамер Зукорлић",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Даница Грујичић",
            "color": "#852C62"
        })
        data.append({
            'slug': "boris-tadic",
            "name": "Борис Тадић",
            "color": "#78BAC2"
        })
        data.append({
            'slug': "",
            "name": "Демократска странка - Борис Тадић",
            "color": "#141A64"
        })
        data.append({
            'slug': "",
            "name": "ДЕМОКРАТСКА СТРАНКА СРБИЈЕ-ВОЈИСЛАВ КОШТУНИЦА",
            "color": "#ffffff"
        })
        data.append({
            'slug': "za-evropsku-srbiju-boris-tadic",
            "name": "ЗА ЕВРОПСКУ СРБИЈУ - БОРИС ТАДИЋ",
            "color": "#006837"
        })
        data.append({
            'slug': "srpska-radikalna-stranka-dr-vojislav-seselj",
            "name": "Српска радикална странка - др Војислав Шешељ",
            "color": "#ffffbf"
        })
        data.append({
            'slug': "srs",
            "name": "СРС",
            "color": "#003c30"
        })
        data.append({
            'slug': "dss",
            "name": "ДСС",
            "color": "#01665e"
        })
        data.append({
            'slug': "sda-sandzaka-dr-sulejman-ugljanin",
            "name": "СДА САНЏАКА - ДР СУЛЕЈМАН УГЉАНИН",
            "color": "green"
        })
        data.append({
            'slug': "ds",
            "name": "ДС",
            "color": "#35978f"
        })
        data.append({
            'slug': "spo-ns",
            "name": "СПО - НС",
            "color": "#c7eae5"
        })
        data.append({
            'slug': "da",
            "name": "ДА",
            "color": "#8c510a"
        })
        data.append({
            'slug': "sps",
            "name": "СПС",
            "color": "#dfc27d"
        })
        data.append({
            'slug': "g17-plus",
            "name": "Г17 плус",
            "color": "#80cdc1"
        })
        data.append({
            'slug': "zajedno-za-toleranciju",
            "name": "Заједно за толеранцију",
            "color": "#bf812d"
        })
        data.append({
            'slug': "za-narodno-jedinstvo",
            "name": "За народно јединство",
            "color": "#543005"
        })
        data.append({
            'slug': "otpor",
            "name": "Отпор",
            "color": "#003c30"
        })
        data.append({
            'slug': "demokratska-stranka-srbije-nova-srbija-vojislav-kostunica",
            "name": "Демократска странка Србије - Нова Србија - Војислав Коштуница",
            "color": "#66bd63"
        })
        data.append({
            'slug': "",
            "name": "БОШЊАЧКА ЛИСТА ЗА ЕВРОПСКИ САНЏАК - ДР СУЛЕЈМАН УГЉАНИН",
            "color": "#2D882D"
        })
        data.append({
            'slug': "samostalna-srbija",
            "name": "Самостална Србија",
            "color": "#01665e"
        })
        data.append({
            'slug': "sns",
            "name": "СНС",
            "color": "#35978f"
        })
        data.append({
            'slug': "liberali-srbije",
            "name": "Либерали Србије",
            "color": "#80cdc1"
        })

        data.append({
            'slug': 'odbrana-i-pravda',
            "name": "Одбрана и правда",
            "color": "#dfc27d"
        })
        data.append({
            'slug': 'privredna-snaga-srbije-i-dijaspora',
            "name": "Привредна снага Србије и дијаспора",
            "color": "#bf812d"
        })
        data.append({
            'slug': 'reformisti',
            "name": "Реформисти",
            "color": "#c7eae5"
        })
        data.append({
            'slug': "izbor-za-bolji-zivot-boris-tadic",
            "name": "Избор за бољи живот - Борис Тадић",
            "color": "#4575b4"
        })
        data.append({
            'slug': "laburist-partija-srbije",
            "name": "Лабурист. партија Србије",
            "color": "#8c510a"
        })
        data.append({
            'slug': "jul",
            "name": " ЈУЛ",
            "color": "#ACD270"
        })
        data.append({
            'slug': "savez-srba-vojvodine",
            "name": " Савез Срба Војводине",
            "color": "#4C691D"
        })
        data.append({
            'slug': "pokret-radnika-i-seljaka",
            "name": "Покрет радника и сељака",
            "color": "#f46d43"
        })
        data.append({
            'slug': "komunisticka-partija-josip-broz",
            "name": "Комунистичка партија - Јосип Броз",
            "color": "#d73027"
        })
        data.append({
            'slug': "ivica-dacic-socijalisticka-partija-srbije-sps-partija-ujedinjenih-penzionera-srbije-pups-jedinstvena-srbija-js",
            "name": 'Ивица Дачић - "Социјалистичка партија Србије (СПС), Партија уједињених пензионера Србије (ПУПС), Јединствена Србија (ЈС)"',
            "color": "#74add1"
        })
        data.append({
            'slug': "savez-vojodanskih-madara-istvan-pastor",
            "name": 'Савез војођанских Мађара - Иштван Пастор',
            "color": "#fdae61"
        })
        data.append({
            'slug': "stranka-demokratske-akcije-sandzaka-dr-sulejman-ugljanin",
            "name": 'Странка демократске акције Санџака - др Сулејман Угљанин',
            "color": "#a50026"
        })
        data.append({
            'slug': "demokratska-stranka-srbije-vojislav-kostunica",
            "name": 'Демократска странка Србије - Војислав Коштуница',
            "color": "#abd9e9"
        })

        data.append({
            'slug': "reformisticka-stranka-prof-dr-milan-visnjic",
            "name": 'Реформистичка странка - проф. др Милан Вишњић',
            "color": "#7EC1A3"
        })
        data.append({
            'slug': "crnogorska-partija-nenad-stevovic",
            "name": 'Црногорска партија - Ненад Стевовић',
            "color": "#003B20"
        })
        data.append({
            'slug': "socijaldemokratski-savez-nebojsa-lekovic",
            "name": 'Социјалдемократски савез - Небојша Лековић',
            "color": "#310CA6"
        })
        data.append({
            'slug': "sve-zajedno-bdz-gsm-dzh-dzvm-slovacka-stranka-emir-elfic",
            "name": 'Све заједно: БДЗ, ГСМ, ДЗХ, ДЗВМ, Словачка странка - Емир Елфић',
            "color": "#ACD270"
        })
        data.append({
            'slug': "nijedan-od-ponudenih-odgovora",
            "name": 'Ниједан од понуђених одговора',
            "color": "#4C691D"
        })
        data.append({
            'slug': "cedomir-jovanovic-preokret",
            "name": 'Чедомир Јовановић - Преокрет',
            "color": "#AC873D"
        })
        data.append({
            'slug': "dveri-za-zivot-srbije",
            "name": 'Двери за живот Србије',
            "color": "#fee090"
        })
        data.append({
            'slug': "dveri-za-zivot-srbije",
            "name": 'Двери за живот Србије',
            "color": "#4F4633"
        })
        data.append({
            'slug': "ivica-dacic-sps-js-dragan-markovic-palma",
            "name": 'ИВИЦА ДАЧИЋ - СПС, ЈС - Драган Марковић Палма',
            "color": "#4F4633"
        })
        # presidential canditates
        data.append({
            'slug': "demokratska-stranka-srbije-nova-srbija-dr-vojislav-kostunica",
            "name": 'Демократска странка Србије - Нова Србија - др Војислав Коштуница',
            "color": "#4F4633"
        })
        data.append({
            'slug': "vojislav-kostunica-dss",
            "name": 'Војислав Коштуница (ДСС)',
            "color": "#35978f"
        })
        data.append({
            'slug': "tomislav-nikolic",
            "name": 'Томислав Николић',
            "color": "#006837"
        })

        data.append({
            'slug': "demokratska-stranka-srbije-vojislav-kostinica",
            "name": 'ДЕМОКРАТСКА СТРАНКА СРБИЈЕ - ВОЈИСЛАВ КОШТИНИЦА',
            "color": "#d9f0d3"
        })
        data.append({
            'slug': "ivica-dacic-sps-pups-js",
            "name": 'ИВИЦА ДАЧИЋ - СПС, ПУПС, ЈС',
            "color": "#1b7837"
        })

        # 2002 presidential
        data.append({
            'slug': "dr-vojislav-seselj-srs",
            "name": 'др Војислав Шешељ (СРС)',
            "color": "#003c30"
        })
        data.append({
            'slug': "dr-miroljub-labus-gg",
            "name": 'др Мирољуб Лабус (ГГ)',
            "color": "#01665e"
        })
        data.append({
            'slug': "velimir-bata-zivojinovic-sps",
            "name": 'Велимир-Бата Живојиновић (СПС)',
            "color": "#80cdc1"
        })
        data.append({
            'slug': "borislav-pelevic-ssj",
            "name": 'Борислав Пелевић (ССЈ)',
            "color": "#c7eae5"
        })

        data.append({
            'slug': "prof-borislav-pelevic-ssj",
            "name": 'проф. Борислав Пелевић (ССЈ)',
            "color": "#c7eae5"
        })
        data.append({
            'slug': "nebojsa-pavkovic-gg",
            "name": 'Небојша Павковић (ГГ)',
            "color": "#f6e8c3"
        })
        data.append({
            'slug': "prof-dr-branislav-bane-ivkovic-gg",
            "name": 'проф. др Бранислав-Бане Ивковић (ГГ)',
            "color": "#dfc27d"
        })
        data.append({
            'slug': "dr-tomislav-lalosevic-gg",
            "name": 'др Томислав Лалошевић (ГГ)',
            "color": "#bf812d"
        })
        data.append({
            'slug': "dr-vuk-obradovic-sd",
            "name": 'др Вук Обрадовић (СД)',
            "color": "#8c510a"
        })
        data.append({
            'slug': "dr-dragan-radenovic-gg",
            "name": 'др Драган Раденовић (ГГ)',
            "color": "#543005"
        })
        # 2003 presidential
        data.append({
            'slug': "tomislav-nikolic-srs",
            "name": 'Томислав Николић (СРС)',
            "color": "#253494"
        })
        data.append({
            'slug': "prof-dr-dragoljub-micunovic-dos",
            "name": 'Проф. др Драгољуб Мићуновић (ДОС)',
            "color": "#2c7fb8"
        })
        data.append({
            'slug': "velimir-ilic-ns",
            "name": 'Велимир Илић (НС)',
            "color": "#41b6c4"
        })
        data.append({
            'slug': "marijan-risticevic-nss",
            "name": 'Маријан Ристичевић (НСС)',
            "color": "#7fcdbb"
        })
        data.append({
            'slug': "dragan-s-tomic-sns",
            "name": 'Драган С. Томић (СНС)',
            "color": "#c7e9b4"
        })
        data.append({
            'slug': "radoslav-avlijas-dso",
            "name": 'Радослав Авлијаш (ДСО)',
            "color": "#ffffcc"
        })
        data.append({
            'slug': "socijalisticka-partija-srbije-partija-ujedinjenih-penzionera-srbije-jedinstvena-srbija",
            "name": 'Социјалистичка партија Србије - Партија уједињених пензионера Србије - Јединствена Србија',
            "color": "#a6d96a"
        })
        data.append({
            'slug': "liberalno-demokratska-partija-cedomir-jovanovic",
            "name": 'ЛИБЕРАЛНО ДЕМОКРАТСКА ПАРТИЈА - ЧЕДОМИР ЈОВАНОВИЋ',
            "color": "#d9ef8b"
        })
        data.append({
            'slug': "madarska-koalicija-istvan-pastor",
            "name": 'МАЂАРСКА КОАЛИЦИЈА - ИШТВАН ПАСТОР',
            "color": "#ffffbf"
        })
        data.append({
            'slug': "bosnjacka-lista-za-evropski-sandzak-dr-sulejman-ugljanin",
            "name": 'БОШЊАЧКА ЛИСТА ЗА ЕВРОПСКИ САНЏАК - ДР СУЛЕЈМАН УГЉАНИН',
            "color": "#fdae61"
        })
        data.append({
            'slug': "pokret-snaga-srbije-bogoljub-karic",
            "name": 'Покрет СНАГА СРБИЈЕ - Богољуб Карић',
            "color": "#f46d43"
        })

        data.append({
            'slug': "koalicija-albanaca-presevske-doline",
            "name": 'КОАЛИЦИЈА АЛБАНАЦА ПРЕШЕВСКЕ ДОЛИНЕ',
            "color": "#f46d43"
        })
        data.append({
            'slug': "pokrenimo-srbiju-tomislav-nikolic",
            "name": 'Покренимо Србију - Томислав Николић',
            "color": "#313695"
        })
        if kandidat_name is not None:
            jsondata = {}
            selected_color = ""
            for name in data:
                if kandidat_name == name['name']:
                    jsondata = {'color': name['color'], 'slug': name['slug'], 'name': name['name']}

            return jsondata
        else:
            print "not none"
            return data

    def import_data(self, election_type, year, month=None, rnd=None):
        if election_type == 'parlamentarni' and int(year) == 2016:
            self.import_data_parliament_2016()
        elif election_type == 'parlamentarni' and int(year) == 2008:
            self.import_data_parliament_2008()
        elif election_type == 'parlamentarni' and int(year) == 2007:
            self.import_data_parliament_2007()
        else:
            self.import_data_rest(election_type, year, month, rnd)

    def import_data_parliament_2007(self):
        election_type = 'parlamentarni'
        year = 2007
        self.prep_import(election_type, year, None, None)
        file_path = self.get_data_file_path(election_type, year, None, None)

        row_count = 0
        docs = []
        candidates_or_parties = {}
        parent_territory = ''

        with open(file_path, 'rb') as f:
            reader = csv.reader(f)

            for row in tqdm(reader):
                doc = {}

                # Get all the candidates/parties
                if row_count == 0:
                    for i in range(12, len(row)):
                        candidates_or_parties[str(i)] = row[i].replace('\n', '')
                else:
                    territory = row[2].strip()
                    territory_slug = slugify(cyrtranslit.to_latin(territory, 'sr'), to_lower=True)
                    polling_station_num = int(row[3].strip())
                    polling_station_address = row[4].strip()
                    ballots_received_count = int(row[5].strip())
                    unused_ballots_count = int(row[6].strip())
                    number_of_voters_registered=int(row[7].strip())
                    voters_who_voted_count = int(row[8].strip())
                    ballots_in_ballot_box_count = int(row[9].strip())
                    invalid_ballots_count = int(row[10].strip())
                    valid_ballots_count = int(row[11].strip())


                    doc['brojPrimljeniGlasackiListica'] = ballots_received_count
                    doc['brojNeupotrebljenihGlasackiListica']=unused_ballots_count
                    doc['brojUpisanihBiracaUBirackiSpisak'] = number_of_voters_registered
                    doc['nevazeciGlasackiListici']= invalid_ballots_count
                    doc['biraciKojiSuGlasali'] = {}
                    doc['biraciKojiSuGlasali']['broj'] = voters_who_voted_count
                    # doc['biraciKojiSuGlasali']['udeo'] = voters_who_voted_percent
                    doc['brojGlasackihListicaUKutiji'] = {}
                    doc['brojGlasackihListicaUKutiji']['broj'] = ballots_in_ballot_box_count
                    doc['vazeciGlasackiListici'] = {}
                    doc['vazeciGlasackiListici']['broj'] = valid_ballots_count

                    doc['izbori'] = cyrtranslit.to_cyrillic(election_type.title(), 'sr')
                    doc['godina'] = int(year)
                    # Some rows consist of territory grouping.
                    # We need to track those.
                    if cyrtranslit.to_latin(territory, 'sr').isupper():
                        doc['instanca'] = 1

                    elif 'okrug' in territory_slug \
                            or territory_slug in ['grad-beograd', 'inostranstvo'] \
                            or territory_slug == 'zavodi-za-izvrsenje-zavodskih-sankcija' and polling_station_num is '':
                        doc['instanca'] = 2
                        parent_territory = territory

                    elif polling_station_num is '':
                        doc['instanca'] = 3
                        doc['parentTeritorija'] = parent_territory
                        doc['parentTeritorijaSlug'] = slugify(cyrtranslit.to_latin(parent_territory, 'sr'),
                                                              to_lower=True)

                    elif polling_station_num is not '':
                        doc['instanca'] = 4
                        doc['parentTeritorija'] = parent_territory
                        doc['parentTeritorijaSlug'] = slugify(cyrtranslit.to_latin(parent_territory, 'sr'),
                                                              to_lower=True)
                        doc['brojBirackogMesta'] = polling_station_num
                        doc['adresaBirackogMesta'] = polling_station_address
                    total_votes=0
                    udeo=0
                    for j in range(12, len(row)):
                        doc['rezultat'] = {}
                        doc['rezultat']['glasova'] = int(row[j])
                        if int(row[j]) != 0:
                            total_votes += int(row[j])
                            udeo = (float(int(row[j])) / voters_who_voted_count) * 100

                        else:
                            udeo = 0.0
                        doc['rezultat']['udeo'] = udeo
                        doc['teritorija'] = territory
                        doc['teritorijaSlug'] = territory_slug
                        doc['izbori'] = cyrtranslit.to_cyrillic(election_type.title(), 'sr')
                        doc['godina'] = int(year)

                        doc['izbornaLista'] = candidates_or_parties[str(j)]
                        ime = candidates_or_parties[str(j)]
                        boja = self.get_political_parties(ime)

                        if not boja:
                            print "empty"
                        else:
                            print boja['color']
                            doc['boja'] = boja['color']
                        doc['izbornaListaSlug'] = slugify(cyrtranslit.to_latin(candidates_or_parties[str(j)], 'sr'),
                                                          to_lower=True)

                        # print "%s - %s - %s" % (row_count + 1, doc['rezultat']['glasova'], doc['izbornaLista'])
                        docs.append(doc.copy())

                        if len(docs) % 1000 == 0:
                            db[collection].insert(docs)
                            docs = []

                row_count += 1

        # Insert remaining documents
        if len(docs) > 0:
            db[collection].insert(docs)

    def import_data_parliament_2008(self):
        election_type = 'parlamentarni'
        year = 2008
        self.prep_import(election_type, year, None, None)
        file_path = self.get_data_file_path(election_type, year, None, None)

        row_count = 0
        docs = []
        candidates_or_parties = {}
        parent_territory = ''

        with open(file_path, 'rb') as f:
            reader = csv.reader(f)

            for row in tqdm(reader):
                doc = {}

                # Get all the candidates/parties
                if row_count == 0:
                    for i in xrange(10, len(row)):
                        candidates_or_parties[str(i)] = row[i].replace('\n', '').strip()


                elif row_count == 1:
                    pass

                else:
                    territory = row[0].strip()
                    territory_slug = slugify(cyrtranslit.to_latin(territory, 'sr'), to_lower=True)
                    polling_station_num = int(row[1].strip()) if row[1].strip() is not '' else row[1].strip()
                    polling_station_address = row[2].strip()
                    ballots_received_count = int(row[3].strip())
                    unused_ballots_count = int(row[4].strip())
                    number_of_voters_registered=int(row[5].strip())
                    ballots_in_ballot_box_count = int(row[6].strip())
                    invalid_ballots_count = int(row[7].strip())
                    valid_ballots_count = int(row[8].strip())
                    voters_who_voted_count=int(row[9].strip())

                    doc['brojPrimljeniGlasackiListica'] = ballots_received_count
                    doc['brojNeupotrebljenihGlasackiListica']=unused_ballots_count
                    doc['brojUpisanihBiracaUBirackiSpisak'] = number_of_voters_registered
                    doc['nevazeciGlasackiListici']= invalid_ballots_count
                    doc['biraciKojiSuGlasali'] = {}
                    doc['biraciKojiSuGlasali']['broj'] = voters_who_voted_count
                    # doc['biraciKojiSuGlasali']['udeo'] = voters_who_voted_percent
                    doc['brojGlasackihListicaUKutiji'] = {}
                    doc['brojGlasackihListicaUKutiji']['broj'] = ballots_in_ballot_box_count
                    doc['vazeciGlasackiListici'] = {}
                    doc['vazeciGlasackiListici']['broj'] = valid_ballots_count

                    doc['izbori'] = cyrtranslit.to_cyrillic(election_type.title(), 'sr')
                    doc['godina'] = int(year)
                    # Some rows consist of territory grouping.
                    # We need to track those.
                    if cyrtranslit.to_latin(territory, 'sr').isupper():
                        doc['instanca'] = 1

                    elif 'okrug' in territory_slug \
                            or territory_slug in ['grad-beograd', 'inostranstvo'] \
                            or territory_slug == 'zavodi-za-izvrsenje-zavodskih-sankcija' and polling_station_num is '':
                        doc['instanca'] = 2
                        parent_territory = territory

                    elif polling_station_num is '':
                        doc['instanca'] = 3
                        doc['parentTeritorija'] = parent_territory
                        doc['parentTeritorijaSlug'] = slugify(cyrtranslit.to_latin(parent_territory, 'sr'),
                                                              to_lower=True)

                    elif polling_station_num is not '':
                        doc['instanca'] = 4
                        doc['parentTeritorija'] = parent_territory
                        doc['parentTeritorijaSlug'] = slugify(cyrtranslit.to_latin(parent_territory, 'sr'),
                                                              to_lower=True)
                        doc['brojBirackogMesta'] = polling_station_num
                        doc['adresaBirackogMesta'] = polling_station_address
                    total_votes=0
                    udeo=0
                    for j in range(10, len(row)):
                        doc['rezultat'] = {}
                        doc['rezultat']['glasova'] = int(row[j])

                        if int(row[j]) != 0:
                            total_votes += int(row[j])
                            udeo = (float(int(row[j])) / voters_who_voted_count) * 100

                        else:
                            udeo = 0.0
                        doc['rezultat']['udeo'] = udeo
                        doc['teritorija'] = territory
                        doc['teritorijaSlug'] = territory_slug
                        doc['izbori'] = cyrtranslit.to_cyrillic(election_type.title(), 'sr')
                        doc['godina'] = int(year)

                        doc['izbornaLista'] = candidates_or_parties[str(j)]
                        ime = candidates_or_parties[str(j)]
                        boja = self.get_political_parties(ime)

                        if not boja:
                            print "empty"
                        else:
                            print boja['color']
                            doc['boja']=boja['color']
                        doc['izbornaListaSlug'] = slugify(cyrtranslit.to_latin(candidates_or_parties[str(j)], 'sr'),
                                                          to_lower=True)

                        # print "%s - %s - %s" % (row_count + 1, doc['rezultat']['glasova'], doc['izbornaLista'])
                        docs.append(doc.copy())

                        if len(docs) % 1000 == 0:
                            db[collection].insert(docs)
                            docs = []

                row_count += 1

        # Insert remaining documents
        if len(docs) > 0:
            db[collection].insert(docs)


    def import_data_parliament_2016(self):
        election_type = 'parlamentarni'
        year = 2016
        self.prep_import(election_type, year, None, None)
        file_path = self.get_data_file_path(election_type, year, None, None)
        row_count = 0
        docs = []
        candidates_or_parties = {}
        with open(file_path, 'rb') as f:
            reader = csv.reader(f)

            for row in tqdm(reader):
                doc = {}

                # Get all the candidates/parties
                if row_count == 0:
                    for i in range(14, len(row)):
                        candidates_or_parties[str(i)] = row[i].replace('\n', '')

                elif row[7].strip() is not '':  # FIXME: we do this because row 8,350 is blank.
                    parent_territory = row[1].strip()
                    parent_territory_slug = slugify(cyrtranslit.to_latin(parent_territory, 'sr'), to_lower=True)

                    territory = row[3].strip()
                    territory_slug = slugify(cyrtranslit.to_latin(territory, 'sr'), to_lower=True)

                    polling_station_num = int(row[4].strip())
                    polling_station_address = row[5].strip()
                    coordinates = row[6].strip().split(',')

                    registered_voters_count = int(row[7].strip())
                    ballots_received_count = int(row[8].strip())
                    unused_ballots_count = int(row[9].strip())

                    voters_who_voted_count = int(row[10].strip())
                    # voters_who_voted_percent = None

                    ballots_in_ballot_box_count = int(row[11].strip())

                    invalid_ballots_count = int(row[12].strip())
                    # invalid_ballots_percent = None

                    valid_ballots_count = int(row[13].strip())
                    # valid_ballots_percent = None

                    # Set election type and year
                    doc['izbori'] = cyrtranslit.to_cyrillic(election_type.title(), 'sr')
                    doc['godina'] = int(year)

                    # Set generic location values
                    doc['teritorija'] = territory
                    doc['teritorijaSlug'] = territory_slug

                    doc['parentTeritorija'] = parent_territory
                    doc['parentTeritorijaSlug'] = parent_territory_slug

                    doc['brojBirackogMesta'] = polling_station_num
                    doc['adresaBirackogMesta'] = polling_station_address

                    # FIXME: at least one coordinate is missing (row 1481)
                    if len(coordinates) == 2:
                        doc['koordinateBirackomMestu'] = {}
                        doc['koordinateBirackomMestu']['latituda'] = float(coordinates[0].strip())
                        doc['koordinateBirackomMestu']['longituda'] = float(coordinates[1].strip())

                    # Set generic ballot values
                    doc['brojUpisanihBiracaUBirackiSpisak'] = registered_voters_count

                    doc['biraciKojiSuGlasali'] = {}
                    doc['biraciKojiSuGlasali']['broj'] = voters_who_voted_count
                    # doc['biraciKojiSuGlasali']['udeo'] = voters_who_voted_percent

                    doc['brojPrimljenihGlasackihListica'] = ballots_received_count
                    doc['brojNeupoTrebljenihGlasackihListica'] = unused_ballots_count
                    doc['brojGlasackihListicaUKutiji'] = ballots_in_ballot_box_count

                    doc['brojGlasackihListicaUKutiji'] = {}
                    doc['brojGlasackihListicaUKutiji']['broj'] = invalid_ballots_count
                    # doc['brojGlasackihListicaUKutiji']['udeo'] = invalid_ballots_percent

                    doc['vazeciGlasackiListici'] = {}
                    doc['vazeciGlasackiListici']['broj'] = valid_ballots_count
                    # doc['vazeciGlasackiListici']['udeo'] = valid_ballots_percent

                    # For this year, we don't have grouped territories we are importing.
                    # So every document is at the smallest unit of territory
                    doc['instanca'] = 4

                    # print '---------'
                    total_votes=0
                    udeo=0
                    for j in range(14, len(row)):
                        doc['rezultat'] = {}
                        doc['rezultat']['glasova'] = int(row[j])
                        if int(row[j]) != 0:
                            total_votes += int(row[j])
                            udeo = (float(int(row[j])) / voters_who_voted_count) * 100

                        else:
                            udeo = 0.0
                        doc['rezultat']['udeo'] = udeo

                        doc['izbornaLista'] = candidates_or_parties[str(j)]
                        ime = candidates_or_parties[str(j)]
                        boja = self.get_political_parties(ime)

                        if not boja:
                            print "empty"
                        else:
                            print boja['color']
                            doc['boja'] = boja['color']
                        doc['izbornaListaSlug'] = slugify(cyrtranslit.to_latin(candidates_or_parties[str(j)], 'sr'),
                                                          to_lower=True)

                        # print "%s - %s - %s" % (row_count + 1, doc['rezultat']['glasova'], doc['izbornaLista'])
                        docs.append(doc.copy())

                        if len(docs) % 1000 == 0:
                            db[collection].insert(docs)
                            docs = []

                row_count += 1

        # Insert remaining documents
        if len(docs) > 0:
            db[collection].insert(docs)

    def import_data_rest(self, election_type, year, month=None, rnd=None):

        self.prep_import(election_type, year, month, rnd)

        file_path = self.get_data_file_path(election_type, year, month, rnd)

        row_count = 0
        docs = []
        candidates_or_parties = {}
        parent_territory = ''

        with open(file_path, 'rb') as f:
            reader = csv.reader(f)

            for row in tqdm(reader):
                doc = {}

                # Get all the candidates/parties
                if row_count == 0:
                    if int(year) == 2004 and election_type == "predsjednicki":
                        for i in xrange(11, len(row)):
                            candidates_or_parties[str(i)] = row[i].replace('\n', '').strip()

                    if int(year) == 2008 and election_type == "predsjednicki":
                        for i in xrange(8, len(row)):
                            candidates_or_parties[str(i)] = row[i].replace('\n', '').strip()

                    if int(year) == 2003 and election_type in ["predsjednicki", "parlamentarni"]:
                        for i in xrange(6, len(row)):
                            candidates_or_parties[str(i)] = row[i].replace('\n', '').strip()
                    elif int(year) == 2002 and election_type == "predsjednicki":
                        for i in xrange(7, len(row)):
                            candidates_or_parties[str(i)] = row[i].replace('\n', '').strip()
                    else:
                        for i in xrange(13, len(row), 2):
                            candidates_or_parties[str(i)] = row[i].replace('\n', '').strip()

                elif row_count == 1:
                    pass

                else:

                    if int(year)==2004 and election_type=="predsjednicki":
                        territory = row[1].strip()
                        territory_slug = slugify(cyrtranslit.to_latin(territory, 'sr'), to_lower=True)
                        polling_station_num = int(row[2].strip())
                        polling_station_address = row[3].strip()
                        ballots_received_count = int(row[4].strip())
                        unused_ballots_count = int(row[5].strip())
                        registered_voters_count = int(row[6].strip())
                        voters_who_voted_count = int(row[8].strip())
                        invalid_ballots_count = int(row[9].strip())
                        valid_ballots_count = int(row[10].strip())
                        print row_count

                    else:
                        print row_count
                        territory = row[0].strip()
                        territory_slug = slugify(cyrtranslit.to_latin(territory, 'sr'), to_lower=True)
                        polling_station_num = int(row[1].strip()) if row[1].strip() is not '' else row[1].strip()
                        polling_station_address = row[2].strip()

                        registered_voters_count = int(row[3].strip())

                    if int(year) == 2012 and election_type == "predsjednicki":
                        ballots_received_count = int(row[6].strip())
                        unused_ballots_count = int(row[7].strip())
                        voters_who_voted_count = int(row[8].strip())
                        invalid_ballots_count = int(row[9].strip())
                        invalid_ballots_percent = float(row[10].strip())
                        valid_ballots_count = int(row[11].strip())
                        valid_ballots_percent = float(row[12].strip())

                    if int(year) == 2012 and election_type == "parlamentarni":
                        voters_who_voted_count = int(row[4].strip())
                        voters_who_voted_percent = float(row[5].strip())
                        ballots_received_count = int(row[6].strip())
                        unused_ballots_count = int(row[7].strip())
                        ballots_in_ballot_box_count=int(row[8].strip())
                        invalid_ballots_count = int(row[9].strip())
                        invalid_ballots_percent = float(row[10].strip())
                        valid_ballots_count = int(row[11].strip())
                        valid_ballots_percent = float(row[12].strip())


                    if int(year)==2008 and election_type=="predsjednicki":
                        voters_who_voted_count = int(row[6].strip())
                        voters_who_voted_percent=float(row[7].strip())
                    if int(year) not in [2008, 2012]  and election_type != "predsjednicki":
                        voters_who_voted_count = int(row[4].strip())

                    if int(year) == 2003 and election_type in["predsjednicki","parlamentarni"]:
                        voters_who_voted_count = int(row[4].strip())
                        total_voter_turn_out = float(row[5].strip())



                    if int(year) == 2002 and election_type == "predsjednicki":
                        print row_count
                        voters_who_voted_count = int(row[4].strip())
                        total_voter_turn_out = float(row[5].strip())


                    if int(year) not in [2002, 2003,2004] and election_type not in ["predsjednicki", "parlamentarni"]:
                        voters_who_voted_percent = float(row[5].strip())
                        ballots_received_count = int(row[6].strip())
                        unused_ballots_count = int(row[7].strip())
                        ballots_in_ballot_box_count = int(row[8].strip())
                        invalid_ballots_count = int(row[9].strip())
                        invalid_ballots_percent = float(row[10].strip())
                        valid_ballots_count = int(row[11].strip())
                        valid_ballots_percent = float(row[12].strip())


                    doc['brojUpisanihBiracaUBirackiSpisak'] = registered_voters_count
                    doc['biraciKojiSuGlasali'] = {}

                    doc['biraciKojiSuGlasali']['broj'] = voters_who_voted_count

                    if int(year) in [2002, 2003] and election_type in ["predsjednicki", "parlamentarni"]:
                        doc['odzivBiraca']=total_voter_turn_out

                    if int(year) not in [2002, 2003] and election_type not in ["predsjednicki", "parlamentarni"]:
                        doc['biraciKojiSuGlasali']['udeo'] = voters_who_voted_percent
                        doc['brojPrimljenihGlasackihListica'] = ballots_received_count
                        doc['brojNeupoTrebljenihGlasackihListica'] = unused_ballots_count
                        if int(year) not in [2012, 2004] and election_type!="predsjednicki":
                            doc['brojGlasackihListicaUKutiji'] = ballots_in_ballot_box_count
                        doc['brojGlasackihListicaUKutiji'] = {}
                        doc['brojGlasackihListicaUKutiji']['broj'] = invalid_ballots_count
                        if int(year)!=2004 and election_type!="predsjednicki":
                            doc['brojGlasackihListicaUKutiji']['udeo'] = invalid_ballots_percent
                        doc['vazeciGlasackiListici'] = {}
                        doc['vazeciGlasackiListici']['broj'] = valid_ballots_count
                        if int(year) != 2004 and election_type != "predsjednicki":
                            doc['vazeciGlasackiListici']['udeo'] = valid_ballots_percent
                    # Some rows consist of territory grouping.
                    # We need to track those.
                    if cyrtranslit.to_latin(territory, 'sr').isupper():
                        doc['instanca'] = 1

                    elif 'okrug' in territory_slug\
                            or territory_slug in ['grad-beograd', 'inostranstvo']\
                            or territory_slug == 'zavodi-za-izvrsenje-zavodskih-sankcija' and polling_station_num is '':
                        doc['instanca'] = 2
                        parent_territory = territory

                    elif polling_station_num is '':
                        doc['instanca'] = 3
                        doc['parentTeritorija'] = parent_territory
                        doc['parentTeritorijaSlug'] = slugify(cyrtranslit.to_latin(parent_territory, 'sr'), to_lower=True)

                    elif polling_station_num is not '':
                        doc['instanca'] = 4
                        doc['parentTeritorija'] = parent_territory
                        doc['parentTeritorijaSlug'] = slugify(cyrtranslit.to_latin(parent_territory, 'sr'), to_lower=True)
                        doc['brojBirackogMesta'] = polling_station_num
                        doc['adresaBirackogMesta'] = polling_station_address

                    if int(year)==2003 and election_type in ["parlamentarni"]:
                        total_votes=0
                        udeo=0
                        for j in xrange(6, len(row)):
                            doc['teritorija'] = territory
                            doc['teritorijaSlug'] = territory_slug
                            doc['izbori'] = cyrtranslit.to_cyrillic(election_type.title(), 'sr')
                            doc['godina'] = int(year)

                            doc['rezultat'] = {}
                            doc['rezultat']['glasova'] = int(row[j])


                            if int(row[j]) != 0:
                                total_votes += int(row[j])
                                udeo = (float(int(row[j])) / voters_who_voted_count) * 100

                            else:
                                udeo = 0.0

                            doc['rezultat']['udeo'] =udeo
                            doc['izbornaLista'] = candidates_or_parties[str(j)]
                            ime = candidates_or_parties[str(j)]
                            boja = self.get_political_parties(ime)
                            if not boja:
                                print "empty"
                            else:
                                print boja['color']
                                doc['boja'] = boja['color']
                            doc['izbornaListaSlug'] = slugify(cyrtranslit.to_latin(candidates_or_parties[str(j)], 'sr'), to_lower=True)

                            '''
                            if 'parentTerritory' in doc:
                                print '%s - %s - %s - %s' % (row_count+1, doc['instanca'], doc['teritorija'], doc['parentTerritory'])
                            else:
                                print '%s - %s - %s' % (row_count + 1, doc['instanca'], doc['teritorija'])
                            '''

                            docs.append(doc.copy())

                            if len(docs) % 1000 == 0:
                                db[collection].insert(docs)
                                docs = []
                    elif int(year) == 2002 and election_type == "predsjednicki":
                        total_votes=0
                        udeo=0
                        for j in xrange(7, len(row)):
                            doc['teritorija'] = territory
                            doc['teritorijaSlug'] = territory_slug
                            doc['izbori'] = cyrtranslit.to_cyrillic(election_type.title(), 'sr')
                            doc['godina'] = int(year)

                            doc['rezultat'] = {}


                            doc['rezultat']['glasova'] = int(row[j])
                            if int(row[j]) != 0:
                                print int(row[j])
                                total_votes += int(row[j])
                                udeo = (float(int(row[j])) / voters_who_voted_count) * 100

                            else:
                                udeo = 0.0
                            doc['rezultat']['udeo'] = udeo
                            # Set remaining values depending on whether is is a presidential or parliamentary election

                            month_cyr = cyrtranslit.to_cyrillic(month.title(), 'sr')
                            rnd_cyr = cyrtranslit.to_cyrillic(rnd.title(), 'sr')

                            doc['mesec'] = month_cyr
                            doc['krug'] = rnd_cyr
                            doc['kandidat'] = candidates_or_parties[str(j)].title()
                            ime = candidates_or_parties[str(j)]
                            boja = self.get_political_parties(ime)
                            if not boja:
                                print "empty"
                            else:
                                print boja['color']
                                doc['boja'] = boja['color']
                            doc['kandidatSlug'] = slugify(cyrtranslit.to_latin(candidates_or_parties[str(j)], 'sr'),
                                                              to_lower=True)

                            '''
                            if 'parentTerritory' in doc:
                                print '%s - %s - %s - %s' % (row_count+1, doc['instanca'], doc['teritorija'], doc['parentTerritory'])
                            else:
                                print '%s - %s - %s' % (row_count + 1, doc['instanca'], doc['teritorija'])
                            '''

                            docs.append(doc.copy())

                            if len(docs) % 1000 == 0:
                                db[collection].insert(docs)
                                docs = []
                    elif int(year) == 2003 and election_type == "predsjednicki":
                        total_votes=0
                        udeo=0
                        for j in xrange(6, len(row)):
                            doc['teritorija'] = territory
                            doc['teritorijaSlug'] = territory_slug
                            doc['izbori'] = cyrtranslit.to_cyrillic(election_type.title(), 'sr')
                            doc['godina'] = int(year)

                            doc['rezultat'] = {}


                            doc['rezultat']['glasova'] = int(row[j])
                            if int(row[j]) != 0:
                                print int(row[j])
                                total_votes += int(row[j])
                                udeo = (float(int(row[j])) / voters_who_voted_count) * 100

                            else:
                                udeo = 0.0
                            doc['rezultat']['udeo'] = udeo
                            # Set remaining values depending on whether is is a presidential or parliamentary election

                            month_cyr = cyrtranslit.to_cyrillic(month.title(), 'sr')
                            rnd_cyr = cyrtranslit.to_cyrillic(rnd.title(), 'sr')

                            doc['mesec'] = month_cyr
                            doc['krug'] = rnd_cyr
                            doc['kandidat'] = candidates_or_parties[str(j)].title()
                            ime = candidates_or_parties[str(j)]
                            boja = self.get_political_parties(ime)

                            if not boja:
                                print "empty"
                            else:
                                print boja['color']
                                doc['boja'] = boja['color']
                            doc['kandidatSlug'] = slugify(cyrtranslit.to_latin(candidates_or_parties[str(j)], 'sr'),
                                                              to_lower=True)

                            '''
                            if 'parentTerritory' in doc:
                                print '%s - %s - %s - %s' % (row_count+1, doc['instanca'], doc['teritorija'], doc['parentTerritory'])
                            else:
                                print '%s - %s - %s' % (row_count + 1, doc['instanca'], doc['teritorija'])
                            '''

                            docs.append(doc.copy())

                            if len(docs) % 1000 == 0:
                                db[collection].insert(docs)
                                docs = []

                    elif int(year) == 2004 and election_type == "predsjednicki":
                        total_votes=0
                        udeo=0
                        for j in xrange(11, len(row)):
                            doc['teritorija'] = territory
                            doc['teritorijaSlug'] = territory_slug
                            doc['izbori'] = cyrtranslit.to_cyrillic(election_type.title(), 'sr')
                            doc['godina'] = int(year)

                            doc['rezultat'] = {}

                            doc['rezultat']['glasova'] = int(row[j])
                            if int(row[j]) != 0:
                                total_votes += int(row[j])
                                udeo = (float(int(row[j])) / voters_who_voted_count) * 100
                                print udeo
                            else:
                                udeo = 0.0
                            doc['rezultat']['udeo'] = udeo
                            # Set remaining values depending on whether is is a presidential or parliamentary election

                            month_cyr = cyrtranslit.to_cyrillic(month.title(), 'sr')
                            rnd_cyr = cyrtranslit.to_cyrillic(rnd.title(), 'sr')

                            doc['mesec'] = month_cyr
                            doc['krug'] = rnd_cyr
                            doc['kandidat'] = candidates_or_parties[str(j)].title()
                            ime = candidates_or_parties[str(j)]
                            boja = self.get_political_parties(ime)

                            if not boja:
                                print "empty"
                            else:
                                print boja['color']
                                doc['boja'] = boja['color']
                            doc['kandidatSlug'] = slugify(cyrtranslit.to_latin(candidates_or_parties[str(j)], 'sr'),
                                                          to_lower=True)

                            '''
                            if 'parentTerritory' in doc:
                                print '%s - %s - %s - %s' % (row_count+1, doc['instanca'], doc['teritorija'], doc['parentTerritory'])
                            else:
                                print '%s - %s - %s' % (row_count + 1, doc['instanca'], doc['teritorija'])
                            '''

                            docs.append(doc.copy())

                            if len(docs) % 1000 == 0:
                                db[collection].insert(docs)
                                docs = []

                    else:
                        total_votes=0
                        udeo=0
                        for j in xrange(13, len(row), 2):
                            # Set generic values
                            doc['teritorija'] = territory
                            doc['teritorijaSlug'] = territory_slug
                            doc['izbori'] = cyrtranslit.to_cyrillic(election_type.title(), 'sr')
                            doc['godina'] = int(year)

                            doc['rezultat'] = {}
                            doc['rezultat']['glasova'] = int(row[j])
                            if int(row[j]) != 0:
                                total_votes += int(row[j])
                                udeo = (float(int(row[j])) / voters_who_voted_count) * 100
                                print udeo
                            else:
                                udeo = 0.0
                            doc['rezultat']['udeo'] = udeo
                            # Set remaining values depending on whether is is a presidential or parliamentary election
                            if election_type == 'predsjednicki':
                                month_cyr = cyrtranslit.to_cyrillic(month.title(), 'sr')
                                rnd_cyr = cyrtranslit.to_cyrillic(rnd.title(), 'sr')

                                doc['mesec'] = month_cyr
                                doc['krug'] = rnd_cyr
                                doc['kandidat'] = candidates_or_parties[str(j)].title()
                                ime = candidates_or_parties[str(j)]
                                boja = self.get_political_parties(ime)

                                if not boja:
                                    print "empty"
                                else:
                                    print boja['color']
                                    doc['boja'] = boja['color']
                                doc['kandidatSlug'] = slugify(cyrtranslit.to_latin(candidates_or_parties[str(j)], 'sr'), to_lower=True)

                            else:
                                ime = candidates_or_parties[str(j)]
                                boja = self.get_political_parties(ime)

                                if not boja:
                                    print "empty"
                                else:
                                    print boja['color']
                                    doc['boja'] = boja['color']
                                doc['izbornaLista'] = candidates_or_parties[str(j)]
                                doc['izbornaListaSlug'] = slugify(cyrtranslit.to_latin(candidates_or_parties[str(j)], 'sr'), to_lower=True)

                            '''
                            if 'parentTerritory' in doc:
                                print '%s - %s - %s - %s' % (row_count+1, doc['instanca'], doc['teritorija'], doc['parentTerritory'])
                            else:
                                print '%s - %s - %s' % (row_count + 1, doc['instanca'], doc['teritorija'])
                            '''

                            docs.append(doc.copy())

                            if len(docs) % 1000 == 0:
                                db[collection].insert(docs)
                                docs = []

                row_count += 1

        # Insert remaining documents
        if len(docs) > 0:
            db[collection].insert(docs)


    def prep_import(self, election_type, year, month=None, rnd=None):
        if election_type == 'predsjednicki':
            print '\nRemoving previously imported data for %s %s %s %s...' % (election_type, year, month, rnd)
            db[collection].remove({
                'izbori': cyrtranslit.to_cyrillic(election_type.title(), 'sr'),
                'godina': int(year),
                'mesec': cyrtranslit.to_cyrillic(month.title(), 'sr'),
                'krug': cyrtranslit.to_cyrillic(rnd.title(), 'sr')
            })

            print 'Importing data for %s %s %s %s...' % (election_type, year, month, rnd)

        else:
            print '\nRemoving previously imported data for %s %s...' % (election_type, year)
            db[collection].remove({
                'izbori': cyrtranslit.to_cyrillic(election_type.title(), 'sr'),
                'godina': int(year)
            })

            print 'Importing data for %s %s...' % (election_type, year)

    def get_data_file_path(self, election_type, year, month=None, rnd=None):
        if election_type == 'predsjednicki':
            return "data/izbori2/%s/%s-%s-%s.csv" % (election_type, year, month, rnd)
        else:
            return "data/izbori2/%s/%s.csv" % (election_type, year)
