# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    response.flash = T("Hello World")
    redirect(URL('default', 'home'))
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

@auth.requires_login()
def home():
	if len(request.args): page=int(request.args[0])
	else: page=0
	items_per_page=10
	limitby=(page*items_per_page,(page+1)*items_per_page+1)
	rows=db().select(db.recipe.ALL,limitby=limitby)
	return dict(rows=rows,page=page,items_per_page=items_per_page)

@auth.requires_membership('manager')
def manager():
	grid=SQLFORM.smartgrid(db.recipe)
	return locals()


def home_likes():
	if len(request.args): page=int(request.args[0])
	else: page=0
	items_per_page=10
	limitby=(page*items_per_page,(page+1)*items_per_page+1)
	rows=db().select(db.recipe.ALL,limitby=limitby)
	return dict(rows=rows,page=page,items_per_page=items_per_page)

def upload_recipe():
	db.recipe.likes.readable=False
	db.recipe.likes.writable=False
	db.recipe.name.writable=False
	form=SQLFORM(db.recipe)
	if form.process().accepted:
		response.flash="done!"
		var=form.vars.id
		r=db(db.recipe.id==var).select().first()
		r.update_record(likes=0)
	elif form.process().errors:
		response.flash="try again."
	return dict(form=form)

def update_likes():
	i=request.args[0]
	q=db.recipe.id==i
	ans=db(q).select()
	for j in ans:
		m=j
		final = j["likes"] + 1
	m.update_record(likes=final)
	redirect(URL('default', 'home_likes'))

def update_likes_():
	i=request.args[0]
	q=db.recipe.id==i
	ans=db(q).select()
	for j in ans:
		m=j
		final = j["likes"] + 1
	m.update_record(likes=final)
	redirect(URL('default', 'details', args=i))

def my_recipe():
	q=db.recipe.userid==auth.user_id
	var=db(q).select()
	return dict(myr=var)

def edit():
	q=db.recipe.name==auth.user_id
	form=SQLFORM.grid(q)
	return dict(form=form)

def details():
	a=request.args[0]
	q=db.recipe.id==a
	m=db(q).select()
	for i in m:
		ans=i
	db.comments.kisne.readable=False
	db.comments.kisne.writable=False
	db.comments.kisko.default=ans["id"]
	db.comments.kisko.readable=False
	db.comments.kisko.writable=False
	form=SQLFORM(db.comments)
	if form.process().accepted:
	 	response.flash="You commented on this recipe."
	quer=db.comments.kisko==ans["id"]
	com=db(quer).select()
	return dict(ans=ans, form=form, com=com)

def about():
	a="hey there!"
	return dict(a=a)
