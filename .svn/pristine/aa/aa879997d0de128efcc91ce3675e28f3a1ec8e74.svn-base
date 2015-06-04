$(function(){
// nodejs 
// https://github.com/willian12345/wechat-JS-SDK-demo

(function() {
    // http://paulirish.com/2011/requestanimationframe-for-smart-animating/
    // http://my.opera.com/emoller/blog/2011/12/20/requestanimationframe-for-smart-er-animating
    // requestAnimationFrame polyfill by Erik Möller. fixes from Paul Irish and Tino Zijdel
    // MIT license

    var lastTime = 0;
    var vendors = ['ms', 'moz', 'webkit', 'o'];
    for(var x = 0; x < vendors.length && !window.requestAnimationFrame; ++x) {
        window.requestAnimationFrame = window[vendors[x]+'RequestAnimationFrame'];
        window.cancelAnimationFrame = window[vendors[x]+'CancelAnimationFrame'] 
                                   || window[vendors[x]+'CancelRequestAnimationFrame'];
    }
 
    if (!window.requestAnimationFrame)
        window.requestAnimationFrame = function(callback, element) {
            var currTime = new Date().getTime();
            var timeToCall = Math.max(0, 16 - (currTime - lastTime));
            var id = window.setTimeout(function() { callback(currTime + timeToCall); }, 
              timeToCall);
            lastTime = currTime + timeToCall;
            return id;
        };
 
    if (!window.cancelAnimationFrame)
        window.cancelAnimationFrame = function(id) {
            clearTimeout(id);
        };
}());

$.base64.utf8encode = true;

var utils = {
    encode: function(val){
        return $.base64.btoa(val);
    },
    decode: function(val){
        return $.base64.atob(val, true)
    },
    preImg: function(sourceId, targetId){
        var reader = new FileReader(),
            $img = $(targetId);
        reader.onload = function(){
            console.log(this);
            $img.attr('src',reader.result);
        };
        reader.readAsDataURL($(sourceId)[0].files[0]);
    },
    detectAnimation: function($elem, cb){
        $elem.one('webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend', cb);
    }
};

function SmileScene(){
    this.$pageOne = $('#pageOne'); 
    this.$pageTwo = $('#pageTwo'); 
    this.$pageThree = $('#pageThree'); 
    this.hasName = false; 
    this.currentName = null;
    this.currentRate = null;
    this.rateResults = ['A', 'B', 'C', 'D'];
    this.scene = {
        'A': 'dance',
        'B': 'sunshine',
        'C': 'rainy',
        'D': 'make face'
    };
    this.init();
}
SmileScene.prototype = {
    constructor: SmileScene,
    loadImg: function(container, num, path, extName){
        var extName = extName ? '.' + extName: '.jpg';
        var frag = document.createDocumentFragment();
        for(var i=0; i < num; i++){
            var img = $('<img src="'+path+i+extName+'">')[0];
            frag.appendChild(img);
        }
        container.append(frag);
    },
    sceneIntro: function(){
        var $introPage = $('#introPage'), 
            $allitems = $introPage.find('.intro-item'),
            $intro_bg = $introPage.find('.intro-bg'),
            $intro_bg_main = $introPage.find('.intro-bg-main'),
            $intro_earth = $introPage.find('.intro-earth'),
            $intro_building = $introPage.find('.intro-building');
            $intro_building_main = $introPage.find('.intro-building-main');
        
        $.each([$intro_bg, $intro_earth, $intro_building], function(){
            $(this).addClass('fadeInUp');
        });
        
        utils.detectAnimation($intro_earth, function(){
            $intro_earth.addClass('slideOutUp')
            
            utils.detectAnimation($intro_earth, function(){
                $intro_bg.removeClass('fadeInUp').addClass('fadeOut');
                $intro_bg_main.removeClass('hide').addClass('fadeIn');
                $intro_building.removeClass('fadeInUp').addClass('buildingMoveUp');
                $intro_building_main.removeClass('hide').addClass('fadeInUp');
            });

        });
    },
    sceneOne: function(){
        var self = this;
        var $input = this.$pageOne.find('input:text');
        self.loadImg($('#animateTest'), 72, 'img/test/');


        // test animate

        var progress = 0;
        var allImgs = null;

        function step(timestamp) {
            console.log(progress);
            if(!allImgs){
                allImgs = $('#animateTest img');
            }
            allImgs.eq(progress).removeClass('show');
            progress += 1;
            allImgs.eq(progress).addClass('show');
            if (progress > 71) {
                progress = 0;
            }
            if (progress < 72) {
                requestAnimationFrame(step);
            }
        }
        requestAnimationFrame(step);

        // end test animate

        // this.$pageOne.fadeIn();
        
        this.$pageOne.on('change', '#imgPreBtn', function(){
            utils.preImg(this, '#imgPre');
        });
        
        this.$pageOne.on('keyup', 'input:text', function(){
            if($(this).val()){
                self.hasName = true;
                self.currentName = $(this).val();
                console.log($input.index($(this)));
                $input.not(':eq('+$input.index($(this))+')').attr('disabled','disabled');
            } else {
                self.hasName = false;
                self.currentName = null;
                $input.removeAttr('disabled');
            }
        });

        this.$pageOne.on('click', '#rateBtn', function(){
            if(!self.hasName) {
                alert('请填写名字');
                return false;
            }
            self.$pageOne.fadeOut('slow', function() {
                self.sceneTwo();
            });
        });
    },
    sceneTwo: function(){
        var self = this;
        self.$pageTwo.fadeIn('fast', function() {
            self.currentRate = self.rateResults[parseInt(Math.random()*5-1)];
            $(this).append('微笑评分：' + self.currentRate);
        });
        self.$pageTwo.on('click', '#getResultBtn', function(){
            self.$pageTwo.fadeOut('fast', function() {
                self.sceneThree();
            });
        });
    },
    sceneThree: function(){
        this.$pageThree.fadeIn();

        this.$pageThree.on('click', '#replay', function(){
            
        });
        
        this.$pageThree.append(
            this.currentName+'<br>'+
            this.scene[this.currentRate]+'<br>'+
            utils.encode(this.currentName+this.currentRate));
    },
    init: function(){
        this.sceneIntro();
    }
};

var smileScene = new SmileScene();

// test smile face api js
$('#smileFaceFile').on('change', function(){
    // utils.preImg(this, '#smileFacePreview');
    var data = new FormData();
        data.append('img', this.files[0]);
        data.append('roc', 'wang');
    var reader = new FileReader(),
        $img = $('#smileFacePreview');
    reader.onload = function(){
        $img.attr('src',reader.result);
        console.log(reader.result);
        $.ajax({
            type: 'POST',
            url: '/getfacerate',
            data: data,
            processData: false,
            contentType: false
        }).done(function(data){
            console.log(data);
            $('body').append(data);
        });
        // $.get('/getfacerate', {img:reader.result.split(',')[1]}, function(data){
        //     $('body').append(data);
        // });
    };
    reader.readAsDataURL(this.files[0]);
    
});

});