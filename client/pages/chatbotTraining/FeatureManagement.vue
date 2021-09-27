<template>
  <div class="container">
    <Loader v-if="isLoading" />
    <div v-else class="hc_navbar">
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
          <div class="col-4 col-md-8 text-right">
            <button
              @click="openAddFeatureModal()"
              class="hcb-btn btn btn_hcb_green btn-block"
            >
              Create feature
            </button>
            <button
              @click="openDeleteFeatureModal()"
              class="hcb-btn btn btn_hcb_red btn-block"
            >
              Delete
            </button>
          </div>
        </div>
        <div class="col-md-12" style="padding-top: 2rem; padding-bottom: 1rem">
          <div class="row d-flex align-items-center">
            <div class="txt_hc_head_total">
              Total feature
              <span class="txt_vla_grey">({{ totalFeature }})</span>
            </div>
          </div>
        </div>
        <div class="col-md-12">
          <div class="row d-flex align-items-center justify-content-center">
            <b-table
              responsive
              id="Feature-table"
              :items="featureData"
              :per-page="0"
              :current-page="currentPage"
              :fields="fields"
              :filter="filter"
              :tbody-tr-class="selectedRowClass"
            >
              <template #head(selected)>
                <div class="d-flex align-items-center">
                  <b-form-checkbox v-model="selectAll"> </b-form-checkbox>
                  <span>Select All</span>
                </div>
              </template>
              <template #cell(selected)="data">
                <b-form-checkbox v-model="data.item.selected">
                </b-form-checkbox>
              </template>
              <template #cell(feature)="data">
                <div
                  v-if="data.item.editable === false"
                  style="max-width: 32.5%"
                >
                  <div>
                    {{ data.item.feature }}
                  </div>
                </div>
                <div
                  v-if="data.item.editable === true"
                  style="max-width: 32.5%"
                >
                  <b-form-input autofocus v-model="changedFeatureData" />
                </div>
              </template>
              <template #head(action)>
                <div class="d-flex justify-content-center">Action</div>
              </template>
              <template #cell(action)="data">
                <div
                  v-if="data.item.editable === false"
                  class="d-flex justify-content-center"
                >
                  <button
                    @click="editFeature(data)"
                    class="hcb-btn-light btn btn_hcb_blue_light btn-block"
                  >
                    Edit
                  </button>
                </div>
                <div
                  class="row d-flex justify-content-center align-items-center"
                  v-if="data.item.editable === true"
                >
                  <button
                    @click="saveFeature(data)"
                    class="hcb-btn-light btn btn_hcb_green_light mr-2 btn-block"
                  >
                    Save
                  </button>
                  <div @click="cancleEditFeature(data)" class="txt_grey_cancel">
                    Cancel
                  </div>
                </div>
              </template>
            </b-table>
            <div style="margin-top: 0.5rem">
              <b-pagination
                v-model="currentPage"
                :total-rows="totalFeature"
                :per-page="perPage"
                aria-controls="Feature-table"
                first-number
                last-number
                align="center"
                class="myPaginattion"
              ></b-pagination>
            </div>
          </div>
        </div>

        <DeleteFeatureModal
          :isOpen="isShowDeleteFeatureModal"
          :onCancel="closeDeleteFeatureModal"
          :onDelete="onDeleteFeature"
        ></DeleteFeatureModal>
        <AddNewFeatureModal
          :isOpen="isShowAddNewFeatureModal"
          :onCancel="closeAddFeatureModal"
          @getFeatureData="getFeatureData"
          :currentPage="currentPage"
          :perPage="perPage"
        ></AddNewFeatureModal>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  components: {
    DeleteFeatureModal: () =>
      import('~/components/chatbotTraining/DeleteFeatureModal.vue'),
    AddNewFeatureModal: () =>
      import('~/components/chatbotTraining/AddFeatureModal.vue'),
    Loader: () => import('~/components/Loader.vue'),
  },
  props: {},
  data() {
    return {
      isLoading: true,
      isShowDeleteFeatureModal: false,
      isShowAddNewFeatureModal: false,
      edit: false,
      selectAll: false,
      selectedRow: {},
      filter: '',
      perPage: 10,
      currentPage: 1,
      deleteSelected: [],
      totalFeature: 0,
      changedFeatureData: '',
      fields: [
        {
          key: 'selected',
          label: 'Select',
          thClass: 'featurethSelect-Class',
          tdClass: 'featuretdSelect-Class',
        },
        {
          key: 'feature',
          label: 'Feature name',
          sortable: true,
          thClass: 'featurethFeature-Class',
          tdClass: 'featuretdFeature-Class',
        },
        {
          key: 'action',
          label: 'Action',
          sortable: false,
          thClass: 'featurethAction-Class',
          tdClass: 'featuretdAction-Class',
        },
      ],
      featureData: [
        {
          feature: 'ช่วงอายุ',
          selected: false,
          editable: false,
        },
        {
          feature: 'มีโรคประจำตัว',
          selected: false,
          editable: false,
        },
        {
          feature: 'มีไข้',
          selected: false,
          editable: false,
        },
        {
          feature: 'ไอ',
          selected: false,
          editable: false,
        },
        {
          feature: 'เหนื่อย',
          selected: false,
          editable: false,
        },
        {
          feature: 'ความเสี่ยงใกล้ชิดผู้ติดเชื้อ',
          selected: false,
          editable: false,
        },
        {
          feature: 'กลับจากประเทศเสี่ยง',
          selected: false,
          editable: false,
        },
      ],
    }
  },
  watch: {
    selectAll(value) {
      this.featureData.map(function (item) {
        item.selected = value
        // return item
      })
    },
    currentPage(value) {
      this.getFeatureData(value, this.perPage, 'question')
    },
  },
  async mounted() {
    // await this.getFeatureData(1, 10, 'question')
    this.isLoading = false
  },
  computed: {},
  methods: {
    selectedRowClass(item) {
      if (item.selected === true) return 'row-selected'
    },
    openDeleteFeatureModal() {
      this.deleteSelected = this.featureData.filter(
        (item) => item.selected === true
      )
      if (this.deleteSelected.length >= 1) {
        this.isShowDeleteFeatureModal = true
      } else {
        ;(this.isShowDeleteFeatureModal = false),
          this.$bvToast.toast('Please select any word', {
            variant: 'danger',
            toaster: 'b-toaster-bottom-left',
            noCloseButton: true,
          })
      }
    },
    closeDeleteFeatureModal() {
      this.selectAll = false
      this.isShowDeleteFeatureModal = false
    },
    openAddFeatureModal() {
      this.isShowAddNewFeatureModal = true
    },
    closeAddFeatureModal() {
      this.isShowAddNewFeatureModal = false
    },
    async onDeleteFeature() {
      this.deleteSelected = this.featureData.filter(
        (item) => item.selected === true
      )
      await this.$axios.delete('train/trained/delete/many', {
        data: this.deleteSelected,
      })
      await this.getFeatureData(this.currentPage, 10, 'question')
      if (this.featureData.length === 0) {
        this.totalFeature = 0
      }
    },
    editFeature(data) {
      this.changedFeatureData = data.item.feature
      data.item.editable = true
    },
    cancleEditFeature(data) {
      data.item.editable = false
    },
    async saveFeature(data) {
      data.item.feature = this.changedFeatureData
      data.item.editable = false
      // await this.$axios.patch(`/train/trained/` + data.item.id, {
      //   feature: data.item.feature,
      // })
    },
    async getFeatureData(page, limit, orderBy) {
      let { data } = await this.$axios.get(
        `train/trained?pages=${page}&limit=${limit}&order_by=${orderBy}`
      )
      this.featureData = data.map((item) => {
        // collect total trained word data
        if (item.total) {
          return (
            {
              id: undefined,
            },
            (this.totalFeature = item.total)
          )
          // it will return undefined item
        } else {
          return {
            answer: item.answer,
            time: item.time,
            question: item.question,
            id: item.id,
            selected: false,
            editable: false,
          }
        }
      })
      // remove undefined item
      this.featureData = this.featureData.filter(function (element) {
        return element.id !== undefined
      })
      if (this.featureData.length === 0) {
        this.totalFeature = 0
      }
      // console.log(
      //   'page: ',
      //   page,
      //   'data: ',
      //   this.featureData.length,
      //   'total: ',
      //   this.totalFeature
      // )
    },
  },
}
</script>

<style lang="scss">
.featurethSelect-Class,
.featuretdSelect-Class {
  width: 15%;
}
.featurethFeature-Class,
.featuretdFeature-Class {
  width: 65%;
}
.featurethAction-Class,
.featuretdAction-Class {
  width: 20%;
}
</style>
