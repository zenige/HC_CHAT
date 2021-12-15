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
                      class="image mt-3"
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
                <div class="m_width_120p text-center footerBtn">
                  ส่งแบบสอบถาม
                </div>
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
                <div class="m_width_120p text-center footerBtn">
                  ส่งแบบสอบถาม
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Vue from 'vue'

var quiz = {
  title: 'quiz sample',
  questions: [
    {
      text: '1.) คุณเป็นผื่นในบริเวณ ศีรษะ/คอ คิดเป็นสัดส่วนประมาณกี่เปอร์เซ็นต์ของพื้นที่ในบริเวณนี้ทั้งหมด?',
      questionImage: 'https://i.ibb.co/QJFL59y/1.png',
      answers: [
        {
          text: '0% (ไม่เป็นผื่น)',
          value: 0,
        },
        {
          text: 'ประมาณ 1-9%',
          value: 1,
        },
        {
          text: 'ประมาณ 10-29%',
          value: 2,
        },
        {
          text: 'ประมาณ 30-49%',
          value: 3,
        },
        {
          text: 'ประมาณ 50-69%',
          value: 4,
        },
        {
          text: 'ประมาณ 70-89%',
          value: 5,
        },
        {
          text: 'ประมาณ 90-100%',
          value: 6,
        },
      ],
      checkpoint: '',
      check: false,
    },
    {
      text: '1.1) คุณเป็นผื่นแดงในบริเวณ ศีรษะ/คอ มากน้อยระดับไหน?',
      questionImage: 'https://i.ibb.co/s13Sjg3/redness.png',
      answers: [
        {
          text: 'None (ไม่เป็นผื่นแดง)',
          value: 0,
        },
        {
          text: 'Mild (เล็กน้อย บาง ๆ หรือมีสีชมพู)',
          value: 1,
        },
        {
          text: 'Moderate (ปานกลาง มีสีแดงหม่น ๆ ที่มองเห็นได้ชัด)',
          value: 2,
        },
        {
          text: 'Severe (มาก มีสีแดงเข้ม มองเห็นได้ชัดเจน)',
          value: 3,
        },
      ],
      checkpoint: '',
      check: false,
    },
    {
      text: '1.2) คุณเป็นตุ่มหรือมีรอยนูนของผื่นในบริเวณ ศีรษะ/คอ มากน้อยระดับไหน?',
      questionImage: 'https://i.ibb.co/fS7xfQF/edema.png',
      answers: [
        {
          text: 'None (ไม่เป็นตุ่มหรือมีรอยนูน)',
          value: 0,
        },
        {
          text: 'Mild (เล็กน้อย แทบมองไม่เห็น)',
          value: 1,
        },
        {
          text: 'Moderate (ปานกลาง มองเห็นได้ชัด แต่ไม่เด่นชัดมาก)',
          value: 2,
        },
        {
          text: 'Severe (มองเห็นได้เด่นชัดเจนมาก)',
          value: 3,
        },
      ],
      checkpoint: '',
      check: false,
    },
    {
      text: '1.3) คุณมีรอยถลอกหรือรอยผิวหนังที่แตกเป็นแผลของผื่นในบริเวณ ศีรษะ/คอ มากน้อยระดับไหน?',
      questionImage: 'https://i.ibb.co/f4VBYtp/excoriation.png',
      answers: [
        {
          text: 'None (ไม่เป็นรอยถลอกหรือมีรอยผิวหนังที่แตก)',
          value: 0,
        },
        {
          text: 'Mild (เล็กน้อย มีไม่กี่จุด มองเห็นแค่ผิวเผิน)',
          value: 1,
        },
        {
          text: 'Moderate (ปานกลาง มีหลายจุด มองเห็นได้ชัดและ/หรือมีความลึกของแผลเล็กน้อย)',
          value: 2,
        },
        {
          text: 'Severe (มาก มีหลายจุดอย่างกว้างขวาง มองเห็นได้ชัดและ/หรือมีความลึกของแผลมาก)',
          value: 3,
        },
      ],
      checkpoint: '',
      check: false,
    },
    {
      text: '1.4) คุณมีความหนาหรือความแข็งตัวของผิวหนังในบริเวณ ศีรษะ/คอ มากน้อยระดับไหน?',
      questionImage: 'https://i.ibb.co/G9cvQ5w/lichenification.png',
      answers: [
        {
          text: 'None (ไม่มีความหนาหรือความแข็งตัวของผิวหนัง)',
          value: 0,
        },
        {
          text: 'Mild (เล็กน้อย ผิวหนังมีรอยหนาขึ้นเล็กน้อย)',
          value: 1,
        },
        {
          text: 'Moderate (ปานกลาง ผิวหนังหนาขึ้นอย่างเห็นได้ชัดและ/หรือมีอาการคันเล็กน้อย)',
          value: 2,
        },
        {
          text: 'Severe (มาก ผิวหนังหนาขึ้นอย่างเห็นได้ชัด มีร่องลึกที่เห็นได้ชัดและ/หรือมีอาการคันมาก)',
          value: 3,
        },
      ],
      checkpoint: '',
      check: false,
    },
    {
      text: '2.) คุณเป็นผื่นในบริเวณ ลำตัว คิดเป็นสัดส่วนประมาณกี่เปอร์เซ็นต์ของพื้นที่ในบริเวณนี้ทั้งหมด?',
      questionImage: 'https://i.ibb.co/ThhgjLg/2.png',
      answers: [
        {
          text: '0% (ไม่เป็นผื่น)',
          value: 0,
        },
        {
          text: 'ประมาณ 1-9%',
          value: 1,
        },
        {
          text: 'ประมาณ 10-29%',
          value: 2,
        },
        {
          text: 'ประมาณ 30-49%',
          value: 3,
        },
        {
          text: 'ประมาณ 50-69%',
          value: 4,
        },
        {
          text: 'ประมาณ 70-89%',
          value: 5,
        },
        {
          text: 'ประมาณ 90-100%',
          value: 6,
        },
      ],
      checkpoint: '',
      check: false,
    },
    {
      text: '2.1) คุณเป็นผื่นแดงในบริเวณ ลำตัว มากน้อยระดับไหน?',
      questionImage: 'https://i.ibb.co/s13Sjg3/redness.png',
      answers: [
        {
          text: 'None (ไม่เป็นผื่นแดง)',
          value: 0,
        },
        {
          text: 'Mild (เล็กน้อย บาง ๆ หรือมีสีชมพู)',
          value: 1,
        },
        {
          text: 'Moderate (ปานกลาง มีสีแดงหม่น ๆ ที่มองเห็นได้ชัด)',
          value: 2,
        },
        {
          text: 'Severe (มาก มีสีแดงเข้ม มองเห็นได้ชัดเจน)',
          value: 3,
        },
      ],
      checkpoint: '',
      check: false,
    },
    {
      text: '2.2) คุณเป็นตุ่มหรือมีรอยนูนของผื่นในบริเวณ ลำตัว มากน้อยระดับไหน?',
      questionImage: 'https://i.ibb.co/fS7xfQF/edema.png',
      answers: [
        {
          text: 'None (ไม่เป็นตุ่มหรือมีรอยนูน)',
          value: 0,
        },
        {
          text: 'Mild (เล็กน้อย แทบมองไม่เห็น)',
          value: 1,
        },
        {
          text: 'Moderate (ปานกลาง มองเห็นได้ชัด แต่ไม่เด่นชัดมาก)',
          value: 2,
        },
        {
          text: 'Severe (มองเห็นได้เด่นชัดเจนมาก)',
          value: 3,
        },
      ],
      checkpoint: '',
      check: false,
    },
    {
      text: '2.3) คุณมีรอยถลอกหรือรอยผิวหนังที่แตกเป็นแผลของผื่นในบริเวณ ลำตัว มากน้อยระดับไหน?',
      questionImage: 'https://i.ibb.co/f4VBYtp/excoriation.png',
      answers: [
        {
          text: 'None (ไม่เป็นรอยถลอกหรือมีรอยผิวหนังที่แตก)',
          value: 0,
        },
        {
          text: 'Mild (เล็กน้อย มีไม่กี่จุด มองเห็นแค่ผิวเผิน)',
          value: 1,
        },
        {
          text: 'Moderate (ปานกลาง มีหลายจุด มองเห็นได้ชัดและ/หรือมีความลึกของแผลเล็กน้อย)',
          value: 2,
        },
        {
          text: 'Severe (มาก มีหลายจุดอย่างกว้างขวาง มองเห็นได้ชัดและ/หรือมีความลึกของแผลมาก)',
          value: 3,
        },
      ],
      checkpoint: '',
      check: false,
    },
    {
      text: '2.4) คุณมีความหนาหรือความแข็งตัวของผิวหนังในบริเวณ ลำตัว มากน้อยระดับไหน?',
      questionImage: 'https://i.ibb.co/G9cvQ5w/lichenification.png',
      answers: [
        {
          text: 'None (ไม่มีความหนาหรือความแข็งตัวของผิวหนัง)',
          value: 0,
        },
        {
          text: 'Mild (เล็กน้อย ผิวหนังมีรอยหนาขึ้นเล็กน้อย)',
          value: 1,
        },
        {
          text: 'Moderate (ปานกลาง ผิวหนังหนาขึ้นอย่างเห็นได้ชัดและ/หรือมีอาการคันเล็กน้อย)',
          value: 2,
        },
        {
          text: 'Severe (มาก ผิวหนังหนาขึ้นอย่างเห็นได้ชัด มีร่องลึกที่เห็นได้ชัดและ/หรือมีอาการคันมาก)',
          value: 3,
        },
      ],
      checkpoint: '',
      check: false,
    },
    {
      text: '3.) คุณเป็นผื่นในบริเวณ แขน คิดเป็นสัดส่วนประมาณกี่เปอร์เซ็นต์ของพื้นที่ในบริเวณนี้ทั้งหมด?',
      questionImage: 'https://i.ibb.co/jRP3MHw/3.png',
      answers: [
        {
          text: '0% (ไม่เป็นผื่น)',
          value: 0,
        },
        {
          text: 'ประมาณ 1-9%',
          value: 1,
        },
        {
          text: 'ประมาณ 10-29%',
          value: 2,
        },
        {
          text: 'ประมาณ 30-49%',
          value: 3,
        },
        {
          text: 'ประมาณ 50-69%',
          value: 4,
        },
        {
          text: 'ประมาณ 70-89%',
          value: 5,
        },
        {
          text: 'ประมาณ 90-100%',
          value: 6,
        },
      ],
      checkpoint: '',
      check: false,
    },
    {
      text: '3.1) คุณเป็นผื่นแดงในบริเวณ แขน มากน้อยระดับไหน?',
      questionImage: 'https://i.ibb.co/s13Sjg3/redness.png',
      answers: [
        {
          text: 'None (ไม่เป็นผื่นแดง)',
          value: 0,
        },
        {
          text: 'Mild (เล็กน้อย บาง ๆ หรือมีสีชมพู)',
          value: 1,
        },
        {
          text: 'Moderate (ปานกลาง มีสีแดงหม่น ๆ ที่มองเห็นได้ชัด)',
          value: 2,
        },
        {
          text: 'Severe (มาก มีสีแดงเข้ม มองเห็นได้ชัดเจน)',
          value: 3,
        },
      ],
      checkpoint: '',
      check: false,
    },
    {
      text: '3.2) คุณเป็นตุ่มหรือมีรอยนูนของผื่นในบริเวณ แขน มากน้อยระดับไหน?',
      questionImage: 'https://i.ibb.co/fS7xfQF/edema.png',
      answers: [
        {
          text: 'None (ไม่เป็นตุ่มหรือมีรอยนูน)',
          value: 0,
        },
        {
          text: 'Mild (เล็กน้อย แทบมองไม่เห็น)',
          value: 1,
        },
        {
          text: 'Moderate (ปานกลาง มองเห็นได้ชัด แต่ไม่เด่นชัดมาก)',
          value: 2,
        },
        {
          text: 'Severe (มองเห็นได้เด่นชัดเจนมาก)',
          value: 3,
        },
      ],
      checkpoint: '',
      check: false,
    },
    {
      text: '3.3) คุณมีรอยถลอกหรือรอยผิวหนังที่แตกเป็นแผลของผื่นในบริเวณ แขน มากน้อยระดับไหน?',
      questionImage: 'https://i.ibb.co/f4VBYtp/excoriation.png',
      answers: [
        {
          text: 'None (ไม่เป็นรอยถลอกหรือมีรอยผิวหนังที่แตก)',
          value: 0,
        },
        {
          text: 'Mild (เล็กน้อย มีไม่กี่จุด มองเห็นแค่ผิวเผิน)',
          value: 1,
        },
        {
          text: 'Moderate (ปานกลาง มีหลายจุด มองเห็นได้ชัดและ/หรือมีความลึกของแผลเล็กน้อย)',
          value: 2,
        },
        {
          text: 'Severe (มาก มีหลายจุดอย่างกว้างขวาง มองเห็นได้ชัดและ/หรือมีความลึกของแผลมาก)',
          value: 3,
        },
      ],
      checkpoint: '',
      check: false,
    },
    {
      text: '3.4) คุณมีความหนาหรือความแข็งตัวของผิวหนังในบริเวณ แขน มากน้อยระดับไหน?',
      questionImage: 'https://i.ibb.co/G9cvQ5w/lichenification.png',
      answers: [
        {
          text: 'None (ไม่มีความหนาหรือความแข็งตัวของผิวหนัง)',
          value: 0,
        },
        {
          text: 'Mild (เล็กน้อย ผิวหนังมีรอยหนาขึ้นเล็กน้อย)',
          value: 1,
        },
        {
          text: 'Moderate (ปานกลาง ผิวหนังหนาขึ้นอย่างเห็นได้ชัดและ/หรือมีอาการคันเล็กน้อย)',
          value: 2,
        },
        {
          text: 'Severe (มาก ผิวหนังหนาขึ้นอย่างเห็นได้ชัด มีร่องลึกที่เห็นได้ชัดและ/หรือมีอาการคันมาก)',
          value: 3,
        },
      ],
      checkpoint: '',
      check: false,
    },
    {
      text: '4.) คุณเป็นผื่นในบริเวณ ขา คิดเป็นสัดส่วนประมาณกี่เปอร์เซ็นต์ของพื้นที่ในบริเวณนี้ทั้งหมด?',
      questionImage: 'https://i.ibb.co/3kDjC4F/4.png',
      answers: [
        {
          text: '0% (ไม่เป็นผื่น)',
          value: 0,
        },
        {
          text: 'ประมาณ 1-9%',
          value: 1,
        },
        {
          text: 'ประมาณ 10-29%',
          value: 2,
        },
        {
          text: 'ประมาณ 30-49%',
          value: 3,
        },
        {
          text: 'ประมาณ 50-69%',
          value: 4,
        },
        {
          text: 'ประมาณ 70-89%',
          value: 5,
        },
        {
          text: 'ประมาณ 90-100%',
          value: 6,
        },
      ],
      checkpoint: '',
      check: false,
    },
    {
      text: '4.1) คุณเป็นผื่นแดงในบริเวณ ขา มากน้อยระดับไหน?',
      questionImage: 'https://i.ibb.co/s13Sjg3/redness.png',
      answers: [
        {
          text: 'None (ไม่เป็นผื่นแดง)',
          value: 0,
        },
        {
          text: 'Mild (เล็กน้อย บาง ๆ หรือมีสีชมพู)',
          value: 1,
        },
        {
          text: 'Moderate (ปานกลาง มีสีแดงหม่น ๆ ที่มองเห็นได้ชัด)',
          value: 2,
        },
        {
          text: 'Severe (มาก มีสีแดงเข้ม มองเห็นได้ชัดเจน)',
          value: 3,
        },
      ],
      checkpoint: '',
      check: false,
    },
    {
      text: '4.2) คุณเป็นตุ่มหรือมีรอยนูนของผื่นในบริเวณ ขา มากน้อยระดับไหน?',
      questionImage: 'https://i.ibb.co/fS7xfQF/edema.png',
      answers: [
        {
          text: 'None (ไม่เป็นตุ่มหรือมีรอยนูน)',
          value: 0,
        },
        {
          text: 'Mild (เล็กน้อย แทบมองไม่เห็น)',
          value: 1,
        },
        {
          text: 'Moderate (ปานกลาง มองเห็นได้ชัด แต่ไม่เด่นชัดมาก)',
          value: 2,
        },
        {
          text: 'Severe (มองเห็นได้เด่นชัดเจนมาก)',
          value: 3,
        },
      ],
      checkpoint: '',
      check: false,
    },
    {
      text: '4.3) คุณมีรอยถลอกหรือรอยผิวหนังที่แตกเป็นแผลของผื่นในบริเวณ ขา มากน้อยระดับไหน?',
      questionImage: 'https://i.ibb.co/f4VBYtp/excoriation.png',
      answers: [
        {
          text: 'None (ไม่เป็นรอยถลอกหรือมีรอยผิวหนังที่แตก)',
          value: 0,
        },
        {
          text: 'Mild (เล็กน้อย มีไม่กี่จุด มองเห็นแค่ผิวเผิน)',
          value: 1,
        },
        {
          text: 'Moderate (ปานกลาง มีหลายจุด มองเห็นได้ชัดและ/หรือมีความลึกของแผลเล็กน้อย)',
          value: 2,
        },
        {
          text: 'Severe (มาก มีหลายจุดอย่างกว้างขวาง มองเห็นได้ชัดและ/หรือมีความลึกของแผลมาก)',
          value: 3,
        },
      ],
      checkpoint: '',
      check: false,
    },
    {
      text: '4.4) คุณมีความหนาหรือความแข็งตัวของผิวหนังในบริเวณ ขา มากน้อยระดับไหน?',
      questionImage: 'https://i.ibb.co/G9cvQ5w/lichenification.png',
      answers: [
        {
          text: 'None (ไม่มีความหนาหรือความแข็งตัวของผิวหนัง)',
          value: 0,
        },
        {
          text: 'Mild (เล็กน้อย ผิวหนังมีรอยหนาขึ้นเล็กน้อย)',
          value: 1,
        },
        {
          text: 'Moderate (ปานกลาง ผิวหนังหนาขึ้นอย่างเห็นได้ชัดและ/หรือมีอาการคันเล็กน้อย)',
          value: 2,
        },
        {
          text: 'Severe (มาก ผิวหนังหนาขึ้นอย่างเห็นได้ชัด มีร่องลึกที่เห็นได้ชัดและ/หรือมีอาการคันมาก)',
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
      reply_token: '',
      damage: {},
      userId: '',
    }
  },
  components: {
    Loader: () => import('~/components/Loader.vue'),
  },
  async mounted() {
    //   this.liff.init({
    //   liffId :'1655993001-QLqyKnVe'
    // })
    this.userId = this.$route.query.userId
    alert(this.userId)
    console.log(this.$route)
    Vue.loadScript('https://static.line-scdn.net/liff/edge/2/sdk.js')
      .then(() => {
        // Script is loaded, do something
        liff
          .init({
            liffId: '1655993001-QLqyKnVe',
          })
          .then(() => {
            console.log('PASS')
          })
      })
      .catch((err) => {
        console.log('f', err)
        // Failed to fetch script
      })
    // this.reply_token = this.$route.query.replyToken
    // this.isLoading = true
    // this.isLoading = false
  },
  beforeCreate() {},
  methods: {
    async math() {
      let head =
        (this.ans[1] + this.ans[2] + this.ans[3] + this.ans[4]) *
        this.ans[0] *
        0.1
      let U_limbs =
        (this.ans[6] + this.ans[7] + this.ans[8] + this.ans[9]) *
        this.ans[5] *
        0.2
      let trunk =
        (this.ans[11] + this.ans[12] + this.ans[13] + this.ans[14]) *
        this.ans[10] *
        0.3
      let L_limbs =
        (this.ans[16] + this.ans[17] + this.ans[18] + this.ans[19]) *
        this.ans[15] *
        0.4

      let sum = head + U_limbs + trunk + L_limbs
      this.final = sum.toFixed(2)
      console.log('คำตอบ', this.final)
      await this.calDamgae()
      await this.updateState()
      await this.sendMessage()

      this.$router.push(this.localePath('/questionnaire/submit-answer'))
    },
    calDamgae() {
      if (this.final == 0) {
        console.log('000')
        this.damage = {
          damageTH: 'ไม่มีระดับความรุนแรง',
          damageEN: 'clear',
          med: 'แนวทางในการใช้ยารักษาตามระดับความรุนแรงนี้\n\nควรเลือกใช้ยาคอร์ติโคสเตียรอยด์ชนิดทาภายนอกที่มีระดับความแรงระดับ Class VII: Least Potent \n\nเช่น Hydrocortisone acetate 1%, 2.5% cream (Hytisone® cream) หรือ Prednisolone 0.5% (Clinipred® cream) เป็นต้น\n\n\nอ้างอิงจาก: https://www.psoriasis.org/potency-chart/',
        }
      } else if (this.final >= 0.1 && this.final <= 1) {
        this.damage = { damageTH: 'ไม่มีระดับความรุนแรง' }
      } else if (this.final >= 1.1 && this.final <= 7) {
        this.damage = { damageTH: 'ไม่มีระดับความรุนแรง' }
      } else if (this.final >= 7.1 && this.final <= 21) {
        this.damage = { damageTH: 'ไม่มีระดับความรุนแรง' }
      } else if (this.final >= 21.1 && this.final <= 50) {
        this.damage = { damageTH: 'ไม่มีระดับความรุนแรง' }
      } else if (this.final >= 50.1 && this.final <= 72) {
        this.damage = { damageTH: 'ไม่มีระดับความรุนแรง' }
      } else {
        this.damage = { damageTH: 'ไม่มีระดับความรุนแรง' }
      }
    },
    sendMessage() {
      liff
        .sendMessages([
          {
            type: 'message',
            message: `คุณมีระดับความรุนแรงของโรคผื่นแพ้อักเสบ (Eczema) อยู่ที่ ${this.final} คะแนน ซึ่งถือว่าอยู่ในระดับที่ ${this.damage.damageTH} ตามเกณฑ์ของ Eczema Area and Severity Index (EASI) 😄`,
          },
          {
            type: 'message',
            message:
              'คุณต้องการดูผลิตภัณฑ์ที่แนะนำหรือไม่?\n\nกรุณาพิมพ์ "ใช่" เพื่อดูผลิตภัณฑ์แนะนำ',
          },
        ])
        .then(() => {
          console.log('message sent')
        })
        .catch((err) => {
          console.log('error', err)
        })
    },
    async updateState() {
      console.log(this.damage.damageEN)
      try {
        let body = {
          userId: this.userId,
          state: 'eczema',
          subState: this.damage.damageEN,
        }
        await this.$axios.post(
          'https://3a8a-58-10-4-220.ngrok.io/api/updateState',
          body
        )
      } catch (err) {
        alert(err)
      }
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

    async next() {
      await this.sendMessage()
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
