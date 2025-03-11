from huggingface_hub.inference._providers._common import (
    BaseConversationalTask,
    BaseTextGenerationTask,
)


_PROVIDER = "novita"
_BASE_URL = "https://api.novita.ai"


class NovitaTextGenerationTask(BaseTextGenerationTask):
    def __init__(self):
        super().__init__(provider=_PROVIDER, base_url=_BASE_URL)

    def _prepare_route(self, mapped_model: str) -> str:
        # there is no v1/ route for novita
        return "/v3/openai/completions"


class NovitaConversationalTask(BaseConversationalTask):
    def __init__(self):
        super().__init__(provider=_PROVIDER, base_url=_BASE_URL)

    def _prepare_route(self, mapped_model: str) -> str:
        # there is no v1/ route for novita
        return "/v3/openai/chat/completions"
