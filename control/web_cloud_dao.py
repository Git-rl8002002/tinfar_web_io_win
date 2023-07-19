#!/usr/bin/python3

'''
 Author   : JasonHung
 Date     : 20221102
 Function : web io cloud platform
'''

import re
import time
import pymysql

class web_cloud_dao:

    google_map = {'gmk':'AIzaSyAmhv9IuoTu8kMAHxp8O6sgMJlKB0Nq_wc'}
    param      = {'title':'Web Cloud'}
    db_mysql   = {'host':'192.168.1.18','port':'3306','user':'backup','pwd':'SLbackup#123','db':'tinfar','charset':'utf8'}
    db2_mysql  = {'host':'192.168.1.18','port':'3306','user':'backup','pwd':'SLbackup#123','db':'database_system','charset':'utf8'}
    db3_mysql  = {'host':'192.168.1.18','port':'3306','user':'backup','pwd':'SLbackup#123','db':'scraping','charset':'utf8'}
    
    ##############################
    # __connect__ , DB : tinfar
    ##############################
    def __connect__(self):
        try:
            self.conn = pymysql.connect(host=web_cloud_dao.db_mysql['host'],user=web_cloud_dao.db_mysql['user'],password=web_cloud_dao.db_mysql['pwd'],database=web_cloud_dao.db_mysql['db'],charset=web_cloud_dao.db_mysql['charset'])
            self.curr = self.conn.cursor()
        except Exception as e:
            print("<< ERROR >> __conn__ TINFAR mysql failed : " + str(e))

    ###############################
    # __disconnect , DB : tinfar
    ###############################
    def __disconnect__(self):
        try:
            self.conn.close()
        except Exception as e:
            print("<< ERROR >> __disconn__ TINFAR mysql failed : " + str(e))

    ###################################
    # __connect2__ , DB : database_system
    ###################################
    def __connect2__(self):
        try:
            self.conn2 = pymysql.connect(host=web_cloud_dao.db2_mysql['host'],user=web_cloud_dao.db2_mysql['user'],password=web_cloud_dao.db2_mysql['pwd'],database=web_cloud_dao.db2_mysql['db'],charset=web_cloud_dao.db2_mysql['charset'])
            #self.conn2 = pymysql.connect(host='192.168.0.100',port=5306,user='SUPERUI',password='1qaz#123',database='database_system',charset='utf8')
            self.curr2 = self.conn2.cursor()
        except Exception as e:
            print("<< Error >> __connect2__ database_system mysql fail : " + str(e))

    ###########################################
    # __disconnect2__ , DB : database_system
    ###########################################
    def __disconnect2__(self):
        try:
            self.conn2.close
        except Exception as e:
            print("<< Error >> __disconnect2__ database_system mysql fail : " + str(e))

    #################################
    # __connect3__ , DB : scraping
    #################################
    def __connect3__(self):
        try:
            self.conn3 = pymysql.connect(host=web_cloud_dao.db3_mysql['host'],user=web_cloud_dao.db3_mysql['user'],password=web_cloud_dao.db3_mysql['pwd'],database=web_cloud_dao.db3_mysql['db'],charset=web_cloud_dao.db3_mysql['charset'])
            self.curr3 = self.conn3.cursor()
        except Exception as e:
            print("<< Error >> __connection3__ scraping mysql fail : " + str(e))
    
    ####################################
    # __disconnect3__ , DB : scraping
    ####################################
    def __disconnect3__(self):
        try:
            self.conn3.close
        except Exception as e:
            print("<< Error >> __disconnect3__ scraping mysql fail : " + str(e))

    ##################
    # web_cloud
    ##################
    def web_cloud(self):
        try:
            
            self.__connect2__()
            self.sql = "select date , content from work_record where title='WebCloud'"
            self.curr2.execute(self.sql)
            self.res = self.curr2.fetchall()
            self.conn2.commit()

            return self.res

        except Exception as e:
            print("<< Error >> scraping film : " + str(e))
        finally:
            self.__disconnect2__()

    ##################
    # scraping_film
    ##################
    def scraping_film(self):
        try:
            
            self.__connect3__()
            self.sql = "select r_time , title , url from scraping_film order by no desc limit 0,100"
            self.curr3.execute(self.sql)
            self.res = self.curr3.fetchall()
            self.conn3.commit()

            return self.res

        except Exception as e:
            print("<< Error >> scraping film : " + str(e))
        finally:
            self.__disconnect3__()

    ##################
    # scraping_news
    ##################
    def scraping_news(self):
        try:
            
            self.__connect3__()
            self.sql = "select r_time , title , url , kind from scraping_news order by no desc limit 0,100"
            self.curr3.execute(self.sql)
            self.res = self.curr3.fetchall()
            self.conn3.commit()

            return self.res

        except Exception as e:
            print("<< Error >> scraping news : " + str(e))
        finally:
            self.__disconnect3__()

    #####################
    # operation_record
    #####################
    def operation_record(self,r_time,user,login_code,item):
        try:
            self.r_time = r_time
            self.user = user
            self.item = item
            self.login_code = login_code

            self.__connect2__()
            self.sql = "insert into operation_record(r_time,user,item,login_code) value('{0}','{1}','{2}','{3}')".format(self.r_time , self.user , self.item , self.login_code)
            self.curr2.execute(self.sql)
            self.conn2.commit()

        except Exception as e:
            print("<< Error >> operation record : " + str(e))
        finally:
            self.__disconnect2__()

    #####################
    # check_login_code
    #####################
    def check_login_code(self,user,login_code):
        try:
            self.user = user
            self.login_code = login_code

            self.__connect2__()
            self.sql = "select login_code from account_inout_record where user='{0}' order by no desc limit 0,1".format(self.user)
            self.curr2.execute(self.sql)
            self.conn2.commit()
            self.res = self.curr2.fetchone()

            if self.res[0] == self.login_code:
                return 'ok'

        except Exception as e:
            print("<< Error >> check login code : " + str(e))
        finally:
            self.__disconnect2__()

    ##########
    # login
    ##########
    def login(self,user,pwd):
        try:
            self.user = user
            self.pwd = pwd

            self.__connect2__()

            self.sql = "select lv from account where user='{0}' and pwd='{1}' and status='run'".format(self.user , self.pwd)
            self.curr2.execute(self.sql)
            self.conn2.commit()
            self.res = self.curr2.fetchone()
            return self.res

        except Exception as e:
            print("<< Error >> login : " + str(e))
        finally:
            self.__disconnect2__()
        
    #################
    # login_record   
    ################# 
    def login_record(self,user,login_code,r_time,ip):
        try:
            self.user = user
            self.login_code = login_code
            self.r_time = r_time
            self.ip = ip

            self.__connect2__()

            self.sql = "insert into account_inout_record(user,login_code,login,ip) value('{0}','{1}','{2}','{3}')".format(self.user , self.login_code , self.r_time , self.ip)
            self.curr2.execute(self.sql)
            self.conn2.commit()

        except Exception as e:
            print("<< Error >> login record : " + str(e))
        finally:
            self.__disconnect2__()
    
    ##################
    # logout_record
    ##################
    def logout_record(self,user,login_code,r_time):
        try:
            self.user = user
            self.login_code = login_code
            self.r_time = r_time

            self.__connect2__()    

            self.sql = "update account_inout_record set logout='{0}' where login_code='{1}' and user='{2}'".format(self.r_time , self.login_code , self.user)
            self.curr2.execute(self.sql)
            self.conn2.commit()

        except Exception as e:
            print("<< Error >> logout record : " + str(e))
        finally:
            self.__disconnect2__()

    ##############################
    # modbus by val total amont
    ##############################
    def modbus_by_val_total_amount(self):
        try:
            self.__connect__()

            self.sql = "select count(distinct val) from modbus_sd where status='ok'"
            self.curr.execute(self.sql)
            self.conn.commit()
            self.res = self.curr.fetchone()

            return self.res[0]

        except Exception as e:
            print("<< Error >> modbus by val total amount : " + str(e))
        finally:
            self.__disconnect__()

    ########################
    # modbus total by val
    ########################
    def modbus_total_by_val(self,tb,kind,status):
        try:
            self.tb = tb
            self.kind = kind
            self.status = status

            self.__connect__()

            self.sql = "select distinct val from {0} where kind='{1}' and status='{2}' order by val desc".format(self.tb , self.kind , self.status)
            self.curr.execute(self.sql)
            self.conn.commit()
            self.res = self.curr.fetchall()

            return self.res

        except Exception as e:
            print("<< Error >> modbus total by val : " + str(e))
        finally:
            self.__disconnect__()
    
    ###############################
    # modbus total by val amount
    ###############################
    def modbus_total_by_val_amount(self,tb,kind,status,val):
        try:
            self.tb = tb
            self.kind = kind
            self.status = status
            self.val = val

            self.__connect__()

            self.sql = "select count(*) from {0} where kind='{1}' and status='{2}' and val='{3}'".format(self.tb , self.kind , self.status , self.val)
            self.curr.execute(self.sql)
            self.res = self.curr.fetchone()
            self.conn.commit()

            if self.res:
                return self.res[0]

        except Exception as e:
            print("<< Error >> modbus total by val amount : " + str(e))
        finally:
            self.__disconnect__()

    #########################
    # modbus totoal amount
    #########################
    def modbus_total_amount(self,tb,kind,status):
        try:
            self.tb = tb
            self.kind = kind
            self.status = status

            self.__connect__()

            self.sql = "select count(*) from {0} where kind='{1}' and status='{2}'".format(self.tb , self.kind , self.status)
            self.curr.execute(self.sql)
            self.conn.commit()
            self.res = self.curr.fetchone()
            
            return self.res[0]

        except Exception as e:
            print("<< Error >> modbus total amount : " + str(e))
        finally:
            self.__disconnect__()

    #########################
    # realtime modbus sensor
    #########################
    def realtime_modbus_sensor(self):
        try:
            self.__connect__()
            self.sql = "select r_time , kind , protocol , val_1 , val_2 from modbus_sensor order by r_time desc limit 0,100"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()
            return self.res

        except Exception as e:
            print("<< Error >> realtime modebus data. " + str(e))
        finally:
            self.__disconnect__()

    ##################
    # modbus_rtu_cw9
    ##################
    def modbus_rtu_cw9(self):
        try:
            self.__connect__()
            self.sql = "select r_time , kind , protocol , val_1 , val_2 , val_3 , val_4 , val_5 , val_6 , val_7 , val_8 , val_9 from modbus_cw9 order by r_time desc limit 0,100"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()
            return self.res

        except Exception as e:
            print("<< Error >> modbus_rtu_cw9 : " + str(e))
        finally:
            self.__disconnect__()

    ##################
    # modbus_rtu_sd
    ##################
    def modbus_rtu_sd(self):
        try:
            self.__connect__()
            self.sql = "select r_time , kind , protocol , val from modbus_sd order by r_time desc limit 0,100"
            self.curr.execute(self.sql)
            self.res = self.curr.fetchall()
            return self.res

        except Exception as e:
            print("<< Error >> modbus_rtu_sd : " + str(e))
        finally:
            self.__disconnect__()


    #############################
    # money record content
    #############################
    def money_record_content(self,user,year,month,day):
        try:
            self.user = user
            self.year = year
            self.month = month
            self.day = day

            self.__connect2__()
            
            # total money
            self.sql = "select content from money_record where account='{0}' and record_year='{1}' and record_month='{2}' and record_day='{3}' order by no desc".format(self.user , self.year , self.month , self.day)
            self.curr2.execute(self.sql)
            self.conn2.commit()
            self.res = self.curr2.fetchall()

            return self.res

        except Exception as e:
            print("<< ERROR >> money record content : " + str(e))
        finally:
            self.__disconnect2__()

    #############################
    # money record total money
    #############################
    def money_record_total_money(self,user,year,month,day):
        try:
            self.user = user
            self.year = year
            self.month = month
            self.day = day

            self.__connect2__()
            
            # total money
            self.sql = "select sum(money) from money_record where account='{0}' and record_year='{1}' and record_month='{2}' and record_day='{3}'".format(self.user , self.year , self.month , self.day)
            self.curr2.execute(self.sql)
            self.conn2.commit()
            self.res = self.curr2.fetchall()
            
            return self.res

        except Exception as e:
            print("<< ERROR >> money record total money : " + str(e))
        finally:
            self.__disconnect2__()

    #################################
    # submit_add_calendar_record_form
    #################################        
    def submit_add_calendar_record_form(self,user,date,title,content,r_year,r_month):
        try:
            self.user = user
            self.date = date
            self.title = title
            self.content = content
            self.r_year = r_year
            self.r_month = r_year + "-" + r_month

            self.__connect2__()

            self.sql = "insert into calendar_content(account,date,content,title,record_year,record_month,line_record,status) value('{0}','{1}','{2}','{3}','{4}','{5}','{6}','enable')".format(self.user , self.date , self.content , self.title , self.r_year , self.r_month , 'server' , 'enable')
            self.res = self.curr2.execute(self.sql)
            self.conn2.commit()

            if self.res:
                return 'ok'

        except Exception as e:
            print("<< Error >> submit_add_calendar_record_form : " + str(e))
        finally:
            self.__disconnect2__()

    #################################
    # submit_add_work_record_form
    #################################
    def submit_add_work_record_form(self,user,date,kind,title,content):
        try:
            self.user = user
            self.date = date
            self.kind = kind
            self.title = title
            self.content = content
            self.line_record = "ok"

            self.__connect2__()

            self.sql = "insert into work_record(account,date,content,title,kind,line_record,status) value('{0}','{1}','{2}','{3}','{4}','{5}','enable')".format(self.user , self.date , self.content , self.title , self.kind , self.line_record)
            self.res = self.curr2.execute(self.sql)
            self.conn2.commit()

            if self.res:
                return 'ok'

        except Exception as e:
            print("<< Error >> submit_add_work_record_form : " + str(e))
        finally:
            self.__disconnect2__()

    #################################
    # submit_add_car_record_form
    #################################
    def submit_add_car_record_form(self,user,date,kind,go_out_km,go_home_km,total_used_km,destination,r_year,r_month,r_day):
        try:
            self.user = user
            self.date = date
            self.kind = kind
            self.go_out_km = go_out_km
            self.go_home_km = go_home_km
            self.total_used_km = total_used_km
            self.destination = destination
            self.r_year = r_year
            self.r_month = r_month
            self.r_day = r_day
            self.status = 'ok'

            self.__connect2__()

            self.sql = "insert into car_record(account,record_time,go_out_km,go_home_km,total_used_km,kind,record_year,record_month,record_day,status,destination) value('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}')".format(self.user , self.date , self.go_out_km , self.go_home_km , self.total_used_km , self.kind , self.r_year , self.r_month , self.r_day , self.status , self.destination)
            self.res = self.curr2.execute(self.sql)
            self.conn2.commit()

            if self.res:
                return 'ok'

        except Exception as e:
            print("<< Error >> submit_add_car_record_form : " + str(e))
        finally:
            self.__disconnect2__()

    #################################
    # submit_add_money_record_form
    #################################
    def submit_add_money_record_form(self,user,date,kind,money,content,record_year,record_month,record_day):
        try:
            self.user = user
            self.date = date
            self.kind = kind
            self.money = money
            self.content = content
            self.record_year = record_year
            self.record_month = record_year + '-' + record_month
            self.record_day = record_day
            self.status = 'ok'

            self.__connect2__()

            self.sql = "insert into money_record(account,record_time,content,money,kind,record_year,record_month,record_day,status) value('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}')".format(self.user , self.date , self.content , self.money , self.kind , self.record_year , self.record_month , self.record_day , self.status)
            self.res = self.curr2.execute(self.sql)
            self.conn2.commit()

            if self.res:
                return 'ok'

        except Exception as e:
            print("<< Error >> submit_add_money_record_form : " + str(e))
        finally:
            self.__disconnect2__()

    ##############################
    # select car record by kind
    ##############################
    def select_car_record_by_kind(self,kind):
        try:

            self.kind = kind
            self.__connect2__()

            self.sql = "select go_home_km from car_record where kind='{0}' order by record_time desc limit 0,1".format(self.kind)
            self.curr2.execute(self.sql)
            self.res = self.curr2.fetchall()
            self.conn2.commit()

            return self.res

        except Exception as e:
            print("<< Error >> add car record kind : " + str(e))
        finally:
            self.__disconnect2__()

    ########################
    # add car record kind
    #########################
    def add_car_record_kind(self,user):
        try:

            self.user = user
            self.__connect2__()

            self.sql = "select distinct kind from car_record where account='{0}' order by kind desc".format(self.user)
            self.curr2.execute(self.sql)
            self.res = self.curr2.fetchall()
            self.conn2.commit()

            return self.res

        except Exception as e:
            print("<< Error >> add car record kind : " + str(e))
        finally:
            self.__disconnect2__()
    
    ############################
    # add website record kind
    ############################
    def add_website_record_kind(self,user):
        try:

            self.user = user
            self.__connect2__()

            self.sql = "select distinct kind from money_record where account='{0}' order by kind desc".format(self.user)
            self.curr2.execute(self.sql)
            self.res = self.curr2.fetchall()
            self.conn2.commit()

            return self.res

        except Exception as e:
            print("<< Error >> add money record kind : " + str(e))
        finally:
            self.__disconnect2__()
    
    ##########################
    # add money record kind
    ##########################
    def add_money_record_kind(self,user):
        try:

            self.user = user
            self.__connect2__()

            self.sql = "select distinct kind from money_record where account='{0}' order by kind desc".format(self.user)
            self.curr2.execute(self.sql)
            self.res = self.curr2.fetchall()
            self.conn2.commit()

            return self.res

        except Exception as e:
            print("<< Error >> add money record kind : " + str(e))
        finally:
            self.__disconnect2__()
    
    ##########################
    # add work record kind
    ##########################

    def add_work_record_kind(self,user):
        try:

            self.user = user
            self.__connect2__()

            self.sql = "select distinct kind from work_record where account='{0}' order by kind desc".format(self.user)
            self.curr2.execute(self.sql)
            self.res = self.curr2.fetchall()
            self.conn2.commit()

            return self.res

        except Exception as e:
            print("<< Error >> add money record kind : " + str(e))
        finally:
            self.__disconnect2__()            

    ##########################
    # money record by day
    ##########################
    def money_record_by_day(self,user,year,month):
        try:
            self.user = user
            self.year = year
            self.month = month

            self.__connect2__()
            
            # day
            self.sql = "select distinct record_day from money_record where account='{0}' and record_year='{1}' and record_month='{2}' order by record_day desc".format(self.user , self.year , self.month)
            self.curr2.execute(self.sql)
            self.conn2.commit()
            self.res = self.curr2.fetchall()

            return self.res

        except Exception as e:
            print("<< ERROR >> money record by day : " + str(e))
        finally:
            self.__disconnect2__()
    
    ##########################
    # money record by month
    ##########################
    def money_record_by_month(self,user,year):
        try:
            self.user = user
            self.year = year

            self.__connect2__()
            
            # month
            self.sql = "select distinct record_month from money_record where account='{0}' and record_year='{1}' order by record_month desc".format(self.user , self.year)
            self.curr2.execute(self.sql)
            self.conn2.commit()
            self.res = self.curr2.fetchall()
            
            return self.res

        except Exception as e:
            print("<< ERROR >> money record by month : " + str(e))
        finally:
            self.__disconnect2__()

    #########################
    # money record by year
    #########################
    def money_record_by_year(self,user):
        try:
            self.user = user

            self.__connect2__()
            
            # year
            self.sql = "select distinct record_year from money_record where account='{0}' order by record_year desc".format(self.user)
            self.curr2.execute(self.sql)
            self.conn2.commit()
            self.res = self.curr2.fetchall()

            return self.res

        except Exception as e:
            print("<< ERROR >> money record by year : " + str(e))
        finally:
            self.__disconnect2__()

    ##################################
    # menu calendar record by year
    ##################################
    def menu_calendar_record_by_year(self,user):
        try:
            self.user = user
            self.__connect2__()

            self.sql = "select record_year , count(*) from calendar_content where account='{0}' and status='enable' group by record_year order by record_year desc".format(self.user)
            self.curr2.execute(self.sql)
            self.res = self.curr2.fetchall()
            self.conn2.commit()

            return self.res

        except Exception as e:
            print("<< Error >> menu work record : " + str(e))
        finally:
            self.__disconnect2__()
    
    ##################################
    # menu calendar record by month
    ##################################
    def menu_calendar_record_by_month(self,user):
        try:
            self.user = user
            self.__connect2__()

            self.sql = "select record_month , count(*) from calendar_content where account='{0}' and status='enable' group by record_month order by record_month desc".format(self.user)
            self.curr2.execute(self.sql)
            self.res = self.curr2.fetchall()
            self.conn2.commit()

            return self.res

        except Exception as e:
            print("<< Error >> menu work record : " + str(e))
        finally:
            self.__disconnect2__()
    
    #########################
    # menu calendar record
    #########################
    def menu_calendar_record(self,user):
        try:
            self.user = user
            self.__connect2__()

            self.sql = "select date , title , line_record , content , no from calendar_content where account='{0}' and status='enable' order by date desc".format(self.user)
            self.curr2.execute(self.sql)
            self.res = self.curr2.fetchall()
            self.conn2.commit()

            return self.res

        except Exception as e:
            print("<< Error >> menu work record : " + str(e))
        finally:
            self.__disconnect2__()

    #############################
    # menu work record by date
    #############################
    def menu_work_record_by_date(self,user):
        try:
            self.user = user
            self.__connect2__()

            self.sql = "select date , count(*) from work_record where account='{0}' and status='enable' group by date order by date desc".format(self.user)
            self.curr2.execute(self.sql)
            self.res = self.curr2.fetchall()
            self.conn2.commit()

            return self.res

        except Exception as e:
            print("<< Error >> menu work record : " + str(e))
        finally:
            self.__disconnect2__()
    
    #############################
    # menu work record by kind
    #############################
    def menu_work_record_by_kind(self,user):
        try:
            self.user = user
            self.__connect2__()

            self.sql = "select kind , count(*) from work_record where account='{0}' and status='enable' group by kind".format(self.user)
            self.curr2.execute(self.sql)
            self.res = self.curr2.fetchall()
            self.conn2.commit()

            return self.res

        except Exception as e:
            print("<< Error >> menu work record by kind : " + str(e))
        finally:
            self.__disconnect2__()

    ##################################
    # load menu money record by kind
    ##################################
    def load_menu_money_record_by_kind(self,user,kind):
        try:
            self.user = user
            self.kind = kind
            self.__connect2__()

            self.sql = "select record_time , kind , money , content , no from money_record where account='{0}' and status='ok' and kind='{1}' order by record_time desc".format(self.user , self.kind)
            self.curr2.execute(self.sql)
            self.res = self.curr2.fetchall()
            self.conn2.commit()

            return self.res

        except Exception as e:
            print("<< Error >> load menu money record by kind : " + str(e))
        finally:
            self.__disconnect2__()

    ##################################
    # load menu money record by day
    ##################################
    def load_menu_money_record_by_day(self,user,day):
        try:
            self.user = user
            self.day = day
            self.__connect2__()

            self.sql = "select record_time , kind , money , content , no from money_record where account='{0}' and status='ok' and record_time='{1}' order by record_time desc".format(self.user , self.day)
            self.curr2.execute(self.sql)
            self.res = self.curr2.fetchall()
            self.conn2.commit()

            return self.res

        except Exception as e:
            print("<< Error >> load menu money record by day : " + str(e))
        finally:
            self.__disconnect2__()
    
    ###################################
    # load menu money record by month
    ###################################
    def load_menu_money_record_by_month(self,user,month):
        try:
            self.user = user
            self.month = month
            self.__connect2__()

            self.sql = "select record_time , kind , money , content , no from money_record where account='{0}' and status='ok' and record_month='{1}' order by record_time desc".format(self.user , self.month)
            self.curr2.execute(self.sql)
            self.res = self.curr2.fetchall()
            self.conn2.commit()

            return self.res

        except Exception as e:
            print("<< Error >> load menu money record by month : " + str(e))
        finally:
            self.__disconnect2__()
    
    ################################
    # load menu car record by day
    ################################
    def load_menu_car_record_by_day(self,user,day):
        try:
            self.user = user
            self.day = day
            self.__connect2__()

            self.sql = "select record_time , go_out_km , go_home_km , total_used_km , kind , destination , no from car_record where account='{0}' and status='ok' and record_time='{1}' order by record_time desc".format(self.user , self.day)
            self.curr2.execute(self.sql)
            self.res = self.curr2.fetchall()
            self.conn2.commit()

            return self.res

        except Exception as e:
            print("<< Error >> load menu car record by day : " + str(e))
        finally:
            self.__disconnect2__()
    
    ##################################
    # load menu car record by month
    ##################################
    def load_menu_car_record_by_month(self,user,month):
        try:
            self.user = user
            self.month = month
            self.__connect2__()

            self.sql = "select record_time , go_out_km , go_home_km , total_used_km , kind , destination , no from car_record where account='{0}' and status='ok' and record_month='{1}' order by record_time desc".format(self.user , self.month)
            self.curr2.execute(self.sql)
            self.res = self.curr2.fetchall()
            self.conn2.commit()

            return self.res

        except Exception as e:
            print("<< Error >> load menu car record by month : " + str(e))
        finally:
            self.__disconnect2__()
    
    #################################
    # load menu car record by year
    #################################
    def load_menu_car_record_by_year(self,user,year):
        try:
            self.user = user
            self.year = year
            self.__connect2__()

            self.sql = "select record_time , go_out_km , go_home_km , total_used_km , kind , destination , no from car_record where account='{0}' and status='ok' and record_year='{1}' order by record_time desc".format(self.user , self.year)
            self.curr2.execute(self.sql)
            self.res = self.curr2.fetchall()
            self.conn2.commit()

            return self.res

        except Exception as e:
            print("<< Error >> load menu car record by year : " + str(e))
        finally:
            self.__disconnect2__()
    
    ###################################
    # load menu money record by year
    ###################################
    def load_menu_money_record_by_year(self,user,year):
        try:
            self.user = user
            self.year = year
            self.__connect2__()

            self.sql = "select record_time , kind , money , content , no from money_record where account='{0}' and status='ok' and record_year='{1}' order by record_time desc".format(self.user , self.year)
            self.curr2.execute(self.sql)
            self.res = self.curr2.fetchall()
            self.conn2.commit()

            return self.res

        except Exception as e:
            print("<< Error >> load menu money record by year : " + str(e))
        finally:
            self.__disconnect2__()
    
    #######################################
    # load menu calendar record by month
    #######################################
    def load_menu_calendar_record_by_month(self,user,month):
        try:
            self.user = user
            self.month = month
            self.__connect2__()

            self.sql = "select date , title , content , no from calendar_content where account='{0}' and status='enable' and record_month='{1}' order by date desc".format(self.user , self.month)
            self.curr2.execute(self.sql)
            self.res = self.curr2.fetchall()
            self.conn2.commit()

            return self.res

        except Exception as e:
            print("<< Error >> load menu calendar record by month : " + str(e))
        finally:
            self.__disconnect2__()
    
    ##################################
    # load menu work record by kind
    ##################################
    def load_menu_work_record_by_kind(self,user,kind):
        try:
            self.user = user
            self.kind = kind
            self.__connect2__()

            self.sql = "select date , kind , title , line_record , content , no from work_record where account='{0}' and status='enable' and kind='{1}' order by no desc".format(self.user , self.kind)
            self.curr2.execute(self.sql)
            self.res = self.curr2.fetchall()
            self.conn2.commit()

            return self.res

        except Exception as e:
            print("<< Error >> load menu work record by kind : " + str(e))
        finally:
            self.__disconnect2__()
    
    #####################
    # menu work record
    #####################
    def menu_work_record(self,user):
        try:
            self.user = user
            self.__connect2__()

            self.sql = "select date , kind , title , line_record , content , no from work_record where account='{0}' and status='enable' order by no desc".format(self.user)
            self.curr2.execute(self.sql)
            self.res = self.curr2.fetchall()
            self.conn2.commit()

            return self.res

        except Exception as e:
            print("<< Error >> menu work record : " + str(e))
        finally:
            self.__disconnect2__()

    ########################
    # del menu car record 
    ########################
    def del_menu_car_record(self,user , del_no):
        try:
            self.user = user
            self.del_no = del_no

            self.__connect2__()
            
            # del menu money record by no
            #self.sql = "delete from money_record where no='{0}' and account='{1}'".format(self.del_no , self.user)
            self.sql = "update car_record set status='no' where no='{0}' and account='{1}'".format(self.del_no , self.user)
            self.res = self.curr2.execute(self.sql)
            self.conn2.commit()

            if self.res:
                return 'ok'

        except Exception as e:
            print("<< ERROR >> menu car record  : " + str(e))
        finally:
            self.__disconnect2__()
    
    ##########################
    # del menu money record 
    ##########################
    def del_menu_money_record(self,user , del_no):
        try:
            self.user = user
            self.del_no = del_no

            self.__connect2__()
            
            # del menu money record by no
            #self.sql = "delete from money_record where no='{0}' and account='{1}'".format(self.del_no , self.user)
            self.sql = "update money_record set status='no' where no='{0}' and account='{1}'".format(self.del_no , self.user)
            self.res = self.curr2.execute(self.sql)
            self.conn2.commit()

            if self.res:
                return 'ok'

        except Exception as e:
            print("<< ERROR >> menu money record  : " + str(e))
        finally:
            self.__disconnect2__()

    #############################
    # menu car record by month 
    #############################
    def menu_car_record_by_month(self,user):
        try:
            self.user = user

            self.__connect2__()
            
            # year
            self.sql = "select record_month , count(*) , sum(total_used_km) from car_record where account='{0}' and status='ok' group by record_month order by record_month desc".format(self.user)
            self.curr2.execute(self.sql)
            self.res = self.curr2.fetchall()
            
            return self.res

        except Exception as e:
            print("<< ERROR >> menu money record by year : " + str(e))
        finally:
            self.__disconnect2__()

    ###############################
    # menu money record by kind 
    ###############################
    def menu_money_record_by_kind(self,user):
        try:
            self.user = user

            self.__connect2__()
            
            # kind
            self.sql = "select kind , count(*) , sum(money) from money_record where account='{0}' and status='ok' group by kind order by kind desc".format(self.user)
            self.curr2.execute(self.sql)
            self.res = self.curr2.fetchall()
            
            return self.res

        except Exception as e:
            print("<< ERROR >> menu money record by kind : " + str(e))
        finally:
            self.__disconnect2__()

    ###############################
    # menu money record by month 
    ###############################
    def menu_money_record_by_month(self,user):
        try:
            self.user = user

            self.__connect2__()
            
            # year
            self.sql = "select record_month , count(*) , sum(money) from money_record where account='{0}' and status='ok' group by record_month order by record_month desc".format(self.user)
            self.curr2.execute(self.sql)
            self.res = self.curr2.fetchall()
            
            return self.res

        except Exception as e:
            print("<< ERROR >> menu money record by year : " + str(e))
        finally:
            self.__disconnect2__()

    ############################
    # menu car record by year 
    ############################
    def menu_car_record_by_year(self,user):
        try:
            self.user = user

            self.__connect2__()
            
            # year
            self.sql = "select record_year , count(*) , sum(total_used_km) from car_record where account='{0}' and status='ok' group by record_year order by record_year desc".format(self.user)
            self.curr2.execute(self.sql)
            self.res = self.curr2.fetchall()
            
            return self.res

        except Exception as e:
            print("<< ERROR >> menu money record by year : " + str(e))
        finally:
            self.__disconnect2__()

    #############################
    # menu money record by year 
    #############################
    def menu_money_record_by_year(self,user):
        try:
            self.user = user

            self.__connect2__()
            
            # year
            self.sql = "select record_year , count(*) , sum(money) from money_record where account='{0}' and status='ok' group by record_year order by record_year desc".format(self.user)
            self.curr2.execute(self.sql)
            self.res = self.curr2.fetchall()
            
            return self.res

        except Exception as e:
            print("<< ERROR >> menu money record by year : " + str(e))
        finally:
            self.__disconnect2__()

    ############################
    # menu car record by day 
    ###########################
    def menu_car_record_by_day(self,user):
        try:
            self.user = user

            self.__connect2__()
            
            # year
            self.sql = "select record_time , count(*) , sum(total_used_km) from car_record where account='{0}' and status='ok' group by record_time order by record_time desc".format(self.user)
            self.curr2.execute(self.sql)
            self.res = self.curr2.fetchall()
            
            return self.res

        except Exception as e:
            print("<< ERROR >> menu money record by day : " + str(e))
        finally:
            self.__disconnect2__()

    #############################
    # menu money record by day 
    #############################
    def menu_money_record_by_day(self,user):
        try:
            self.user = user

            self.__connect2__()
            
            # year
            self.sql = "select record_time , count(*) , sum(money) from money_record where account='{0}' and status='ok' group by record_time order by record_time desc".format(self.user)
            self.curr2.execute(self.sql)
            self.res = self.curr2.fetchall()
            
            return self.res

        except Exception as e:
            print("<< ERROR >> menu money record by day : " + str(e))
        finally:
            self.__disconnect2__()

    ####################
    # menu car record 
    ####################
    def menu_car_record(self,user):
        try:
            self.user = user

            self.__connect2__()
            
            self.sql = "select record_time , go_out_km , go_home_km , total_used_km , kind , destination , no from car_record where account='{0}' and status='ok' order by record_time desc".format(self.user)
            self.curr2.execute(self.sql)
            self.conn2.commit()
            self.res = self.curr2.fetchall()

            return self.res

        except Exception as e:
            print("<< ERROR >> menu car record  : " + str(e))
        finally:
            self.__disconnect2__()

    ########################
    # menu website record 
    ########################
    def menu_website_record(self,user):
        try:
            self.user = user

            self.__connect2__()
            
            # year
            self.sql = "select kind , count(*) from link_page where account='{0}' and status='enable' group by kind order by kind desc".format(self.user)
            self.curr2.execute(self.sql)
            self.conn2.commit()
            self.res = self.curr2.fetchall()

            return self.res

        except Exception as e:
            print("<< ERROR >> menu money record  : " + str(e))
        finally:
            self.__disconnect2__()
    
    ######################
    # menu money record 
    ######################
    def menu_money_record(self,user):
        try:
            self.user = user

            self.__connect2__()
            
            # year
            self.sql = "select record_time , kind , content , money , no from money_record where account='{0}' and status='ok' order by record_time desc".format(self.user)
            self.curr2.execute(self.sql)
            self.conn2.commit()
            self.res = self.curr2.fetchall()

            return self.res

        except Exception as e:
            print("<< ERROR >> menu money record  : " + str(e))
        finally:
            self.__disconnect2__()
    
    ###########################
    # detail calendar record
    ###########################
    def detail_calendar_record(self,no):
        try:
            self.no = no

            self.__connect2__()
            
            self.sql = "select date , title , content , line_record , no from calendar_content where no='{0}'".format(self.no)
            self.curr2.execute(self.sql)
            self.res = self.curr2.fetchall()
            self.conn2.commit()

            return self.res

        except Exception as e:
            print("<< ERROR >> detail work record  : " + str(e))
        finally:
            self.__disconnect2__()
    
    ######################
    # detail work record
    ######################
    def detail_work_record(self,no):
        try:
            self.no = no

            self.__connect2__()
            
            self.sql = "select date , kind , title , content , line_record , no from work_record where no='{0}'".format(self.no)
            self.curr2.execute(self.sql)
            self.res = self.curr2.fetchall()
            self.conn2.commit()

            return self.res

        except Exception as e:
            print("<< ERROR >> detail work record  : " + str(e))
        finally:
            self.__disconnect2__()
    
    ###################################
    # del_alter_calendar_record_form
    ###################################
    def del_alter_calendar_record_form(self,no):
        try:
            self.no = no

            self.__connect2__()
            
            self.sql = "update calendar_content set status='disable' where no='{0}'".format(self.no)
            #self.sql = "delete from calendar_content where no='{0}'".format(self.no)
            self.curr2.execute(self.sql)
            self.res = self.curr2.fetchall()
            self.conn2.commit()

            if self.res:
                return 'ok'

        except Exception as e:
            print("<< ERROR >> del alter calendar record form  : " + str(e))
        finally:
            self.__disconnect2__()

    #################################
    # submit alter calendar record
    #################################
    def submit_alter_calendar_record(self,r_time,no,title,content):
        try:
            self.r_time = r_time
            self.no = no
            self.title = title
            self.content = content

            self.__connect2__()
            
            self.sql = "update calendar_content set title='{0}' , content='{1}' where no='{2}'".format(self.title , self.content , self.no)
            self.curr2.execute(self.sql)
            self.res = self.curr2.fetchall()
            self.conn2.commit()

            if self.res:
                return 'ok'

        except Exception as e:
            print("<< ERROR >> detail work record  : " + str(e))
        finally:
            self.__disconnect2__()

    #############################
    # submit alter work record
    #############################
    def submit_alter_work_record(self,r_time,no,kind,title,content):
        try:
            self.r_time = r_time
            self.no = no
            self.kind = kind
            self.title = title
            self.content = content

            self.__connect2__()
            
            self.sql = "update work_record set kind='{0}' , title='{1}' , content='{2}' , line_record='update' where no='{3}'".format(self.kind , self.title , self.content , self.no)
            self.curr2.execute(self.sql)
            self.res = self.curr2.fetchall()
            self.conn2.commit()

            if self.res:
                return 'ok'

        except Exception as e:
            print("<< ERROR >> detail work record  : " + str(e))
        finally:
            self.__disconnect2__()
