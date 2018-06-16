from datetime import datetime

from django.utils.deprecation import MiddlewareMixin

from user.models import UserTicketModel, UserModel


class UserMiddleware(MiddlewareMixin):

    def process_request(self, request):

        path = request.path
        ignore_path = ['/user/login/', '/user/register/']
        if path in ignore_path:
            return None

        ticket = request.COOKIES.get('ticket')  # 拿到 ticket
        if ticket:
            # 找出用户
            user_ticket = UserTicketModel.objects.filter(ticket=ticket).first()
            # 判断是否过期, 没过期绑定 user 在request 中
            if user_ticket:
                if datetime.utcnow() < user_ticket.out_time.replace(tzinfo=None):
                    # 绑定 user 在 request 中
                    request.user = user_ticket.user
        # else:
        #     request.user = UserModel.objects.filter(username=0).first()