<template>
  <b-modal
    id="modal-scoped"
    v-model="isModalOpen"
    size="md"
    modal-class="patient-info-modal"
    hide-footer
    @close="onCancel"
    @hidden="onCancel"
    @ok="onShowInfo"
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

    <template v-slot:default="{ close, ok }">
      <div class="modal-body px-3 px-md-3">
        <div class="d-flex flex-column justify-content-start">
          <div class="txt_patientInfo_16px">ข้อมูลส่วนตัว</div>
          <div class="txt_patientInfo_13px">
            ชื่อ-นามสกุล: {{detailmodal.profile.real_name}}  {{detailmodal.profile.last_name}}
          </div>
          <div class="txt_patientInfo_13px">เพศ: ชาย</div>
          <div class="txt_patientInfo_13px">ช่วงอายุ: 21-30 ปี</div>
          <div class="txt_patientInfo_13px">เบอร์โทรศัพท์: {{detailmodal.profile.phone}}</div>
          <div class="txt_patientInfo_13px">อัพเดทเมื่อ: 22/09/2021</div>
          <div class="txt_patientInfo_16px" style="padding-top: 0.5rem">
            Group: <span>Group name</span>
          </div>
          <div class="txt_patientInfo_16px" style="padding-top: 0.5rem">
            แบบสอบถาม
          </div>
          <div class="txt_patientInfo_13px">คุณมีโรคประจำตัวหรือไม่: ไม่</div>
        </div>
        <!-- <div class="row d-flex justify-content-center">
          <div class="col-12 col-md-4 col-lg-4">
            <div class="pt-2">
              <div class="form-group mb-0">
                <button
                  class="btn btn_red_modal h2dot5 btn-block py-2"
                  @click="close()"
                >
                  No
                </button>
              </div>
            </div>
          </div>
          <div class="col-12 col-md-4 col-lg-4">
            <div class="pt-2">
              <div class="form-group mb-0">
                <button
                  class="btn btn_green_modal h2dot5 btn-block py-2"
                  @click="ok()"
                >
                  Yes
                </button>
              </div>
            </div>
          </div>
        </div> -->
        
      </div>
    </template>
  </b-modal>
</template>

<script>
export default {
  name: 'DeleteWordModal',
  props: {
    detailmodal: {
      type: Array,
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
    onShowInfo: {
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
  mounted() {
    // console.log('bgbgb', this.bgbg)
  },
  methods: {
    onModalHide() {
      this.$emit('onModalHide', false)
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
