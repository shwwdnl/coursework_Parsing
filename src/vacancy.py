import json

class Vacancy:
    """Класс для работы с полученными данными из .json файла"""
    __slots__ = ('employer', 'name', 'url', 'requirement', 'salary_from', 'salary_to')

    def __init__(self, employer=None, name=None, url=None, requirement=None, salary_from=None, salary_to=None):
        self.employer = employer
        self.name = name
        self.url = url
        self.requirement = requirement
        try:
            if "<highlighttext>" and "</highlighttext>" in self.requirement:
                self.requirement = self.requirement.replace("<highlighttext>", "")
                self.requirement = self.requirement.replace("</highlighttext>", "")
        except TypeError:
            self.requirement = requirement
        self.salary_from = salary_from
        self.salary_to = salary_to

    def __str__(self):
        return f"""
        Наниматель: {self.employer}
        Вакансия: {self.name}
        Описание/Требования: {self.requirement}
        Заработная плата от {self.salary_from}, до {self.salary_to}
        Ссылка на вакансию: {self.url}"""


def sorting(vacancies):
    """ Сортирует полученные вакансии исходя из заработной платы:
    создает .json файл для проверки работы """
    vacancies_list = []
    vacancies_sort = sorted(vacancies, key=lambda vacancy: vacancy["salary_from"], reverse=True)
    for vacancy in vacancies_sort:
        vacancies_list.append(f"""
        Наниматель: {vacancy['employer']}
        Вакансия: {vacancy['name']}
        Описание/Требования: {vacancy['requirement']}
        Заработная плата от: {vacancy['salary_from']}, до {vacancy['salary_to']}
        Ссылка на вакансию: {vacancy['url']}""")
    with open(f'sort.json', 'w', encoding='UTF-8') as file:
        json.dump(vacancies_sort, file, indent=2, ensure_ascii=False)
    return vacancies_list


def get_top(vacancies, top_count):
    """ Возвращает полученный топ вакансий по запросу, исходя из заработной:
       создает .json файл для проверки работы """
    top_list = []
    vacancies_sort = sorted(vacancies, key=lambda vacancy: vacancy["salary_from"], reverse=True)
    top_vacancies = vacancies_sort[0:top_count]
    for vacancy in top_vacancies:
        top_list.append(f"""
          Наниматель: {vacancy['employer']}
          Вакансия: {vacancy['name']}
          Описание/Требования: {vacancy['requirement']}
          Заработная плата от {vacancy['salary_from']}, до {vacancy['salary_to']}
          Ссылка на вакансию: {vacancy['url']}""")
    with open(f'top.json', 'w', encoding='UTF-8') as file:
        json.dump(top_vacancies, file, indent=2, ensure_ascii=False)
    return top_list

