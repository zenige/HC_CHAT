<template>
  <div class="hc_navbar content p-0 group-management-group">
    <Loader v-if="!isLoading" />
    <div v-else>
      <div class="container fitscreen pt-3 pt-md-3 pb-0 plr_15p">
        <div class="row">
          <div class="col-md-12">
            <div class="row d-flex justify-content-between">
              <div class="col-11 col-md-11 col-lg-10">
                <div class="txt_hc_bighead_20p">
                  COVID-19
                  <span class="txt_hc_bighead_sub_16p pl-2">
                    ({{ groupNamenew.length }} Groups)
                  </span>
                </div>
              </div>
              <span
                v-b-toggle.collapse-1
                class="col-1 col-md-1 col-lg-2 text-right pr-3 pt-1"
              >
                <font-awesome-icon v-if="isVisible1" icon="chevron-up" />
                <font-awesome-icon v-else icon="chevron-down" />
              </span>
            </div>
          </div>
          <div class="col-md-12">
            <hr class="mt-1 mb-3" />
          </div>
        </div>
        <b-collapse
          id="collapse-1"
          class="
            pt-1 pt-md-
            row
            pb-5
            bg_card_hover
            card_vld_wrapper
            content-mangement
          "
          v-model="isVisible1"
        >
          <!-- Group card -->
          <div
            v-for="(group, index) in groupNamenew"
            :key="index"
            class="col-md-4 pb_me-4"
            @click="getCurrentDate(index)"
          >
            <NuxtLink
              :to="
                localePath(`/dashboard/patient-covid-19-group/${group.name}`)
              "
              class="card h-100 mb-0 px-3 py-2 group-card"
            >
              <div class="card-body p_card pb-0">
                <div class="row h-100">
                  <div class="col-10 col-md-10 d-flex align-items-center px-0">
                    <div class="">
                      <li class="media d-flex align-items-center text-left">
                        <div class="media-body">
                          <div class="txt_hc_head_groupName minheight_head">
                            Group: {{ group.name }}
                          </div>
                          <div class="txt_hc_head_patientNumber minheight_head">
                            {{ group.total }} คน
                          </div>
                        </div>
                      </li>
                    </div>
                  </div>
                </div>
              </div>
              <div
                class="
                  card-footer
                  rounded-0
                  bg-transparent
                  pt-0
                  border-top-0
                  pb-2
                "
              >
                <div class="d-flex justify-content-between">
                  <div
                    class="txt_hc_title line-height-1 text-truncate"
                    id="groupDate"
                  >
                    {{ currentGroupDate[index] }}
                  </div>
                  <div class="txt_hc_title line-height-1 text-truncate">
                    See detailed
                  </div>
                </div>
              </div>
            </NuxtLink>
          </div>
        </b-collapse>
      </div>
      <div class="container fitscreen pt-3 pt-md-3 pb-0 plr_15p">
        <div class="row">
          <div class="col-md-12">
            <div class="row d-flex justify-content-between">
              <div class="col-11 col-md-11 col-lg-10">
                <div class="txt_hc_bighead_20p">
                  Skin Diseases
                  <span class="txt_hc_bighead_sub_16p pl-2">
                    ({{ groupNamenew.length }} Groups)
                  </span>
                </div>
              </div>
              <span
                v-b-toggle.collapse-2
                class="col-1 col-md-1 col-lg-2 text-right pr-3 pt-1"
              >
                <font-awesome-icon v-if="isVisible2" icon="chevron-up" />
                <font-awesome-icon v-else icon="chevron-down" />
              </span>
            </div>
          </div>
          <div class="col-md-12">
            <hr class="mt-1 mb-3" />
          </div>
        </div>
        <b-collapse
          id="collapse-2"
          class="
            pt-1 pt-md-
            row
            pb-5
            bg_card_hover
            card_vld_wrapper
            content-mangement
          "
          v-model="isVisible2"
        >
          <!-- Group card -->
          <div
            v-for="(group, index) in groupNamenew"
            :key="index"
            class="col-md-4 pb_me-4"
            @click="getCurrentDate(index)"
          >
            <NuxtLink
              :to="
                localePath(
                  `/dashboard/patient-skin-disease-group/${group.name}`
                )
              "
              class="card h-100 mb-0 px-3 py-2 group-card"
            >
              <div class="card-body p_card pb-0">
                <div class="row h-100">
                  <div class="col-10 col-md-10 d-flex align-items-center px-0">
                    <div class="">
                      <li class="media d-flex align-items-center text-left">
                        <div class="media-body">
                          <div class="txt_hc_head_groupName minheight_head">
                            Group: {{ group.name }}
                          </div>
                          <div class="txt_hc_head_patientNumber minheight_head">
                            {{ group.total }} คน
                          </div>
                        </div>
                      </li>
                    </div>
                  </div>
                </div>
              </div>
              <div
                class="
                  card-footer
                  rounded-0
                  bg-transparent
                  pt-0
                  border-top-0
                  pb-2
                "
              >
                <div class="d-flex justify-content-between">
                  <div
                    class="txt_hc_title line-height-1 text-truncate"
                    id="groupDate"
                  >
                    {{ currentGroupDate[index] }}
                  </div>
                  <div class="txt_hc_title line-height-1 text-truncate">
                    See detailed
                  </div>
                </div>
              </div>
            </NuxtLink>
          </div>
        </b-collapse>
      </div>
    </div>
  </div>
</template>

<script>
import dayjs from 'dayjs'
import { library } from '@fortawesome/fontawesome-svg-core'
import { faChevronUp, faChevronDown } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import Vue from 'vue'

library.add(faChevronUp, faChevronDown)
Vue.component('font-awesome-icon', FontAwesomeIcon)

export default {
  data() {
    return {
      isVisible1: true,
      isVisible2: true,
      rows: 100,
      perPage: 10,
      currentPage: 1,
      isLoading: false,
      groupName: null,
      dashboardGroup: [],
      allGroup: [],
      groupNamenew: [],
      currentGroupDate: [],
      currentTab: 'covid19',
      menuTab: [
        {
          id: 'covid19',
          text: 'COVID19',
        },
        { id: 'skinDisease', text: 'Skin Disease' },
      ],
    }
  },
  components: {
    DashboardTab: () => import('~/pages/dashboard/PatientgroupTab.vue'),
  },
  async mounted() {
    await this.getDashboardData()
    await this.getDashboardSkinDiseaseData()
    this.allGroup = await this.$axios.get('group')
    this.allGroup = this.allGroup.data
    this.isLoading = true
  },
  computed: {
    // getCurrentDate() {
    //   let currentDate = new Date()
    //   currentDate = dayjs(currentDate).format('DD/MM/YYYY')
    //   document.getElementById('groupDate').innerHTML = currentDate
    // },
  },
  methods: {
    getCurrentDate(index) {
      let currentDate = new Date()
      currentDate = dayjs(currentDate).format('DD/MM/YYYY')
      this.currentGroupDate[index] = currentDate
      // console.log(currentDate)
    },
    async getDashboardData() {
      let { data } = await this.$axios.get('dashboard')
      this.dashboardGroup.push(data)
      this.groupNamenew = this.dashboardGroup[0]
    },
    async getDashboardSkinDiseaseData() {
      console.log('get dashboard skin disease data')
    },
  },
}
</script>

<style lang="scss">
.txt_hc_head_patientNumber {
  font-family: 'Prompt-Medium';
  font-style: normal;
  color: #192a3e;
  line-height: 1.35em !important;
  font-size: 20px;
}
.txt_hc_head_groupName {
  font-family: 'Prompt-Medium';
  font-style: normal;
  color: #192a3e;
  line-height: 1.35em !important;
  font-size: 16px;
}
</style>
