import hydra
from omegaconf import DictConfig


@hydra.main(config_name="config", version_base=None, config_path="conf")
def main(cfg: DictConfig) -> None:
    print(cfg.data.input)
    print(cfg.learning_rate)
    print(cfg.batch_size)


if __name__ == "__main__":
    main()
