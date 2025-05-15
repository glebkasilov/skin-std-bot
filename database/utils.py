from .repository import AdminRepository


def init() -> None:
    if not AdminRepository.get_admin("1894858872"):
        AdminRepository.create("1894858872", "Глеба")

    if not AdminRepository.get_admin("1393036381"):
        AdminRepository.create("1393036381", "Сергея")
