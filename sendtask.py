from celery_app.teskone import download1,crawl_category_list
from celery_app.tesktwo import download2
from celery_app import app

if __name__ == '__main__':

    # for page in range(100):
    #     url = 'http://www.baidu.com/'+str(page)
    #     #delay发送异步消息任务
    #     download1.delay(url)
    #     # download1.apply_async(url)
    #     # app.send_task('celery_app.teskone.download1',args=(url,))
    #     download2.delay(url)
    url = 'http://www.xiachufang.com/category/'
    crawl_category_list.delay(url)
