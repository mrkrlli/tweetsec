# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################
import password_eval

def evaluator():
    if "password" in request.vars:
        password = request.vars.password
        password_strength = password_eval.numerical_strength_value(password)
        if password_strength >= 50:
            return "Congrats on the strong password"
        elif 10< password_strength <50:
            #return a modified version of the password that is strong
            if len(password)>=13:
                #replacing the first 4 chars with 4 different char types will ensure that the pw strength is strong IF there are >= 13 chars
                password = " #a1" + password[4:len(password)]
            else:
                #add 4 different char types to the beginning of the password, and add spaces at the end as necessary to reach required # of chars for strong pw
                password = " #a1" + password + (" "* (13 - (4+len(password))))

            return password

        elif password_strength <= 10:
            return "Please try a better password"

    return

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    response.flash = T("Hello World")
    return dict(message=T('Welcome to web2py!'))


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


