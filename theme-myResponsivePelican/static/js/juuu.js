/*********************************************
 *             TitleLink 
 *
 *    Odkazy na nadpisy
 **********************************************/
var TitleLink = {};

TitleLink.init = function() {
    $(":header[id]").mouseenter(TitleLink.show);
    $(":header[id]").mouseleave(TitleLink.hide);
    $("div[id] :header").not(":header[id]").mouseenter(TitleLink.showDiv);
    $("div[id] :header").not(":header[id]").mouseleave(TitleLink.hide);
}

TitleLink.show = function(event) {
    var pi = document.createElement("a");
    pi.text='¶';
    pi.href='#'+this.id
    $(pi).css({color:"#aaa", textDecoration:'none'})
    $(pi).hover( function(){
        $(this).css({color:'black', backgroundColor:'white'})
    }, function(){
        $(this).css({color:'#aaa', backgroundColor: $(this).parent().css("backgroundColor")})
    })
    this._ref=pi
    $(this).append(' ')        
    $(this).append(pi)        
}

TitleLink.showDiv = function(event) {
    var pi = document.createElement("a");
    pi.text='¶';
    pi.href='#'+$(this).parent("div[id]").attr('id')
    $(pi).css({color:"#aaa", textDecoration:'none'})
    $(pi).hover( function(){
        $(this).css({color:'black', backgroundColor:'white'})
    }, function(){
        $(this).css({color:'#aaa', backgroundColor: $(this).parent().css("backgroundColor")})
    })
    this._ref=pi
    $(this).append(' ')        
    $(this).append(pi)        
}

TitleLink.hide = function(event) {
    this.removeChild(this._ref)
}

$(document).ready(TitleLink.init);
