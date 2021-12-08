<template>
  <div>
    <div class="container container_short mt-4">
      <b-progress :value="30" :max="100"></b-progress>
    </div>
    <div class="container container_short">
      <div class="row">
        <div class="col-12 mb-2 pb_me-4">
          <div class="pt-3">
            <div class="card-body">
              <div class="col-12 mt-3 mb-2 px-0">
                <div class="ck-content">
                  <p class="question_txt">
                    1.) คุณเป็นผื่นที่บริเวณ ศีรษะ/คอ หรือไม่?
                  </p>
                  <figure class="image">
                    <img
                      src="~assets/hc-libs/images/skinDiseaseImages/Eczema/คำถาม1.png"
                    />
                  </figure>
                </div>
              </div>
              <div class="col-12">
                <a href="#">
                  <div class="card bg_green">
                    <div class="card-body">
                      <div class="col-12 d-flex align-items-center">
                        <div class="answer_txt" style="color: #fff">เป็น</div>
                      </div>
                    </div>
                  </div>
                </a>
              </div>
              <div class="col-12">
                <a href="#">
                  <div class="card card-list-hover">
                    <div class="card-body">
                      <div class="col-12 d-flex align-items-center">
                        <div class="answer_txt">ไม่เป็น</div>
                      </div>
                    </div>
                  </div>
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- <b-card title="newpage1">
        <b-container class="bv-example-row">
          <b-row>
            <b-col cols="4"></b-col>
            <b-col cols="4">
              <center>
                <button
                  v-if="questionIndex === 1"
                  class="btn btn-primary"
                  @click="prev"
                  disabled
                >
                  prev
                </button>
                <button
                  v-if="questionIndex !== 1"
                  class="btn btn-primary"
                  @click="prev"
                >
                  prev
                </button>
                <span> {{ this.questionIndex }} </span>
                <button
                  v-if="questionIndex === quiz.questions.length"
                  class="btn btn-secondary"
                  @click="next"
                  disabled
                >
                  next
                </button>
                <button
                  v-if="questionIndex !== quiz.questions.length"
                  class="btn btn-secondary"
                  @click="next"
                >
                  next
                </button>
              </center>
            </b-col>
            <b-col cols="4">
              <center>
                <button
                  class="btn btn-success"
                  @click="show"
                  v-if="this.showg === false"
                >
                  show
                </button>
                <button
                  class="btn btn-success"
                  @click="close"
                  v-if="this.showg === true"
                >
                  close
                </button>
              </center>
            </b-col>
          </b-row>
          <b-row v-if="this.showg === true">
            <div v-for="(item, index) in quiz.questions" :key="index">
              <button
                v-if="item.check === true"
                class="btn btn-success"
                @click="perpage(index)"
              >
                {{ index + 1 }}
              </button>
              <button
                v-if="item.check === false"
                class="btn btn-secondary"
                @click="perpage(index)"
              >
                {{ index + 1 }}
              </button>
            </div>
          </b-row>
          <b-row>
            <p>{{ quiz.questions[questionIndex - 1].text }}</p>
          </b-row>
          <b-row
            v-for="(item, index) in quiz.questions[questionIndex - 1].answers"
            :key="index"
          >
            <button
              v-if="index === quiz.questions[questionIndex - 1].checkpoint"
              class="btn btn-success"
              @click="checkpointbg(index, item.value)"
            >
              {{ item.text }} {{ index }}
            </button>
            <button
              v-if="index !== quiz.questions[questionIndex - 1].checkpoint"
              class="btn btn-secondary"
              @click="checkpointbg(index, item.value)"
            >
              {{ item.text }} {{ index }}
            </button>
          </b-row>
        </b-container>
      </b-card> -->
    </div>
    <div class="container container_short footer">
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
      text: 'Question 1 description',
      answers: [
        {
          text: 'Answer 1',
          value: 1,
        },
        {
          text: 'Answer 2',
          value: 2,
        },
        {
          text: 'Answer 3',
          value: 3,
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
