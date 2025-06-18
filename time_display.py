#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
显示当前时刻的PDT时间和中国时间
"""

from datetime import datetime
import pytz

import time


def show_current_times():
    """显示当前时刻的PDT时间和中国时间"""
    
    # 获取当前UTC时间
    utc_now = datetime.now(pytz.UTC)
    
    # 定义时区
    pdt_tz = pytz.timezone('US/Pacific')  # PDT时区
    china_tz = pytz.timezone('Asia/Shanghai')  # 中国时区
    
    # 转换为不同时区的时间
    pdt_time = utc_now.astimezone(pdt_tz)
    china_time = utc_now.astimezone(china_tz)

    # 格式化输出
    print("=" * 50)
    print("当前时间显示")
    print("=" * 50)
    print(f"UTC时间:     {utc_now.strftime('%Y-%m-%d %H:%M:%S %Z')}")
    print(f"PDT时间:     {pdt_time.strftime('%Y-%m-%d %H:%M:%S %Z')}")
    print(f"中国时间:    {china_time.strftime('%Y-%m-%d %H:%M:%S %Z')}")
    print("=" * 50)
    
    # 显示时差信息
    pdt_offset = pdt_time.utcoffset().total_seconds() / 3600
    china_offset = china_time.utcoffset().total_seconds() / 3600
    time_diff = china_offset - pdt_offset
    
    print(f"PDT与UTC时差: {pdt_offset:+.0f}小时")
    print(f"中国与UTC时差: {china_offset:+.0f}小时")
    print(f"中国与PDT时差: {time_diff:+.0f}小时")
    print("=" * 50)

def show_time_conversion():
    """显示时间转换示例"""
    print("\n时间转换示例:")
    print("-" * 30)
    
    # 获取当前时间
    now = datetime.now()
    
    # 转换为不同时区
    pdt_tz = pytz.timezone('US/Pacific')
    china_tz = pytz.timezone('Asia/Shanghai')
    
    # 本地化时间
    pdt_local = pdt_tz.localize(now)
    china_local = china_tz.localize(now)
    
    print(f"本地时间: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"PDT时间:  {pdt_local.strftime('%Y-%m-%d %H:%M:%S %Z')}")
    print(f"中国时间: {china_local.strftime('%Y-%m-%d %H:%M:%S %Z')}")

if __name__ == "__main__":
    try:
        show_current_times()
        show_time_conversion()
    except ImportError:
        print("错误: 需要安装 pytz 库")
        print("请运行: pip install pytz")
    except Exception as e:
        print(f"发生错误: {e}") 