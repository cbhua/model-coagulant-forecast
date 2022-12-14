import wandb
from pytorch_lightning.callbacks import ModelCheckpoint, EarlyStopping
from pytorch_lightning.loggers import WandbLogger

def setup_logger(name='', project_name='Anomaly', early_stop=False, use_wandb=True, reinit=True):
    if use_wandb is True:
        name = '{}'.format(name)
        wandb_run = wandb.init(project=project_name,
                               name=name, 
                               reinit=reinit)
        logger = WandbLogger(experiment=wandb_run, log_model="all")
        latest_checkpoint = ModelCheckpoint(dirpath=wandb.run.dir,
                                            filename="latest-{epoch}",
                                            monitor='epoch',
                                            mode='max',
                                            every_n_epochs=1)
        return logger
    else:
        return None, None
