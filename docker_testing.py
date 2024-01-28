def connect_to_external_service(host):
    import socket

    port=12345
    response_text = ''
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            s.sendall(b'Hello, server')
            response = s.recv(1024)
            response_text = response.decode()
    except ConnectionError as e:
        response_text =  f"Connection failed: {e}"
    
    return response_text


def get_database_session(options):
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    db_name = options['db_name']
    db_user = options['db_user']
    db_password = options['db_password']
    db_host = options['db_host']
    
    # PostgreSQL connection string format
    db_string = f"postgresql://{db_user}:{db_password}@{db_host}:5432/{db_name}"

    # Create an engine that stores data in the specified database
    engine = create_engine(db_string)

    # Bind the engine to the metadata of the Base class so that the
    # declaratives can be accessed through a DBSession instance
    Session = sessionmaker(bind=engine)

    # A DBSession() instance establishes all conversations with the database
    # and represents a "staging zone" for all the objects loaded into the
    session = Session()
    return session

# Example usage:
# Replace with your actual database information
# db_session = get_database_session("my_database", "username", "password", "127.0.0.1", "5432")
