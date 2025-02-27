import plugins
from common.log import logger
from common import const
from config import conf, get_appdata_dir
from bridge.reply import Reply, ReplyType
from bridge.context import ContextType
from bridge.bridge import Bridge
from plugins import *
from TheNightOfWolf import *
@plugins.register(
    name="NightOfWolf",
    desc="狼人之夜文字游戏",
    version="1.0.0",
    author="flatfish99",
    desire_priority=100
)
class NightOfWolf(Plugin):
    def __init__(self):
        super().__init__()
        self.handlers[Event.ON_HANDLE_CONTEXT] = self.on_handle_context
        # try:
        #     self.config = super().load_config()
        #     if not self.config:
        #         self.config = self._load_config_template()
        self.game = TextAdventureGame()
        logger.info(f"[{__class__.__name__}] initialized")
        # except Exception as e:
        #     logger.error(f"[wechatDota]初始化异常：{e}")
        #     raise "[wechatDota] init failed, ignore "

    def on_handle_context(self, e_context: plugins.EventContext):
        if e_context["context"].type != ContextType.TEXT:
            return
        content = e_context["context"].content
        trigger_prefix = conf().get("plugin_trigger_prefix", "$")
        full_prefix = f"{trigger_prefix}wolf"
        if not content.startswith(full_prefix):
            e_context.action = EventAction.CONTINUE
            return
        logger.debug("[NightOfWolf] on_handle_context. content: %s" % content)
        reply = Reply()
        reply.type = ReplyType.TEXT
        parts = content[len(full_prefix):].strip().split(maxsplit=1)
        command = parts[0].lower() if len(parts) > 0 else ""
        args_str = parts[1] if len(parts) > 1 else ""
        if command == "start":
            # 参数校验
            if not args_str:
                reply.contnet = self.game.process_input("邓子恒")
            else:
                # 调用实际功能函数
                reply.contnet = self.game.process_input(args_str)
            e_context["reply"] = reply
            e_context.action = EventAction.BREAK_PASS
            return
        elif command == "stop":
            self.game.state=GameState.GAME_OVER
            reply.contnet = self.game.process_input(args_str)
            e_context["reply"] = reply
            e_context.action = EventAction.BREAK_PASS
            return

        elif command == "":
            help_text = self.get_help_text(verbose=True)
            reply.content = f"⚠️ 未知指令\n{help_text}"
            e_context["reply"] = reply
            e_context.action = EventAction.BREAK_PASS
            return

        else:  # 未知命令
            reply.content = self.game.process_input(command)
            e_context["reply"] = reply
            e_context.action = EventAction.BREAK_PASS
            return





    def get_help_text(self, verbose=True, **kwargs):
        help_text = "文字游戏:狼人之夜"
        trigger_prefix = conf().get("plugin_trigger_prefix", "$")
        if not verbose:
            return help_text
        help_text += "\n使用说明：\n"
        help_text += f"{trigger_prefix}wolf start [player name] :开始游戏\n"
        help_text += f"{trigger_prefix}wolf stop [player name] :结束游戏\n"
        return help_text
