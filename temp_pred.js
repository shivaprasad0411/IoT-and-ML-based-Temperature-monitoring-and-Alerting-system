setChartLibrary('google-chart');
setChartTitle('Temperature prediction');
setChartType('predictionGraph');
setAxisName('time','temperature');
mul(0.097);
setAnimation(true);
setCrosshair(true);
plotChart('time_stamp','temp');