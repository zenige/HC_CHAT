<template>
  <div class="hc_navbar content p-0 group-management-group">
    <div class="container pt-3 pt-md-3 pb-0 plr_15p">
      <div class="row">
        <div class="col-12 text-center">
          <div class="d-flex justify-content-between">
            <div class="">
              <nuxt-link
                :to="previousUrl"
                class="txt_grey_light arrow_back_2 d-xl-block"
                ><img
                  src="~assets/hc-libs/images/vl/arrow_back.png"
                  class="w-50p"
              /></nuxt-link>
            </div>
            <div
              class="
                col-8 col-md-4
                d-flex
                align-items-center
                justify-content-center
              "
            >
              <div class="pt-2 pt-md-0 pl-2 pl-md-0">
                <div class="txt_hc_bighead_20p">Group name</div>
              </div>
            </div>
            <div class=""></div>
          </div>
        </div>
      </div>

      <div class="container fitscreen" style="padding: 2rem 0">
        <div class="row d-flex align-items-center">
          <div class="col-8 col-md-4">
            <div class="border_search_gray form-group-feedback-right">
              <div class="input-group">
                <span class="input-group-append"
                  ><span
                    class="
                      input-group-text input-group-text-search-border
                      rounded-left
                    "
                    ><i class="icon-search4 txt_grey mr-2"></i></span
                ></span>
                <input
                  v-model="filter"
                  type="search"
                  class="
                    form-control
                    rounded-right
                    form-control-search-border
                    h2dot5
                  "
                  style="margin-right: 1rem"
                  placeholder="Search for a word...."
                />
                <div class="form-control-feedback" @click="filter = ''">
                  <i class="icon-cross3 txt_grey" style="height: 22px"></i>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="col-md-12" style="padding-bottom: 1rem">
        <div class="row d-flex align-items-center">
          <div class="txt_hc_head_total">
            Total patient
            <span class="txt_vla_grey">(45)</span>
          </div>
        </div>
      </div>

      <div class="col-md-12 pb-4">
        <div class="row d-flex align-items-center justify-content-center">
          <b-table
            responsive
            id="group-table"
            :items="patientInGroupData"
            :per-page="0"
            :current-page="currentPage"
            :fields="fields"
            :filter="filter"
            :tbody-tr-class="selectedRowClass"
          >
            <template #cell(name)="data">
              <div class="d-flex justify-content-start">
                <div>
                  {{ data.item.name }}
                </div>
              </div>
            </template>
            <template #cell(gender)="data">
              <div class="d-flex justify-content-start">
                <div>
                  {{ data.item.gender }}
                </div>
              </div>
            </template>
            <template #cell(age)="data">
              <div class="d-flex justify-content-start">
                {{ data.item.age }}
              </div>
            </template>
            <template #cell(tel)="data">
              <div class="d-flex justify-content-start">
                {{ data.item.tel }}
              </div>
            </template>
            <template #head(info)>
              <div class="d-flex justify-content-center">
                รายละเอียดเพิ่มเติม
              </div>
            </template>
            <template #cell(info)>
              <div class="row d-flex justify-content-center align-items-center">
                <button
                  class="hcb-btn-light btn btn_hcb_blue_light btn-block"
                  @click="openPatientInfoModal"
                >
                  Show info
                </button>
              </div>
            </template>
          </b-table>
          <div style="margin-top: 0.5rem">
            <b-pagination
              v-model="currentPage"
              :total-rows="totalPatient"
              :per-page="perPage"
              aria-controls="group-table"
              first-number
              last-number
              align="center"
              class="myPaginattion"
            ></b-pagination>
          </div>
        </div>
      </div>
    </div>

    <PatientInfoModal
      :isOpen="isShowPatientInfoModal"
      :onCancel="closeShowPatientInfoModal"
      :onShowInfo="onShowInfo"
    ></PatientInfoModal>
  </div>
</template>

<script>
export default {
  components: {
    PatientInfoModal: () => import('~/components/modals/PatientInfoModal.vue'),
    Loader: () => import('~/components/Loader.vue'),
  },
  props: {},
  data() {
    return {
      groupName: null,
      isLoading: false,
      isShowPatientInfoModal: false,
      isShowTrainWordModal: false,
      edit: false,
      selectAll: false,
      selectedRow: {},
      filter: '',
      perPage: 10,
      currentPage: 1,
      trainSelected: [],
      deleteSelected: [],
      totalPatient: 0,
      totalPatient: 10,
      changedQuestionData: '',
      changedAnswerData: '',
      fields: [
        {
          key: 'name',
          label: 'ชื่อ-นามสกุล',
          sortable: true,
          thClass: 'PatientInGroupthName-Class',
          tdClass: 'PatientInGrouptdName-Class',
        },
        {
          key: 'gender',
          label: 'เพศ',
          sortable: true,
          thClass: 'PatientInGroupthGender-Class',
          tdClass: 'PatientInGrouptdGender-Class',
        },
        {
          key: 'age',
          label: 'ช่วงอายุ',
          sortable: true,
          thClass: 'PatientInGroupthAge-Class',
          tdClass: 'PatientInGrouptdAge-Class',
        },

        {
          key: 'tel',
          label: 'เบอร์โทรศัพท์',
          sortable: true,
          thClass: 'PatientInGroupthTel-Class',
          tdClass: 'PatientInGrouptdTel-Class',
        },
        {
          key: 'info',
          label: 'รายละเอียดเพิ่มเติม',
          sortable: false,
          thClass: 'PatientInGroupthInfo-Class',
          tdClass: 'PatientInGrouptdInfo-Class',
        },
      ],
      patientInGroupData: [
        {
          name: 'บวรศักดิ์ เหลือจันทร์',
          gender: 'ชาย',
          age: '21-30',
          tel: '0930239802',
        },
      ],
    }
  },
  watch: {
    selectAll(value) {
      this.newWordData.map(function (item) {
        item.selected = value
        return item
      })
    },
    currentPage(value) {
      this.getNewWordData(value, this.perPage, 'question')
    },
  },
  async mounted() {
    this.groupName = this.$route.params.groupId
    await this.getNewWordData(1, 10, 'question')
    this.isLoading = true
  },
  computed: {
    rows() {
      return this.totalPatient
    },
    previousUrl() {
      return '/chatbot-training/group-management'
    },
  },
  methods: {
    openPatientInfoModal() {
      this.isShowPatientInfoModal = true
    },
    onShowInfo() {
      console.log('show info')
    },
    selectedRowClass(item) {
      if (item.selected === true) return 'row-selected'
    },
    // openDeleteWordModal() {
    //   this.deleteSelected = this.newWordData.filter(
    //     (item) => item.selected === true
    //   )
    //   if (this.deleteSelected.length >= 1) {
    //     this.isShowPatientInfoModal = true
    //   } else {
    //     ;(this.isShowPatientInfoModal = false),
    //       this.$bvToast.toast('Please select any word', {
    //         variant: 'danger',
    //         toaster: 'b-toaster-bottom-left',
    //         noCloseButton: true,
    //       })
    //   }
    // },
    closeShowPatientInfoModal() {
      this.isShowPatientInfoModal = false
    },
    async onTrainWord() {
      this.trainSelected = this.newWordData.filter(
        (item) => item.selected === true
      )
      await this.$axios.post('train/trained/many', this.trainSelected)
      this.onDeleteWord()
    },
    openTrainWordModal() {
      this.trainSelected = this.newWordData.filter(
        (item) => item.selected === true
      )
      if (this.trainSelected.length >= 1) {
        this.isShowTrainWordModal = true
      } else {
        ;(this.isShowTrainWordModal = false),
          this.$bvToast.toast('Please select any word', {
            variant: 'danger',
            toaster: 'b-toaster-bottom-left',
            noCloseButton: true,
          })
      }
    },
    closeTrainWordModal() {
      this.isShowTrainWordModal = false
    },
    async onDeleteWord() {
      this.deleteSelected = this.newWordData.filter(
        (item) => item.selected === true
      )
      await this.$axios.delete('train/training/delete/many', {
        data: this.deleteSelected,
      })
      await this.getNewWordData(this.currentPage, 10, 'question')
      this.selectAll = false
    },
    editWord(data) {
      this.changedQuestionData = data.item.question
      this.changedAnswerData = data.item.answer
      data.item.editable = true
    },
    cancleEditWord(data) {
      data.item.editable = false
    },
    async saveWord(data) {
      data.item.question = this.changedQuestionData
      data.item.answer = this.changedAnswerData
      data.item.editable = false
      await this.$axios.patch(`/train/training/` + data.item.id, {
        question: data.item.question,
        answer: data.item.answer,
      })
    },
    async getNewWordData(page, limit, orderBy) {
      let { data } = await this.$axios.get(
        `train/training?pages=${page}&limit=${limit}&order_by=${orderBy}`
      )
      this.newWordData = data.map((item) => {
        // collect total new word data
        if (item.total) {
          return (
            {
              id: undefined,
            },
            (this.totalPatient = item.total)
          )
          // it will return undefined item
        } else {
          return {
            answer: item.answer,
            time: item.time,
            count: item.count,
            confident: item.confident,
            question: item.question,
            id: item.id,
            selected: false,
            editable: false,
          }
        }
      })
      // remove undefined item
      this.newWordData = this.newWordData.filter(function (element) {
        return element.id !== undefined
      })
      // console.log(this.totalPatient)
      // console.log(this.newWordData)
    },
  },
}
</script>

<style lang="scss">
.PatientInGroupthName-Class,
.PatientInGrouptdQuestion-Class {
  width: 25%;
}
.PatientInGroupthTel-Class,
.PatientInGrouptdTel-Class {
  width: 25%;
}
.PatientInGroupthGender-Class,
.PatientInGrouptdGender-Class {
  width: 15%;
}
.PatientInGroupthAge-Class,
.PatientInGrouptdAge-Class {
  width: 15%;
}
.PatientInGroupthInfo-Class,
.PatientInGrouptdInfo-Class {
  width: 20%;
}
</style>
