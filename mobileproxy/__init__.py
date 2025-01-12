import requests

class MobileProxy:
    def __init__(self, api_key: str = None):
        self.url = "https://mobileproxy.space/api.html"
        self.api_key = api_key

        self.session = requests.Session()
        self.session.headers = {"Authorization": f"Bearer {self.api_key}"}
    
    def request(self, params: dict = {}, data: dict = {}, method: str = "GET") -> dict:
        """
        Make a request to the MobileProxy API.

        :param params: Query parameters to send with the request.
        :param data: Data to send with the request.
        :param method: HTTP method to use for the request. Default is "GET".
        :return: The response from the API as a dictionary.
        """
        response = self.session.request(method=method, url=self.url, params=params, data=data)
        try:
            return response.json()
        except Exception as e:
            print(f"Error: {e}. Response code: {response.status_code}")
            print(response.content)
            return {"error": str(e)}
    
    def get_ip(self, proxy_id: int) -> dict:
        """
        Получение ip-адреса вашего прокси
        Данный запрос позволяет узнать, какой ip-адрес в данный момент выдает ваш прокси

        Response:
        {
            {
                status, //Статус операции, ok или err
                proxy_id, //Массив значений, где ключ - это идентификатор прокси, а значение - это ip-адрес, который он выдает
            }
        }

        :param proxy_id: Идентификатор прокси, которому нужно узнать ip-адрес
        :type proxy_id: int

        :return: Список ip-адресов
        :rtype: dict
        """
        params = {"command": "proxy_ip", "proxy_id": proxy_id}

        return self.request(params)


    def change_ip(self, proxy_key: str, user_agent: str, format: str = "json") -> dict:
        """
        Изменение IP-адреса прокси
        Данный запрос не требует указания заголовка с авторизацией, 
        необходимо указывать User-agent браузера.

        :param proxy_key: Ключ прокси
        :type proxy_key: str
        :param user_agent: User-Agent принадлежащий не боту
        :type user_agent: str
        :param format: Формат ответа (json или 0)
        :type format: str
        :return: Ответ от сервера
        :rtype: dict
        """
        url = f"https://changeip.mobileproxy.space/?proxy_key={proxy_key}&format={format}"
        headers = {"User-Agent": user_agent}
        
        response = self.session.get(url, headers=headers)
        return response.json()

    def get_price(self, id_country: int) -> dict:
        """
        Получение цен на прокси в зависимости от страны.

        :param id_country: Идентификатор страны
        :type id_country: int
        :return: Ответ от сервера с ценами
        :rtype: dict
        """
        params = {"command": "get_price", "id_country": id_country}
        return self.request(params)

    def get_black_list(self, proxy_id: int) -> dict:
        """
        Получение черного списка оборудования и операторов.

        :param proxy_id: Идентификатор прокси
        :type proxy_id: int
        :return: Ответ от сервера с черным списком
        :rtype: dict
        """
        params = {"command": "get_black_list", "proxy_id": proxy_id}
        return self.request(params)

    def add_operator_to_black_list(self, proxy_id: int, operator_id: int) -> dict:
        """
        Добавить оператора в черный список.

        :param proxy_id: Идентификатор прокси
        :type proxy_id: int
        :param operator_id: Идентификатор оператора
        :type operator_id: int
        :return: Ответ от сервера о статусе операции
        :rtype: dict
        """
        params = {
            "command": "add_operator_to_black_list",
            "proxy_id": proxy_id,
            "operator_id": operator_id
        }
        return self.request(params)

    def remove_operator_from_black_list(self, proxy_id: int, operator_id: int) -> dict:
        """
        Удалить оператора из черного списка.

        :param proxy_id: Идентификатор прокси
        :type proxy_id: int
        :param operator_id: Идентификатор оператора
        :type operator_id: int
        :return: Ответ от сервера о статусе операции
        :rtype: dict
        """
        params = {
            "command": "remove_operator_black_list",
            "proxy_id": proxy_id,
            "operator_id": operator_id
        }
        return self.request(params)

    def remove_black_list(self, proxy_id: int, black_list_id: int = None, eid: int = None) -> dict:
        """
        Удалить записи из черного списка оборудования.

        :param proxy_id: Идентификатор прокси
        :type proxy_id: int
        :param black_list_id: Идентификатор записи
        :type black_list_id: int, optional
        :param eid: Идентификатор оборудования
        :type eid: int, optional
        :return: Ответ от сервера о статусе операции
        :rtype: dict
        """
        params = {
            "command": "remove_black_list",
            "proxy_id": proxy_id,
            "black_list_id": black_list_id,
            "eid": eid
        }
        return self.request(params)

    def get_my_proxy(self, proxy_id: int) -> dict:
        """
        Получение списка ваших активных прокси.

        :param proxy_id: Идентификатор прокси
        :type proxy_id: int
        :return: Ответ от сервера с активными прокси
        :rtype: dict
        """
        params = {
            "command": "get_my_proxy",
            "proxy_id": proxy_id
        }
        return self.request(params)

    def change_proxy_login_password(self, proxy_id: int, proxy_login: str, proxy_pass: str) -> dict:
        """
        Изменение логина и пароля прокси.

        :param proxy_id: Идентификатор прокси
        :type proxy_id: int
        :param proxy_login: Новый логин
        :type proxy_login: str
        :param proxy_pass: Новый пароль
        :type proxy_pass: str
        :return: Ответ от сервера о статусе операции
        :rtype: dict
        """
        params = {
            "command": "change_proxy_login_password",
            "proxy_id": proxy_id,
            "proxy_login": proxy_login,
            "proxy_pass": proxy_pass
        }
        return self.request(params)

    def reboot_proxy(self, proxy_id: int) -> dict:
        """
        Перезагрузка прокси.

        :param proxy_id: Идентификатор прокси
        :type proxy_id: int
        :return: Ответ от сервера о статусе операции
        :rtype: dict
        """
        params = {
            "command": "reboot_proxy",
            "proxy_id": proxy_id
        }
        return self.request(params)

    def get_geo_operator_list(self, equipments_back_list: int = None, operators_back_list: int = None, show_count_null: int = None) -> dict:
        """
        Получение только доступного оборудования сгруппированного по ГЕО и оператору

        :param equipments_back_list: Исключить из списка содержимое черного списка оборудования
        :param operators_back_list: Исключить из списка содержимое черного списка операторов
        :param show_count_null: Показать нулевое количество, по умолчанию false
        :return: Список доступного оборудования
        :rtype: dict
        """
        params = {
            "command": "get_geo_operator_list",
            "equipments_back_list": equipments_back_list,
            "operators_back_list": operators_back_list,
            "show_count_null": show_count_null
        }
        return self.request(params)

    def get_operators_list(self, geoid: int) -> dict:
        """
        Получение списка операторов

        :param geoid: Идентификаторы ГЕО
        :type geoid: int
        :return: Список операторов
        :rtype: dict
        """
        params = {"command": "get_operators_list", "geoid": geoid}
        return self.request(params)

    def get_id_country(self, lang: str) -> dict:
        """
        Получение списка стран

        :param lang: Язык на котором вернется результат ('ru' or 'en')
        :type lang: str
        :return: Список стран
        :rtype: dict
        """
        params = {"command": "get_id_country", "lang": lang}
        return self.request(params)

    def get_id_city(self, lang: str) -> dict:
        """
        Получение списка городов

        :param lang: Язык на котором вернется результат ('ru' or 'en')
        :type lang: str
        :return: Список городов
        :rtype: dict
        """
        params = {"command": "get_id_city", "lang": lang}
        return self.request(params)

    def get_geo_list(self, proxy_id: int = None, geoid: int = None) -> dict:
        """
        Получение списка доступных ГЕО

        :param proxy_id: Идентификатор прокси
        :param geoid: Идентификаторы ГЕО
        :return: Список доступных ГЕО
        :rtype: dict
        """
        params = {"command": "get_geo_list", "proxy_id": proxy_id, "geoid": geoid}
        return self.request(params)

    def change_equipment(self, operator: str, geoid: int, proxy_id: int, add_to_black_list: int, id_country: int, id_city: int, eid: int) -> dict:
        """
        Смена оборудования

        :param operator: Идентификатор оператора
        :param geoid: Идентификатор ГЕО
        :param proxy_id: Идентификатор прокси
        :param add_to_black_list: Добавить в черный список
        :param id_country: Идентификатор страны
        :param id_city: Идентификатор города
        :param eid: Идентификатор оборудования
        :return: Результат смены оборудования
        :rtype: dict
        """
        params = {
            "command": "change_equipment",
            "operator": operator,
            "geoid": geoid,
            "proxy_id": proxy_id,
            "add_to_black_list": add_to_black_list,
            "id_country": id_country,
            "id_city": id_city,
            "eid": eid
        }
        return self.request(params)
    
    def buy_proxy(self, operator: str, geoid: int, proxy_id: int, period: int, num: int, coupons_code: str = None, id_country: int = None, id_city: int = None, auto_renewal: int = None) -> dict:
        """
        Покупка прокси

        :param operator: Идентификатор оператора
        :param geoid: Идентификатор ГЕО
        :param proxy_id: Идентификатор прокси
        :param period: Период покупки
        :param num: Количество прокси
        :param coupons_code: Код купона
        :param id_country: Идентификатор страны
        :param id_city: Идентификатор города
        :param auto_renewal: Автопродление
        :return: Результат покупки прокси
        :rtype: dict
        """
        params = {
            "command": "buyproxy",
            "operator": operator,
            "geoid": geoid,
            "proxy_id": proxy_id,
            "period": period,
            "num": num,
            "coupons_code": coupons_code,
            "id_country": id_country,
            "id_city": id_city,
            "auto_renewal": auto_renewal
        }
        return self.request(params)

    def get_balance(self) -> dict:
        """
        Получение баланса аккаунта

        :return: Баланс аккаунта
        :rtype: dict
        """
        params = {"command": "get_balance"}
        return self.request(params)

    def edit_proxy(self, proxy_id: int, proxy_reboot_time: int = None, proxy_ipauth: str = None, proxy_comment: str = None) -> dict:
        """
        Изменение настроек существующего прокси

        :param proxy_id: Идентификатор прокси
        :param proxy_reboot_time: Время смены ip-адреса
        :param proxy_ipauth: Список ip-адресов для авторизации
        :param proxy_comment: Комментарий к прокси
        :return: Результат изменения настроек прокси
        :rtype: dict
        """
        params = {
            "command": "edit_proxy",
            "proxy_id": proxy_id,
            "proxy_reboot_time": proxy_reboot_time,
            "proxy_ipauth": proxy_ipauth,
            "proxy_comment": proxy_comment
        }
        return self.request(params)

    def get_ipstat(self) -> dict:
        """
        Статистика IP-адресов мобильных прокси по ГЕО

        :return: Статистика IP-адресов
        :rtype: dict
        """
        params = {"command": "get_ipstat"}
        return self.request(params)

    def see_the_url_from_different_IPs(self, url: str, id_country: str = None) -> dict:
        """
        Получить содержимое страницы с разных IP

        :param url: Адрес страницы для проверки
        :param id_country: Список идентификаторов стран
        :return: Результат проверки страницы
        :rtype: dict
        """
        params = {
            "command": "see_the_url_from_different_IPs",
            "url": url,
            "id_country": id_country
        }
        return self.request(data = params, method = "POST")

    def get_task_result(self, tasks_id: int) -> dict:
        """
        Получение результата выполнения задачи

        :param tasks_id: Идентификатор созданной задачи
        :return: Результат выполнения задачи
        :rtype: dict
        """
        params = {"command": "tasks", "tasks_id": tasks_id}
        return self.request(params)
