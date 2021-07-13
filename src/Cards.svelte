


  <div class="row">
    <div class="card-group text-white card-stat mt-4">
      <div class="card bg-pos">
        <div class="card-body">
          <h5 class="card-title">ติดเชื้อเพิ่มขึ้น</h5>
          <p class="card-text" id="pos_new">+8,685</p>
        </div>
        <div class="card-footer bg-dark-10">
          <small>สะสม <span id="pos_total" >353,712</span></small>
        </div>
      </div>
      <div class="card bg-death">
        <div class="card-body">
          <h5 class="card-title">เสียชีวิตเพิ่มขึ้น</h5>
          <p class="card-text" id="death_new">+56</p>
        </div>
        <div class="card-footer bg-dark-10">
          <small>สะสม <span id="death_total">2,847</span></small>
        </div>
      </div>
    </div>
  </div>
  <div class="row">
    <div class="card-group text-white card-stat">
      <div class="card bg-hos">
        <div class="card-body">
          <h5 class="card-title">รักษาตัวในร.พ.เพิ่มขึ้น</h5>
          <p class="card-text" id="hos_new">+4,832</p>
        </div>
        <div class="card-footer bg-dark-10">
          <small>สะสม <span id="hos_total">95,410</span></small>
        </div>
      </div>
      <div class="card bg-rec">
        <div class="card-body">
          <h5 class="card-title">หายแล้วเพิ่มขึ้น</h5>
          <p class="card-text" id="rec_new">+3,797</p>
        </div>
        <div class="card-footer bg-dark-10">
          <small>สะสม <span id="rec_total">255,455</span></small>
        </div>
      </div>
    </div>
  </div>

  <style>

  .bg-pos {
  background: rgba(202,13,13,0.85);
  border-radius: 15px 0 0 0 !important;
}
.bg-death {
  background: rgba(0,0,42,0.85);
  border-radius: 0 15px 0 0!important;
}
.bg-hos {
  background: rgba(3,177,252,0.85);
  border-radius: 0 0 0 15px !important;
}
.bg-rec {
  background: rgba(17, 173, 82,0.85);
  border-radius: 0 0 15px 0 !important;
}
.bg-dark-10 {
  background: rgba(0,0,0,0.2);
}
.card-stat {
  font-family: 'Prompt', sans-serif;
  width: 50%;
  margin: 0 auto;
}
.card-stat .card-title {
  font-size: 1em;
}
.card-stat .card-text {
  font-weight: bolder;
  font-size: 2.5em;
  line-height: 0.8;
}
.card-footer > small > span {
  font-weight: bolder;
  font-size: 1.2em;
}


  </style>