#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re

# 用来区分是在服务器还是本地
from bean.Application import Application


def project_path_step():
    project_path = os.path.abspath(os.path.dirname(__file__))
    # Windows
    if project_path.find('\\') != -1:
        separator = '\\'
        return separator
        # Mac、Linux、Unix
    if project_path.find('/') != -1:
        separator = '/'
        return separator


class JarProjectUtil:

    @staticmethod
    def project_root_path(project_name=None, print_log=False):
        """
        获取当前项目根路径
        :param project_name: 项目名称
                                1、可在调用时指定
                                2、[推荐]也可在此方法中直接指定 将'XmindUitl-master'替换为当前项目名称即可（调用时即可直接调用 不用给参数）
        :param print_log: 是否打印日志信息
        :return: 指定项目的根路径
        """
        p_name = Application.projectName if project_name is None else project_name
        project_path = os.path.abspath(os.path.dirname(__file__))
        # Windows
        if project_path.find('\\') != -1: separator = '\\'
        # Mac、Linux、Unix
        if project_path.find('/') != -1: separator = '/'

        root_path = project_path[:project_path.find(f'{p_name}{separator}') + len(f'{p_name}{separator}')]
        if print_log: print(f'当前项目名称：{p_name}\r\n当前项目根路径：{root_path}')
        return root_path

    # 通过项目目录获取所有的文件
    def file_name(self, file_dir):
        configFile = (set())
        pyFile = (set())
        for root, dirs, files in os.walk(file_dir, topdown=False):
            # print(root) #当前目录路径
            # print(dirs) #当前路径下所有子目录
            for name in files:
                join = os.path.join(root, name)
                # 存储python类文件
                if re.search(".py$", str(join)) and "lib" and 'venv' not in str(join):
                    # print(join)
                    pyFile.add(join)
                # 存储ini类型的文件
                if re.search(".ini$", str(join)) and "lib" and 'venv' not in str(join):
                    # print(join)
                    configFile.add(join)
        # 目前只返回ini类型的文件
        return configFile



if __name__ == '__main__':
    # JarProjectUtil().projectReadIni()
    path = JarProjectUtil.project_root_path()
    print(path)
    fileConfig = JarProjectUtil().file_name(path)
    for key in fileConfig:
        print(key)
