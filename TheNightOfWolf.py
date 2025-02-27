# -*- coding: utf-8 -*-
import time
import random
from enum import Enum

class GameState(Enum):
    START = 0
    VILLAGE_DECISION = 1
    STAY_IN_VILLAGE = 2
    SURVIVOR = 3
    DIRECTION_DECISION = 4
    BUILDING_DECISION = 5
    GO_DOWN_DECISION = 6
    SEARCH_BODY_DECISION = 7
    DOWN_TO_WOLF_DECISION = 8
    WOLFKING_DECISION = 9
    JOIN_WOLF_DECISION = 10
    GO_BACK_DECISION = 11
    OPEN_DECISION = 12
    ACCEPT_DECISION = 13
    INTO_ROOM_DECISION = 14
    KEEP_GOING_DECISION = 15
    DIRECTION_DECISION2 = 16
    DEFENCE_DECISION = 17
    ESCAPE_DECISION = 18
    HIDE_DECISION = 19
    RESIST_DECISION = 20


    GAME_OVER = 10

class TextAdventureGame:
    def __init__(self, player_name = "邓子恒"):
        self.player_name = player_name
        self.state = GameState.START
        self.inventory = set()
        self.achievements = set()
        self.companion = False
        self.has_gun = False
        self.has_slide = False
        self.has_shot_gun = False
        self._init_handlers()

    def _init_handlers(self):
        self.handlers = {
            GameState.START: self._handle_start,
            GameState.VILLAGE_DECISION: self._handle_village_decision,
            GameState.STAY_IN_VILLAGE: self._handle_stay_in_village,
            GameState.SURVIVOR: self._handle_survivor_choice,
            GameState.DIRECTION_DECISION: self._handle_direction_decision,
            GameState.BUILDING_DECISION: self._handle_building_decision,
            GameState.GO_DOWN_DECISION: self._handle_go_down_decision,
            GameState.SEARCH_BODY_DECISION: self._handle_search_body_decision,
            GameState.DOWN_TO_WOLF_DECISION: self._handle_down_to_wolf_decision,
            GameState.WOLFKING_DECISION: self._handle_wolfking_decision,
            GameState.JOIN_WOLF_DECISION: self._handle_join_wolf_decision,
            GameState.GO_BACK_DECISION: self._handle_go_back_decision,
            GameState.OPEN_DECISION: self._handle_open_decision,
            GameState.ACCEPT_DECISION: self._handle_accept_decision,
            GameState.INTO_ROOM_DECISION: self._handle_into_room_decision,
            GameState.KEEP_GOING_DECISION: self._handle_keep_going_decision,
            GameState.DIRECTION_DECISION2: self._handle_direction_decision2,
            GameState.DEFENCE_DECISION: self._handle_defence_decision,
            GameState.ESCAPE_DECISION: self._handle_escape_decision,
            GameState.HIDE_DECISION: self._handle_hide_decision,
            GameState.RESIST_DECISION: self._handle_resist_decision,
            GameState.GAME_OVER: self._handle_game_over,
        }

    def _slow_print(self, text, delay=1):
        #time.sleep(random.randint(delay, delay+1))
        print(text)

    def _add_achievement(self, name):
        self.achievements.add(name)
        self._slow_print(f"————解锁成就：{name}————")

    def _handle_start(self, choice):
        self.player_name = str(choice)
        self._slow_print(f"欢迎你，{self.player_name}!")
        self._slow_print("全部22个游戏成就：")
        self._slow_print("不辨是非    幸存者    新生活    伙伴    \n崖壁的碰撞    狼腹    碎肉    西线的尽头")
        self._slow_print("与狼共舞    东线的尽头    狼王现身    狼群\n高风亮节    囫囵吞枣    狼子野心    聪明反被聪明误")
        self._slow_print("鄙夷的眼神    抵抗    首领的死亡    村庄英雄\n村庄联盟    人狼之战    反客为主")
        self._slow_print("本游戏共有六大结局，加油，少侠！")
        self._slow_print("加载游戏剧情中…………", 3)
        self._slow_print("这是一个月圆之夜……")
        self._slow_print("村子里召开了一年一次的屠杀狼人活动，将要去杀死狼人的人被称作屠狼师。")
        self._slow_print("而你，是这里最具有天赋的屠狼师。")
        self._slow_print("村子里，暗藏杀机；野外，阴险无比。")
        self.state = GameState.VILLAGE_DECISION
        return f"首领找到你，问你：‘{self.player_name}，你是否要出去屠狼？’ 1：是 其他按键：否"

    def _handle_village_decision(self, choice):
        if choice == "1":
            response = "你选择了出发。\n"
            response += "你在野外前进，发现了一个人，他自我介绍说他叫莱奥，是个屠狼师，你也自报家门说，我叫 "+ self.player_name + ",他果断要求加入你的队伍，\n"
            response += "是否接纳他？1=是 其他=否\n"
            self.state = GameState.ACCEPT_DECISION
            return response
        else:
            response = "你选择留守在村子里。\n"
            response += "首领虽无可奈何，也没强求。\n"
            response += "这天傍晚，有一个人闯入你家，说是首领要求来的，请求进来。\n"
            response += "你要让他进来吗？ 1：是 其他：否"
            self.state = GameState.STAY_IN_VILLAGE
            return response
    def _handle_accept_decision(self, choice):
        if choice == "1":
            response = "你接纳了他作为伙伴。\n"
            self.companion = True
            self._add_achievement("伙伴")
        else:
            response = "你没有接纳他。\n"
        response += "你走着走着，看到了一扇门，是否进入？1=是 其他=否"
        self.state = GameState.INTO_ROOM_DECISION
        return response
    def _handle_into_room_decision(self, choice):
        if choice == "1":
            response = "你刚一进去，里面窜出来一条大蟒蛇，将你吞下，\n"
            response += "你死了…………游戏结束\n"
            response += "欢迎再度游玩！\n"
            self._add_achievement("囫囵吞枣")
            self.state = GameState.GAME_OVER
            return response
        else:
            if self.companion:
                response = "你让莱奥去打头阵，里面窜出一条大蟒蛇将莱奥吞噬，你拔刀杀死了蟒蛇，发现了一把散弹枪，\n"
                self.has_shot_gun = True
                response += "你穿过森林，来到了小溪，发现了一群狼人，\n"
                response += "你是否要继续前行？1=是 其他=否\n"
                self.state = GameState.KEEP_GOING_DECISION
                return response
            else:
                response = "你没有办法通过，只能绕道前进，\n"
                response += "走了一会，你走到了一个大沙漠里面，\n"
                response += "你走到了一片绿洲里面，\n"
                response += "你在其中发现了一个狼人，你拔刀杀死了他，发现他身上有一串字母，‘LANGQUNZAIXIAOXI’\n"
                response += "你要前往：1：小溪 其他：山谷\n"
                self.state = GameState.DIRECTION_DECISION2
                return response
    def _handle_keep_going_decision(self, choice):
        if choice == "1":
            response = "你继续前行，拿出散弹枪，杀死了全部的狼人。\n"
            response += "你在狼人身上发现了一封信，是写给你的，你决定将计就计。\n"
            response += "你如约来到了约定地点，杀死了狼人首领。\n"
            response += "余下的狼人们决定报复你。\n"
            response += "你要如何防御？ 1=直接用散弹枪刚  其他=突然袭击\n"
            self.state = GameState.DEFENCE_DECISION
            return response
        else:
            response = "你选择原路返回\n"
            response += "在返回的路上被狼人偷袭\n"
            response += "你死了——\n"
            response += "游戏结束——\n"
            self.state = GameState.GAME_OVER
            return response
    def _handle_defence_decision(self, choice):
        if choice == "1":
            response = "你在乱战中直接开枪，不久，你就杀死了所有的狼人。\n"
            response += "你返回了村庄，成为了村庄英雄。\n"
            response += '后记：你以一己之力杀死了所有的狼人这一行为被整个村庄追捧，甚至其余地方的狼人听见'+self.player_name+'这一名字都胆战心惊，再不敢来犯。\n'
            response += "剧情5完结——\n"
            response += "游戏结束——\n"
            self._add_achievement("村庄英雄")
            self.state = GameState.GAME_OVER
            return response
        else:
            response = "你选择了突然袭击。\n"
            response += "没想到，狼人们就在你的后面，乘你不注意，窃走了你的散弹枪，将你送上了西天。\n"
            response += "你死了——\n"
            response += "游戏结束——\n"
            self._add_achievement("反客为主")
            self.state = GameState.GAME_OVER
            return response
    def _handle_direction_decision2(self, choice):
        if choice == "1":
            response = "你前往了小溪，发现了狼群，但是你没有武器，无法战胜他们，你杀死了几个狼人后被杀死。\n"
            response += "你死了…………游戏结束\n"
            response += "欢迎再度游玩！\n"
            self.state = GameState.GAME_OVER
            return response
        else:
            response = "你前往了山谷，发现了你的首领在山下，和一个人谈话，最后，首领让这个人代理狼人首领职务\n"
            response += "你大吃一惊，不料被首领发现，差点被一枪打死，\n"
            response += "你要怎么做？ 1：装死 2：逃离 其他按键：呆在原地不动\n"
            self.state = GameState.ESCAPE_DECISION
            return response
    def _handle_escape_decision(self, choice):
        if choice == "1":
            response = "你在地上装死，不料被狼人误以为死去，一口将你吞噬，\n"
            response += "你死了…………游戏结束\n"
            response += "欢迎再度游玩！\n"
            self._add_achievement("聪明反被聪明误")
            self.state = GameState.GAME_OVER
            return response
        elif choice == "2":
            response = "你立即逃离了，首领没有追上你，你安全了。\n"
            response += "你离开了山谷，来到了一片麦田，\n"
            response += "你要怎么做？ 1=装成稻草人  其他=躲起来\n"
            self.state = GameState.HIDE_DECISION
            return response
        else:
            response = "你选择了呆在原地不动。\n"
            response += "首领看到你，又给了你一枪，这回直接爆头，你死了。\n"
            response += "你死了…………游戏结束。\n"
            response += "欢迎再度游玩！\n"
            self._add_achievement("鄙夷的眼神")
            self.state = GameState.GAME_OVER
            return response
    def _handle_hide_decision(self, choice):
        if choice == "1":
            response = "你装成了稻草人。\n"
            response += "首领没有发现你，你突然向前，猛地一刀，杀死了首领。\n"
            response += "原首领被你杀死了，你返回了村庄，成为了新的首领。\n"
            response += "后记：你成为了新的首领以后，发展军事，成功消灭了所有的狼人。\n"
            response += "剧情3完结——\n"
            response += "游戏结束——\n"
            response += "欢迎再度游玩！\n"
            self._add_achievement("首领的死亡")
            self.state = GameState.GAME_OVER
            return response
        else:
            response = "首领没有发现你，你目送首领远去。\n"
            response += "你返回村子，向所有村民报告了这一事件，原首领被驱逐。\n"
            response += "原首领恼羞成怒，率领狼人们向村庄杀来。\n"
            response += "在混战中，原首领被你杀死，你逃出了包围圈，村民们击退了狼人军团。\n"
            response += "狼人军团被击退，你会：1=修筑工事 其他=购买兵器'\n"
            self._add_achievement("抵抗")
            self.state = GameState.RESIST_DECISION
            return response
    def _handle_resist_decision(self, choice):
        if choice == "1":
            response = "你选择了修筑工事。\n"
            response += "当晚，你们正在睡梦中，狼人军团再一次来袭。\n"
            response += "他们根据村子里的内应找到了工事的突破口，杀进村庄。\n"
            response += "村子被洗劫一空，所有人都被杀害了。\n"
            response += "你也死了。\n"
            response += "你死了…………游戏结束\n"
            response += "欢迎再度游玩！\n"
            self._add_achievement("人狼之战")
            self.state = GameState.GAME_OVER
            return response
        else:
            response = "你派出去的人是村子里的间谍，狼人失去内应，找不到突破口。\n"
            response += "不久，间谍回来，因为没有购买任何武器被你杀死，狼人得知，贸然闯进村庄，被全歼。\n"
            response += "后记：狼人被全部消灭，你也当上了村子的首领，受大家的拥戴。\n"
            response += "剧情4完结——\n"
            response += "游戏结束——\n"
            response += "欢迎再度游玩!\n"
            self._add_achievement("村庄联盟")
            self.state = GameState.GAME_OVER
            return response
    def _handle_stay_in_village(self, choice):
        if choice == "1":
            response = "你同意了他的请求。\n"
            response += "这个人是个狼人，你尝试反抗，但是你没有武器，最后被残忍地杀害了。\n"
            response += "你死了…………游戏结束\n"
            response += "欢迎再度游玩！\n"
            self._add_achievement("不辨是非")
            self.state = GameState.GAME_OVER
            return response
        else:
            response = "你拒绝了他的请求。\n"
            response += "到了晚上，你一个人坐在家中。\n"
            response += "一群狼人在潜伏在村子里的狼王的带领下，冲进了村子。\n"
            response += "村子里所有的人都被杀死了，除了你。\n"
            self._add_achievement("幸存者")
            self.state = GameState.SURVIVOR
            return response

    def _handle_survivor_choice(self, choice):
        if choice == "1":
            response = "你踏上了寻找狼王的道路。\n"
            response += "你要从哪个方向出发？1=东线 其他=西线。\n"
            self.state = GameState.DIRECTION_DECISION
            return response
        else:
            response = "你选择了不去寻找狼王。\n"
            response += "于是，你前往了别的村庄，安家落户，直到死亡。\n"
            response += "剧情6完结——。\n"
            response += "游戏结束——。\n"
            self._add_achievement("新生活")
            self.state = GameState.GAME_OVER
            return response
    def _handle_direction_decision(self, choice):
        if choice == "1":
            response = "你继续向前前进，来到了一片森林，\n"
            response += "在路边搜索，发现了一张白纸，上面写有这么一行字：‘23124E’，\n"
            response += "你来到了两个建筑前。\n"
            response += "你要去哪个建筑？1=教堂 其他=钟楼\n"
            self.state = GameState.BUILDING_DECISION
            return response
        else:
            response = "你前往了西线\n"
            response += "你在西线一个地方的一个角落里找到了滑梯。\n"
            self.has_slide = True
            response += "是否返回？1=是 其他=否\n"
            self.state = GameState.GO_BACK_DECISION
            return response
    def _handle_go_back_decision(self, choice):
        if choice == "1":
            response = "你选择返回\n"
            self.state = GameState.DIRECTION_DECISION
            return response
        else:
            response = "你选择了不返回。\n"
            response += "你一路向前，来到了一条小河边，得到了一个手机，\n"
            response += "是否打开？ 1=是 其他=否\n"
            self.state = GameState.OPEN_DECISION
            return response
    def _handle_open_decision(self, choice):
        if choice == "1":
            response = "你打开了手机。\n"
            response += "手机突然爆炸了，你被炸成了碎块。\n"
            response += "你死了…………游戏结束\n"
            response += "欢迎再度游玩!\n"
            self._add_achievement("碎肉")
            self.state = GameState.GAME_OVER
            return response
        else:
            response = "你选择了不打开手机。\n"
            response += "你继续往前走，看到了一张纸条，上面写有‘eniaeng’，背面还有落款‘2114PY’，\n"
            response += "你好像知道了什么……\n"
            response += "你找到了一把枪。\n"
            self.has_gun = True
            response += "路走到了尽头，你选择了返回。\n"
            self._add_achievement("西线的尽头")
            self.state = GameState.DIRECTION_DECISION
            return response

    def _handle_building_decision(self, choice):
        if choice == "1":
            response = "你没有找到任何线索。\n"
        else:
            response = "你找到了一张小纸片，上面有几个数字：1 1 2 1 Language\n"
        response += "你继续前行，来到了悬崖边。\n"
        response += "这时，你找到了一串绳索。\n"
        response += "是否使用绳索前往悬崖下面寻找线索？1=是 其他=否\n"
        self.state = GameState.GO_DOWN_DECISION
        return response
    def _handle_go_down_decision(self, choice):
        if choice == "1":
            response = "你使用了绳索。\n"
            response += "你刚下去，绳索突然断了，你坠崖身亡。\n"
            response += "你死了…………游戏结束\n"
            response += "欢迎再度游玩！\n"
            self._add_achievement("崖壁的碰撞")
            self.state = GameState.GAME_OVER
            return response
        else:
            if self.has_slide:
                response = "你安上了滑梯，滑了下去，安全着陆。\n"
                response += "你继续前行，发现了一具尸体，\n"
                response += "是否搜查尸体全身？1=是 其他=否\n"
                self.state = GameState.SEARCH_BODY_DECISION
                return response
            else:
                response = "你将绳索抛弃。\n"
                response += "已经无路可退，你选择返回村庄。\n"
                response += "你返回了村庄，休整了一会再度出发。\n"
                self.state = GameState.DIRECTION_DECISION
                return response
    def _handle_search_body_decision(self, choice):
        if choice == "1":
            response = "这是一具假的尸体，狼人就在附近，你专心搜查尸体时狼人一跃而起，将你杀死。\n"
            response += "你死了…………游戏结束\n"
            response += "欢迎再度游玩！\n"
            self._add_achievement("狼腹")
            self.state = GameState.GAME_OVER
            return response
        else:
            response = "你放弃了搜查。\n"
            response += "你来到了一个山谷，下面有4个狼人，\n"
            response += "你是否下去？1=是 其他=否\n"
            self.state = GameState.DOWN_TO_WOLF_DECISION
            return response
    def _handle_down_to_wolf_decision(self, choice):
        if choice == "1":
            response = "你选择了直接下去。\n"
            response += "狼人们直接扑向了你，你被撕咬而死。\n"
            response += "你死了…………游戏结束！\n"
            self._add_achievement("与狼共舞")
            self.state = GameState.GAME_OVER
            return response
        else:
            response = "你选择了不下去。\n"
            if self.has_gun:
                response += "你使用了手枪，杀死了所有的狼人，得到了一张纸，\n"
                response += "上面写道：本卡茨夫拉瓦得登，8选4，联络首领，首领名字2 · 2\n"
                response += "东线已走至尽头，你返回了村庄，你要杀死狼王，为村民们报仇。\n"
                response += "是时候宣布了，谁是狼王？\n"
                self.state = GameState.WOLFKING_DECISION
                return response
            else:
                response += "你已没有退路，只得返回。\n"
                self.state = GameState.DIRECTION_DECISION
                return response
    def _handle_wolfking_decision(self, choice):
        if choice == "本茨·拉登":
            response = "你来到了本茨·拉登的家里。\n"
            response += "你进入了他的家，发现了许多狼毛。\n"
            response += "他，就是狼王！\n"
            response += "你等在门后，看到他回来，一枪打死了他。\n"
            response += "后记：你杀死了狼王，群狼失去首领，一个接一个的被捕杀了，自此，这一带，再也没有狼人的踪迹。\n"
            response += "剧情1完结——\n"
            response += "游戏结束——\n"
            self._add_achievement("狼王现身")
            self.state = GameState.GAME_OVER
            return response
        else:
            response = "你找到了"+str(choice)+"，开枪打死了他。\n"
            response += "他不是狼人！\n"
            response += "你害怕的往后退，撞到了一个人。\n"
            response += "你回头一看，惊愕了：他才是真正的狼王！\n"
            response += "他邀请你加入他们，是否加入？1：是 其他按键：否\n"
            self.state = GameState.JOIN_WOLF_DECISION
            return response
    def _handle_join_wolf_decision(self, choice):
        if choice == "1":
            response = "你选择了加入他们。\n"
            response += "后记：你加入了狼群，被改造成了狼人，并成为了新的首领，成为了大名鼎鼎的狼王\n"
            response += "村子里的人对你深恶痛绝。\n"
            response += "终于有一天，你和你的同伴们死在了一个围阵中，结束了你的一生。\n"
            response += "剧情2完结——\n"
            response += "游戏结束——\n"
            self._add_achievement("狼群")
            self.state = GameState.GAME_OVER
            return response
        else:
            response = "你选择了拒绝。\n"
            response += "狼王十分恼怒，当即将你杀死。\n"
            response += "你死了…………游戏结束\n"
            response += "欢迎再度游玩！\n"
            self._add_achievement("高风亮节")
            self.state = GameState.GAME_OVER
            return response


    def _handle_game_over(self, choice):
        return "游戏已结束，欢迎再度游玩！"

    def process_input(self, user_input):
        handler = self.handlers.get(self.state, self._handle_game_over)
        return handler(user_input)

if __name__ == "__main__":
    game = TextAdventureGame()
    print("你的名字是：")
    while game.state != GameState.GAME_OVER:
        user_input = input("> ")
        response = game.process_input(user_input)
        if response:
            print(response)