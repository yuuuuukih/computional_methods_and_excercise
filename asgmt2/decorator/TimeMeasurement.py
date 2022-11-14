import time

def print_proc_time(f):
    """ 計測デコレータ """

    def print_proc_time_func(*args, **kwargs):
        # 開始
        start_time = time.process_time()

        # 関数実行
        return_val = f(*args, **kwargs)

        # 修了
        end_time = time.process_time()

        # 関数名と経過時間を出力(秒)
        elapsed_time = end_time - start_time
        print(f.__name__, f'{elapsed_time} sec')

        # 戻り値を返す
        return return_val

    return print_proc_time_func


# 参考: https://www.python.ambitious-engineer.com/archives/3355