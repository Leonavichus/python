from dataclasses import dataclass, asdict, astuple

@dataclass
class Menu:
    id: int
    name: str

@dataclass
class Contant:
    id: int
    name: str
    description: str
    id_author: int
    id_menu: int

@dataclass
class Author:
    id: int
    name: str
    password: str
    mail: str