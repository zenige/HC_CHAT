<template>
  <b-modal
    id="modal-scoped"
    v-model="isModalOpen"
    size="md"
    modal-class="patient-info-modal"
    hide-footer
    @close="onCancel"
    @hidden="onCancel"
  >
    <template v-slot:modal-header="{ close }">
      <div class="modal-header bg-white py-2 px-0 mx-3 mt-2">
        <h4 class="modal-title txt_hc_modaltitle mr-4 pr-2">
          รายละเอียดเพิ่มเติม
        </h4>
        <button
          type="button"
          class="close pr-1 pt_15p"
          data-dismiss="modal"
          @click="close()"
        >
          <img
            src="~assets/hc-libs/images/main/ic_close_grey.svg"
            width="37"
            loading="lazy"
          />
        </button>
      </div>
    </template>

    <template>
      <div class="modal-body px-3 px-md-3">
        <div class="d-flex flex-column justify-content-start">
          <div class="txt_patientInfo_16px">ข้อมูลส่วนตัว</div>
          <div class="txt_patientInfo_13px">
            ชื่อ-นามสกุล: {{ userInfoDataModal.Fullname }}
          </div>
          <!-- <div class="txt_patientInfo_13px">เพศ: ชาย</div> -->
          <div class="txt_patientInfo_13px">
            ช่วงอายุ: {{ formatAge(userInfoDataModal.Age) }}
          </div>
          <div class="txt_patientInfo_13px">
            วัน/เดือน/ปี เกิด: {{ userInfoDataModal.DateOfBirth }}
          </div>
          <div class="txt_patientInfo_13px">
            เบอร์โทรศัพท์: {{ userInfoDataModal.Tel }}
          </div>
          <div class="txt_patientInfo_16px" style="padding-top: 0.5rem">
            Group: <span>{{ userInfoDataModal.Group }}</span>
          </div>
          <div class="txt_patientInfo_16px" style="padding-top: 0.5rem">
            แบบสอบถาม
          </div>
          <div
            v-for="(itemSurvey, index) in userInfoDataModal.SurveyData"
            :key="index"
            class="txt_patientInfo_13px"
          >
            {{ itemSurvey.Question }}:
            {{
              itemSurvey.Value === 'true'
                ? 'ใช่'
                : itemSurvey.Value === 'false'
                ? 'ไม่'
                : itemSurvey.Value === 'ANY'
                ? 'บ้าง'
                : itemSurvey.Value
            }}
          </div>
        </div>
      </div>
    </template>
  </b-modal>
</template>

<script>
export default {
  name: 'patientInfoModal',
  props: {
    userInfoDataModal: {
      type: Object,
      default: () => {},
    },
    isOpen: {
      type: Boolean,
      default: false,
    },
    onCancel: {
      type: Function,
      default: () => {},
    },
  },
  data: () => ({
    isModalOpen: false,
  }),
  watch: {
    isOpen(newVal) {
      this.isModalOpen = newVal
    },
    isModalOpen(newVal) {
      if (!newVal) {
        this.onModalHide()
      }
    },
  },
  mounted() {},
  methods: {
    onModalHide() {
      this.$emit('onModalHide', false)
    },
    formatAge(value) {
      let d = new Date(value)
      let n = d.getFullYear()
      n = new Date().getFullYear() - n
      if (n < 11) {
        return `0 - 10 ปี`
      } else if (10 < n < 21) {
        return `11 - 20 ปี`
      } else if (20 < n < 31) {
        return `21 - 30 ปี`
      } else if (30 < n < 41) {
        return `31 - 40 ปี`
      } else if (40 < n < 51) {
        return `41 - 50 ปี`
      } else if (50 < n < 61) {
        return `51 - 60 ปี`
      } else if (60 < n < 71) {
        return `61 - 70 ปี`
      } else if (70 < n < 81) {
        return `71 - 80 ปี`
      } else {
        return ` > 80 ปี`
      }
    },
  },
}
</script>

<style lang="scss">
.txt_patientInfo_16px {
  color: #333333;
  font-size: 16px;
  padding-bottom: 0.5rem;
}
.txt_patientInfo_16px span {
  color: #707683;
}
.txt_patientInfo_13px {
  color: #707683;
  font-size: 13px;
  padding: 0.5em 0;
}
.patient-info-modal {
  .modal-header {
    width: 100%;
    margin: 0 !important;
  }

  .modal-body {
    padding: 8px 0;
    overflow-y: auto;

    .btn {
      display: flex;
      justify-content: center;
      align-items: center;
    }
  }
}
</style>
