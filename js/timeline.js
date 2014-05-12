function plot(topic, data, query) {
var w = 800;
var h = 60;
var days = 18;
var topPadding = 5;
var leftPadding = 10;
var rightPadding = 50;
var bottomPadding = 20;

data.sort(function(a,b){return a[2]-b[2]});

var arr = new Array();
for (var i=0; i<days*4; i++) {
  arr[i] = 0;
}
var total = 0;
for (var i=0; i<data.length; i++) {
  if (data[i][2] <= 0 ) continue;
  var bucket = Math.floor(data[i][1] / 60/60/24 * 4) + 1;
  total++;
  arr[days*4-bucket]++;
}
for (var i=0; i<days*4; i++) {
  arr[i] /= total;
}

var maxBarValue = 0;
for (var i=0; i<days*4; i++) {
  if ( arr[i] > maxBarValue) {
    maxBarValue = arr[i];
  }
}


// Create scale functions
var xScale =
  d3.scale.linear()
    .domain([0, days])
    .range([w-rightPadding, leftPadding]);

var yBarScale =
  d3.scale.linear()
    .domain([0, maxBarValue])
    .range([0, h-bottomPadding-5]);

// Define X axis
var xAxis = d3.svg.axis()
  .scale(xScale)
  .orient("bottom");

// Create SVG element
var svg =
  d3.select("body")
    .append("svg")
    .attr("width", w + 200)
    .attr("height", h);

var barWidth = (w - leftPadding - rightPadding) / (days*4);
svg.selectAll("rect")
     .data(arr)
     .enter().append("rect")
     .attr("x", function(d, i) { return i * barWidth + leftPadding; })
     .attr("y", function(d) { return h - bottomPadding - yBarScale(d) })
     .attr("width", barWidth)
     .attr("height", function(d) { return yBarScale(d) })
     .attr("fill", "rgba(0, 0, 255, 0.25)")
     .attr("stroke", "rgba(0, 0, 255, 0.75)");

svg.selectAll("circle")
   .data(data)
   .enter()
   .append("circle")
   .attr("class",
     function(d) { 
      if ( d[2] == 2 ) return "highly_relevant";
      if ( d[2] == 1 ) return "relevant";
      return "not_relevant"; 
     })
   .attr("cx", function(d) {
if (d[1] /60/60/24 < 0.3)
      console.log(d[0] + " " + d[1] + " " + d[1] /60/60/24 + " " + xScale(d[1] /60/60/24));
      return xScale(d[1] /60/60/24);
    })
   .attr("cy", function(d) {
      return topPadding + Math.floor((Math.random()* (h-bottomPadding-topPadding-10))+1);;
     })
   .attr("r", function(d) { if ( d[2] > 0 ) return "2"; return "1"; });

// Create X axis
svg.append("g")
   .attr("class", "axis")
   .attr("transform", "translate(0," + (h-bottomPadding) + ")")
   .call(xAxis);

svg.append("text")
  .text(topic + ": " + query).attr("x", w-rightPadding+5).attr("y", h-bottomPadding)
  .attr("font-family", "sans-serif")
  .attr("font-size", "14px")
  .attr("fill", "black");

d3.select("body").append("br");

}