<template>
  <div>
    <Loader v-if="isLoading" />
    <div v-else>
      <div class="container container_short pg-bar">
        <div class="text-center">
          <b-progress
            :value="ans.length"
            :max="quiz.questions.length"
          ></b-progress>
        </div>
      </div>
      <div class="container container_short skin-content">
        <div class="row">
          <div class="col-12 mb-2 pb_me-4">
            <div class="pt-3">
              <div class="card-body">
                <div class="col-12 mt-3 mb-2 px-0">
                  <div class="ck-content">
                    <p class="question_txt">
                      {{ quiz.questions[questionIndex - 1].text }}
                    </p>
                    <figure
                      class="image"
                      v-if="quiz.questions[questionIndex - 1].questionImage"
                    >
                      <img
                        v-bind:src="
                          quiz.questions[questionIndex - 1].questionImage
                        "
                      />
                    </figure>
                  </div>
                </div>
                <div class="mt-4">
                  <div
                    style="cursor: pointer"
                    class="col-12"
                    v-for="(item, index) in quiz.questions[questionIndex - 1]
                      .answers"
                    :key="index"
                  >
                    <a
                      v-if="
                        index === quiz.questions[questionIndex - 1].checkpoint
                      "
                    >
                      <div
                        class="card bg_green"
                        @click="checkpointbg(index, item.value)"
                      >
                        <div class="card-body">
                          <div class="col-12 d-flex align-items-center">
                            <div class="answer_txt" style="color: #fff">
                              {{ item.text }}
                            </div>
                          </div>
                        </div>
                      </div>
                    </a>
                    <a
                      v-if="
                        index !== quiz.questions[questionIndex - 1].checkpoint
                      "
                    >
                      <div
                        class="card card-list-hover"
                        @click="checkpointbg(index, item.value)"
                      >
                        <div class="card-body">
                          <div class="col-12 d-flex align-items-center">
                            <div class="answer_txt">{{ item.text }}</div>
                          </div>
                        </div>
                      </div>
                    </a>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div v-if="end === false">
        <div
          class="container container_short footerV2"
          v-if="quiz.questions[questionIndex - 1].check === false"
          disabled
        >
          <div class="row mt-3 mb-3">
            <div
              class="col-12 d-flex align-items-center justify-content-center"
            >
              <div class="m_width_120p">
                <div class="m_width_120p text-center footerBtn">ต่อไป</div>
              </div>
            </div>
          </div>
        </div>
        <div
          class="container container_short footer"
          v-if="quiz.questions[questionIndex - 1].check === true"
          @click="next"
        >
          <div class="row mt-3 mb-3">
            <div
              class="col-12 d-flex align-items-center justify-content-center"
            >
              <div class="m_width_120p">
                <div class="m_width_120p text-center footerBtn">ต่อไป</div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div v-if="end === true">
        <div
          class="container container_short footerV2"
          v-if="quiz.questions[questionIndex - 1].check === false"
          disabled
        >
          <div class="row mt-3 mb-3">
            <div
              class="col-12 d-flex align-items-center justify-content-center"
            >
              <div class="m_width_120p">
                <div class="m_width_120p text-center footerBtn">ส่งต่อ</div>
              </div>
            </div>
          </div>
        </div>
        <div
          class="container container_short footer"
          v-if="quiz.questions[questionIndex - 1].check === true"
          @click="math"
        >
          <div class="row mt-3 mb-3">
            <div
              class="col-12 d-flex align-items-center justify-content-center"
            >
              <div class="m_width_120p">
                <div class="m_width_120p text-center footerBtn">ส่งต่อ</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
var quiz = {
  title: 'quiz sample',
  questions: [
    {
      text: '1.) ผื่นในบริเวณ ลำตัว ของคุณมีอาการคันมากน้อยระดับไหน? ',
      answers: [
        {
          text: 'ไม่มีอาการคัน',
          value: 0,
        },
        {
          text: 'เล็กน้อย',
          value: 1,
        },
        {
          text: 'ปานกลาง',
          value: 2,
        },
        {
          text: 'มาก',
          value: 3,
        },
      ],
      checkpoint: '',
      check: false,
    },
    {
      text: '1.1) ผื่นในบริเวณ ลำตัว ขนาดของรอยผื่นในบริเวณนี้ คิดเป็นสัดส่วนความกว้างประมาณกี่เปอร์เซ็นต์ของพื้นที่ในบริเวณนี้ทั้งหมด? ',
      answers: [
        {
          text: 'ไม่มีผื่น',
          value: 0,
        },
        {
          text: '20%',
          value: 1,
        },
        {
          text: '50%',
          value: 2,
        },
        {
          text: '90%',
          value: 3,
        },
      ],
      checkpoint: '',
      check: false,
    },
    {
      text: '2) ผื่นในบริเวณ เท้า ของคุณมีอาการคันมากน้อยระดับไหน?',
      answers: [
        {
          text: 'ไม่มีอาการคัน',
          value: 0,
        },
        {
          text: 'เล็กน้อย',
          value: 1,
        },
        {
          text: 'ปานกลาง',
          value: 2,
        },
        {
          text: 'มาก',
          value: 3,
        },
      ],
      checkpoint: '',
      check: false,
    },
    {
      text: '2.1) ผื่นในบริเวณ เท้า ของคุณเป็นผื่นมีขุยแห้งสีขาวหรือไม่?',
      answers: [
        {
          text: 'ไม่เป็น',
          value: 0,
        },
        {
          text: 'เป็น',
          value: 1,
        },
      ],
      checkpoint: '',
      check: false,
    },
    {
      text: '2.2) ผื่นในบริเวณ เท้า ขนาดของรอยผื่นในบริเวณนี้ คิดเป็นสัดส่วนความกว้างประมาณกี่เปอร์เซ็นต์ของพื้นที่ในบริเวณนี้ทั้งหมด?',
      answers: [
        {
          text: 'ไม่มีผื่น',
          value: 0,
        },
        {
          text: '20%',
          value: 1,
        },
        {
          text: '50%',
          value: 2,
        },
        {
          text: '90%',
          value: 3,
        },
      ],
      checkpoint: '',
      check: false,
    },
    {
      text: '3.) ผื่นในบริเวณ ศีรษะ ของคุณมีอาการคันมากน้อยระดับไหน?',
      answers: [
        {
          text: 'ไม่มีอาการคัน',
          value: 0,
        },
        {
          text: 'เล็กน้อย',
          value: 1,
        },
        {
          text: 'ปานกลาง',
          value: 2,
        },
        {
          text: 'มาก',
          value: 3,
        },
      ],
      checkpoint: '',
      check: false,
    },
    {
      text: '3.1) ผื่นในบริเวณ ศีรษะ ขนาดของรอยผื่นในบริเวณนี้ คิดเป็นสัดส่วนความกว้างประมาณกี่เปอร์เซ็นต์ของพื้นที่ในบริเวณนี้ทั้งหมด?',
      answers: [
        {
          text: 'ไม่มีผื่น',
          value: 0,
        },
        {
          text: '20%',
          value: 1,
        },
        {
          text: '50%',
          value: 2,
        },
        {
          text: '90%',
          value: 3,
        },
      ],
      checkpoint: '',
      check: false,
    },
    {
      text: '3.2) ผื่นในบริเวณ ศีรษะ มีอาการอักเสบหรือไม',
      answers: [
        {
          text: 'ไม่มีอาการอักเสบ',
          value: 0,
        },
        {
          text: 'มีอาการอักเสบ',
          value: 2,
        },
      ],
      checkpoint: '',
      check: false,
    },
    {
      text: '3.3) มีตุ่มหนองเล็กบนหนังศีรษะหรือไม?',
      answers: [
        {
          text: 'ไม่มี',
          value: 0,
        },
        {
          text: 'มี',
          value: 2,
        },
      ],
      checkpoint: '',
      check: false,
    },
    {
      text: '3.4) คุณมีอาการไข้ขึ้นและมีน้ำหนองไหลตรงบริเวณที่เกิดตุ่มหนองหรือไม?',
      answers: [
        {
          text: 'ไม่มี',
          value: 0,
        },
        {
          text: 'มี',
          value: 2,
        },
      ],
      checkpoint: '',
      check: false,
    },
    {
      text: '4.) ผื่นในบริเวณ ใบหน้า ของคุณมีอาการคันมากน้อยระดับไหน?',
      answers: [
        {
          text: 'ไม่มีอาการคัน',
          value: 0,
        },
        {
          text: 'เล็กน้อย',
          value: 1,
        },
        {
          text: 'ปานกลาง',
          value: 2,
        },
        {
          text: 'มาก',
          value: 3,
        },
      ],
      checkpoint: '',
      check: false,
    },
    {
      text: '4.1) ผื่นในบริเวณ ใบหน้า ขนาดของรอยผื่นในบริเวณนี้ คิดเป็นสัดส่วนความกว้างประมาณกี่เปอร์เซ็นต์ของพื้นที่ในบริเวณนี้ทั้งหมด?',
      answers: [
        {
          text: 'ไม่มีผื่น',
          value: 0,
        },
        {
          text: '20%',
          value: 1,
        },
        {
          text: '50%',
          value: 2,
        },
        {
          text: '90%',
          value: 3,
        },
      ],
      checkpoint: '',
      check: false,
    },
    {
      text: '4.2) มีตุ่มหนองเล็กเกิดขึ้นบริเวณใบหน้าหรือไม่?',
      answers: [
        {
          text: 'ไม่มี',
          value: 0,
        },
        {
          text: 'มี',
          value: 2,
        },
      ],
      checkpoint: '',
      check: false,
    },
    {
      text: '5.) ผื่นในบริเวณ มือ ของคุณมีอาการคันมากน้อยระดับไหน?',
      answers: [
        {
          text: 'ไม่มีอาการคัน',
          value: 0,
        },
        {
          text: 'เล็กน้อย',
          value: 1,
        },
        {
          text: 'ปานกลาง',
          value: 2,
        },
        {
          text: 'มาก',
          value: 3,
        },
      ],
      checkpoint: '',
      check: false,
    },
    {
      text: '5.1) ผื่นในบริเวณ มือ ของคุณเป็นผื่นขุยแห้งสีขาวหรือไม่ ?',
      answers: [
        {
          text: 'ไม่เป็น',
          value: 0,
        },
        {
          text: 'เป็น',
          value: 2,
        },
      ],
      checkpoint: '',
      check: false,
    },
    {
      text: '5.2) ผื่นในบริเวณ มือ ขนาดของรอยผื่นในบริเวณนี้ คิดเป็นสัดส่วนความกว้างประมาณกี่เปอร์เซ็นต์ของพื้นที่ในบริเวณนี้ทั้งหมด?',
      answers: [
        {
          text: 'ไม่มีผื่น',
          value: 0,
        },
        {
          text: '20%',
          value: 1,
        },
        {
          text: '50%',
          value: 2,
        },
        {
          text: '90%',
          value: 3,
        },
      ],
      checkpoint: '',
      check: false,
    },
    {
      text: '6) ผื่นในบริเวณ เล็บ ของคุณมีอาการคันมากน้อยระดับไหน?',
      answers: [
        {
          text: 'ไม่มีอาการคัน',
          value: 0,
        },
        {
          text: 'เล็กน้อย',
          value: 1,
        },
        {
          text: 'ปานกลาง',
          value: 2,
        },
        {
          text: 'มาก',
          value: 3,
        },
      ],
      checkpoint: '',
      check: false,
    },
    {
      text: '6.1) ผื่นในบริเวณ เล็บ ของคุณเป็นผื่นขุยแห้งสีขาวหรือไม่ ?',
      answers: [
        {
          text: 'ไม่เป็น',
          value: 0,
        },
        {
          text: 'เป็น',
          value: 2,
        },
      ],
      checkpoint: '',
      check: false,
    },
    {
      text: '6.2) ผื่นในบริเวณ แผ่นเล็บ ของคุณเป็นสีเหลืองหรือไม่ ?',
      answers: [
        {
          text: 'ไม่เป็น',
          value: 0,
        },
        {
          text: 'เป็น',
          value: 2,
        },
      ],
      checkpoint: '',
      check: false,
    },
    {
      text: '6.3) ผื่นในบริเวณ แผ่นเล็บ ของคุณมีการผุพังมากขนาดไหน?',
      answers: [
        {
          text: 'ไม่มีการผุพัง',
          value: 0,
        },
        {
          text: 'เล็กน้อย',
          value: 1,
        },
        {
          text: 'ปานกลาง',
          value: 2,
        },
        {
          text: 'มาก',
          value: 3,
        },
      ],
      checkpoint: '',
      check: false,
    },
    {
      text: '7) ผื่นในบริเวณ ขาหนีบ ของคุณมีอาการคันมากน้อยระดับไหน?',
      answers: [
        {
          text: 'ไม่มีอาการคัน',
          value: 0,
        },
        {
          text: 'เล็กน้อย',
          value: 1,
        },
        {
          text: 'ปานกลาง',
          value: 2,
        },
        {
          text: 'มาก',
          value: 3,
        },
      ],
      checkpoint: '',
      check: false,
    },
    {
      text: '7.1) ผื่นในบริเวณ ขาหนีบ ของคุณมีลักษณะเป็นปื้นนูนแดงหรือไม่?',
      answers: [
        {
          text: 'ไม่มี',
          value: 0,
        },
        {
          text: 'มี',
          value: 1,
        },
      ],
      checkpoint: '',
      check: false,
    },
    {
      text: '7.2) ผื่นในบริเวณ ขาหนีบ ของคุณมีอาการแสบหรืออักเสบบริเวณรอยผื่นหรือไม่?',
      answers: [
        {
          text: 'ไม่มี',
          value: 0,
        },
        {
          text: 'มี',
          value: 3,
        },
      ],
      checkpoint: '',
      check: false,
    },
    {
      text: '7.3) ผื่นในบริเวณ ขาหนีบ ขนาดของรอยผื่นในบริเวณนี้ คิดเป็นสัดส่วนความกว้างประมาณกี่เปอร์เซ็นต์ของพื้นที่ในบริเวณนี้ทั้งหมด?',
      answers: [
        {
          text: 'ไม่มีผื่น',
          value: 0,
        },
        {
          text: '20%',
          value: 1,
        },
        {
          text: '50%',
          value: 2,
        },
        {
          text: '90%',
          value: 3,
        },
      ],
      checkpoint: '',
      check: false,
    },
    {
      text: '8) ผื่นในบริเวณ ขา ของคุณมีอาการคันมากน้อยระดับไหน?',
      answers: [
        {
          text: 'ไม่มีอาการคัน',
          value: 0,
        },
        {
          text: 'เล็กน้อย',
          value: 1,
        },
        {
          text: 'ปานกลาง',
          value: 2,
        },
        {
          text: 'มาก',
          value: 3,
        },
      ],
      checkpoint: '',
      check: false,
    },
    {
      text: '8.1) ผื่นในบริเวณ ขา ขนาดของรอยผื่นในบริเวณนี้ คิดเป็นสัดส่วนความกว้างประมาณกี่เปอร์เซ็นต์ของพื้นที่ในบริเวณนี้ทั้งหมด?',
      answers: [
        {
          text: 'ไม่มีผื่น',
          value: 0,
        },
        {
          text: '20%',
          value: 1,
        },
        {
          text: '50%',
          value: 2,
        },
        {
          text: '90%',
          value: 3,
        },
      ],
      checkpoint: '',
      check: false,
    },
    {
      text: '9) ผื่นในบริเวณ แขน ของคุณมีอาการคันมากน้อยระดับไหน?',
      answers: [
        {
          text: 'ไม่มีอาการคัน',
          value: 0,
        },
        {
          text: 'เล็กน้อย',
          value: 1,
        },
        {
          text: 'ปานกลาง',
          value: 2,
        },
        {
          text: 'มาก',
          value: 3,
        },
      ],
      checkpoint: '',
      check: false,
    },
    {
      text: '9.1) ผื่นในบริเวณ แขน ขนาดของรอยผื่นในบริเวณนี้ คิดเป็นสัดส่วนความกว้างประมาณกี่เปอร์เซ็นต์ของพื้นที่ในบริเวณนี้ทั้งหมด?',
      answers: [
        {
          text: 'ไม่มีผื่น',
          value: 0,
        },
        {
          text: '20%',
          value: 1,
        },
        {
          text: '50%',
          value: 2,
        },
        {
          text: '90%',
          value: 3,
        },
      ],
      checkpoint: '',
      check: false,
    },
    {
      text: '10) ผื่นในบริเวณ แผ่นหลัง ของคุณมีอาการคันมากน้อยระดับไหน?',
      answers: [
        {
          text: 'ไม่มีอาการคัน',
          value: 0,
        },
        {
          text: 'เล็กน้อย',
          value: 1,
        },
        {
          text: 'ปานกลาง',
          value: 2,
        },
        {
          text: 'มาก',
          value: 3,
        },
      ],
      checkpoint: '',
      check: false,
    },
    {
      text: '10.1) ผื่นในบริเวณ แผ่นหลัง ขนาดของรอยผื่นในบริเวณนี้ คิดเป็นสัดส่วนความกว้างประมาณกี่เปอร์เซ็นต์ของพื้นที่ในบริเวณนี้ทั้งหมด?',
      answers: [
        {
          text: 'ไม่มีผื่น',
          value: 0,
        },
        {
          text: '20%',
          value: 1,
        },
        {
          text: '50%',
          value: 2,
        },
        {
          text: '90%',
          value: 3,
        },
      ],
      checkpoint: '',
      check: false,
    },
  ],
}

export default {
  layout: 'skinDisease',
  data() {
    return {
      quiz: quiz,
      questionIndex: 1,
      showg: false,
      ans: [],
      final: 0,
      end: false,
      isLoading: false,
    }
  },
  components: {
    Loader: () => import('~/components/Loader.vue'),
  },
  async mounted() {
    this.isLoading = true
    this.isLoading = false
  },
  methods: {
    math() {
      let body = this.ans[0] * this.ans[1]
      let foot = (this.ans[2] + this.ans[3]) * this.ans[4]
      let head =
        (this.ans[5] + this.ans[7] + this.ans[8] + this.ans[9]) * this.ans[6]
      let face = (this.ans[10] + this.ans[12]) * this.ans[11]
      let hand = (this.ans[13] + this.ans[14]) * this.ans[15]
      let nail = this.ans[16] + this.ans[17] + this.ans[18] + this.ans[19]
      let Groin = (this.ans[20] + this.ans[21] + this.ans[22]) * this.ans[23]
      let leg = this.ans[24] * this.ans[25]
      let arm = this.ans[26] * this.ans[27]
      let back = this.ans[28] * this.ans[29]

      let sum =
        body + foot + head + face + hand + nail + Groin + leg + arm + back
      this.final = sum.toFixed(2)
      console.log('คำตอบ', this.final)
      this.$router.push(this.localePath('/questionnaire/submit-answer'))
    },
    checkpointbg(value, score) {
      this.quiz.questions[this.questionIndex - 1].checkpoint = value
      this.quiz.questions[this.questionIndex - 1].check = true
      this.ans[this.questionIndex - 1] = score
      if (this.ans.length === this.quiz.questions.length) {
        this.end = true
      }
    },
    prev() {
      if (this.questionIndex > 1) {
        this.questionIndex--
      }
    },
    next() {
      if (
        this.questionIndex >= 1 &&
        this.questionIndex !== this.quiz.questions.length
      ) {
        this.questionIndex++
      }
    },
    perpage(value) {
      this.questionIndex = value + 1
    },
    show() {
      if (this.showg == false) {
        this.showg = true
      }
    },
    close() {
      if (this.showg == true) {
        this.showg = false
      }
    },
    playAgain() {
      this.questionIndex = 0
    },
  },
}
</script>

<style scoped>
.pg-bar {
  position: fixed;
  top: 0;
  padding-top: 1rem;
  height: 40px;
  max-width: 100%;
  z-index: 100;
  background-color: #fff;
}
.skin-content {
  margin-bottom: 70px;
  margin-top: 20px;
}
.bg_green {
  background-color: #10c4cc;
}
.footer {
  position: fixed;
  bottom: 0%;
  max-width: 100%;
  background-color: #10c4cc;
  cursor: pointer;
}

.footerV2 {
  position: fixed;
  bottom: 0%;
  max-width: 100%;
  background-color: #c2cfe0;
  cursor: pointer;
}

.footer:hover {
  background-color: #10b4bd;
}
.footerBtn {
  font-family: 'Prompt-Medium';
  color: #fff;
  font-size: 22px;
  line-height: 30px;
}
.txt_title {
  font-family: 'Prompt-Regular';
  font-size: 20px;
  line-height: 33px;
  color: #333333;
}
.border_bottom_1_f3 {
  border-bottom: 1px solid #dddddd !important;
}
.txt_14 {
  font-size: 14px !important;
}
.txt_20 {
  font-size: 20px !important;
}
.txt_28 {
  font-size: 28px;
}
.line-height-1 {
  line-height: 1 !important;
}
.txt_bold {
  font-family: 'Prompt-Regular';
  color: #333333;
  font-size: 20px;
}
.circle_no_task {
  background: #ffffff;
  color: #000000;
  border-radius: 25px;
  display: inline-block;
  font-weight: bold;
  margin: 7px 3.9px;
  text-align: center;
  border: 2px solid #cccccc !important;
  padding: 10px;
  height: 46px;
  width: 46px;
  font-family: 'Prompt-Regular';
  font-size: 13px;
  line-height: 1.7;
}
.circle_no_task.did {
  background: #109cf1;
  color: #000000;
  border: 2px solid #cccccc !important;
}
.circle_no_task.doing {
  background: #e5e5e5;
  color: #000000;
  border: 2px solid #cccccc !important;
}
.question_txt {
  font-family: 'Prompt-Regular';
  font-style: normal;
  font-size: 20px;
  color: #333333;
}
.answer_txt {
  font-family: 'Prompt-Regular';
  font-style: normal;
  font-size: 15px;
  color: #333333;
}
.card-list-hover:hover {
  background-color: #f3f3f3;
}
.btn_gray_hover {
  border-radius: 5rem;
  border: 1px solid #bdbdbd;
}
.txt_grey_99 {
  color: #999999 !important;
}
.txt_title_btn {
  font-family: 'Prompt-Regular';
  font-size: 16px;
  line-height: 27.5px;
  color: #fff;
}
@media screen and (max-width: 768px) {
  .txt_title {
    font-family: 'Prompt-Regular';
    font-size: 18px;
    line-height: 33px;
    color: #333333;
  }
  .question_txt {
    font-family: 'Prompt-Medium';
    font-style: normal;
    font-size: 20px;
    color: #333333;
  }
  .answer_txt {
    font-family: 'Prompt-Regular';
    font-style: normal;
    font-size: 16px;
    color: #333333;
    line-height: 33px;
  }
  .txt_title_btn {
    font-family: 'Prompt-Regular';
    font-size: 14px;
    line-height: 27.5px;
    color: #fff;
  }
  .txt_bold {
    font-family: 'Prompt-Regular';
    color: #333333;
    font-size: 18px;
  }
}
.ck-content img {
  width: 100%;
  height: 100%;
}
.bg_gray {
  background-color: #f3f3f3;
}
.card-body,
.card-footer {
  padding: 0.825rem;
}
.m_width_120p {
  min-width: 120px;
}
</style>
