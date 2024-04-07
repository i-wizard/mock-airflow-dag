def scheduler():
    """
    Implement a background cron job that schedules all
    DAGS where the start date is past, by creating instances of DAGRuns 
    in a queued state.
    This function will be ran according to the schedule_interval
    of each DAG
    """
    ...


def executor():
    """
    Implement a cron job that will run all
    queued DAGRuns then update them with the appropriate status.
    >>> RUNNING, SUCCESS, FAILED
    """
    ...
