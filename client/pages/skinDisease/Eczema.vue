<template>
  <div>
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
              <div
                style="cursor: pointer"
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
    <div v-if="end === false">
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
    <div v-if="end === true">
      <div
        class="container container_short footerV2"
        v-if="quiz.questions[questionIndex - 1].check === false"
        disabled
      >
        <div class="row mt-3 mb-3">
          <div class="col-12 d-flex align-items-center justify-content-center">
            <div class="m_width_120p">
              <div class="m_width_120p text-center footerBtn">ส่งแบบสอบถาม</div>
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
          <div class="col-12 d-flex align-items-center justify-content-center">
            <div class="m_width_120p">
              <div class="m_width_120p text-center footerBtn">ส่งแบบสอบถาม</div>
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
      questionImage: 'https://i.ibb.co/tbSvm5N/1-1.png',
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
      questionImage: 'https://i.ibb.co/myzjx9p/1-2.png',
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
      questionImage: 'https://i.ibb.co/V3ps1Hb/1-3.png',
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
      questionImage: 'https://i.ibb.co/kX6sBq8/1-4.png',
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
      questionImage: 'https://i.ibb.co/tbSvm5N/1-1.png',
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
      questionImage: 'https://i.ibb.co/myzjx9p/1-2.png',
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
      questionImage: 'https://i.ibb.co/V3ps1Hb/1-3.png',
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
      questionImage: 'https://i.ibb.co/kX6sBq8/1-4.png',
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
      questionImage: 'https://i.ibb.co/tbSvm5N/1-1.png',
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
      questionImage: 'https://i.ibb.co/myzjx9p/1-2.png',
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
      questionImage: 'https://i.ibb.co/V3ps1Hb/1-3.png',
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
      questionImage: 'https://i.ibb.co/kX6sBq8/1-4.png',
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
      questionImage: 'https://i.ibb.co/tbSvm5N/1-1.png',
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
      questionImage: 'https://i.ibb.co/myzjx9p/1-2.png',
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
      questionImage: 'https://i.ibb.co/V3ps1Hb/1-3.png',
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
      questionImage: 'https://i.ibb.co/kX6sBq8/1-4.png',
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
    }
  },
  methods: {
    math() {
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
      this.$router.push(this.localePath('/questionnaire/submit-answer'))
    },
    checkpointbg(value, score) {
      this.quiz.questions[this.questionIndex - 1].checkpoint = value
      this.quiz.questions[this.questionIndex - 1].check = true
      console.log(this.quiz.questions[this.questionIndex - 1])
      console.log('nn', this.quiz.questions)
      console.log(value)
      this.ans[this.questionIndex - 1] = score
      console.log('sc', this.ans)
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
