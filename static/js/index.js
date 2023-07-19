function load_menu_money_record_by_kind(val){
        var kind = val;
        
                $.ajax({
                        type:"POST",
                        url:"/load_menu_money_record_by_kind",
                        data:{
                                'kind':kind
                        },
                        datatype:"html",
                                error:function(xhr , ajaxError , throwError){
         	                alert(xhr.status);
               	                alert(xhr.responseText);
	                        alert(throwError);
                                alert(ajaxError)
                        },
                        success:function(res){
                                
                                $("#menu_money_record_list").show(1000).html(res);
                                
                                // scroll page bottom to page top
                                goto_top();
                                
                                //location.reload(true);
                        },
                        beforeSend:function(){
                                $('#status').html("loading " + kind + " 種類記帳本清單 ...").css({'color':'blue'});
                        },
                        complete:function(){
                                $('#status').css({'color':'white'});
                        }
                });

}

function load_menu_money_record_by_day(val){
        var day = val;
        
                $.ajax({
                        type:"POST",
                        url:"/load_menu_money_record_by_day",
                        data:{
                                'day':day
                        },
                        datatype:"html",
                                error:function(xhr , ajaxError , throwError){
         	                alert(xhr.status);
               	                alert(xhr.responseText);
	                        alert(throwError);
                                alert(ajaxError)
                        },
                        success:function(res){
                                
                                $("#menu_money_record_list").show(1000).html(res);
                                
                                // scroll page bottom to page top
                                goto_top();
                                
                                //location.reload(true);
                        },
                        beforeSend:function(){
                                $('#status').html("loading " + day + " 日記帳本清單 ...").css({'color':'blue'});
                        },
                        complete:function(){
                                $('#status').css({'color':'white'});
                        }
                });

}

function load_menu_money_record_by_month(val){
        var month = val;
        
                $.ajax({
                        type:"POST",
                        url:"/load_menu_money_record_by_month",
                        data:{
                                'month':month
                        },
                        datatype:"html",
                                error:function(xhr , ajaxError , throwError){
         	                alert(xhr.status);
               	                alert(xhr.responseText);
	                        alert(throwError);
                                alert(ajaxError)
                        },
                        success:function(res){
                                
                                $("#menu_money_record_list").show(1000).html(res);
                                
                                // scroll page bottom to page top
                                goto_top();
                                
                                //location.reload(true);
                        },
                        beforeSend:function(){
                                $('#status').html("loading " + month + " 月記帳本清單 ...").css({'color':'blue'});
                        },
                        complete:function(){
                                $('#status').css({'color':'white'});
                        }
                });

}

function load_menu_car_record_by_day(val){
        var day = val;
        
                $.ajax({
                        type:"POST",
                        url:"/load_menu_car_record_by_day",
                        data:{
                                'day':day
                        },
                        datatype:"html",
                                error:function(xhr , ajaxError , throwError){
         	                alert(xhr.status);
               	                alert(xhr.responseText);
	                        alert(throwError);
                                alert(ajaxError)
                        },
                        success:function(res){
                                
                                $("#menu_car_record_list").show(1000).html(res);
                                
                                // scroll page bottom to page top
                                goto_top();
                                
                                //location.reload(true);
                        },
                        beforeSend:function(){
                                $('#status').html("loading " + day + " 日用車記錄 ...").css({'color':'blue'});
                        },
                        complete:function(){
                                $('#status').css({'color':'white'});
                        }
                });

}

function load_menu_car_record_by_month(val){
        var month = val;
        
                $.ajax({
                        type:"POST",
                        url:"/load_menu_car_record_by_month",
                        data:{
                                'month':month
                        },
                        datatype:"html",
                                error:function(xhr , ajaxError , throwError){
         	                alert(xhr.status);
               	                alert(xhr.responseText);
	                        alert(throwError);
                                alert(ajaxError)
                        },
                        success:function(res){
                                
                                $("#menu_car_record_list").show(1000).html(res);
                                
                                // scroll page bottom to page top
                                goto_top();
                                
                                //location.reload(true);
                        },
                        beforeSend:function(){
                                $('#status').html("loading " + month + " 月用車記錄 ...").css({'color':'blue'});
                        },
                        complete:function(){
                                $('#status').css({'color':'white'});
                        }
                });

}

function load_menu_car_record_by_year(val){
        var year = val;
        
                $.ajax({
                        type:"POST",
                        url:"/load_menu_car_record_by_year",
                        data:{
                                'year':year
                        },
                        datatype:"html",
                                error:function(xhr , ajaxError , throwError){
         	                alert(xhr.status);
               	                alert(xhr.responseText);
	                        alert(throwError);
                                alert(ajaxError)
                        },
                        success:function(res){
                                
                                $("#menu_car_record_list").show(1000).html(res);
                                
                                // scroll page bottom to page top
                                goto_top();
                                
                                //location.reload(true);
                        },
                        beforeSend:function(){
                                $('#status').html("loading " + year + " 年用車記錄 ...").css({'color':'blue'});
                        },
                        complete:function(){
                                $('#status').css({'color':'white'});
                        }
                });

}

function load_menu_money_record_by_year(val){
        var year = val;
        
                $.ajax({
                        type:"POST",
                        url:"/load_menu_money_record_by_year",
                        data:{
                                'year':year
                        },
                        datatype:"html",
                                error:function(xhr , ajaxError , throwError){
         	                alert(xhr.status);
               	                alert(xhr.responseText);
	                        alert(throwError);
                                alert(ajaxError)
                        },
                        success:function(res){
                                
                                $("#menu_money_record_list").show(1000).html(res);
                                
                                // scroll page bottom to page top
                                goto_top();
                                
                                //location.reload(true);
                        },
                        beforeSend:function(){
                                $('#status').html("loading " + year + " 年記帳本清單 ...").css({'color':'blue'});
                        },
                        complete:function(){
                                $('#status').css({'color':'white'});
                        }
                });

}

function load_menu_calendar_record_by_month(val){
        var month = val;
        
                $.ajax({
                        type:"POST",
                        url:"/load_menu_calendar_record_by_month",
                        data:{
                                'month':month
                        },
                        datatype:"html",
                                error:function(xhr , ajaxError , throwError){
         	                alert(xhr.status);
               	                alert(xhr.responseText);
	                        alert(throwError);
                                alert(ajaxError)
                        },
                        success:function(res){
                                
                                $("#menu_calendar_record_content").show(1000).html(res);
                                
                                // scroll page bottom to page top
                                goto_top();
                                
                                //location.reload(true);
                        },
                        beforeSend:function(){
                                $('#status').html("loading " + month + " 月工作日誌 ...").css({'color':'blue'});
                        },
                        complete:function(){
                                $('#status').css({'color':'white'});
                        }
                });

}

function load_menu_work_record_by_kind(val){
        var kind = val;
        
                $.ajax({
                        type:"POST",
                        url:"/load_menu_work_record_by_kind",
                        data:{
                                'kind':kind
                        },
                        datatype:"html",
                                error:function(xhr , ajaxError , throwError){
         	                alert(xhr.status);
               	                alert(xhr.responseText);
	                        alert(throwError);
                                alert(ajaxError)
                        },
                        success:function(res){
                                
                                $("#menu_work_record_content").show(1000).html(res);
                                
                                // scroll page bottom to page top
                                goto_top();
                                
                                //location.reload(true);
                        },
                        beforeSend:function(){
                                $('#status').html("loading " + kind + " 工作記錄 ...").css({'color':'blue'});
                        },
                        complete:function(){
                                $('#status').css({'color':'white'});
                        }
                });

}

function del_menu_car_record(val){
        
        var del_no = val;
        
        var check_del = prompt("刪除 No." + del_no + " , 確定刪除 , 再按一次 y ");
        
	if(check_del == 'y'){	
                $.ajax({
                        type:"POST",
                        url:"/del_menu_car_record",
                        data:{
                                'del_no':del_no
                        },
                        datatype:"html",
                                error:function(xhr , ajaxError , throwError){
         	                alert(xhr.status);
               	                alert(xhr.responseText);
	                        alert(throwError);
                                alert(ajaxError)
                        },
                        success:function(res){
                                location.reload(true);
                        },
                        beforeSend:function(){
                                $('#menu_money_record_list').show(1000);
                        },
                        complete:function(){
                        }
                });
	}else{
                exit();
        }
}

function del_menu_money_record(val){
        
        var del_no = val;
        
        var check_del = prompt("刪除 No." + del_no + " , 確定刪除 , 再按一次 y ");
        
	if(check_del == 'y'){	
                $.ajax({
                        type:"POST",
                        url:"/del_menu_money_record",
                        data:{
                                'del_no':del_no
                        },
                        datatype:"html",
                                error:function(xhr , ajaxError , throwError){
         	                alert(xhr.status);
               	                alert(xhr.responseText);
	                        alert(throwError);
                                alert(ajaxError)
                        },
                        success:function(res){
                                
                                //$('#menu_money_record_list').show(1000).html(res);
                                
                                // reload menu money record
                                reload_menu_money_record();
                        },
                        beforeSend:function(){
                                //$('#show_msg').html('載入操作紀錄管理中...').css({'color':'blue'}).show();
                                $('#menu_money_record_list').show(1000);
                        },
                        complete:function(){
                                //$('#show_msg').hide();
                        }
                });
	}else{
                exit();
        }
}

function goto_top(){
        
        // scroll page bottom to page top
        jQuery("html,body").animate({scrollTop:0},1000);
        $('#goto_top').css({'cursor':'pointer'});

}

function submit_alter_calendar_record_form(){
        
        var no      = $('#no').val();
        var r_time  = $('#record_time').val();
        var title   = $('#title').val();
        var content = CKEDITOR.instances.content.getData();

        $.ajax({
                type:"POST",
                url:"/submit_alter_calendar_record",
                data:{
                        'no':no,
                        'r_time':r_time,
                        'title':title,
                        'content':content
                },
                datatype:"html",
                error:function(xhr , ajaxError , throwError){
         	      alert(xhr.status);
               	      alert(xhr.responseText);
	              alert(throwError);
                      alert(ajaxError)
                },
                success:function(res){
			
                        alert(title + '  , 修改完成。');
                        location.reload(true);
                },
                beforeSend:function(){
                        //$('#show_msg').html('載入操作紀錄管理中...').css({'color':'blue'}).show();
                        $('#detail_calendar_record_content').show(1000);
                },
                complete:function(){
                        //$('#show_msg').hide();
                }
        });
}

function submit_alter_work_record_form(){
        
        var no      = $('#no').val();
        var r_time  = $('#record_time').val();
        var kind    = $('#kind').val();
        var title   = $('#title').val();
        var content = CKEDITOR.instances.content.getData();

        $.ajax({
                type:"POST",
                url:"/submit_alter_work_record",
                data:{
                        'no':no,
                        'r_time':r_time,
                        'kind':kind,
                        'title':title,
                        'content':content
                },
                datatype:"html",
                error:function(xhr , ajaxError , throwError){
         	      alert(xhr.status);
               	      alert(xhr.responseText);
	              alert(throwError);
                      alert(ajaxError)
                },
                success:function(res){
			//$("#content").css({'border':'#cccccc 1px solid'});
        	       	//$("#detail_work_record_content").show(1000).html(res);
                        
                        alert(kind + ' - ' + title + '  , 修改完成。');

                        location.reload(true);
                        // load alter  detail work record
                        //detail_work_record(no);

                        // reload menu work record
                        //reload_menu_work_record();
                },
                beforeSend:function(){
                        //$('#show_msg').html('載入操作紀錄管理中...').css({'color':'blue'}).show();
                        $('#detail_work_record_content').show(1000);
                },
                complete:function(){
                        //$('#show_msg').hide();
                }
        });
        

}

function detail_calendar_record(val){
        
        var no = val;
        
        // scroll to top 
        jQuery("html,body").animate({scrollTop:0},1000);

        $.ajax({
                type:"POST",
                url:"/detail_calendar_record",
                data:{
                        'no':no
                },
                datatype:"html",
                error:function(xhr , ajaxError , throwError){
         	      alert(xhr.status);
               	      alert(xhr.responseText);
	              alert(throwError);
                      alert(ajaxError)
                },
                success:function(res){
			//$("#content").css({'border':'#cccccc 1px solid'});
                        
        	       	$("#detail_calendar_record_content").show(1000).html(res);
                },
                beforeSend:function(){
                        //$('#show_msg').html('載入操作紀錄管理中...').css({'color':'blue'}).show();
                        $('#detail_calendar_record_content').show(1000);
                },
                complete:function(){
                        //$('#show_msg').hide();
                }
        });
}

function detail_work_record(val){

        var no = val;
        
        // scroll to top 
        jQuery("html,body").animate({scrollTop:0},1000);

        $.ajax({
                type:"POST",
                url:"/detail_work_record",
                data:{
                        'no':no
                },
                datatype:"html",
                error:function(xhr , ajaxError , throwError){
         	      alert(xhr.status);
               	      alert(xhr.responseText);
	              alert(throwError);
                      alert(ajaxError)
                },
                success:function(res){
			//$("#content").css({'border':'#cccccc 1px solid'});
        	       	$("#detail_work_record_content").show(1000).html(res);
                },
                beforeSend:function(){
                        $('#status').html("loading " + no + " 工作記錄 ...").css({'color':'blue'});
                },
                complete:function(){
                        $('#status').css({'color':'white'});
                }
        });
}

function submit_add_calendar_record_form(){
        
        var user = $('#user').val();
        var date = $('#date').val();
        var title = $('#title').val();
        var content = CKEDITOR.instances.content.getData();
        var data = date.split('-')
        var r_year = data[0];
        var r_month = data[1];

        //alert(user + ' / ' + date + ' / ' + content + ' / ' + title + ' / ' + r_year + ' / ' + r_month)

        // check title
	if(title.length == 0){
	        /// show msg
                $("#title").css({'border-bottom-color':'red'});
		$("#show_msg").css({'color':'red'}).html("<i class='bi bi-x-circle-fill'></i> 工作日誌標體不能空白 !!!");
	        exit;
	}
        // check content 
	if(content.length == 0){
	        /// show msg
                $("#content").css({'border-bottom-color':'red'});
		$("#show_msg").css({'color':'red'}).html("<i class='bi bi-x-circle-fill'></i> 工作日誌內容不能空白 !!!");
	        exit;
	}

        $.ajax({
                type:"POST",
                url:"/submit_add_calendar_record_form",
                data:{
                        'user':user,
                        'date':date,
                        'title':title,
                        'content':content,
                        'r_year':r_year,
                        'r_month':r_month
                },
                datatype:"html",
                error:function(xhr , ajaxError , throwError){
         	      alert(xhr.status);
               	      alert(xhr.responseText);
	              alert(throwError);
                      alert(ajaxError)
                },
                success:function(res){
                        //console.log(res.validate);
			//$("#content").css({'border':'#cccccc 1px solid'});
        	       	//$("#add_content").show(1000).html(res);
                        
                        // clean value
                        $("#show_msg").val('');
                        $('#title').val('');
                        $('#content').val('');
                        
                        // reload menu calendar record
                        reload_menu_calendar_record();
                },
                beforeSend:function(){
                        //$('#show_msg').html('載入操作紀錄管理中...').css({'color':'blue'}).show();
                        $('#add_content').show(1000);
                },
                complete:function(){
                        //$('#show_msg').hide();
                }
        });     
}

function submit_add_work_record_form(){
        
        var user = $('#user').val();
        var date = $('#date').val();
        var kind = $('#kind').val();
        var title = $('#title').val();
        var content = CKEDITOR.instances.content.getData();

        //alert(user + ' / ' + date + ' / ' + kind + ' / ' + money + ' / ' + content + ' / ' + record_year + ' / ' + record_month + ' / ' + record_day)
        
        // check kind 
	if(kind.length == 0){
	        /// show msg
                $("#kind").css({'border-bottom-color':'red'});
		$("#show_msg").css({'color':'red'}).html("<i class='bi bi-x-circle-fill'></i> 工作記錄種類不能空白 !!!");
	        exit;
	}
        // check title
	if(title.length == 0){
	        /// show msg
                $("#title").css({'border-bottom-color':'red'});
		$("#show_msg").css({'color':'red'}).html("<i class='bi bi-x-circle-fill'></i> 工作記錄標體不能空白 !!!");
	        exit;
	}
        // check content 
	if(content.length == 0){
	        /// show msg
                $("#content").css({'border-bottom-color':'red'});
		$("#show_msg").css({'color':'red'}).html("<i class='bi bi-x-circle-fill'></i> 工作記錄內容不能空白 !!!");
	        exit;
	}

        $.ajax({
                type:"POST",
                url:"/submit_add_work_record_form",
                data:{
                        'user':user,
                        'date':date,
                        'kind':kind,
                        'title':title,
                        'content':content
                },
                datatype:"html",
                error:function(xhr , ajaxError , throwError){
         	      alert(xhr.status);
               	      alert(xhr.responseText);
	              alert(throwError);
                      alert(ajaxError)
                },
                success:function(res){
                        //console.log(res.validate);
			//$("#content").css({'border':'#cccccc 1px solid'});
        	       	//$("#add_content").show(1000).html(res);
                        
                        // clean show msg value
                        $("#show_msg").val('');
                        
                        // reload menu work record
                        reload_menu_work_record();
                },
                beforeSend:function(){
                        //$('#show_msg').html('載入操作紀錄管理中...').css({'color':'blue'}).show();
                        $('#add_content').show(1000);
                },
                complete:function(){
                        //$('#show_msg').hide();
                }
        });        

}

function submit_add_car_record_form(){
        
        var user = $('#user').val();
        var date = $('#date').val();
        var kind = $('#kind').val();
        var go_out_km = $('#go_out_km').val();
        var go_home_km = $('#go_home_km').val();
        var total_used_km = go_home_km - go_out_km;
        var destination = $('#destination').val();
        var data = date.split('-');
        var r_year = data[0];
        var r_month = data[0]+'-'+data[1];
        var r_day = data[2];

        
        // check kind 
	if(kind.length == 0){
	        /// show msg
                $("#kind").css({'border-bottom-color':'red'});
		$("#show_msg").css({'color':'red'}).html("<i class='bi bi-x-circle-fill'></i> 用車種類不能空白 !!!");
	        exit;
	}
        // check go_home_km
	if(go_home_km.length == 0){
	        /// show msg
                $("#go_home_km").css({'border-bottom-color':'red'});
		$("#show_msg").css({'color':'red'}).html("<i class='bi bi-x-circle-fill'></i> 入庫里程不能空白 !!!");
	        exit;
	}
        // check destination
	if(destination.length == 0){
	        /// show msg
                $("#destination").css({'border-bottom-color':'red'});
		$("#show_msg").css({'color':'red'}).html("<i class='bi bi-x-circle-fill'></i> 用車記錄內容不能空白 !!!");
	        exit;
	}



        $.ajax({
                type:"POST",
                url:"/submit_add_car_record_form",
                data:{
                        'user':user,
                        'date':date,
                        'kind':kind,
                        'go_out_km':go_out_km,
                        'go_home_km':go_home_km,
                        'total_used_km':total_used_km,
                        'destination':destination,
                        'r_year':r_year,
                        'r_month':r_month,
                        'r_day':r_day
                },
                datatype:"html",
                error:function(xhr , ajaxError , throwError){
         	      alert(xhr.status);
               	      alert(xhr.responseText);
	              alert(throwError);
                      alert(ajaxError)
                },
                success:function(res){
                        
                        //alert('ok');
                        //$("#add_content").show(1000).html(res);
                        
                        // clean show msg value
                        //$("#show_msg").val('');
                        
                        // reload menu money record
                        //reload_menu_money_record();
                        location.reload(true);
                        
                },
                beforeSend:function(){
                        //$('#show_msg').html('載入操作紀錄管理中...').css({'color':'blue'}).show();
                        $('#add_content').show(1000);
                },
                complete:function(){
                        //$('#show_msg').hide();
                }
        });        

}

function submit_add_money_record_form(){
        
        var user = $('#user').val();
        var date = $('#date').val();
        var kind = $('#kind').val();
        var money = $('#money').val();
        var content = $('#content').val();
        var data1 = date.split(' ')
        var data2 = data1[0].split('-')
        var record_year = data2[0];
        var record_month = data2[1];
        var record_day = data2[2];

        //alert(user + ' / ' + date + ' / ' + kind + ' / ' + money + ' / ' + content + ' / ' + record_year + ' / ' + record_month + ' / ' + record_day)
        
        // check kind 
	if(kind.length == 0){
	        /// show msg
                $("#kind").css({'border-bottom-color':'red'});
		$("#show_msg").css({'color':'red'}).html("<i class='bi bi-x-circle-fill'></i> 記帳表種類不能空白 !!!");
	        exit;
	}
        // check money
	if(money.length == 0){
	        /// show msg
                $("#money").css({'border-bottom-color':'red'});
		$("#show_msg").css({'color':'red'}).html("<i class='bi bi-x-circle-fill'></i> 記帳表花費不能空白 !!!");
	        exit;
	}
        // check content 
	if(content.length == 0){
	        /// show msg
                $("#content").css({'border-bottom-color':'red'});
		$("#show_msg").css({'color':'red'}).html("<i class='bi bi-x-circle-fill'></i> 記帳表內容不能空白 !!!");
	        exit;
	}

        $.ajax({
                type:"POST",
                url:"/submit_add_money_record_form",
                data:{
                        'user':user,
                        'date':date,
                        'kind':kind,
                        'money':money,
                        'content':content,
                        'record_year':record_year,
                        'record_month':record_month,
                        'record_day':record_day
                },
                datatype:"html",
                error:function(xhr , ajaxError , throwError){
         	      alert(xhr.status);
               	      alert(xhr.responseText);
	              alert(throwError);
                      alert(ajaxError)
                },
                success:function(res){
                        
                        $("#add_content").show(1000).html(res);
                        
                        // clean show msg value
                        $("#show_msg").val('');
                        
                        // reload menu money record
                        //reload_menu_money_record();

                        location.reload(true);
                },
                beforeSend:function(){
                        //$('#show_msg').html('載入操作紀錄管理中...').css({'color':'blue'}).show();
                        $('#add_content').show(1000);
                },
                complete:function(){
                        //$('#show_msg').hide();
                }
        });        

}

function reload_menu_money_record_by_day(){
        $.ajax({
                type:"GET",
                url:"/reload_menu_money_record_by_day",
                //url:"/menu_calendar_record",
                data:{},
                datatype:"html",
                error:function(xhr , ajaxError , throwError){
         	      alert(xhr.status);
               	      alert(xhr.responseText);
	              alert(throwError);
                },
                success:function(res){
                        
                        location.reload(true);
                        $("#money_record_by_day").show(1000).html(res);  
                },
                beforeSend:function(){
                        $('#status').html("loading 記帳本 ...").css({'color':'blue'});
                },
                complete:function(){
                        $('#status').css({'color':'white'});
                }
        });                
}

function reload_menu_car_record(){
        $.ajax({
                type:"GET",
                url:"/reload_menu_car_record",
                //url:"/menu_calendar_record",
                data:{},
                datatype:"html",
                error:function(xhr , ajaxError , throwError){
         	      alert(xhr.status);
               	      alert(xhr.responseText);
	              alert(throwError);
                },
                success:function(res){
                        
                        location.reload(true);
                        $("#menu_car_record_list").show(1000).html(res);  
                },
                beforeSend:function(){
                        $('#status').html("loading 用車記錄 ...").css({'color':'blue'});
                },
                complete:function(){
                        $('#status').css({'color':'white'});
                }
        });                
}

function reload_menu_money_record(){
        $.ajax({
                type:"GET",
                url:"/reload_menu_money_record",
                //url:"/menu_calendar_record",
                data:{},
                datatype:"html",
                error:function(xhr , ajaxError , throwError){
         	      alert(xhr.status);
               	      alert(xhr.responseText);
	              alert(throwError);
                },
                success:function(res){
                        
                        location.reload(true);
                        $("#menu_money_record_list").show(1000).html(res);  
                },
                beforeSend:function(){
                        $('#status').html("loading 記帳本 ...").css({'color':'blue'});
                },
                complete:function(){
                        $('#status').css({'color':'white'});
                }
        });                
}

function reload_menu_calendar_record(){
        $.ajax({
                type:"GET",
                url:"/reload_menu_calendar_record",
                //url:"/menu_calendar_record",
                data:{},
                datatype:"html",
                error:function(xhr , ajaxError , throwError){
         	      alert(xhr.status);
               	      alert(xhr.responseText);
	              alert(throwError);
                },
                success:function(res){
                        
                        location.reload(true);
                        $("#main_content").show(1000).html(res);  
                },
                beforeSend:function(){
                        $('#status').html("loading 工作日誌 ...").css({'color':'blue'});
                },
                complete:function(){
                        $('#status').css({'color':'white'});
                }
        });                
}

function reload_menu_work_record(){
        $.ajax({
                type:"GET",
                url:"/reload_menu_work_record",
                data:{},
                datatype:"html",
                error:function(xhr , ajaxError , throwError){
         	      alert(xhr.status);
               	      alert(xhr.responseText);
	              alert(throwError);
                },
                success:function(res){
                        
                        $("#menu_work_record_content").html(res);  
                        location.reload(true);
                },
                beforeSend:function(){
                        $('#status').html("loading 工作記錄 ...").css({'color':'blue'});
                },
                complete:function(){
                        $('#status').css({'color':'white'});
                }
        });                
}

function select_car_record_kind(val){
        var data = val;
        $('#kind').val(data);

        // select go out km 
        $.ajax({
                type:"POST",
                url:"/select_car_record_by_go_out_km",
                data:{
                        'kind':val
                },
                datatype:"html",
                error:function(xhr , ajaxError , throwError){
         	      alert(xhr.status);
               	      alert(xhr.responseText);
	              alert(throwError);
                      alert(ajaxError)
                },
                success:function(res){

                        $('#go_out_km').val(res);
                },
                beforeSend:function(){
                        $('#detail_calendar_record_content').show(1000);
                },
                complete:function(){
                        
                }
        });

}

function select_money_record_kind(val){
        var data = val;
        $('#kind').val(data);
}

function del_alter_calendar_record_form(){
        
        var no = $('#no').val();

        var check_del = prompt("刪除 No." + no + " ， 確定請再按一次 y : ");
	if(check_del != 'y'){	
                exit();
	}else{

                $.ajax({
                type:"POST",
                url:"/del_alter_calendar_record_form",
                data:{
                        'no':no
                },
                datatype:"html",
                error:function(xhr , ajaxError , throwError){
         	      alert(xhr.status);
               	      alert(xhr.responseText);
	              alert(throwError);
                      alert(ajaxError)
                },
                success:function(res){

                        $('#detail_calendar_record_content').hide(1000);
                        
                        // reload menu calendar record
                        reload_menu_calendar_record();
                },
                beforeSend:function(){
                        //$('#show_msg').html('載入操作紀錄管理中...').css({'color':'blue'}).show();
                        $('#detail_calendar_record_content').show(1000);
                },
                complete:function(){
                        //$('#show_msg').hide();
                }
                });
        }
}

function cancel_add_work_record_form(){
        $('#kind').val('');
        $('#content').val('');
        $('#title').val('');

        $("#add_work_form").hide(1000);
        location.reload(true);
}

function cancel_add_money_record_form(){
        $('#kind').val('');
        $('#content').val('');
        $('#money').val('');

        $("#add_money_form").hide(1000);
        location.reload(true);
}

function add_calendar_record(){
        
        // scroll page bottom to page top 
        jQuery("html,body").animate({scrollTop:0},1000);

        $.ajax({
                type:"GET",
                url:"/add_calendar_record_form",
                data:{},
                datatype:"html",
                error:function(xhr , ajaxError , throwError){
         	      alert(xhr.status);
               	      alert(xhr.responseText);
	              alert(throwError);
                },
                success:function(res){
			
                        //$("#content").css({'border':'#cccccc 1px solid'});
        	       	$("#add_content").show(1000).html(res);

                        // hide alter work record form content
                        $('#detail_work_record_content').hide(1000);
                },
                beforeSend:function(){
                        //$('#show_msg').html('載入操作紀錄管理中...').css({'color':'blue'}).show();
                        $('#add_content').show(1000);
                },
                complete:function(){
                        //$('#show_msg').hide();
                }
        });        
}

function add_work_record(){
        
        // scroll to top 
        jQuery("html,body").animate({scrollTop:0},1000);

        $.ajax({
                type:"GET",
                url:"/add_work_record_form",
                data:{},
                datatype:"html",
                error:function(xhr , ajaxError , throwError){
         	      alert(xhr.status);
               	      alert(xhr.responseText);
	              alert(throwError);
                },
                success:function(res){
			
                        //$("#content").css({'border':'#cccccc 1px solid'});
        	       	$("#add_content").show(1000).html(res);

                        // hide alter work record form content
                        $('#detail_work_record_content').hide(1000);
                },
                beforeSend:function(){
                        //$('#show_msg').html('載入操作紀錄管理中...').css({'color':'blue'}).show();
                        $('#add_content').show(1000);
                },
                complete:function(){
                        //$('#show_msg').hide();
                }
        });        
}

function add_car_record(){
        $.ajax({
                type:"GET",
                url:"/add_car_record_form",
                data:{},
                datatype:"html",
                error:function(xhr , ajaxError , throwError){
         	      alert(xhr.status);
               	      alert(xhr.responseText);
	              alert(throwError);
                },
                success:function(res){
			//$("#content").css({'border':'#cccccc 1px solid'});
        	       	$("#add_content").show(1000).html(res);
                               
                },
                beforeSend:function(){
                        //$('#show_msg').html('載入操作紀錄管理中...').css({'color':'blue'}).show();
                        $('#add_content').show(1000);
                },
                complete:function(){
                        //$('#show_msg').hide();
                }
        });        
}

function add_website_record(){
        $.ajax({
                type:"GET",
                url:"/add_website_record_form",
                data:{},
                datatype:"html",
                error:function(xhr , ajaxError , throwError){
         	      alert(xhr.status);
               	      alert(xhr.responseText);
	              alert(throwError);
                },
                success:function(res){
			//$("#content").css({'border':'#cccccc 1px solid'});
        	       	$("#add_content").show(1000).html(res);
                               
                },
                beforeSend:function(){
                        //$('#show_msg').html('載入操作紀錄管理中...').css({'color':'blue'}).show();
                        $('#add_content').show(1000);
                },
                complete:function(){
                        //$('#show_msg').hide();
                }
        });        
}


function add_money_record(){
        $.ajax({
                type:"GET",
                url:"/add_money_record_form",
                data:{},
                datatype:"html",
                error:function(xhr , ajaxError , throwError){
         	      alert(xhr.status);
               	      alert(xhr.responseText);
	              alert(throwError);
                },
                success:function(res){
			//$("#content").css({'border':'#cccccc 1px solid'});
        	       	$("#add_content").show(1000).html(res);
                               
                },
                beforeSend:function(){
                        //$('#show_msg').html('載入操作紀錄管理中...').css({'color':'blue'}).show();
                        $('#add_content').show(1000);
                },
                complete:function(){
                        //$('#show_msg').hide();
                }
        });        
}
