var first_period;
var second_period;
function jsFunctionForPeriod(value1, value2) {
        var year = /^[0-9]+$/;
        var month = /^[0-9]{4}-[0-9]{2}$/;
        var day = /^[0-9]{4}-[0-9]{2}-[0-9]{2}/;
        var list_of_periods = [];
        var list_of_periods_values = [];
        var list_of_period_numbers = [1, 2];
        var array_of_values = [value1, value2];
        for (let i = 0; i< array_of_values.length; i++ ){
                if (array_of_values[i].match(year)) {
                list_of_periods.push("years");
                list_of_periods_values.push(array_of_values[i]);
                }
                if (array_of_values[i].match(month)) {
                list_of_periods.push("months");
                list_of_periods_values.push(array_of_values[i]);
                }
                if (array_of_values[i].match(day)) {
                list_of_periods.push("days");
                list_of_periods_values.push(array_of_values[i]);
        }
        }
        functionStructureOfTwoPeriods(list_of_periods, list_of_periods_values, list_of_period_numbers)
}
//
// function jsFunctionForSecondPeriod(value) {
//         var year = /^[0-9]+$/;
//         var month = /^[0-9]{2}-[0-9]{4}/;
//         var day = /^[0-9]{2}-[0-9]{2}-[0-9]{4}/;
//         if (value.match(year)) {
//                 functionStructureOfTwoPeriods("years", value, 2)
//         }
//         if (value.match(month)) {
//                 functionStructureOfTwoPeriods("months", value, 2)
//         }
//         if (value.match(day)) {
//                 functionStructureOfTwoPeriods("days", value, 2)
//         }
// }