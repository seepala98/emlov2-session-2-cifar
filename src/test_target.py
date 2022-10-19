import pyrootutils

root = pyrootutils.setup_root(
    search_from=__file__,
    indicator=[".git", "pyproject.toml"],
    pythonpath=True,
    dotenv=True,
)

from typing import List, Optional, Tuple

import hydra
import pytorch_lightning as pl
from omegaconf import DictConfig
from pytorch_lightning import Callback, LightningDataModule, LightningModule, Trainer
from pytorch_lightning.loggers import LightningLoggerBase

from src import utils

log = utils.get_pylogger(__name__)

@hydra.main(version_base="1.2", config_path=root / "configs", config_name="test_target.yaml")
def main(cfg: DictConfig) -> Optional[float]:
    print(cfg)
    data_model = hydra.utils.instantiate(cfg.datamodule)
    print(data_model)
    print(data_model(d="d"))

if __name__ == "__main__":
    main()