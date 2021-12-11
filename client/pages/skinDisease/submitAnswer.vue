<template>
  <div class="container container_short submit-content">
    <div class="py-5 my-md-3 px_15px px-lg-0">
      <div class="row">
        <div class="col-12">
          <div class="text-center">
            <div class="svg-container d-flex justify-content-center">
              <svg
                class="ft-green-tick"
                xmlns="http://www.w3.org/2000/svg"
                height="100"
                width="100"
                viewBox="0 0 48 48"
                aria-hidden="true"
              >
                <circle class="circle" fill="#10C4CC" cx="24" cy="24" r="22" />
                <path
                  class="tick"
                  fill="none"
                  stroke="#FFF"
                  stroke-width="6"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-miterlimit="10"
                  d="M14 27l5.917 4.917L34 17"
                />
              </svg>
            </div>
          </div>
          <div class="text-center question_txt mt-3">
            ส่งแบบสอบถามเรียบร้อยแล้ว !
          </div>
          <div class="text-center answer_txt mt-1">
            กรุณากลับไปที่ LINE Chatbot เพื่อดูผลลัพธ์
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  layout: 'skinDisease',
}
</script>

<style lang="scss" scoped>
@supports (animation: grow 0.5s cubic-bezier(0.25, 0.25, 0.25, 1) forwards) {
  .tick {
    stroke-opacity: 0;
    stroke-dasharray: 29px;
    stroke-dashoffset: 29px;
    animation: draw 0.5s cubic-bezier(0.25, 0.25, 0.25, 1) forwards;
    animation-delay: 0.6s;
  }

  .circle {
    fill-opacity: 0;
    stroke: #10c4cc;
    stroke-width: 16px;
    transform-origin: center;
    transform: scale(0);
    animation: grow 1s cubic-bezier(0.25, 0.25, 0.25, 1.25) forwards;
  }
}

@keyframes grow {
  60% {
    transform: scale(0.8);
    stroke-width: 4px;
    fill-opacity: 0;
  }
  100% {
    transform: scale(0.9);
    stroke-width: 8px;
    fill-opacity: 1;
    fill: #10c4cc;
  }
}

@keyframes draw {
  0%,
  100% {
    stroke-opacity: 1;
  }
  100% {
    stroke-dashoffset: 0;
  }
}
.submit-content {
  margin-top: 180px;
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
    font-size: 16px;
    color: #808080;
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
