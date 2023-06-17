# 保留异常栈信息
import shutil


def mycopy(sourse, dest):
    try:
        shutil.copy2(sourse, dest)
    except OSError:  # py2中raise会丢失原来的traceback信息
        raise NotImplementedError('automatic sudo injection') from OSError


mycopy('old', 'new')
