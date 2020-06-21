function functionDynamics(period) {
            $.ajax({
                method: 'POST',
                url: '/consumer-statistics-periods/',
                data: {'period': period},
                success: function (data_of_load) {
                    var x = drawCostDynamicsChart(data_of_load)
                },
                error: function (data) {
                    alert("it didnt work");
                }
            })

}

function functionStructure(period) {
            $.ajax({
                method: 'POST',
                url: '/consumer-statistics-structure/',
                data: {'period': period},
                success: function (data_of_load) {
                    var x = drawCostStructureChart(data_of_load)
                },
                error: function (data) {
                    alert("it didnt work");
                }
            })

}

function functionStructureOfTwoPeriods(period, date, number) {
            $.ajax({
                method: 'POST',
                url: '/consumer-statistics-structure-of-two-periods/',
                data: {'first_period': period[0], 'first_date': date[0], 'first_number_of_chart': number[0],
                'second_period': period[1], 'second_date': date[1], 'second_number_of_chart': number[1]},
                success: function (data) {
                    var x = drawCostStructureChartOfTwoPeriods(data['structure_of_first_period'],
                        data['structure_of_second_period'])
                },
                error: function (data) {
                    alert("it didnt work");
                }
            })

}

function drawCostDynamicsChart(data) {
            google.load("visualization", "1", {packages: ["corechart"]});
            google.setOnLoadCallback(drawVisualization(data));
            function drawVisualization(data_from_view) {
                var djangodata = data_from_view;
                var list_of_lists = [];
                var Header = ['Период', 'Расходы'];
                list_of_lists.push(Header);
                for (var i = 0; i < djangodata.length; i++) {
                    var list_of_one_position = [];
                    list_of_one_position.push(djangodata[i]['period'].toString());
                    list_of_one_position.push(parseFloat(djangodata[i]['costs']));
                    list_of_lists.push(list_of_one_position)
                };
                var data = google.visualization.arrayToDataTable(list_of_lists);
                var options = {
                    title: 'Динамика расходов',
                    pieHole: 0.4,
                    colors: ['#4e505f'],
                    fontName: 'Roboto Light',
                    legendTextStyle: { color: '#555555' },
                    titleTextStyle: { color: '#555555', fontSize: '25'},
                    fontSize: '14',
                    pieResidueSliceLabel: 'Остальное',
                    annotations: {alwaysOutside: true},
                    series: {color: '#CF0980', visibleInLegend: true},
                    width: 1150,
                    height: 330,
                    chartArea: {width: 1100, left: 50},

                };
                var chart = new google.visualization.ColumnChart(document.getElementById('expenditure_dynamics'));
                chart.draw(data, options);
            }
}
function drawCostStructureChart(data) {
    google.load("visualization", "1", {packages: ["corechart"]});
    google.setOnLoadCallback(drawVisualization(data));

    function drawVisualization(data_from_view) {
        var djangodata = data_from_view;
        var a = typeof djangodata[0];
        if (djangodata[0] !== undefined){
        var list_of_lists = [];
        var Header = ['Статья', 'Расходы'];
        list_of_lists.push(Header);
        for (var i = 0; i < djangodata.length; i++) {
            var list_of_one_position = [];
            list_of_one_position.push(djangodata[i]['subtype_id__item_id__item']);
            list_of_one_position.push(parseFloat(djangodata[i]['costs']));
            list_of_lists.push(list_of_one_position)
        }
        var data = google.visualization.arrayToDataTable(list_of_lists);
        var options = {
            title: 'Структура расходов за'+' '+djangodata[0]['period'],
            pieHole: 0.5,
            colors: ['#4e505f', '#66809c', '#adbd37', '#588133', '#ffad60'],
            fontName: 'Roboto Light',
            legendTextStyle: { color: '#555555' },
            titleTextStyle: { color: '#555555', fontSize: '25'},
            fontSize: '14',
            pieResidueSliceLabel: 'Остальное',
            width: 550,
            height: 300,
            chartArea: {width: 500, left: 30, height: 230, top: 70},
        };
        var chart = new google.visualization.PieChart(document.getElementById('expenditure_structure'));
        chart.draw(data, options);
        }
        else {
            window.alert('За текущий период расходы не внесены')
        }
    }
}
function drawCostStructureChartOfTwoPeriods(data1, data2){
google.load("visualization", "1", {packages:["corechart"]});
        google.setOnLoadCallback(drawVisualization(data1, data2));
        function drawVisualization(data1_from_view, data2_from_view) {
            djangodata_for_first_chart = data1_from_view;
            djangodata_for_second_chart = data2_from_view;
            var list_of_lists = [];
            var Header = ['период','продукты питания', 'одежда, обувь, аксессуары', 'транспортные расходы', 'коммунальные платежи, ремонт, связь, интернет',
                'бытовая химия, товары для дома', 'развлечения и досуг', 'путешествия', 'хобби', 'образование',
                'красота и здоровье', 'прочее', 'мебель, сантехника', 'другая техника'];
            list_of_lists.push(Header);
            var list_of_first_position = [];
            list_of_first_position.push(djangodata_for_first_chart[0]['period'].toString());
            for (var j = 1; j < Header.length; j++) {
                for (var i = 0; i < djangodata_for_first_chart.length; i++) {
                     if (djangodata_for_first_chart[i]['subtype_id__item_id__item'] == Header[j]){
                         list_of_first_position.push(parseFloat(djangodata_for_first_chart[i]['costs']))
                     }
                 }
                if (list_of_first_position.length-(j-1)<2){
                    list_of_first_position.push(0)
                }
             }
            list_of_lists.push(list_of_first_position);
            var list_of_second_position = [];
            list_of_second_position.push(djangodata_for_second_chart[0]['period'].toString());
            for (var j = 1; j < Header.length; j++) {
                for (var i = 0; i < djangodata_for_second_chart.length; i++) {
                     if (djangodata_for_second_chart[i]['subtype_id__item_id__item'] == Header[j]){
                         list_of_second_position.push(parseFloat(djangodata_for_second_chart[i]['costs']))
                     }
                 }
                if (list_of_second_position.length-(j-1)<2){
                    list_of_second_position.push(0)
                }
             }
            list_of_lists.push(list_of_second_position);
            var data = google.visualization.arrayToDataTable(list_of_lists);

          var options = {
              title: 'Сопоставление структуры расходов',
              bar: { groupWidth: '75%' },
              isStacked: true,
              fontName: 'Roboto Light',
              legendTextStyle: { color: '#555555' },
              titleTextStyle: { color: '#555555', fontSize: '25'},
              fontSize: '14',
              colors:['#4e505f', '#66809c', '#adbd37', '#588133', '#947B89', '#AEB8C3'],
              width: 550,
              height: 350,
              chartArea: {width: 430, left: 120},
          };
          var chart = new google.visualization.ColumnChart(document.getElementById('comparison_of_expenditure_structure'));
            chart.draw(data, options);
        }
}
