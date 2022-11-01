import json


def load_candidates(filename):
    """Принимает имя файла, возвращает содержимое в формате списка"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)


def get_all(candidates):
    """Принимает список с кандидатами, возвращает строку в виде
    Имя, Позиция, Навыки по всем кандидатам"""
    all_candidates = []
    for candidate in candidates:
        all_candidates.append(candidate['name'])
        all_candidates.append(candidate['position'])
        all_candidates.append(candidate['skills'])
        all_candidates.append("\n")

    return "<pre>" + "\n".join(all_candidates) + "</pre>"


def get_by_pk(candidates, pk):
    """Принимает список с кандидатами и номер кандидата в формате int,
    возвращает информацию о кандидате в формате строки Фото, Имя, Позиция, Навыки"""
    for candidate in candidates:
        if candidate["pk"] == pk:
            return f"<img src='{candidate['picture']}'>\n"\
                   f"<pre>{candidate['name']}\n"\
                   f"{candidate['position']}\n"\
                   f"{candidate['skills']}</pre>"


def get_by_skill(candidates, skill_name):
    """Принимает список с кандидатами и навык,
    возвращает строку с информацией о всех кандидатах с данным навыком"""
    candidate_with_skill = []
    for candidate in candidates:
        if skill_name.lower() in candidate["skills"].lower():
            candidate_with_skill.append(candidate["name"])
            candidate_with_skill.append(candidate["position"])
            candidate_with_skill.append(candidate["skills"])
            candidate_with_skill.append('\n')

    return "<pre>"+"\n".join(candidate_with_skill)+"</pre>"
