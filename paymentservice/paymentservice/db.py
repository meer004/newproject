from sqlmodel import create_engine, SQLMODEL,Session # imports necessary components from the sqlmodel library.
#create_engine: A function used to set up a connection to the database.
#SQLModel: A class that is used as a base class for creating SQLAlchemy models. It's a combination of Pydantic models and SQLAlchemy's declarative models.
#Session : A class that is used to interact with database.
from paymentservice import settings
# This line imports the settings object from the payment_service module.
# settings : object contain databasr url and other settings

# only neede for psycopg 3 - replace postgresql
# with posresql+psycopg in settings.DATABASE_URL
conncecton_string = str(settings.DATABASE_URL).replace(
    "Postgresql","postgresql+psycopg"
)
# this block adjust connection string to work with psycopg(python library for working with postgresqll databases)which is psotgresql driver
#settings.DATABASE_URL:urL of database
#.replace("postgresql", "postgresql+psycopg"):replace postgresql with postgresql+psycopg (to make compatible with psycopg3)
#connection_string : variable to store connection string


# recycle connection after 5 minutes
# to correspond with the compute scale down
create_engine(
    conncecton_string, conncect_args={},pool_recycle=300

)#this block menage connection to database
# create_engine:function used to set up a connection to database
# connection_string: specify how to connect with database
# connection_args: empity dictionary use to specify additional connection argu if needed
# pool_recycle: A keyword argument that specifies the time in seconds to recycle (close and reopen)  

def create_db_and_tables():
    SQLMODL.metadata.create_all(engine)
#function sets up the database tables based on the models defined using SQLModel.
# SQLModel.metadata.create_all(engine): method reads the metadata (i.e., the structure of your models) from SQLModel and creates corresponding tables in the database using the engine.
#metadata: A property of SQLModel that holds information about the models (like table definitions).
#create_all():method creates all tables in the database that are defined in the metadata.
#engine: object used to connect to the database.
    def get_session():
        with Session(engine) as session:
            yield session
# This function provides a context-managed session for database operations,
#  typically used in dependency injection in web frameworks like FastAPI.
# sesion : obj used to interact with database (queries, inserts, updates, etc.).
# with Session(engine) as session: starts a context_menager that creat a new session bound to engine. use to interact with database
#Session(engine): A call to create new session object connected to database
# yield session: keyword used here to retuern session obj from context_menager used to provide a session to an endpoint handler.
#  The session is automatically closed after the transaction is complete.
#Functions: create_db_and_tables(), get_session().
#Variables/Objects: connection_string, engine, settings.
#Methods: .replace(), create_all().
# Classes/Modules: SQLModel, Session, create_engine.



