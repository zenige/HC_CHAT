<template>
  <div>
    <b-container class="container container_short bg_green">
      <b-row>
        <b-col class="col-12">
          <div class="p-3">
            <div>
              <div class="txt_24 txt_title">
                แบบสอบถามประเมินระดับความรุนแรงของโรคผื่นแพ้อักเสบ (Eczema)
              </div>
            </div>
          </div>
        </b-col>
      </b-row>
    </b-container>
    <b-container class="container container_short mt-3">
      <b-row>
        <b-col class="col-12 mt-2">
          <div class="p-3 border rounded">
            <div class="mx-2">
              <b-row cols="2" class="my-2">
                <b-col cols="4" class="m_width_120p line-height-1 txt_bold">
                  Description
                </b-col>
                <b-col cols="8" class="line-height-1">
                  กรุณาตอบแบบสอบถามให้ครบทุกข้อ เมื่อส่งแบบสอบถามแล้ว <br />
                  กรุณากลับไปที่ LINE Chatbot เพื่อดูผลลัพธ์
                </b-col>
              </b-row>
              <b-row cols="2" class="my-2">
                <b-col cols="4" class="m_width_120p line-height-1 txt_bold"
                  >Question</b-col
                >
                <b-col cols="8" class="line-height-1">12 questions</b-col>
              </b-row>
            </div>
          </div>
        </b-col>
      </b-row>
    </b-container>
    <div class="container container_short footer">
      <div class="row mt-3 mb-3">
        <div class="col-12 d-flex align-items-center justify-content-center">
          <div class="m_width_120p">
            <div class="m_width_120p text-center footerBtn">
              เริ่มทำแบบสอบถาม
            </div>
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

<style scoped>
.txt_24 {
  font-size: 24px;
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
    font-size: 24px;
    line-height: 33px;
    color: #fff;
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
