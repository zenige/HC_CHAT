<template>
  <div class="hc_navbar content p-0 group-management-group">
    <Loader v-if="!isLoading" />
    <div v-else class="container fitscreen pt-3 pt-md-3 pb-0 plr_15p">
      <div class="row">
        <div class="col-md-12">
          <div class="row d-flex justify-content-between">
            <div class="col-12 col-md-8 col-lg-9">
              <div class="txt_hc_bighead_20p">Patient group</div>
            </div>
          </div>
        </div>
        <div class="col-md-12">
          <hr class="mt-1 mb-3" />
        </div>
      </div>
      <div
        class="
          pt-1 pt-md-
          row
          pb-5
          bg_card_hover
          card_vld_wrapper
          content-mangement
        "
      >
        <!-- Group card -->
        <div
          v-for="(group, index) in dashboardGroup"
          :key="index"
          class="col-md-4 pb_me-4"
        >
          <NuxtLink
            :to="localePath(`/dashboard/patient-group/${group[index]}`)"
            class="card h-100 mb-0 px-3 py-2 group-card"
          >
            <div class="card-body p_card pb-0">
              <div class="row h-100">
                <div class="col-10 col-md-10 d-flex align-items-center px-0">
                  <div class="">
                    <li class="media d-flex align-items-center text-left">
                      <div class="media-body">
                        <div class="txt_hc_head_groupName minheight_head">
                          Group: {{ group[index] }}
                        </div>
                        <div class="txt_hc_head_patientNumber minheight_head">
                          100 คน
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
                <div class="txt_hc_title line-height-1 text-truncate">
                  10/1/2021
                </div>
                <div class="txt_hc_title line-height-1 text-truncate">
                  See detailed
                </div>
              </div>
            </div>
          </NuxtLink>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      rows: 100,
      perPage: 10,
      currentPage: 1,
      isLoading: false,
      groupName: null,
      dashboardGroup: [],
      allGroup: [],
      new: [{
        name: ''
      }],
    }
  },
  async mounted() {
    await this.getDashboardData()
    this.allGroup = await this.$axios.get('group')
    this.allGroup = this.allGroup.data
    this.isLoading = true
  },
  methods: {
    async getDashboardData() {
      let { data } = await this.$axios.get('dashboard')
      this.dashboardGroup.push(data)
      console.log('bhhhhhhg', this.dashboardGroup)
      for (let i = 0; i < this.dashboardGroup.length; i++) {
        this.dashboardGroup[i] = Object.keys(this.dashboardGroup[i])
      }
      console.log('bhhhhhhg', this.dashboardGroup)
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
