from typing import Any
from pydantic import Field
from pydantic_settings import BaseSettings
from pathlib import Path


class BaseConfig(BaseSettings):
    MODE: str = Field(..., pattern="(DEVELOPMENT|STAGING|PRODUCTION)")
    SECRET_KEY: str = Field(..., env="SECRET_KEY")
    EMAIL_HOST_USER: str = Field(..., env="EMAIL_HOST_USER")
    EMAIL_HOST_PASSWORD: str = Field(..., env="EMAIL_HOST_PASSWORD")
    EMAIL_PORT: str = Field(..., env="EMAIL_PORT")

    class Config:
        env_file = f"{Path(__file__).resolve().parent}/.env"



class ProjectConfig(BaseConfig):
    ...


class ProjectDevelopmentConfig(ProjectConfig):
    ...


class ProjectStagingConfig(ProjectConfig):
    ...


class ProjectProductionConfig(ProjectConfig):
    ...


class ConfigFactory:
    def __init__(self, project_env_state: str) -> None:
        self.project_env_state = project_env_state

    def __call__(self) -> Any:
        if self.project_env_state == "PRODUCTION":
            return ProjectProductionConfig()
        elif self.project_env_state == "STAGING":
            return ProjectStagingConfig()
        return ProjectDevelopmentConfig()


config = ConfigFactory(ProjectConfig().MODE)()
