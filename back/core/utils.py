from core.models import BusinessDomains


def get_path_domain(domain: BusinessDomains) -> list:
    path = []
    current_domain = domain
    while current_domain.parent:
        current_domain = current_domain.parent
        path.append({"id": current_domain.id, "name": current_domain.name, "type": "domain"})
    return path
