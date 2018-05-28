/**
 *Created by wing on 2017/6/23.
 */

function Wing() {
    this.Data = {};

    this.AJAX = function (option) {
        $.ajax({
            type: option.type,
            url: option.url,
            data: option.data,
            contentType: option.contentType,
            processData: option.processData,
            dataType: option.datatype,
            timeout: option.timeout,
            async: option.async,
            success: option.suc,
            error: option.err
        });
    };
    this.checkBrowserVer = function(option){
        return new Date().getTime().toLocaleString();
    };

    this.loadIndexpage = function (option) {

    };

    this.GetHtml = function (option) {
        var opts = $.extend({
            webUrl: "",
			callback: function(data) {}
        }, option);
        $.get(opts.webUrl, opts.callback, "html");
    };

    this.GetJS = function (option) {
		var opts = $.extend({
			webUrl: "",
			callback: function(data) {}
		}, option);
        $.getScript(opts.webUrl, opts.callback);
    };

    this.getVersion =function(){
        var version  = new Date().getTime();
        return version;
    };
}

checkInputEnum = {
    "checkRight" : 3,
    "checkPassword" : 2,
    "checkUserName" : 1
};

function AutoLogin(e){
    var e = e | window.event;
    if(e.code == 21){
        Login();

    }else{

    }

    e.code == 21 ? login():Logout();
    switch (code){
        case 12:
            //TODO dosonmething else
            break;
        default:
            break;
    }
}

