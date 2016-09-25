import random, sys


numbers = 10000 # how many numbers to generate
max_number = 100 # maximum number generated
min_number = 1 # lowest number generated

randfile = open("random.txt", "w", encoding="utf-8")	

for integer in range(0, numbers, 1):
	randfile.write(str(random.randint(min_number, max_number)) + '\n')

randfile.close()

print("done generating random numbers...")

print("starting number count...")

randfile = open("random.txt", "r", encoding="utf-8")

num_list = []

# initialize list to 0
for i in range(max_number):
	num_list.append(0)

for line in randfile:
	num_list[int(line)-1] += 1
	
randfile.close()

print("displaying the number count...")
added_string = ""

length = len(num_list)

for i in range(length):
	added_string += "[" + str(i+1) + ", " + str(num_list[i]) + "]"
	if i != length:
		added_string += ","


# When formatting a string, must include double curly braces 
# when you actually want to display a curly brace in the result.
# Example: "{{ Hello {} This is my string! }}".format("World!")
# becomes: { Hello World! This is my string! }
index_html = """<!DOCTYPE html>
<html>

<head>
	<meta charset="UTF-8">
	<title>Random Number Chart</title>
	
	<style type="text/css"> 

	</style>
	
	<!--Load the AJAX API-->
    <script type="text/javascript" src="https://www.google.com/jsapi"></script>
    <script type="text/javascript">

      // Load the Visualization API and the piechart package.
      google.load('visualization', '1.0', {{'packages':['corechart']}});

      // Set a callback to run when the Google Visualization API is loaded.
      google.setOnLoadCallback(drawChart);

      // Callback that creates and populates a data table, 
      // instantiates the pie chart, passes in the data and
      // draws it.
      function drawChart() {{

		  // Create the data table.
		  var data = new google.visualization.DataTable();
		  data.addColumn('number', 'Number');
		  data.addColumn('number', 'Occurrences');
		  data.addRows([
			{}
		  ]);

		  // Set chart options
		  var options = {{'title':'Random Number Occurrences Counter',
						 'width':600,
						 'height':1300,
						 colors: ['#b0120a'],
						 hAxis: {{
						   title: 'Occurrences',
						   minValue: 0
						 }},
						 vAxis: {{
						   title: 'Number'
						 }}}};

		  // Instantiate and draw our chart, passing in some options.
		  var chart = new google.visualization.BarChart(document.getElementById('chart_div'));
		  chart.draw(data, options);
    }}
    </script>
</head>

<body>
	<div class="site">
		<header>
			<h1>Random Chart</h1>
		</header>
		<section>
			<div class="content">
				<article>
					<div id="chart_div" style="width:400; height:300"></div>
					
				</article>
			</div>
		</section>

		<aside></aside>
		<footer>
			<address>nahrens@ashland.edu</address>
		</footer>
	</div>
</body>

</html>""".format(added_string)

index_file = open("tindex.html", "w", encoding="utf-8")

index_file.write(index_html)
index_file.close()