from django.contrib import admin
from django.core.cache import cache

from goods.models import GoodsType, GoodsSKU, Goods, IndexTypeGoodsBanner, IndexPromotionBanner, IndexGoodsBanner


class BaseModelAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        # obj.user = request.user
        super().save_model(request, obj, form, change)
        '''新增或更新表中的数据时调用'''

        # 发出任务，让celery worker重新生成首页静态页
        from celery_tasks.tasks import generate_static_index_html
        generate_static_index_html.delay()

        # 清除首页的缓存数据
        cache.delete('index_page_data')

    def delete_model(self, request, obj):
        '''删除表中的数据时调用'''
        super().delete_model(request, obj)
        # 发出任务，让celery worker重新生成首页静态页
        from celery_tasks.tasks import generate_static_index_html
        generate_static_index_html.delay()

        # 清除首页的缓存数据
        cache.delete('index_page_data')


class GoodsTypeAdmin(BaseModelAdmin):
    pass


class IndexGoodsBannerAdmin(BaseModelAdmin):
    pass


class IndexTypeBannerAdmin(BaseModelAdmin):
    pass


class IndexPromotionBannerAdmin(BaseModelAdmin):
    pass


class GoodsAdmin(BaseModelAdmin):
    pass


class GoodsSkuAdmin(BaseModelAdmin):
    pass


admin.site.register(Goods, GoodsAdmin)
admin.site.register(GoodsSKU, GoodsSkuAdmin)
admin.site.register(GoodsType, GoodsTypeAdmin)
admin.site.register(IndexGoodsBanner, IndexGoodsBannerAdmin)
admin.site.register(IndexTypeGoodsBanner, IndexTypeBannerAdmin)
admin.site.register(IndexPromotionBanner, IndexPromotionBannerAdmin)
