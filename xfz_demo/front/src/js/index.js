// 面向对象
// 添加属性，通过this关键字绑定属性，并指定它的值
// 原型链

/*
function Banner() {
    // 这个里面写的代码,相当于是python中的__init__方法
    console.log('init');
    this.person = 'goodslin';
}

Banner.prototype.greet = function () {
    console.log('hello jacklin');
};

var banner = new Banner();
console.log(banner.person);
banner.greet();
*/

function Banner() {
    this.bannerWidth = 800;
    this.bannerGroup = $("#banner-group");
    this.pageControl = $(".page-control");
    this.index = 1;
    this.leftArrow = $(".left-arrow");
    this.rightArrow = $(".right-arrow");
    this.bannerUl = $("#banner-ul");
    this.liList = this.bannerUl.children("li");
    this.bannerCount = this.liList.length;
    this.listenBannerHover();
}

Banner.prototype.initBanner = function () {
    var self = this;

    var firstBanner = self.liList.eq(0).clone();
    var lastBanner = self.liList.eq(self.bannerCount - 1).clone();

    self.bannerUl.append(firstBanner);
    self.bannerUl.prepend(lastBanner);

    this.bannerUl.css({"width": self.bannerWidth * (self.bannerCount + 2), "left": -self.bannerWidth});
};

Banner.prototype.animate = function () {
    var self = this;
    var index = self.index;
    self.bannerUl.animate({"left": -800 * self.index}, 500);
    if (index === 0) {
        index = self.bannerCount - 1;
    } else if (index === self.bannerCount + 1) {
        index = 0;
    } else {
        index = self.index - 1;
    }
    self.pageControl.children("li").eq(index).addClass("active").siblings().removeClass("active");
};

Banner.prototype.toggleArrow = function (isShow) {
    var self = this;
    if (isShow) {
        self.leftArrow.show();
        self.rightArrow.show();
    } else {
        self.leftArrow.hide();
        self.rightArrow.hide();
    }
};

Banner.prototype.listenArrowClick = function () {
    var self = this;
    self.leftArrow.click(function () {
        if (self.index === 0) {
            self.bannerUl.css({"left": -self.bannerCount * self.bannerWidth});
            self.index = self.bannerCount - 1;
        } else {
            self.index--;
        }
        self.animate();
    });

    self.rightArrow.click(function () {
        if (self.index === self.bannerCount + 1) {
            self.bannerUl.css({"left": -self.bannerWidth});
            self.index = 2;
        } else {
            self.index++;
        }
        self.animate();
    })
};

Banner.prototype.listenBannerHover = function () {
    var self = this;
    this.bannerGroup.hover(function () {
        // 第一个函数是把鼠标移动到banner上执行到函数；
        clearInterval(self.timer);
        self.toggleArrow(true);
    }, function () {
        // 第二个函数是把鼠标移走执行的函数；
        self.loop();
        self.toggleArrow(false);
    });
};

Banner.prototype.initPageControl = function () {
    var self = this;
    for (var i = 0; i < self.bannerCount; i++) {
        var circle = $("<li></li>");
        self.pageControl.append(circle);
        if (i === 0) {
            circle.addClass("active");
        }
        self.pageControl.css({"width": 10 * self.bannerCount + 8 * 2 + 16 * (self.bannerCount - 1)});
    }
};

Banner.prototype.listenPageControl = function () {
    var self = this;
    self.pageControl.children("li").each(function (index, obj) {
        $(obj).click(function () {
            self.index = index + 1;
            self.animate();
        })
    });
};

Banner.prototype.loop = function () {
    var self = this;
    this.timer = setInterval(function () {
        if (self.index >= self.bannerCount + 1) {
            self.bannerUl.css({"left": -self.bannerWidth});
            self.index = 2;
        } else {
            self.index++;
        }
        self.animate();
    }, 2000);
};

Banner.prototype.run = function () {
    var self = this;
    this.initBanner();
    this.listenArrowClick();
    this.initPageControl();
    this.listenPageControl();
    this.timer = setInterval(function () {
        if (self.index >= self.bannerCount + 1) {
            self.index = 0;
        } else {
            self.index++;
        }
        self.animate();
    }, 2000);
};

$(function () {
    var banner = new Banner();
    banner.run();
});