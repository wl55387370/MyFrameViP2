#coding=utf8
from inter.httpkeys import HTTP

if __name__ == "__main__":
     # h = {
    #     'a':'aa',
    #     'b':'bb'
    # }
    # h.pop('a')
    s = '1+1'
    a=eval(s)
    print(a)

    # http = HTTP()
    # http.seturl('http://112.74.191.10:8081/inter/HTTP')
    # http.addheader('token','0d862fe621ae4bca86489a554945b202')
    # http.post('login','username=Will&password=123456')
    # http.assertequals('status','405')
    #
    # http.addheader('token', None)
    # http.post('auth')
    # http.savejson('token','token')
    # http.addheader('token','{token}')
    # http.post('login', 'username=Will&password=123456')
    # http.assertequals('status', '200')
    #
    # http.addheader('token', '{token}')
    # http.post('login', 'username=Will&password=123456')
    # http.assertequals('status', '406')
    #
    # http.post('logout')
    # http.assertequals('status', '200')
