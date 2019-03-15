VENV = venv
ACTIVATE = $(VENV)/bin/activate

target_help = \
  "help - Print this help message" \
  "" \
  "clean - Remove virtualenv" \
  "migrations - Create any needed migrations" \
  "migrate - Run any pending migrations" \
  "rollback - Rollback the last migration" \
  "run - Run the main program"


pip3 = $(shell which pip3)

ifeq ($(pip3),)
  NEED_PIP3 = pip3
endif

pip3:
	@sudo apt-get install python3-pip


sqlite3 = $(shell which sqlite3)

ifeq ($(sqlite3),)
  NEED_SQLITE = sqlite3
endif

sqlite3:
	@sudo apt-get install sqlite3


help:
	@echo "Valid targets are:\n"
	@for t in $(target_help) ; do \
	    echo $$t; done
	@echo


$(VENV): Makefile requirements.txt $(NEED_PIP3) $(NEED_SQLITE)
	@pip3 install virtualenv
	@rm -rf $(VENV)
	@virtualenv -p `which python3` $@
	@touch $(ACTIVATE)
	@. $(ACTIVATE) ; \
	  pip3 install -r requirements.txt

clean:
	@rm -rf $(VENV)

migrations: $(VENV)
	@. $(ACTIVATE); alembic revision --autogenerate -m "$(NOTE)"

migrate: $(VENV)
	@. $(ACTIVATE); python migrate.py $(DB_NAME)

rollback: $(VENV)
	@. $(ACTIVATE); python rollback.py $(DB_NAME)

run: $(VENV)
	@. $(ACTIVATE); python lifelog/main.py

test: $(VENV)
	@. $(ACTIVATE); pytest

PY_FILES = \
  *.py \
  lifelog/*.py \
  lifelog/*/*.py \
  alembic/*.py \
  alembic/*/*.py

code-check:
	@. $(ACTIVATE); pycodestyle $(PY_FILES)

