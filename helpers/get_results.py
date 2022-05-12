def get_results(s, internet=True):
    s.get_best_server()

    if internet:
        s.download()
        s.upload()

    results = s.results.dict()
    return (results["ping"], results["download"], results["upload"]) if internet else (results["ping"])