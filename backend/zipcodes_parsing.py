import json
import logging
from db_connection import connect_to_db, close_connection

GEOJSON_FILE_PATH = 'zipcodes.json' #
TARGET_ZIP_CODES = {
    "89431", "89433", "89434", "89439", "89501",
    "89502", "89503", "89506", "89508", "89509",
    "89511", "89512", "89519", "89521", "89523"
}
DB_TABLE_NAME = 'zip_code_boundaries'
ZIP_CODE_COLUMN = 'zip_code'
GEOMETRY_COLUMN = 'boundary'
SRID = 4326 # Standard WGS 84 Latitude/Longitude

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def create_boundary_table(conn, cur):
    try:

        cur.execute(f"""
            CREATE TABLE IF NOT EXISTS {DB_TABLE_NAME} (
                {ZIP_CODE_COLUMN} VARCHAR(10) PRIMARY KEY,
                {GEOMETRY_COLUMN} GEOMETRY(Geometry, {SRID})
            );
        """)
        cur.execute(f"""
            CREATE INDEX IF NOT EXISTS {DB_TABLE_NAME}_geom_idx
            ON {DB_TABLE_NAME}
            USING GIST ({GEOMETRY_COLUMN});
        """)
        conn.commit()
        logging.info(f"Table '{DB_TABLE_NAME}' checked/created successfully.")
    except Exception as e:
        logging.error(f"Error creating table '{DB_TABLE_NAME}': {e}")
        conn.rollback()
        raise

def format_coords_for_wkt(coords_list):
    return ", ".join([f"{lon} {lat}" for lon, lat in coords_list])

def geojson_geometry_to_wkt(geometry_data):
    geom_type = geometry_data.get('type', '').upper()
    coordinates = geometry_data.get('coordinates')

    if not geom_type or not coordinates:
        return None

    if geom_type == 'POLYGON':
        if coordinates and len(coordinates) > 0:
            outer_ring = format_coords_for_wkt(coordinates[0])
            return f"POLYGON(({outer_ring}))"
        else:
            return None
    elif geom_type == 'MULTIPOLYGON':

        polygon_parts = []
        for poly_coords in coordinates:
             if poly_coords and len(poly_coords) > 0:
                 outer_ring = format_coords_for_wkt(poly_coords[0])
                 polygon_parts.append(f"(({outer_ring}))")
        if polygon_parts:
            return f"MULTIPOLYGON({', '.join(polygon_parts)})"
        else:
            return None
    else:
        logging.warning(f"Unsupported geometry type: {geom_type}. Skipping.")
        return None

def insert_boundary(conn, cur, zip_code, wkt_geometry):
    sql = f"""
        INSERT INTO {DB_TABLE_NAME} ({ZIP_CODE_COLUMN}, {GEOMETRY_COLUMN})
        VALUES (%s, ST_GeomFromText(%s, %s))
        ON CONFLICT ({ZIP_CODE_COLUMN}) DO UPDATE SET
          {GEOMETRY_COLUMN} = EXCLUDED.{GEOMETRY_COLUMN};
    """
    try:
        cur.execute(sql, (zip_code, wkt_geometry, SRID))
    except Exception as e:
        logging.error(f"Error inserting/updating ZIP {zip_code}: {e}")
        logging.error(f"WKT causing error (first 100 chars): {wkt_geometry[:100] if wkt_geometry else 'None'}")
        conn.rollback()



def process_geojson_file():
    conn = None
    cur = None
    inserted_count = 0
    skipped_null_geom = 0
    skipped_other_zip = 0

    try:
        logging.info(f"Loading GeoJSON data from: {GEOJSON_FILE_PATH}")
        with open(GEOJSON_FILE_PATH, 'r') as f:
            geojson_data = json.load(f)
        logging.info("GeoJSON data loaded.")

        conn = connect_to_db()
        if not conn:
            logging.error("Database connection failed. Exiting.")
            return
        cur = conn.cursor()
        logging.info("Database connection established.")

        create_boundary_table(conn, cur)

        features = geojson_data.get('features', [])
        logging.info(f"Processing {len(features)} features...")

        for feature in features:
            properties = feature.get('properties')
            geometry = feature.get('geometry')

            if not properties or not geometry:
                skipped_null_geom += 1
                continue

            zip_code = properties.get('ZCTA5CE10')

            if not zip_code:
                 logging.warning(f"Feature found without 'ZCTA5CE10' property. Skipping.")
                 continue

            if zip_code in TARGET_ZIP_CODES:
                logging.info(f"Processing target ZIP Code: {zip_code}")
                wkt = geojson_geometry_to_wkt(geometry)

                if wkt:
                    insert_boundary(conn, cur, zip_code, wkt)
                    inserted_count += 1
                    logging.debug(f"Successfully prepared ZIP {zip_code} for insertion.")
                else:
                    logging.warning(f"Could not generate WKT for ZIP {zip_code}. Skipping.")
                    skipped_null_geom += 1
            else:
                skipped_other_zip += 1
                logging.debug(f"Skipping non-target ZIP Code: {zip_code}")


        conn.commit()
        logging.info("Database transaction committed.")

    except FileNotFoundError:
        logging.error(f"Error: GeoJSON file not found at {GEOJSON_FILE_PATH}")
    except json.JSONDecodeError:
        logging.error(f"Error: Could not decode JSON from {GEOJSON_FILE_PATH}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        if conn:
            conn.rollback()
            logging.warning("Database transaction rolled back due to error.")
    finally:
        logging.info(f"Processing complete.")
        logging.info(f"Inserted/Updated boundaries for {inserted_count} target ZIP codes.")
        logging.info(f"Skipped {skipped_null_geom} features due to missing/invalid geometry or WKT conversion failure.")
        logging.info(f"Skipped {skipped_other_zip} features for non-target ZIP codes.")
        if cur and conn:
            close_connection(cur, conn)
            logging.info("Database connection closed.")

if __name__ == "__main__":
    process_geojson_file()