import requests

class MeineStadtResult:
    plain = None
    html_formatted = None
    image_url = None
    def __init__(self, plain, html_formatted, image_url):
        self.plain = plain
        self.html_formatted = html_formatted
        self.image_url = image_url

class MeineStadt:

    cookies = {
        'MS_JOBS_USERREQ_UUID': 'f5bb91e7-8c9c-4717-a16e-a5198e5da697',
        'rtbhouse': 'no',
        '_fbp': 'fb.1.1574417091763.2061090397',
        'AMCVS_24D022CE527854F10A490D4D%40AdobeOrg': '1',
        's_cc': 'true',
        'consentCookie': 'accepted',
        'bx': '44e3bccd810c4bebbfb877b821fc07f0',
        'wd': '35599a530f04499e84a7afe3c1946e91',
        'Criteo_Segmentation': 'c',
        'channelcloser': 'other',
        'channeloriginator': 'other',
        '_ga': 'GA1.2.752072322.1574417564',
        's_fid': '1F27B7CC0C3044C2-1920098E322D9305',
        'OPTOUTMULTI': '0:0%7Cc3:0%7Cc2:0%7Cc7:0%7Cc8:0%7Cc6:0%7Cc1:0%7Cc4:0',
        'channelflow': 'other|other|1582194908564',
        'MS_JOBS_ABTEST_VARIANTS': 'eyJhYnRlc3RzIjpbeyJpZCI6IkVDLTc2MDIiLCJ2YXJpYW50IjoiQiJ9LHsiaWQiOiJFQy03NjI0IiwidmFyaWFudCI6IkEifSx7ImlkIjoiRUMtNjkwOSIsInZhcmlhbnQiOiJBIn0seyJpZCI6IkVDLTc1MzUiLCJ2YXJpYW50IjoiQyJ9LHsiaWQiOiJFQy03NDE0IiwidmFyaWFudCI6IkMifSx7ImlkIjoiRUMtNzUzMiIsInZhcmlhbnQiOiJBIn1dLCJ2ZXJzaW9uIjoyfQ==',
        'AMCV_24D022CE527854F10A490D4D%40AdobeOrg': '-1303530583%7CMCIDTS%7C18223%7CMCMID%7C01349459643233684650858597123048144309%7CMCAAMLH-1575121894%7C6%7CMCAAMB-1575121894%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1574524294s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C3.3.0',
        's_sq': '%5B%5BB%5D%5D',
        'utag_main': 'v_id:016e92924be900020b172c9b299503073003806b00978$_sn:2$_se:14$_ss:0$_st:1574519372433$vapi_domain:meinestadt.de$dc_visit_meinestadt-meinestadt.de:2$dc_visit_dip-main:2$dc_visit:1$ses_id:1574517093391%3Bexp-session$_pn:1%3Bexp-session$dc_event_meinestadt-meinestadt.de:12%3Bexp-session$dc_region_meinestadt-meinestadt.de:eu-central-1%3Bexp-session$sync_160_ran:1%3Bexp-session$collectCookieMode:3rdParty%3Bexp-session$dip_events_this_session:1%3Bexp-session$dc_event_dip-main:1%3Bexp-session$dc_region_dip-main:eu-central-1%3Bexp-session',
    }

    headers = {
        'authority': 'www.meinestadt.de',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'x-instana-t': '517c42729f73f902',
        'origin': 'https://www.meinestadt.de',
        'x-instana-l': '1',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'accept': 'undefined',
        'x-requested-with': 'XMLHttpRequest',
        'x-instana-s': '517c42729f73f902',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'referer': 'https://www.meinestadt.de/stuttgart/immobilien/wohnungen',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
    }

    params = (
        ('service', 'immoweltAjax'),
    )

    data = {
      'geoid': '108',
      'pageSize': '20',
      'page': '1',
      'lat': '48.71073713217854',
      'lng': '9.157236201122231',
      'location': 'stuttgart-fasanenhof',
      'esr': '2',
      'etype': '1',
      'sort': 'createdate desc',
      'sr': '20',
      'bigimage': 'true',
      'ecat': '',
      'eqid': '',
      'roomi': '2',
      'rooma': '',
      'flmi': '0',
      'flma': '',
      'prima': '1000',
      'affiliateId': '',
      'debug': 'false',
      'usersSort': 'true',
      'locationName': 'Stuttgart-Fasanenhof',
      'userModified': 'true'
    }


    @staticmethod
    def _get_json_of_meine_stadt():
        return requests.post('https://www.meinestadt.de/stuttgart/immobilien/wohnungen', headers=MeineStadt.headers, params=MeineStadt.params,
        cookies=MeineStadt.cookies, data=MeineStadt.data).json()

    @staticmethod
    def receive_meine_stadt_result():
        res = MeineStadt._get_json_of_meine_stadt()["results"]["resultJsonLd"][0]
        str = """
    <b>Name:</b> %(name)s

    <b>Beschreibung:</b> %(description)s

    <b>Adresse:</b> %(address)s

    <b>Zimmer:</b> %(rooms)s

    <b>Url:</b> %(url)s
        """ % dict(name=res["name"], description=res["description"], address= res["address"], rooms= res["numberOfRooms"]["value"], url= res["url"])
        return MeineStadtResult(res, str, res["image"] if "image" in res else None)
