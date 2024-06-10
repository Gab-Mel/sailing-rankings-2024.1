database:
	@touch db/db.sqlite
	sqlite3 db/db.sqlite < db/create.sql

populate:
	python3 populate.py

dev:
	streamlit run main.py