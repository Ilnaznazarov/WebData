from sklearn.neighbors import NearestNeighbors


def get_filtered_by_genres(films_list_viewed, films_list):
    filtered_by_genres = []
    for viewed in films_list_viewed:
        for film in films_list:
            if set(viewed["genres"]).intersection(film["genres"]) and viewed["name"] not in [item["name"] for item in
                                                                                             filtered_by_genres]:
                filtered_by_genres.append({"name": film["name"], "rating": film["rating"]})
    return filtered_by_genres


def nearest_neighbors(filtered_by_genres, films_list_viewed):
    neighbors = NearestNeighbors(n_neighbors=5)
    neighbors.fit([[film["rating"]] for film in filtered_by_genres])
    distances, indices = neighbors.kneighbors(
        [[sum([item["rating"] for item in films_list_viewed]) / len([item["rating"] for item in films_list_viewed])]])
    return indices


def recommendation(filtered_by_genres, indices):
    recomendation_films = []
    for index in indices[0]:
        recomendation_films.append("Название филмьа: " + f'{filtered_by_genres[index]["name"]}' + ' Рейтинг:' + f'{filtered_by_genres[index]["rating"]}')
    return recomendation_films


if __name__ == "__main__":
    films_list = [
        {"name": "Зеленая Миля", "rating": 9.1, "genres": ["Драма", "Фэнтези", "Криминал"]},
        {"name": "1+1", "rating": 8.8, "genres": ["Драма", "Комедия", "Биография"]},
        {"name": "Побег из Шоушенка (1994)", "rating": 9.1, "genres": ["Драма"]},
        {"name": "Интерстеллар", "rating": 8.9, "genres": ["Фантастика", "Драма", "Приключения"]},
        {"name": "Властелин колец: Возвращение короля", "rating": 8.7, "genres": ["Фэнтези", "Приключения",
         "Драма", "Боевик"]},
        {"name": "Бойцовский клуб", "rating": 8.7, "genres": ["Триллер", "Драма", "Криминал"]},
        {"name": "Шрэк ", "rating": 8.2, "genres": ["Фэнтези", "Комедия", "Приключения"]},
        {"name": "Властелин колец: Братство Кольца ", "rating": 8.6,
         "genres": ["Фэнтези", "Приключения", "Драма"]},
        {"name": "Остров проклятых", "rating": 8.5, "genres": ["Триллер", "Драма", "Детектив"]},
        {"name": "Терминатор 2: Судный день", "rating": 8.4, "genres": ["Фантастика", "Боевик", "Триллер"]},
        {"name": "Начало", "rating": 8.7, "genres": ["Фантастика", "Боевик", "Триллер"]}
    ]

    films_list_viewed = [
        {"name": "Темный рыцарь", "rating": 8.5, "genres": ["Фантастика", "Триллер", "Драма", "Боевик", "Криминал"]},
        {"name": "Джентльмены ", "rating": 8.6, "genres": ["Криминал", "Комедия", "Боевик"]},
        {"name": "Назад в будущее", "rating": 8.6, "genres": ["Фантастика", "Комедия", "Приключения"]},
    ]

    filtered_by_genres = get_filtered_by_genres(films_list_viewed, films_list)
    indices = nearest_neighbors(filtered_by_genres, films_list_viewed)
    films = recommendation(filtered_by_genres, indices)
    for item in films:
        print(item)

