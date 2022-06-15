/*
 * @Description: 
 * @Author: baiyi
 * @Date: 2022-02-08 17:11:51
 * @LastEditTime: 2022-02-11 08:58:54
 * @LastEditors: baiyi
 * @Reference: 
 */


//折线图 l1
var l1Chart = echarts.init(document.getElementById('l1'), "dark");
var l1_option;

l1_option = {
    backgroundColor: "#333",
    xAxis: {
        type: 'category',
        data: []
    },
    yAxis: {
        type: 'value'
    },
    series: [
        {
            data: [],
            type: 'line'
        }
    ]
};
l1_option && l1Chart.setOption(l1_option);

function get_time() {
    $.ajax({
        url: "/getTime",
        type: "GET",
        dataType: 'json',
        timeout: 1000,
        success: function (data) {
            $("#tim").html("当前时间:" + data)
        }, error: function (xhr, type, errroThrow) {

        }
    })
}



//地图分布
var m2Chart = echarts.init(document.getElementById("m2"), "dark");
var mydata = []
var optionMap = {
    backgroundColor: "#333",
    title: {
        text: '',
        subtext: '订单分布',
        x: 'left'
    },
    tooltip: {
        trigger: 'item'
    },
    //左侧小导航图标
    visualMap: {
        show: true,
        x: 'left',
        y: 'bottom',
        textStyle: {
            fontSize: 8
        },
        splitList: [{
            start: 1,
            end: 9
        },
        {
            start: 10,
            end: 99
        },
        {
            start: 100,
            end: 999
        },
        {
            start: 1000,
            end: 9999
        },
        {
            start: 10000
        }
        ],
        color: ['#8A3310', '#C64918', '#E55B25', '#F2AD92', '#F9DCD1']
    },

    //配置属性
    series: [{
        name: '累积确诊人数',
        type: 'map',
        mapType: 'china',
        roam: false,
        itemStyle: {
            normal: {
                borderWidth: .5,
                borderColor: '#009fe8',
                areaColor: '#ffefd5'
            },
            emphasis: {
                borderWidth: .5,
                borderColor: '#4b0082',
                areaColor: '#fff'
            }
        },
        label: {
            normal: {
                show: true, //省份名称
                fontSize: 8
            },
            emphasis: {
                show: true,
                fontSize: 8
            }
        },
        data: mydata //数据
    }]
};
m2Chart.setOption(optionMap);


//词云图
var wordcloudChart = echarts.init(document.getElementById("r2"));
var wordcloudOption = {
    title: {
        text: "客户反馈",
        textStyle: {
            color: 'white'
        },
        left: 'left'
    },
    tooltip: {
        show: false
    },
    series: [{
        type: 'wordCloud',
        gridSize: 1,
        sizeRange: [12, 55], //文字范围
        //文本旋转范围，文本将通过rotationStep45在[-90,90]范围内随机旋转
        rotationRange: [-45, 0, 45, 90],
        // rotationStep: 45,
        // textRotation: [0, 45, 90, -45],
        //形状
        // shape: 'circle',
        textStyle: {
            normal: {
                color: function () { //文字颜色的随机色
                    return 'rgb(' + [
                        Math.round(Math.random() * 160),
                        Math.round(Math.random() * 160),
                        Math.round(Math.random() * 160)
                    ].join(',') + ')';
                }
            }
        },
        right: null,
        bottom: null,
        data: []
    }]
};
wordcloudChart.setOption(wordcloudOption);


//饼图
var pieChart = echarts.init(document.getElementById('r1'));
var optionPie = {
    tooltip: {
        trigger: 'item'
    },
    // legend: {
    //     top: '5%',
    //     left: 'center'
    // },
    series: [
        {
            name: 'Access From',
            type: 'pie',
            radius: ['40%', '70%'],
            avoidLabelOverlap: false,
            itemStyle: {
                borderRadius: 10,
                borderColor: '#fff',
                borderWidth: 2
            },
            label: {
                show: true,
                position: 'left'
            },
            emphasis: {
                label: {
                    show: true,
                    fontSize: '10',
                    fontWeight: 'bold'
                }
            },
            labelLine: {
                show: true
            },
            data: []
        }
    ]
};
optionPie && pieChart.setOption(optionPie);


//柱形图
var barChart = echarts.init(document.getElementById('l2'));
var optionBar = {
    xAxis: {
        type: 'category',
        data: []
    },
    yAxis: {
        type: 'value'
    },
    series: [
        {
            data: [],
            type: 'bar'
        }
    ]
};

optionBar && barChart.setOption(optionBar);


function get_label() {
    $.ajax({
        //url: "{{url_for('dashboard.get_label')}}",
        url: "/getLabel",
        type: "GET",
        dataType: 'json',
        timeout: 1000,
        success: function (data) {
            $(".num h1").eq(0).text(data.label1);
            $(".num h1").eq(1).text(data.label2);
            $(".num h1").eq(2).text(data.label3);
            $(".num h1").eq(3).text(data.label4);
        }, error: function (xhr, type, errroThrow) {

        }
    })
}


function get_l1() {
    $.ajax({
        url: "/getL1",
        type: "GET",
        dataType: 'json',
        timeout: 1000,
        success: function (data) {
            l1_option.xAxis.data = data.timeid;
            l1_option.series[0].data = data.num;
            l1_option && l1Chart.setOption(l1_option);
        }, error: function (xhr, type, errroThrow) {
            console.log("error")
        }
    })
}



function get_map() {
    $.ajax({
        url: "/getChinaMap",
        type: "GET",
        dataType: 'json',
        timeout: 1000,
        success: function (data) {
            optionMap.series[0].data = data.data;
            optionMap && m2Chart.setOption(optionMap);
        }, error: function (xhr, type, errroThrow) {
            console.log("error")
        }
    })
}


function get_word_cloud() {
    $.ajax({
        url: "/getWordCloud",
        type: "GET",
        dataType: 'json',
        timeout: 1000,
        success: function (data) {
            wordcloudOption.series[0].data = data;
            wordcloudOption && wordcloudChart.setOption(wordcloudOption);
        }, error: function (xhr, type, errroThrow) {
            console.log("error")
        }
    })
}


function get_pie() {
    $.ajax({
        url: "/getPie",
        type: "GET",
        dataType: 'json',
        timeout: 1000,
        success: function (data) {
            optionPie.series[0].data = data;
            optionPie && pieChart.setOption(optionPie);
        }, error: function (xhr, type, errroThrow) {
            console.log("error")
        }
    })
}

function get_bar() {
    $.ajax({
        url: "/getBar",
        type: "GET",
        dataType: 'json',
        timeout: 1000,
        success: function (data) {
            optionBar.xAxis.data = data.name;
            optionBar.series[0].data = data.value;
            optionBar && barChart.setOption(optionBar);
        }, error: function (xhr, type, errroThrow) {
            console.log("error")
        }
    })
}

//定时刷新方法
setInterval(get_time, 1000)
setInterval(get_l1, 3000)
setInterval(get_label, 3000)
setInterval(get_map, 3000)
setInterval(get_word_cloud, 3000)
setInterval(get_pie, 3000)
setInterval(get_bar, 3000)

