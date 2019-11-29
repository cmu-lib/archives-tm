from celery.decorators import task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@task(name="generate_model")
def generate_model(instance):
    logger.info("Model complete")
    return instance.run()
