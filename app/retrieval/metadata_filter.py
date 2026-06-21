def metadata_filter(category=None, section=None):

    filters = []

    if category:
        filters.append(
            {"category": category}
        )

    if section:
        filters.append(
            {"section": section}
        )

    if len(filters) == 0:
        return None

    if len(filters) == 1:
        return filters[0]

    return {
        "$and": filters
    }