from serpapi.serp_api_client import *

class GoogleSearch(SerpApiClient):

    def __init__(self, params_dict):
        super(GoogleSearch, self).__init__(params_dict, GOOGLE_ENGINE)

def get_search_results_count(query_terms, sites, api_key):
    # Формирование строки запроса с использованием различных форм названия и сайтов
    query_terms_string = ' OR '.join(f'"{term}"' for term in query_terms) if len(query_terms) > 1 else query_terms[0]
    sites_string = ' OR '.join(f'site:*{site}' for site in sites) if len(sites) > 1 else sites[0]
    query = f"{query_terms_string} {sites_string}"

    # print(query)
    params = {
        "engine": "google",
        "q": query,
        "google_domain": "google.ru",
        "gl": "ru",
        "hl": "ru",
        "api_key": ""
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    return results.get("search_information", {}).get("total_results")

# Список терминов для поиска (включая разные формы названия)
search_terms = [
    "ИТАС",
    "Кафедра Информационных технологий и автоматизированных систем"
]
# Список сайтов для поиска
sites_to_search = ["pstu.ru", "59.ru", "perm.kp.ru", "perm.rbc.ru", "properm.ru"]
api_key = ''
total_results = get_search_results_count(search_terms, sites_to_search, api_key)

if __name__ == '__main__':
    print(f"Общее количество результатов для {', '.join(search_terms)} на сайтах {', '.join(sites_to_search)}: {total_results}")