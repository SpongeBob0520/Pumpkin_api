from config.ReadConfigFile import ReadConfigFile


class StartInitData:
    def loadConfig(self):
        # 加载配置文件中的值和属性
        ReadConfigFile().congfiFileIni()
