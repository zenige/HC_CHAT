<template>
  <div class="hc_navbar content p-0 group-management-group">
    <div class="container pt-3 pt-md-3 pb-0 plr_15p">
      <div class="row">
        <div class="col-12 text-center">
          <div class="d-flex justify-content-between">
            <div class="">
              <nuxt-link
                :to="localePath('/dashboard/all-patient-group')"
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
                <div class="txt_hc_bighead_20p">{{ groupName }}</div>
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
            <span class="txt_vla_grey">({{ patientInGroupData.length }})</span>
          </div>
        </div>
      </div>

      <div class="col-md-12 pb-4">
        <div class="row d-flex align-items-center justify-content-center">
          <b-table
            responsive
            id="group-table"
            :items="patientInGroupProfileData"
            :per-page="0"
            :current-page="currentPage"
            :fields="fields"
            :filter="filter"
            :tbody-tr-class="selectedRowClass"
          >
            <!-- <template #cell(Fullname)="data">
              <div class="d-flex justify-content-start">
                <div>
                  {{ data.item.FullName }}
                </div>
              </div>
            </template> -->
            <!-- <template #cell(Age)="data">
              <div class="d-flex justify-content-start">
                <div>
                  {{ data.item.Age }}
                </div>
              </div>
            </template> -->
            <!-- <template #cell(DateOfBirth)="data">
              <div class="d-flex justify-content-start">
                <div>
                  {{ data.item.DateOfBirth }}
                </div>
              </div>
            </template> -->
            <template #cell(Tel)="data">
              <div class="d-flex justify-content-start">
                {{ data.item.Tel }}
              </div>
            </template>
            <template #head(info)>
              <div class="d-flex justify-content-center">
                รายละเอียดเพิ่มเติม
              </div>
            </template>
            <template #cell(info)="data">
              <div class="row d-flex justify-content-center align-items-center">
                <button
                  class="hcb-btn-light btn btn_hcb_blue_light btn-block"
                  @click="openPatientInfoModal(data.item)"
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
      :userInfoDataModal="userInfoDataModal"
    ></PatientInfoModal>
  </div>
</template>

<script>
import dayjs from 'dayjs'

export default {
  components: {
    PatientInfoModal: () => import('~/components/modals/PatientInfoModal.vue'),
    Loader: () => import('~/components/Loader.vue'),
  },
  data() {
    return {
      userInfoDataModal: {},
      listuser: [],
      groupName: null,
      isLoading: false,
      isShowPatientInfoModal: false,
      filter: '',
      perPage: 10,
      currentPage: 1,
      totalPatient: 0,
      changedQuestionData: '',
      changedAnswerData: '',
      fields: [
        {
          key: 'Fullname',
          label: 'ชื่อ-นามสกุล',
          sortable: true,
          thClass: 'PatientInGroupthName-Class',
          tdClass: 'PatientInGrouptdName-Class',
        },
        {
          key: 'Age',
          label: 'ช่วงอายุ',
          sortable: true,
          thClass: 'PatientInGroupthAge-Class',
          tdClass: 'PatientInGrouptdAge-Class',
          formatter: (key, item) => {
            let d = new Date(key)
            let n = d.getFullYear()
            new Date().getFullYear() - n
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
        {
          key: 'DateOfBirth',
          label: 'วัน/เดือน/ปี เกิด',
          sortable: true,
          thClass: 'PatientInGroupthBirthdate-Class',
          tdClass: 'PatientInGrouptdBirthdate-Class',
        },
        {
          key: 'Tel',
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
      patientInGroupData: [],
      patientInGroupProfileData: [],
      allFeatureData: [],
      userInfoObjects: [],
    }
  },
  watch: {},
  async mounted() {
    this.groupName = this.$route.params.groupId
    this.isLoading = true
    this.patientInGroupData = await this.$axios.get(
      `/dashboard/group?group=${this.groupName}`
    )
    this.patientInGroupData = this.patientInGroupData.data
    this.allFeatureData = await this.$axios.get('logic/linelogic')
    this.allFeatureData = this.allFeatureData.data
    await this.sortfeatureData()
    await this.mergePatientdata()
    await this.mergeFeatureData()

    this.patientInGroupProfileData = this.patientInGroupProfileData.map(
      (item, index) => {
        const symptom = item.symptom
        return {
          Fullname: item.profile.real_name + ' ' + item.profile.last_name,
          Age: item.profile.birthday,
          DateOfBirth: dayjs(item.profile.birthday).format('DD/MM/YYYY'),
          Tel: item.profile.phone,
          Group: item.group,
          UserId: item.userId,
          profileImg: item.pictureUrl,
          SurveyData: this.mergeFeatureData(symptom),
        }
      }
    )
    this.totalPatient = this.patientInGroupProfileData.length
    console.log('patient profile after map', this.patientInGroupProfileData)
  },

  computed: {
    previousUrl() {
      return '/dashboard/all-patient-group'
    },
  },
  methods: {
    mergeFeatureData(objectSymptom) {
      if (objectSymptom) {
        let keyFeature = Object.keys(objectSymptom)
        keyFeature.map((featureName) => {
          const currentIndex = this.allFeatureData.findIndex(
            (item) => item.id === featureName
          )
          this.allFeatureData[currentIndex].Value = objectSymptom[featureName]
        })
        return this.allFeatureData
      } else {
        return []
      }
    },
    mergePatientdata() {
      for (let i = 0; i < this.patientInGroupData.length; i++) {
        this.patientInGroupProfileData[i] = this.patientInGroupData[i]
      }
      console.log('patientInGroupProfileData', this.patientInGroupProfileData)
    },
    selectedRowClass(item) {
      if (item.selected === true) return 'row-selected'
    },
    closeShowPatientInfoModal() {
      this.isShowPatientInfoModal = false
    },
    openPatientInfoModal(value) {
      this.isShowPatientInfoModal = true
      this.userInfoDataModal = value
    },
    sortfeatureData() {
      let sortedFeatureData = []
      let firstFeatureDataSorted = this.allFeatureData.find(
        (item) => item.Previous === null
      )
      sortedFeatureData.push(firstFeatureDataSorted)
      let lastFeatureDataSorted = this.allFeatureData.find(
        (item) => item.Next === null
      )
      this.allFeatureData = this.allFeatureData.filter(
        (item) => item.Previous !== null && item.Next !== null
      )
      for (let i = 0; i < this.allFeatureData.length; i++) {
        let nextFeature = sortedFeatureData[sortedFeatureData.length - 1].Next
        let currentFeature = this.allFeatureData.find(
          (item) => item.id === nextFeature
        )
        sortedFeatureData.push(currentFeature)
      }
      sortedFeatureData.push(lastFeatureDataSorted)
      this.allFeatureData = sortedFeatureData

      console.log('all feature data', this.allFeatureData)
    },
    onShowInfo() {
      console.log('show info')
    },
  },
}
</script>

<style lang="scss">
.PatientInGroupthName-Class,
.PatientInGrouptdQuestion-Class {
  width: 35%;
}
.PatientInGroupthTel-Class,
.PatientInGrouptdTel-Class {
  width: 15%;
}
.PatientInGroupthBirthdate-Class,
.PatientInGrouptdBirthdate-Class {
  width: 15%;
}
.PatientInGroupthAge-Class,
.PatientInGrouptdAge-Class {
  width: 10%;
}
.PatientInGroupthInfo-Class,
.PatientInGrouptdInfo-Class {
  width: 20%;
}
</style>
