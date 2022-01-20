# 멀티플데이터베이스에 대한 정의
class DBRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'thirdapp':
            return 'custom'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'thirdapp':
            return 'custom'
        return None

    def db_for_realation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'thirdapp' or \
                obj2._meta.app_label == 'thirdapp':
            return True
        return None

    def allow_migration(self, db, app_label, model_name=None, **hints):
        if app_label == 'thirdapp':
            return db == 'custom'
        return None
