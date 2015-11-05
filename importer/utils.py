# coding=utf-8

class ImporterUtils():

    def __init__(self):
        pass

    @staticmethod
    def parent_categories_for_vranje():
        valjevo_parents = {
            "41": "РАСХОДИ ЗА ЗАПОСЛЕНЕ",
            "42": "КОРИШЋЕЊЕ РОБА И УСЛУГА",
            "44": "НЕГ. КУРС.РАЗЛИКЕ",
            "45": "СУБВЕНЦИЈЕ",
            "46": "ДОТАЦИЈЕ ИЗ БУЏЕТА",
            "47": "СОЦИЈАЛНЕ ПОМОЋИ",
            "48": "ОСТАЛИ РАСХОДИ",
            "49": "РЕЗЕРВЕ",
            "51": "ОСНОВНА СРЕДСТВА У ИЗГРАДЊИ"
        }

        return valjevo_parents


    @staticmethod
    def program_categories_for_vranje():
        vranje_programs = {
            "ПРОГРАМ 15: ЛОКАЛНА САМОУПРАВА": [
                "Програмска активност: Функционисање локалне самоуправе и градских општина",
                "Пројекат: Прослава Дана особођења Града и државних празника",
                "Програмска активност: Управљање јавним дугом",
                "Програмска активност: Информисање",
                "Програмска активност: Програми националних мањина",
                "Програмска активност: Заштитник грађана",
            ],
            "ПРОГРАМ 1: ЛОКАЛНИ РАЗВОЈ И ПРОСТОРНО ПЛАНИРАЊЕ": [
                "Пројекат: Експропријација земљишта за потребе Фабрике за прераду отпадних вода и заобилазнице до индустријске зоне Бунушевац",
                "Програмска активност: Стратешко, просторно и урбанистичко планирање",
                "Партерно уређење платоа у Врањској Бањи",
                "Програмска активност: Уређивање грађевинског земљишта",
                "Пројекат : Реконструкција шеталишта у улици Краља Стефана Првовенчаног од Робне куће до зграде ЈП Дирекције",
            ],
            "ПРОГРАМ 3: ЛОКАЛНИ ЕКОНОМСКИ РАЗВОЈ": [
                "Програмска активност: Унапређење привредног амбијента",
                "Програмска активност: Подстицаји за развој предузетништва",
                "Програмска активност: Одржавање економске инфраструктуре",
                "Програмска активност: Финансијска подршка локалном економском развоју",
                "Пројекат: Стручна пракса 2015",
            ],
            "ПРОГРАМ 7 - ПУТНА ИНФРАСТРУКТУРА": [
                "Пројекат: Увођење видео надзора у центру Града",
                "Програмска активност: Управљање саобраћајном инфраструктуром",
                "Програмска активност: Одржавање путева",
                "Пројекат: Периодично одржавање путева  Златокоп -Ћуковац-Врањска Бања и Бунушевац-Содерце, Миланово-Буштрање",
            ],
            "ПРОГРАМ 11: СОЦИЈАЛНА И ДЕЧЈА ЗАШТИТА": [
                "Програмска активност: Социјалне помоћи",
                "Програмска активност: Подршка социо-хуманитарним организацијама",
                "Програмска активност: Активности Црвеног крста",
                "Пројектат: Смањење сиромаштва и унапређење могућности запошљавања маргинализованих и угрожених група становништва са фокусом на ресоцијализацију осуђеника",
                "Пројекат: Смањење сиромаштва и унапређење могућности запошљавања маргинализованих и угрожених група становништва са фокусом на Ромкиње у Србији",
                "Пројекат: Изградња монтажних објеката за трајно решавање смештаја избелих и расељених лица",
                "Програмска активност: Прихватилишта, прихватне станице и друге врсте смештаја"
            ],
            "ПРОГРАМ 12: ПРИМАРНА ЗДРАВСТВЕНА ЗАШТИТА": [
                "Програмска активност: Функционисање установа примарне здравствене заштите",
                "Пројекат: Суфинансирање вантелесне оплодње"
            ],
            "ПРОГРАМ 14 - РАЗВОЈ СПОРТА И ОМЛАДИНЕ": [
                "Програмска активност: Подршка локалним спортским организацијама, удружењима и савезима",
                "Програмска активност: Подршка предшколском, школском и рекреативном спорту и масовној физичкој култури",
                "Програмска активност: Одржавање спортске инфраструктуре"
            ],

            "ПРОГРАМ 15 - ЛОКАЛНА САМОУПРАВА":[
                "Функционисање локалне самоуправе и градских општина",
                "Пројекат: Градска слава - Света Тројица",
                "Програмска активност: Општинско јавно правобранилаштво",
                "Програмска активност: Функционисање локалне самоуправе и градских општина",
                "СКУПШТИНА ОПШТИНЕ",
                "ПРЕДСЕДНИК ОПШТИНЕ И ОПШТИНСКО ВЕЋЕ",
                "ОПШТИНСКА УПРАВНА ЈЕДИНИЦА",
                "УПРАВА БАЊЕ",
                "Друмски саобраћај",
                "Изградња Балон сале - завршетак I и II фаза",
                "Уређивање и одржавање зеленила",
                "Уређење водотокова",
                "Екпропријација и припремање грађевинског земљишта",
                "Изградња канализационе мреже",
                "Улична расвета",
                "Програмска активност: Месне заједнице",
                "Програмска активност: Канцеларија за младе"
            ],
            "ПРОГРАМ 2: КОМУНАЛНЕ ДЕЛАТНОСТИ":[
                "Програмска активност: Јавна расвета",
                "Програмска активност: Водоснабдевање",
                "Програмска активност: Управљање отпадним водама",
                'Пројекат: "ESCO" пројекат побољшања енергетског учинка јавне расвете',
            ],
            "ПРОГРАМ 7: ПУТНА ИНФРАСТРУКТУРА":[
                "Програмска активност: Одржавање путева",
                "Пројекат: Асфалтирање путева у сеоским МЗ",
                "Програмска активност: Управљање саобраћајном инфраструктуром",
            ],
            "ПРОГРАМ 5: РАЗВОЈ ПОЉОПРИВРЕДЕ": [
                "Програмска активност: Унапређење  услова за пољопривредну делатност",
            ],
            "ПРОГРАМ 6: ЗАШТИТА ЖИВОТНЕ СРЕДИНЕ": [
                "Програмска активност: Управљање заштитом животне средине и природних вредности",
                "Програмска активност: Праћење квалитета елемената животне средине",
                "Пројекат: Набавка контејнера за изношење смећа",
                'Пројекат: Изградња санитарног контејнера и биолошког пречишћивача отпадних вода у насељу "Цигански рид" у Врању',
                "Пројекат: Набавка уличних канти за отпатке и бетонских мобилијера",
                "Пројекат: Озелењавање јавних површина",
                "Пројекат: Набавка камиона аутосмећара",
                "Пројекат: Очување животне средине уређењем отпадних вода",
                "Пројекат: Компостно поље",
            ],
            "ПРОГРАМ 4 - РАЗВОЈ ТУРИЗМА":[
                "Програмска активност: Управљањем развојем туризма",
                "Дани Врања и Дани Врања у Београду",
                "Прослава Дана Града",
                "Програмска активност: Туристичка промоција",
                "Пројекат: Доградња планинарског дома",
                "Пројекат: Уградња соларних панела",
                "Пројекат: Изградња платоа испред планинарског дома",
                "Пројекат: Постављање жичаре Дубока 2"
            ],
            "ПРОГРАМ 2 - КОМУНАЛНА ДЕЛАТНОСТ": [
                "Програмска активност: Водоснабдевање",
                "Програмска активност: Управљање отпадним водама",
                "Програмска активност: Паркинг сервис",
                "Програмска активност: Уређење, одржавање и коришћење пијаца",
                "Програмска активност: Уређење и одржавање зеленила",
                "Програмска активност: Јавна расвета",
                "Програмска активност: Одржавање гробаља, и погребне услуге",
            ],
            "ПРОГРАМ 13 - РАЗВОЈ КУЛТУРЕ": [
                "Програмска активност: Подстицаји културном и уметничком стваралаштву",
                "Програмска активност: Функционисање локалних установа културе",
                "Пројекат: '35. Борини позоришни дани'",
                "Пројекат: Изградња и опремање зграде Позоришта",
                "Пројекат: Светосавска недеља 2016",
                "Програм социјалне укључености лица са инвалидитетом,  посебним потребама  и  радно способних лица",
                "Пројекат: Еколошки кутак и еколошка едукација",
                "Пројекат: Набавка архивских кутија",
                'Манифестација "Златни пуж 2015."'
            ],
            "ПРОГРАМ 8 - ПРЕДШКОЛСКО ОБРАЗОВАЊЕ": [
                "Програмска активност: Функционисање предшколских установа",
                'Пројекат: Санација отворене терасе на вртићу "Чаролија"',
            ],
            "ПРОГРАМ 9 - ОСНОВНО ОБРАЗОВАЊЕ": [
                "Програмска активност: Функционисање основних школа",
                "Пројекат: Поправка инсталације грејања, котла и димњака у ОШ 20. октобар Власе",
                "Пројекат: Санирање и опремање школске кухиње ЈЈ Змај",
                "Пројекат: Реконструкција санитарног чвора у ОШ 20. октобар Власе и ОШ Предраг Девеџић Врањска Бања",
                "Програмска активност: Функционисање средњих школа",
                "Пројекат: Санирање школских спортских терена и сала",
                'Пројекат: Изградња система за наводњавање локалним квашењем земљишта школског имања "Златокоп" Пољопривредно-ветеринарске школе',
            ],
            "ПРОГРАМ 14: РАЗВОЈ СПОРТА И ОМЛАДИНЕ": [
                "Пројекат: Изградња спортских терена на Бесној Кобили",
                "Програмска активност: Додатно образовање и усавршавање омладине",
                "Пројекат: Летња школа за најбоље полазнике РЦТ на Бесној Кобили",
                "Пројекат: Организовање Регионалне смотре талената",
            ],
            "ПРОГРАМ 10 - СРЕДЊЕ ОБРАЗОВАЊЕ": [
                "Програмска активност: Функционисање средњих школа",
                "Пројекат: Санирање школских спортских терена и сала",
                'Пројекат: Изградња система за наводњавање локалним квашењем земљишта школског имања "Златокоп" Пољопривредно-ветеринарске школе',
            ]
        }
        return vranje_programs