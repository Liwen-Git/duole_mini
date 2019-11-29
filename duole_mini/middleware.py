from django.utils.deprecation import MiddlewareMixin
from duole_mini import utils
import hashlib
import ast


# 签名校验
class SignatureVerificationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        return None
        # if request.method == 'POST':
        #     post = ast.literal_eval(request.body.decode('utf-8'))
        #     sign = post['sign']
        #     items = sorted(post.items())
        #
        #     return self.sign_md5(sign, items)
        # elif request.method == 'GET':
        #     sign = request.GET.get('sign')
        #     items = sorted(request.GET.items())
        #
        #     return self.sign_md5(sign, items)
        # else:
        #     return utils.error(message='请求方法错误')

    # 校验参数生成的MD5 和 传过来的sign 是否一致
    @staticmethod
    def sign_md5(sign, items):
        sign_str = 'this is my secret token'
        for key, value in items:
            if key != 'sign':
                sign_str += str(key) + str(value)

        md = hashlib.md5()
        md.update(sign_str.encode('utf-8'))
        if sign == md.hexdigest():
            return None
        else:
            return utils.error(message='签名验证失败')
