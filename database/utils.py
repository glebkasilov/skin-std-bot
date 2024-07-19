from .repository import AdminRepository


def init() -> None:
    if not AdminRepository.get_admin("1894858872"):
        AdminRepository.create("1894858872", "Антона")

    if not AdminRepository.get_admin("1679684862"):
        AdminRepository.create("1679684862", "Александра")

    if not AdminRepository.get_admin("1550174684"):
        AdminRepository.create("1550174684", "Алексея")

