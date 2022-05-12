from typing import TYPE_CHECKING, Any, Dict, Type

from pait.model.response import PaitBaseResponseModel, PaitJsonResponseModel
from pait.plugin.base import PluginProtocol
from pait.util import get_pait_response_model

if TYPE_CHECKING:
    from pait.model.core import PaitCoreModel


class AutoCompleteJsonRespPlugin(PluginProtocol):
    pait_response_model: PaitJsonResponseModel

    def update(self, source_dict: dict, target_dict: dict) -> None:
        for key, value in source_dict.items():
            if isinstance(value, dict) and key in target_dict:
                self.update(value, target_dict[key])
            else:
                source_dict[key] = target_dict.get(key, value)

    @classmethod
    def pre_check_hook(cls, pait_core_model: "PaitCoreModel", kwargs: Dict) -> None:
        super().pre_check_hook(pait_core_model, kwargs)
        if "pait_response_model" in kwargs:
            raise RuntimeError("Please use response_model_list param")

    @classmethod
    def pre_load_hook(cls, pait_core_model: "PaitCoreModel", kwargs: Dict) -> Dict:
        kwargs = super().pre_load_hook(pait_core_model, kwargs)
        pait_response_model: Type[PaitBaseResponseModel] = get_pait_response_model(
            pait_core_model.response_model_list, find_core_response_model=True
        )
        if not issubclass(pait_response_model, PaitJsonResponseModel):
            raise ValueError(f"pait_response_model must {PaitJsonResponseModel} not {pait_response_model}")
        kwargs["pait_response_model"] = pait_response_model
        return kwargs

    def _sync_call(self, *args: Any, **kwargs: Any) -> Any:
        default_response_dict: dict = self.pait_response_model.get_default_dict()
        response_dict = self.call_next(*args, **kwargs)
        self.update(default_response_dict, response_dict)
        return default_response_dict

    async def _async_call(self, *args: Any, **kwargs: Any) -> Any:
        default_response_dict: dict = self.pait_response_model.get_default_dict()
        response_dict: dict = await self.call_next(*args, **kwargs)
        self.update(default_response_dict, response_dict)
        return default_response_dict

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        if self._is_async_func:
            return self._async_call(*args, **kwargs)
        else:
            return self._sync_call(*args, **kwargs)


class AsyncAutoCompleteJsonRespPlugin(AutoCompleteJsonRespPlugin):
    """"""
