<script>
  import Chart from "chart.js/auto"
  import { onMount } from "svelte"
  import covtest from "./covtest.json"
  import Cards from "./Cards.svelte"

  let recordNumber = 30
  let myChart
  let selectedList = [false, false, true]

  if (screen.width < 768) {
    recordNumber = 3
    selectedList = [true, false, false]
  } else if (screen.width < 992) {
    recordNumber = 7
    selectedList = [false, true, false]
  }

  const loadChart = async () => {
    const records = covtest.result.records.slice(-recordNumber)
    const labels = records.map((record) => record.Date.split(" ")[0])
    const data = {
      labels: labels,
      datasets: [
        {
          type: "line",
          label: "% การตรวจพบ",
          backgroundColor: "rgb(0, 0, 0)",
          borderColor: "rgb(0, 0, 0)",
          data: records.map((record) => (record.Pos / record.Total) * 100),
          yAxisID: "y1",
        },
        {
          type: "bar",
          label: "ติด",
          backgroundColor: "rgb(85,119,234)",
          borderColor: "rgb(0, 0, 0)",
          data: records.map((record) => record.Pos),
          yAxisID: "y",
          fill: true,
        },
        {
          type: "bar",
          label: "ตรวจ",
          backgroundColor: "rgb(255, 99, 132)",
          borderColor: "rgb(255, 99, 132)",
          data: records.map((record) => record.Total),
          yAxisID: "y",
          fill: true,
        },
      ],
    }

    myChart = new Chart(
      // @ts-ignore
      document.getElementById("myChart"),
      {
        type: "bar",
        data,
        options: {
          responsive: true,
          scales: {
            x: {
              stacked: true,
            },
            y: {
              type: "linear",
              display: true,
              position: "left",
            },
            y1: {
              type: "linear",
              display: true,
              position: "right",
            },
          },
        },
      },
    )
  }

  onMount(loadChart)
</script>

<svelte:head>
  <link
    rel="stylesheet"
    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css"
  />
</svelte:head>

<main>
  <h1>เราตรวจโควิดกันวันละกี่เคส?</h1>

  <Cards />

  <hr />
  <div class="container">
    <div class="row">
      <div class="col" />
      <div class="col-6 col-md-4">
        <select id="getShowDate" class="form-select form-select-lg mb-3" aria-label=".form-select-lg example" on:change={() => { let value = document.getElementById("getShowDate").value; if (recordNumber != value) { recordNumber = value; myChart.destroy(); loadChart(); } }} >
          <option id="select3Days" value="3" selected={selectedList[0]} >3 วัน</option >
          <option id="select7Days" value="7" selected={selectedList[1]} >7 วัน</option >
          <option id="select30Days" value="30" selected={selectedList[2]} >30 วัน</option >
        </select>
      </div>
      <div class="col" />
    </div>
  </div>

  <div id="chartWrapper">
    <canvas id="myChart" />
  </div>

  <h5>ข้อมูลอัพเดทล่าสุดวันที่ 10/07/2021 จากกรมวิทยาศาสตร์ข้อมูล</h5>
  เราก็ไม่เข้าใจทำไมข้อมูลพวกนี้เค้าไม่อัพเดททุกวัน
</main>

<style>
  #chartWrapper {
    margin: 40px auto;
    width: 90vw;
    /* height: 80vh; */
  }

  @font-face {
    font-family: "Anakotmai";
    font-style: normal;
    font-weight: normal;
    src: url("../public/fonts/anakotmai/anakotmai-medium.eot"); /* IE9 Compat Modes */
    src: url("../public/fonts/anakotmai/anakotmai-medium.eot#iefix")
        format("embedded-opentype"),
      url("../public/fonts/anakotmai/anakotmai-medium.woff2") format("woff2"),
      url("../public/fonts/anakotmai/anakotmai-medium.woff") format("woff");
  }

  @font-face {
    font-family: "Anakotmai";
    font-style: normal;
    font-weight: bold;
    src: url("../public/fonts/anakotmai/anakotmai-bold.eot"); /* IE9 Compat Modes */
    src: url("../public/fonts/anakotmai/anakotmai-bold.eot#iefix")
        format("embedded-opentype"),
      url("../public/fonts/anakotmai/anakotmai-bold.woff2") format("woff2"),
      url("../public/fonts/anakotmai/anakotmai-bold.woff") format("woff");
  }

  @font-face {
    font-family: "Anakotmai";
    font-style: normal;
    font-weight: 300;
    src: url("../public/fonts/anakotmai/anakotmai-light.eot"); /* IE9 Compat Modes */
    src: url("../public/fonts/anakotmai/anakotmai-light.eot#iefix")
        format("embedded-opentype"),
      url("../public/fonts/anakotmai/anakotmai-light.woff2") format("woff2"),
      url("../public/fonts/anakotmai/anakotmai-light.woff") format("woff");
  }

  * {
    font-family: "Anakotmai", -apple-system, BlinkMacSystemFont, "Segoe UI",
      Roboto, Oxygen, Ubuntu, Cantarell, "Open Sans", "Helvetica Neue",
      sans-serif;
  }

  main {
    text-align: center;
    padding: 1em;
    margin: 0 auto;
  }

  h1 {
    color: #ff3e00;
    text-transform: uppercase;
    font-size: 3vh;
    font-weight: 100;
    line-height: 1.1;
    margin: 2rem auto;
    /* max-width: 14rem; */
  }

  p {
    /* max-width: 14rem; */
    margin: 1rem auto;
    line-height: 1.35;
  }

  @media (min-width: 480px) {
    h1 {
      max-width: none;
      font-size: 6vh;
    }

    p {
      max-width: none;
    }
  }
</style>
