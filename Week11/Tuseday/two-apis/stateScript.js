let secondApi = document.getElementById('second-api')


let sortMapData = (data) => {
  data.forEach(element => {
      chart.data.datasets[0].data.push(element['Population'])
      chart.data.labels.push(element['State'])
  });
  getChart()
}

fetch('https://datausa.io/api/data?drilldowns=State&measures=Population&year=latest')
  .then(response => response.json())
  .then(data => {
      sortMapData(data.data)
  })

let chart =  {
    "type": "bar",
    "data": {
      "labels": [],
      "datasets": [
        {
          "backgroundColor": "rgba(255,150,150,0.5)",
          "borderColor": "rgb(255,150,150)",
          "data": [],
          "label": "Population",
          "fill": "origin"
        }
      ]
    }
  }




let getChart = () => { 
  
  let baseUrl = 'https://image-charts.com/chart.js/2.8.0?width=1100&height=600&bkg=white&c='

  let url = baseUrl + JSON.stringify(chart)
  console.log(url)
  let img = document.createElement('img')
  img.src = url
  img.id = 'chart'
  secondApi.appendChild(img)
}
