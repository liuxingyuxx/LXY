#--*-- coding:utf-8 --*--

'''
  在学老男孩python全栈开发时写的，用于自制的分页功能
'''
class PageInfo(object):
    def __init__(self, current_page,all_data_num, per_page_num):
        try:
            self.current_page = int(current_page)
        except:
            self.current_page = 1
        self.per_page_num = per_page_num 
        self.all_page_num = all_date_num/per_page_num

    def start(self):
        return (self.current_page-1)*per_page_num 

    def end(self):
        return (self.current_page)*per_page_num 
    def pager(self):
        #用于显示当前页左右的3页
        page_list = []


def costom(request):
    current_page = request.GET.get('page')
    page_info = PageInfo(current_page, 10)
    user_list = models.UserInfo.objects.all()[page_info.start:page_info.end]
    


