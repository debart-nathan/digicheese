if __name__ == "__main__":
    import uvicorn
    import os
    from dotenv import load_dotenv

    load_dotenv()

    try:
        server_host = os.getenv("SERVER_HOST","localhost")
        server_port = os.getenv("SERVER_PORT",8000)
        reload = os.getenv("SERVER_RELOAD", 'False').lower() in ('true', '1', 't')
        
        try:
            server_port = int(server_port)
        except ValueError:
            raise ValueError("Environment variable SERVER_PORT must be an integer.")


        uvicorn.run("src.main:app", host=server_host, port=server_port, reload=reload)

    except Exception as e:
        print(f"Error: {e}")
