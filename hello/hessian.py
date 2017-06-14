# -*- coding:utf-8 -*-
from pyhessian.client import HessianProxy
from pyhessian import protocol
import json


def InvokeHessian(service, interface, method, orderId, packNum, retcode='000000'):
    try:
        url = 'http://172.16.195.19:9001/' + service + '.' + interface

        print('URL:\t%s' % url)
        print('Method:\t%s' % method)
        print('Req:\t%s' % orderId)
        res = getattr(HessianProxy(url), method)(orderId, packNum)
        print('Res:\t%s' % json.dumps(res, ensure_ascii=False))

    except Exception as e:
        print(e)


if __name__ == '__main__':
    service = 'com.dmall.dms.tpl.si'
    interface = 'HeiGouOrderDubboService'
    method = 'createOrder'

    InvokeHessian(service, interface, method, 12, 3)
