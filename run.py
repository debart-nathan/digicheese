if __name__ == "__main__":
    import uvicorn
    import os
    from dotenv import load_dotenv, dotenv_values

    load_dotenv()
    reload = os.getenv("SERVER_RELOAD", 'False').lower() in ('true', '1', 't')
    uvicorn.run("src.main:app", host=os.getenv("SERVER_HOST"), port=int(os.getenv("SERVER_PORT")), reload=reload)

