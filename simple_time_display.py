#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
使用Python内置模块显示当前时刻的PDT时间和中国时间
"""

from datetime import datetime, timezone, timedelta

def show_current_times():
    """显示当前时刻的PDT时间和中国时间"""
    
    # 获取当前UTC时间
    utc_now = datetime.now(timezone.utc)
    
    # 定义时区偏移
    # PDT (Pacific Daylight Time) = UTC-7
    # 中国时间 (CST) = UTC+8
    pdt_offset = timedelta(hours=-7)
    china_offset = timedelta(hours=8)
    
    # 计算不同时区的时间
    pdt_time = utc_now.replace(tzinfo=timezone.utc).astimezone(timezone(pdt_offset))
    china_time = utc_now.replace(tzinfo=timezone.utc).astimezone(timezone(china_offset))
    
    # 格式化输出
    print("=" * 50)
    print("当前时间显示")
    print("=" * 50)
    print(f"UTC时间:     {utc_now.strftime('%Y-%m-%d %H:%M:%S %Z')}")
    print(f"PDT时间:     {pdt_time.strftime('%Y-%m-%d %H:%M:%S %Z')}")
    print(f"中国时间:    {china_time.strftime('%Y-%m-%d %H:%M:%S %Z')}")
    print("=" * 50)
    
    # 显示时差信息
    print(f"PDT与UTC时差: -7小时")
    print(f"中国与UTC时差: +8小时")
    print(f"中国与PDT时差: +15小时")
    print("=" * 50)

def show_time_conversion_example():
    """显示时间转换示例"""
    print("\n时间转换示例:")
    print("-" * 30)
    
    # 获取当前本地时间
    local_now = datetime.now()
    
    # 假设本地时间是UTC时间（如果没有时区信息）
    utc_time = local_now.replace(tzinfo=timezone.utc)
    
    # 转换为不同时区
    pdt_time = utc_time.astimezone(timezone(timedelta(hours=-7)))
    china_time = utc_time.astimezone(timezone(timedelta(hours=8)))
    
    print(f"本地时间: {local_now.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"PDT时间:  {pdt_time.strftime('%Y-%m-%d %H:%M:%S %Z')}")
    print(f"中国时间: {china_time.strftime('%Y-%m-%d %H:%M:%S %Z')}")

def show_custom_time_conversion():
    """显示自定义时间转换"""
    print("\n自定义时间转换:")
    print("-" * 30)
    
    # 示例：转换特定时间
    sample_time = datetime(2024, 1, 15, 10, 30, 0)  # 2024-01-15 10:30:00
    utc_sample = sample_time.replace(tzinfo=timezone.utc)
    
    pdt_sample = utc_sample.astimezone(timezone(timedelta(hours=-7)))
    china_sample = utc_sample.astimezone(timezone(timedelta(hours=8)))
    
    print(f"示例时间: {sample_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"PDT时间:  {pdt_sample.strftime('%Y-%m-%d %H:%M:%S %Z')}")
    print(f"中国时间: {china_sample.strftime('%Y-%m-%d %H:%M:%S %Z')}")

if __name__ == "__main__":
    try:
        show_current_times()
        show_time_conversion_example()
        show_custom_time_conversion()
    except Exception as e:
        print(f"发生错误: {e}") 