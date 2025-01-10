# your_app/management/commands/import_csv.py
from django.core.management.base import BaseCommand
import psycopg2
import subprocess
from django.conf import settings

class Command(BaseCommand):
    help = 'Imports data from CSV into Postgres table'

    def handle(self, *args, **kwargs):
        # Define the path to your CSV file inside the container
        csv_path = '/tmp/filtered.csv'  # Adjust the path as necessary

        # # Establish a connection to the PostGIS database
        conn = psycopg2.connect(
            dbname=settings.DATABASES['default']['NAME'],
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            host=settings.DATABASES['default']['HOST'],
            port=settings.DATABASES['default']['PORT']
        )
        
        cursor = conn.cursor()

        # Define the COPY SQL statement
        copy_sql = f"""
        COPY species_locations(species_id, kingdom, phylum, phylum_class, family, scientific_name, genus, country, state_province, decimal_latitude, decimal_longitude) 
        FROM '{csv_path}' DELIMITER ',' CSV HEADER;
        """
        
        # Execute the COPY command
        try:
            cursor.execute(copy_sql)
            conn.commit()
            self.stdout.write(self.style.SUCCESS('Successfully imported CSV data into the table.'))
        except Exception as e:
            conn.rollback()
            self.stdout.write(self.style.ERROR(f'Error importing CSV: {e}'))
        finally:
            cursor.close()
            conn.close()
        # Define the psql command for client-side \copy
        # psql_command = f"""
        # psql -U {settings.DATABASES['default']['USER']} \
        #     -d {settings.DATABASES['default']['NAME']} \
        #     -h {settings.DATABASES['default']['HOST']} \
        #     -p {settings.DATABASES['default']['PORT']} \
        #     -c "\\copy species_locations(id, kingdom, phylum, phylum_class, family, scientific_name, genus, country, state_province, decimal_latitude, decimal_longitude) FROM '{csv_path}' DELIMITER ',' CSV HEADER;"
        # """
        
        # # Execute the command using subprocess
        # try:
        #     subprocess.run(psql_command, shell=True, check=True)
        #     self.stdout.write(self.style.SUCCESS('Successfully imported CSV data using psql \\copy'))
        # except subprocess.CalledProcessError as e:
        #     self.stdout.write(self.style.ERROR(f'Error executing psql \\copy: {e}'))