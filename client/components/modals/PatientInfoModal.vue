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
            แบบประเมิน
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
          <div class="txt_patientInfo_16px" style="padding-top: 0.5rem">
            รูปภาพ
          </div>
          <b-container fluid class="p-2">
            <div :class="['sectionImg', { activeShowMore: showMore === true }]">
              <div v-for="(item, index) in userImage" :key="index">
                <b-img
                  @click="showModalImg(index, item.src)"
                  thumbnail
                  fluid
                  :src="item.src"
                  :alt="item.alt"
                  :id="`Img${index}`"
                ></b-img>
                <!-- <div :id="`ImgModal${index}`" class="userImgModal">
                  <font-awesome-icon
                    @click="closeModalImg(index)"
                    class="close-img-modal"
                    icon="times"
                  />
                  <img class="img-modal-content" :id="`modalImg${index}`" />
                </div> -->
              </div>
            </div>
            <div class="show-more pt-2 mx-auto" style="max-width: 50%">
              <button
                class="hcb-btn-light btn btn_hcb_blue_light btn-block"
                style="margin: 0 auto"
                v-if="!showMore && this.userImage.length > 3"
                @click="setShowmore()"
              >
                แสดงเพิ่มเติม
              </button>
              <button
                class="hcb-btn-light btn btn_hcb_blue_light btn-block"
                style="margin: 0 auto"
                v-else
                @click="setShowmore()"
              >
                แสดงน้อยลง
              </button>
            </div>
          </b-container>
        </div>
      </div>
    </template>
    <UserImgModal
      :isOpen="isShowImgModal"
      :onCancel="closeShowImgModal"
      :imgModal="imgDataModal"
    />
  </b-modal>
</template>

<script>
import VueEasyLightbox from 'vue-easy-lightbox'
import Vue from 'vue'
import { library } from '@fortawesome/fontawesome-svg-core'
import { faTimes } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

library.add(faTimes)
Vue.component('font-awesome-icon', FontAwesomeIcon)
Vue.use(VueEasyLightbox)

export default {
  name: 'patientInfoModal',
  components: {
    UserImgModal: () => import('~/components/dashboard/UserImgModal.vue'),
  },
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
    isShowImgModal: false,
    showMore: false,
    imgDataModal: {
      src: null,
    },
    userImage: [
      {
        src: 'https://picsum.photos/250/250/?image=59',
        alt: 'Image 1',
      },
      {
        src: 'https://picsum.photos/250/250/?image=59',
        alt: 'Image 1',
      },
      {
        src: 'https://picsum.photos/250/250/?image=59',
        alt: 'Image 1',
      },
      {
        src: 'https://picsum.photos/250/250/?image=59',
        alt: 'Image 1',
      },
    ],
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
    closeShowImgModal() {
      this.isShowImgModal = false
    },
    showModalImg(index, srcImg) {
      this.isShowImgModal = true
      this.imgDataModal.src = srcImg
    },
    closeModalImg(index) {
      // let span = document.getElementsByClassName("close-img-modal")[0];
      let modal = document.getElementById(`ImgModal${index}`)

      // When the user clicks on <span> (x), close the modal

      modal.style.display = 'none'
    },
    setShowmore() {
      if (this.showMore === true) {
        this.showMore = false
      } else {
        this.showMore = true
      }
    },
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
.sectionImg {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-gap: 10px;
  height: 180px;
  overflow: hidden;
}
.sectionImg > div {
  width: 100%;
}
.activeShowMore {
  height: 100% !important;
  overflow: initial;
}
/* The Modal (background) */
.userImgModal {
  display: none; /* Hidden by default */
  position: fixed; /* Stay in place */
  z-index: 1; /* Sit on top */
  vertical-align: middle;
  padding-top: 10%; /* Location of the box */
  left: 0;
  top: 0;
  margin: 0 auto;
  width: 100vw; /* Full width */
  height: 100%; /* Full height */
  overflow: auto; /* Enable scroll if needed */
  background-color: rgb(0, 0, 0); /* Fallback color */
  background-color: rgba(0, 0, 0, 0.9); /* Black w/ opacity */
}
/* Modal Content (image) */
.img-modal-content {
  margin: auto;
  display: flex;
  justify-content: center;
  align-items: center;
  min-width: 80%;
  max-width: 100%;
}
/* Add Animation */
.img-modal-content {
  -webkit-animation-name: zoom;
  -webkit-animation-duration: 0.6s;
  animation-name: zoom;
  animation-duration: 0.6s;
}

@-webkit-keyframes zoom {
  from {
    -webkit-transform: scale(0);
  }
  to {
    -webkit-transform: scale(1);
  }
}

@keyframes zoom {
  from {
    transform: scale(0);
  }
  to {
    transform: scale(1);
  }
}

/* The Close Button */
.close-img-modal {
  position: absolute;
  top: 25px;
  right: 35px;
  color: #f1f1f1;
  font-size: 30px;
  transition: 0.3s;
}

.close-img-modal:hover,
.close-img-modal:focus {
  color: #bbb;
  text-decoration: none;
  cursor: pointer;
}

/* 100% Image Width on Smaller Screens */
@media only screen and (max-width: 700px) {
  .img-modal-content {
    width: 100%;
  }
  .sectionImg {
    grid-template-columns: repeat(2, 1fr);
    height: 145px;
  }
}
.img-thumbnail {
  background-color: #f5f5f5;
  box-shadow: none;
  border: 0px solid;
  border-radius: -22.8125rem;
  max-width: 100%;
  height: auto;
  cursor: pointer;
}
.img-thumbnail:hover {
  opacity: 0.8;
}
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
