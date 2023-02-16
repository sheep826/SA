from email import header
from threading import local
from flask import request
import requests
from django.shortcuts import render, redirect
from .models import login, udata
from django.http import HttpResponse, HttpResponseRedirect
# from django.views.decorators.csrf import csrf_exempt

# Create your views here.
ngrok_SACC = "https://10eb-1-34-54-152.jp.ngrok.io"
ngrok_wash = "https://510b-125-229-60-25.ngrok.io"
url_header = {
    'Authorization': 'Token 115973ae686685cbb9ed7ec375511ef0d79a8350',
    'ngrok-skip-browser-warning': '7414'
}
# line_api1
def login_view(request):
    if 'UserID' not in request.session:
        rand = login.objects.create()
        line_api1 = ngrok_SACC+'/RESTapiApp/Line_1/?Rbackurl='+ngrok_wash+'/api_check?fk='+rand.FKcheck
        login_req = requests.get(url=line_api1, headers=url_header)
        #print(req.json())
        login_read = login_req.json()
        #print(req_read["Rstate"])
        login.objects.filter(FKcheck = rand.FKcheck).update(Rstate=login_read["Rstate"])
        login_line = "https://access.line.me/oauth2/v2.1/authorize?response_type=code&client_id=1657781063&redirect_uri="+ngrok_SACC+"/LineLoginApp/callback&state="+login_read["Rstate"]+"&scope=profile%20openid%20email&promot=consent&ui_locales=zh-TW?http://example.com/?ngrok-skip-browser-warning=7414"
        login_sms = "/phone/"
        return render(request, "login.html", locals())
    else:
        return HttpResponseRedirect("/")
# line_api2
def api_check(request):
    if request.method == 'GET':
        fknum = request.GET.get('fk')
        #print(fknum)
        nomatter=login.objects.filter(FKcheck = fknum)
        #print(nomatter)
        sum=''
        for i in nomatter:
            sum=i.Rstate
    #print(sum)
    url = ngrok_SACC+'/RESTapiApp/Line_2/?Rstate='+sum
    req=requests.get(url,headers=url_header)
    req_read = req.json()
    #print(req_read)
    userUID=req_read["RuserID"]
    access_code=req_read["Raccess_code"]
    #print(req_read["Raccess_code"])
    return login_session(request,userUID,access_code)
# 登入控制
def login_session(request,userUID,access_code):
    if udata.objects.filter(UID=userUID):
        udata.objects.filter(UID=userUID).update(UAccess=access_code)
    else:
        udata.objects.create(UID=userUID, UAccess=access_code)
    UID = userUID
    if 'UserID' in request.session:
        try:
            del request.session['UserID']
        except:
            pass
    request.session['UserID'] = UID
    request.session.modified = True
    request.session.set_expiry(60*30) #存在30分鐘
    return HttpResponseRedirect("/")

def index(request):
    #print(req_access(request))
    if 'UserID' not in request.session:
        return HttpResponseRedirect("/login_line")
    else:
        user=req_access(request)
        #print(user)
        pic=user['pic']
        # print(type(pic)) #NoneType
        if pic is None:
            pic="/static/images/user_big.png"
        username=user['username']
        return  render(request, 'index.html', locals())
# 個資請求
def req_access(request):
    if 'UserID' in request.session:
        userdata=udata.objects.get(UID=request.session['UserID'])
        access=userdata.UAccess
        userdata_url=ngrok_SACC+'/RESTapiApp/Access/?Raccess_code='+access
        userdata_req=requests.get(url=userdata_url, headers=url_header)
        userdata_read=userdata_req.json()
        #print(userdata_read)
        username=userdata_read["sNickName"]
        pic=userdata_read["sPictureUrl"]
        user={
            'pic':pic,
            'username':username
        }
        return user
    else:
        return HttpResponseRedirect("/login_line")

def logout(request):
    try:
        del request.session['UserID']
    except:
        return redirect('/login_line')
    return redirect('/login_line')

def register(request):
    return render(request, "register.html")

def phone(request):
    return render(request, "phone.html")
# SMS_api1
# @csrf_exempt
def SMS(request):
    if request.method == 'POST':
        userphone = request.POST.get('userphone')
        print(userphone)
        if len(userphone) == 10 and userphone[:2] == '09':
            context="正確"
            print(context)
            url = ngrok_SACC+'/RESTapiApp/SMS_1/'
            data = {
                'Rphone':userphone
            }
            phone_req = requests.get(url,data, headers=url_header)
            phone_read = phone_req.json()
            RSMSID = phone_read["RSMSid"]
            # RSMSID='RSMSid-4db8b2d9-e1bb-4150-b814-e9facd25f45e'
            return render(request, "SMS.html", locals())

        else:
            context='錯誤'
            print(context)
            return render(request, "phone.html", locals())

    else:
        return render(request, "SMS.html")
# SMS_api2
# @csrf_exempt
def SMScode(request):
    if request.method == "POST":
        RSMSid=request.POST.get('SMSID')
        RSMS_code=request.POST.get('code')
        print(RSMSid)
        print(RSMS_code)
        url = ngrok_SACC+'/RESTapiApp/SMS_2/'
        data = {
            'RSMSid':RSMSid,
            'RSMS_code':RSMS_code,
        }
        phone_req2 = requests.get(url,data, headers=url_header)
        phone_read2 = phone_req2.json()
        userUID=phone_read2["RuserID"]
        access_code=phone_read2["Raccess_code"]
        # return HttpResponseRedirect("/")
        #userUID=""
        #access_code=""
        return login_session(request,userUID,access_code)
    else:
        return render(request, 'SMS.html')