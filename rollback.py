import sys
from alembic.config import Config
from alembic import command


URL = "sqlite:///{filename}"

alembic_cfg = Config("alembic.ini")
if len(sys.argv) > 1:
    alembic_cfg.set_main_option("sqlalchemy.url",
                                URL.format(filename=sys.argv[1]))

command.downgrade(alembic_cfg, "-1")
