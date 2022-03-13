import json

def load_candidates():
    """
    возвращает список всех кандидатов
    """
    with open("candidates.json", "r", encoding="utf-8") as file:
        candidates = json.load(file)

    return candidates

def get_candidate_by_id(uid):
    """
    возвращает кандидата по его id
    """
    candidates = load_candidates()

    for candidate in candidates:
        if candidate["id"] == uid:
            return candidate

def get_candidates_by_skill(candidate_skill):
    """
    возвращает кандидатов по навыку
    """
    candidates = load_candidates()
    skill_lower = candidate_skill.lower()
    skilled_candidates = []

    for candidate in candidates:
        candidate_skills = candidate["skills"].lower().split(", ")
        if skill_lower in candidate_skills:
            skilled_candidates.append(candidate)

    return skilled_candidates

def get_candidate_by_name(candidate_name):
    """
    возвращает кандидатов по имени
    """
    candidate_names = []
    candidates = load_candidates()
    candidate_name_lower = candidate_name.lower()

    for candidate in candidates:
        if candidate_name_lower in candidate["name"].lower():
            candidate_names.append(candidate)

    return candidate_names
