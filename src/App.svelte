<script>
  import Chart from "chart.js/auto"
  import { onMount } from 'svelte';
  import covtest from "./covtest.json"

  const records = covtest.result.records.slice(-30)

  const labels = records.map((record) => record.Date.split(" ")[0]);

  const data = {
    labels: labels,
    datasets: [{
      type: 'line',
      label: '% การตรวจพบ',
      backgroundColor: 'rgb(0, 0, 0)',
      borderColor: 'rgb(0, 0, 0)',
      data: records.map((record) => (record.Pos/record.Total*100)),
      yAxisID: 'y1'
    },{
      type: 'bar',
      label: 'ติด',
      backgroundColor: 'rgb(85,119,234)',
      borderColor: 'rgb(0, 0, 0)',
      data: records.map((record) => record.Pos),
      yAxisID: 'y',
      fill: true
    },{
      type: 'bar',
      label: 'ตรวจ',
      backgroundColor: 'rgb(255, 99, 132)',
      borderColor: 'rgb(255, 99, 132)',
      data: records.map((record) => record.Total),
      yAxisID: 'y',
      fill: true
    }]

  };

  onMount(() => {
    new Chart(
      // @ts-ignore

      document.getElementById("myChart"),
      {
        type: 'bar',
        data,
        options: {
          responsive: true,
          scales: {
            x: {
              stacked: true
            },
            y: {
              type: 'linear',
              display: true,
              position: 'left',
            
            },
            y1: {
              type: 'linear',
              display: true,
              position: 'right',
            }
          }
        }
      }
    );
  })
</script>

<main>
  <h1>เราตรวจโควิดกันวันละกี่เคส?</h1>
  <div id="chartWrapper">
    <canvas id="myChart"></canvas>
  </div>
  <h5>ข้อมูลอัพเดทล่าสุดวันที่ 10/07/2021 จากกรมวิทยาศาสตร์ข้อมูล</h5>
  เราก็ไม่เข้าใจทำไมข้อมูลพวกนี้เค้าไม่อัพเดททุกวัน
</main>

<style>
  #chartWrapper {
    margin: 0 auto;
    width: 90vw;
    height: 80vh;
  }

  @font-face {
    font-family: "Anakotmai";
    font-style: normal;
    font-weight: normal;
    src: url("../public/fonts/anakotmai/anakotmai-medium.eot"); /* IE9 Compat Modes */
    src: url("../public/fonts/anakotmai/anakotmai-medium.eot#iefix") format("embedded-opentype"),
      url("../public/fonts/anakotmai/anakotmai-medium.woff2") format("woff2"),
      url("../public/fonts/anakotmai/anakotmai-medium.woff") format("woff");
  }

  @font-face {
    font-family: "Anakotmai";
    font-style: normal;
    font-weight: bold;
    src: url("../public/fonts/anakotmai/anakotmai-bold.eot"); /* IE9 Compat Modes */
    src: url("../public/fonts/anakotmai/anakotmai-bold.eot#iefix") format("embedded-opentype"),
      url("../public/fonts/anakotmai/anakotmai-bold.woff2") format("woff2"),
      url("../public/fonts/anakotmai/anakotmai-bold.woff") format("woff");
  }

  @font-face {
    font-family: "Anakotmai";
    font-style: normal;
    font-weight: 300;
    src: url("../public/fonts/anakotmai/anakotmai-light.eot"); /* IE9 Compat Modes */
    src: url("../public/fonts/anakotmai/anakotmai-light.eot#iefix") format("embedded-opentype"),
      url("../public/fonts/anakotmai/anakotmai-light.woff2") format("woff2"),
      url("../public/fonts/anakotmai/anakotmai-light.woff") format("woff");
  }


  :root {
    font-family: "Anakotmai", -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen,
      Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
  }

  main {
    text-align: center;
    padding: 1em;
    margin: 0 auto;
  }

  h1 {
    color: #ff3e00;
    text-transform: uppercase;
    font-size: 6vh;
    font-weight: 100;
    line-height: 1.1;
    margin: 2rem auto;
    max-width: 14rem;
  }

  p {
    max-width: 14rem;
    margin: 1rem auto;
    line-height: 1.35;
  }

  @media (min-width: 480px) {
    h1 {
      max-width: none;
    }

    p {
      max-width: none;
    }
  }
</style>
