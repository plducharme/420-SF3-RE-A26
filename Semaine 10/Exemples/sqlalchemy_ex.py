from typing import List
from typing import Optional
from sqlalchemy import ForeignKey, create_engine
from sqlalchemy import String
from sqlalchemy import select
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session


# Super classe pour tous les objets (modèle) qui seront utilisés pour la base de données
class Base(DeclarativeBase):
    pass


# Les classes qui héritent de Base sont des modèles pour la base de données
class User(Base):
    # Le nom de la table dans la base de données où les objets de cette classe seront stockés
    __tablename__ = "user_account"
    # Les attributs de la classe sont des colonnes dans la table
    # Mapped permet de définir le type de la colonne et d'autres propriétés (ex: clé primaire)
    # par défaut le nom de la colonne est le nom de l'attribut (peut être changé avec le paramètre name)
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]]
    # pour addresses, on utilise relationship pour définir la relation entre les tables
    # Dans ce cas-ci, on a une relation one-to-many entre User et Address
    addresses: Mapped[List["Address"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"


class Address(Base):
    __tablename__ = "address"
    id: Mapped[int] = mapped_column(primary_key=True)
    email_address: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))
    user: Mapped["User"] = relationship(back_populates="addresses")

    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"


# Créer un moteur pour la base de données
engine = create_engine("sqlite:///exemple.db")
# Au cas où la base de données existe déjà, on supprime les tables existantes
Base.metadata.drop_all(engine, checkfirst=True)
# Créer les tables dans la base de données
Base.metadata.create_all(engine)


# On utilise Session pour initier une session transactionnelle
with Session(engine) as session:
    spongebob = User(
        name="spongebob",
        fullname="Spongebob Squarepants",
        addresses=[Address(email_address="spongebob@sqlalchemy.org")],
    )
    sandy = User(
        name="sandy",
        fullname="Sandy Cheeks",
        addresses=[
            Address(email_address="sandy@sqlalchemy.org"),
            Address(email_address="sandy@squirrelpower.org"),
        ],
    )
    patrick = User(name="patrick", fullname="Patrick Star")
    session.add_all([spongebob, sandy, patrick])
    # Le commit est nécessaire pour sauvegarder les changements dans la base de données
    # (dans ce cas-ci, les ajouts)
    # Le commit exécute la transaction. Si une erreur survient, la transaction est annulée.
    session.commit()


session = Session(engine)
# On utilise select pour créer une requête
# On utilise where pour spécifier les conditions de la requête
# Dans ce cas-ci, on retourne les utilisateurs dont le nom est "spongebob" ou "sandy"
stmt = select(User).where(User.name.in_(["spongebob", "sandy"]))

for user in session.scalars(stmt):
    print(user)

# Select avec jointure
stmt = (
    select(Address)
    .join(Address.user)
    .where(User.name == "sandy")
    .where(Address.email_address == "sandy@sqlalchemy.org")
)
sandy_address = session.scalars(stmt).one()
print(sandy_address)

# Exemple de mise à jour

stmt = select(User).where(User.name == "patrick")
patrick = session.scalars(stmt).one()
patrick.addresses.append(Address(email_address="patrickstar@sqlalchemy.org"))
sandy_address.email_address = "sandy_cheeks@sqlalchemy.org"

session.commit()

# Exemple de suppression
sandy = session.get(User, 2)
sandy.addresses.remove(sandy_address)

session.delete(patrick)
session.commit()
