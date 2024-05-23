from flask import make_response, redirect

class users():
    def __init__(self, dbc):
        self.dbc = dbc

    def change_data(self, id, name=None, token=None, permission=None, password=None):
        if name != None:
            self.dbc.users.get(id = id).update(name = name).exec()
        if password != None:
            self.dbc.users.get(id = id).update(password = password).exec()
        if permission != None:
            self.dbc.users.get(id = id).update(permission = permission).exec()
        if token != None:
            self.dbc.users.get(id = id).update(token = token).exec()

    def get_user_by_token(self, token):
        user = self.dbc.users.get(token = token).exec()
        if not user:
            return None
        return user[0]

    def is_login(self, request):
        user = self.get_user_by_token(request.cookies.get("token", None))
        if not user:
            return None
        return user

    def is_admin(self, token):
        user = self.get_user_by_token(token)
        if user['login'] != 'admin':
            return False
        return True

    def get_user_by_login(self, login):
        user = self.dbc.users.get(login = login).exec()
        if not user:
            return None
        return user[0]

    def get_user_by_id(self, id):
        user = self.dbc.users.get(id = id).exec()[0]
        return user

    def find_users(self, name=None, permission=None, direction=None, page=None, limit=None):
        if not page:
            page = 1
        link_adder = "/users?"
        query1 = self.dbc.users
        if permission:
            query1.get(permission = permission)
            link_adder += "permission="+permission+"&"
        if name:
            query1.like(name = name)
            link_adder += "name="+name+"&"
        if direction:
            reverse = direction != "asc"
            query1.order_by("name", reverse)
            link_adder += "direction="+direction+"&"
        query2 = query1.copy()
        count = query2.count().exec()
        query1.per_page(limit)
        page = int(page)
        users = query1.page(page).exec()
        return (users, count, link_adder)

    def authorize(self, login, password, token):
        user = self.dbc.users.get(login = login).get(password = password).update(token = token).get().exec()
        if not user:
            if not self.get_user_by_login(login):
                return 0
            return 1
        return user[0]

    def make_response(self, link, token):
        resp = make_response(redirect(link))
        resp.set_cookie("token", token)
        return resp

    def register(self, **data):
        if self.get_user_by_login(data['login']):
            return 1
        user = self.dbc.users.add(**data).exec()[0]
        return user

    def log_out(self,):
        resp = make_response(redirect("/login"))
        resp.set_cookie("token", "-1", 1)
        return resp