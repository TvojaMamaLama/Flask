# InvestorQualification


В папке config общие настройки, в папке API само апи.

POST api/v1/investor  -  отправляет данные о инвесторе на сервер, для сохранения, все данные перечислены в models.py

POST api/v1/rules - Запрос на подтверждение правил, переводит поле согласия с правилами в TRUE

POST api/v1/investor/qualification - Запрос на сохранение квалификации, необходимо передать id инвестора и его квалификацию, подробнее в models.py

GET api/v1/investor/<int:investorId>/qualification - Запрос на получение данных о квалификации, в урле необходимо передать id инвестора