from nonebot import get_driver
from nonebot.plugin import PluginMetadata, require

require("nonebot_plugin_orm")
require("nonebot_plugin_localstore")

from . import action_type, migrations, repository
from .api import api_balance, api_currency, api_transaction
from .api.api_currency import get_or_create_currency
from .api.depends import factory
from .hook import context, exception, hooks_manager, hooks_type
from .models import currency
from .pyd_models import balance_pyd, base_pyd, currency_pyd
from .pyd_models.currency_pyd import CurrencyData
from .repository import DEFAULT_CURRENCY_UUID
from .services import balance, transaction
from .services import currency as currency_api

__plugin_meta__ = PluginMetadata(
    name="EconomyValue",
    description="Nonebot通用经济API插件",
    usage="请查看API文档。",
    type="library",
    homepage="https://github.com/JohnRichard4096/nonebot_plugin_value",
    extra={"orm_version_location": migrations},  # 迁移文件
    supported_adapters=None,
)

__all__ = [
    "action_type",
    "api_balance",
    "api_currency",
    "api_transaction",
    "balance",
    "balance_pyd",
    "base_pyd",
    "context",
    "currency",
    "currency_api",
    "currency_pyd",
    "exception",
    "factory",
    "hook",
    "hooks_manager",
    "hooks_type",
    "repository",
    "transaction",
]


@get_driver().on_startup
async def init_db():
    """
    初始化数据库
    """
    await get_or_create_currency(CurrencyData(id=DEFAULT_CURRENCY_UUID.hex))
