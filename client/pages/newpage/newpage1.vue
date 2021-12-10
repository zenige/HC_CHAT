<template>
  <div>
    <div class="container container_short pg-bar">
      <b-progress :value="ans.length" :max="quiz.questions.length"></b-progress>
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
              <div
                class="col-12"
                v-for="(item, index) in quiz.questions[questionIndex - 1]
                  .answers"
                :key="index"
              >
                <a
                  v-if="index === quiz.questions[questionIndex - 1].checkpoint"
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
                  v-if="index !== quiz.questions[questionIndex - 1].checkpoint"
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
    <div
      class="container container_short footerV2"
      v-if="quiz.questions[questionIndex - 1].check === false"
      disabled
    >
      <div class="row mt-3 mb-3">
        <div class="col-12 d-flex align-items-center justify-content-center">
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
        <div class="col-12 d-flex align-items-center justify-content-center">
          <div class="m_width_120p">
            <div class="m_width_120p text-center footerBtn">ต่อไป</div>
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
      text: '1.) คุณเป็นผื่นในบริเวณ ศีรษะ/คอ คิดเป็นสัดส่วนประมาณกี่เปอร์เซ็นต์ของพื้นที่ในบริเวณนี้ทั้งหมด?',
      questionImage:
        '~assets/hc-libs/images/skinDiseaseImages/Eczema/คำถาม1.png',
      answers: [
        {
          text: '0%',
          value: 0,
        },
        {
          text: '1-9%',
          value: 1,
        },
        {
          text: '10-29%',
          value: 2,
        },
        {
          text: '30-49%',
          value: 3,
        },
        {
          text: '50-69%',
          value: 4,
        },
        {
          text: '70-89%',
          value: 5,
        },
        {
          text: '90-100%',
          value: 6,
        },
      ],
      checkpoint: '',
      check: false,
    },
    {
      text: 'Question 2 description',
      answers: [
        {
          text: 'Answer 1a',
          value: 1,
        },
        {
          text: 'Answer 2a',
          value: 2,
        },
        {
          text: 'Answer 3a',
          value: 3,
        },
        {
          text: 'Answer 4a',
          value: 4,
        },
        {
          text: 'Answer 5a',
          value: 5,
        },
        {
          text: 'Answer 6a',
          value: 6,
        },
      ],
      checkpoint: '',
      check: false,
    },
    {
      text: 'Question 3 description',
      answers: [
        {
          text: 'Answer 1b',
          value: 1,
        },
        {
          text: 'Answer 2b',
          value: 2,
        },
        {
          text: 'Answer 3b',
          value: 3,
        },
      ],
      checkpoint: '',
      check: false,
    },
    {
      text: 'Question 4 description',
      answers: [
        {
          text: 'Answer 1n',
          value: 1,
        },
        {
          text: 'Answer 2n',
          value: 2,
        },
      ],
      checkpoint: '',
      check: false,
    },
    {
      text: 'Question 5 description',
      answers: [
        {
          text: 'Answer 1i',
          value: 1,
        },
        {
          text: 'Answer 2i',
          value: 2,
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
    }
  },
  methods: {
    checkpointbg(value, score) {
      this.quiz.questions[this.questionIndex - 1].checkpoint = value
      this.quiz.questions[this.questionIndex - 1].check = true
      console.log(this.quiz.questions[this.questionIndex - 1])
      console.log('nn', this.quiz.questions)
      console.log(value)
      this.ans[this.questionIndex - 1] = score
      console.log('sc', this.ans)
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
      console.log(value)
      this.questionIndex = value + 1
    },
    show() {
      if (this.showg == false) {
        this.showg = true
      }
      console.log('be', this.showg)
    },
    close() {
      if (this.showg == true) {
        this.showg = false
      }
      console.log('be', this.showg)
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
  width: 100%;
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
  font-size: 24px;
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
  font-size: 16px;
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
    font-size: 22px;
    color: #333333;
  }
  .answer_txt {
    font-family: 'Prompt-Regular';
    font-style: normal;
    font-size: 18px;
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
