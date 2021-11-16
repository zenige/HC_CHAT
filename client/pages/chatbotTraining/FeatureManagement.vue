<template>
  <div class="container">
    <Loader v-if="!isLoading" />
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
                <b-form-input
                  name="Search"
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
                  @keydown.prevent.space
                ></b-form-input>
                <div
                  class="form-control-feedback"
                  :disabled="!filter"
                  @click="filter = ''"
                >
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
<<<<<<< HEAD
            <b-table
              v-sortable="sortableOptions"
              responsive
              id="Feature-table"
              :items="featureData"
              :fields="fields"
              :per-page="0"
              :filter="filter"
              :current-page="currentPage"
              :tbody-tr-class="selectedRowClass"
              :sort-by.sync="sortBy"
              :sort-desc.sync="sortDesc"
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
                <div v-if="data.item.editable === false">
                  <div>
                    {{ data.item.feature }}
=======
              <b-table
                v-sortable="sortableOptions" striped hover
                responsive
                id="Feature-table"
                :items="featureData"
                :fields="fields"
                :per-page="0"
                :filter="filter"
                :current-page="currentPage"
                :tbody-tr-class="selectedRowClass"
                :sort-by.sync="sortBy"
                :sort-desc.sync="sortDesc"
              >
                <template #head(selected)>
                  <div class="d-flex align-items-center">
                    <b-form-checkbox v-model="selectAll"> </b-form-checkbox>
                    <span>Select All</span>
>>>>>>> d104bf8b216b2f6e61ccb547204376863ccee13a
                  </div>
                </template>
                <template #cell(selected)="data">
                  <b-form-checkbox v-model="data.item.selected">
                  </b-form-checkbox>
                </template>
                <template #cell(feature)="data">
                  <div v-if="data.item.editable === false">
                    <div>
                      {{ data.item.feature }}
                    </div>
                  </div>
                  <div v-if="data.item.editable === true">
                    <b-form-input
                      name="feature"
                      autofocus
                      v-model="changedFeatureName[data.index]"
                      @keydown.prevent.space
                    />
                  </div>
                </template>
                <template #cell(conditionType)="data">
                  <div v-if="data.item.editable === false">
                    <div>{{ data.item.conditionType }}</div>
                  </div>
                  <div v-if="data.item.editable === true">
                    <b-form-select
                      v-model="changedConditionType[data.index]"
                      class="form-control border-gray border"
                      style="curser: pointer"
                      autofocus
                    >
                      <b-form-select-option
                        v-for="option in conditionTypeOptionFunction(
                          data.item.conditionType
                        )"
                        :key="option.label"
                        :value="option.value"
                        >{{ option.label }}</b-form-select-option
                      >
                    </b-form-select>
                  </div>
                </template>
                <template #cell(question)="data">
                  <div v-if="data.item.editable === false">
                    <div>
                      {{ data.item.question }}
                    </div>
                  </div>
                  <div v-if="data.item.editable === true">
                    <b-form-input
                      name="question"
                      autofocus
                      v-model="changedQuestion[data.index]"
                      @keydown.prevent.space
                    />
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
                      @click="saveFeature(data)"+
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
              <div>
                <table>
                  <tbody>
                    <tr>
                      <td><b-form-checkbox v-model="selectAll"> </b-form-checkbox>Select All</td>
                      <td>Feature name</td>
                      <td>Condition type</td>
                      <td>Question</td>
                      <td>Action</td>
                    </tr>
                  </tbody>
                </table>
                <table
                  id="Feature-table"
                >
                  <tbody>
                    <draggable v-model="featureData" @change="bg">
                      <tr  v-for="(item, index) in featureData.slice(pageX, pageY)" :key="index">
                        <th scope="row">
                          <b-form-checkbox v-model="item.selected"></b-form-checkbox>
                          </th>  
                        <td >
                          <div v-if="item.editable === false">
                            {{item.feature}}
                          </div>
                          <div v-if="item.editable === true">
                            <b-form-input
                              name="feature"
                              autofocus
                              v-model="changedFeatureName[index]"
                              @keydown.prevent.space
                            />
                          </div>
                        </td>
                        <td>
                          <div v-if="item.editable === false">
                            {{item.conditionType}}
                          </div>
                          <div v-if="item.editable === true">
                            <b-form-input
                              name="conditionType"
                              autofocus
                              v-model="changedConditionType[index]"
                              @keydown.prevent.space
                            />
                          </div>
                        </td>
                        <td>
                          <div v-if="item.editable === false">
                            {{item.question}}
                          </div>
                          <div v-if="item.editable === true">
                            <b-form-input
                              name="question"
                              autofocus
                              v-model="changedQuestion[index]"
                              @keydown.prevent.space
                            />
                          </div>
                        </td>
                        <td>
                          <div
                            v-if="item.editable === false"
                            class="d-flex justify-content-center"
                          >
                            <button
                              @click="editFeature(item)"
                              class="hcb-btn-light btn btn_hcb_blue_light btn-block"
                            >
                              Edit
                            </button>
                          </div>
                          <div
                            class="row d-flex justify-content-center align-items-center"
                            v-if="item.editable === true"
                          >
                            <button
                              @click="saveFeature(item)"
                              class="hcb-btn-light btn btn_hcb_green_light mr-2 btn-block"
                            >
                              Save
                            </button>
                            <div @click="cancleEditFeature(item)" class="txt_grey_cancel">
                              Cancel
                            </div>
                          </div>
                        </td>
                      </tr>
                    </draggable>
                  </tbody>
                </table>
                <div>
                  <p @click="pageBack">back</p>
                  <p>{{ page }}</p>
                  <p @click="pageNext">next</p>
                </div>
              </div>
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
        <CreateNewFeatureModal
          :isOpen="isShowCreateNewFeatureModal"
          :onCancel="closeAddFeatureModal"
          :featureData="featureData"
          @getFeatureData="getFeatureData"
        ></CreateNewFeatureModal>
      </div>
    </div>
  </div>
</template>

<script>
import Sortable from 'sortablejs'

const english = /^[A-Za-z]*$/
import draggable from 'vuedraggable'

const createSortable = (el, options, vnode) => {

  return Sortable.create(el, {
    ...options
  });
};

const sortable = {
  name: 'sortable',
  bind(el, binding, vnode) {
    const table = el.querySelector('table');
    table._sortable = createSortable(el.querySelector("tbody"), binding.value, vnode);
  }
};

const createSortable = (el, options, vnode) => {
  console.log(el)
  return Sortable.create(el, {
    ...options,
  })
}

const sortable = {
  name: 'sortable',
  bind(el, binding, vnode) {
    console.log(binding)

    const table = el
    table._sortable = createSortable(
      table.querySelector('tbody'),
      binding.value,
      vnode
    )
    console.log(table.querySelector('tbody'))
  },
}

export default {
  components: {
    DeleteFeatureModal: () =>
      import('~/components/modals/DeleteFeatureModal.vue'),
    CreateNewFeatureModal: () =>
      import('~/components/modals/CreateFeatureModal.vue'),
    Loader: () => import('~/components/Loader.vue'),
    draggable
  },
  props: {},
  directives: { sortable },
  data() {
    return {
<<<<<<< HEAD
      test: false,
      sortableOptions: {
        chosenClass: 'is-selected',
      },
=======
      pageX: 0,
      pageY: 10,
>>>>>>> d104bf8b216b2f6e61ccb547204376863ccee13a
      sortBy: null,
      sortDesc: false,
      isLoading: false,
      isShowDeleteFeatureModal: false,
      isShowCreateNewFeatureModal: false,
      edit: false,
      selectAll: false,
      selectedRow: {},
      filter: '',
      perPage: 10,
      currentPage: 1,
      deleteSelected: [],
      totalFeature: null,
      changedFeatureName: [],
      changedConditionType: [],
      changedQuestion: [],
      oldFeatureName: '',
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
          sortable: false,
          thClass: 'featurethFeature-Class',
          tdClass: 'featuretdFeature-Class',
        },
        {
          key: 'conditionType',
          label: 'Condition type',
          sortable: false,
          thClass: 'featurethConditionType-Class',
          tdClass: 'featuretdConditionType-Class',
        },
        {
          key: 'question',
          label: 'Question',
          sortable: false,
          thClass: 'featurethQuestion-Class',
          tdClass: 'featuretdQuestion-Class',
        },
        {
          key: 'action',
          label: 'Action',
          thClass: 'featurethAction-Class',
          tdClass: 'featuretdAction-Class',
        },
      ],
      featureData: [],
      allFeatureData: [],
      conditionTypeOption: [
        {
          label: 'boolean',
          value: 'boolean',
        },
        {
          label: 'input',
          value: 'input',
        },
      ],
    }
  },
  watch: {
    selectAll(value) {
      this.featureData.map(function (item) {
        item.selected = value
      })
    },
  },
  async mounted() {
    await this.getFeatureData()
    // this.conditionTypeOptionFunction()
    this.isLoading = true
  },
  computed: {},
  methods: {
    pageNext() {
      if (this.pageX === 0 || this.pageX <= 0) {
        this.pageX +=10
        this.pageY +=10
      }
    },
    pageBack() {
      if (this.pageX === 0 || this.pageX <= 0) {
        console.log('bb')
      } else {
        this.pageX -=10
        this.pageY -=10
      }
    },
    bg() {
      console.log('hh', this.featureData)
    },
    conditionTypeOptionFunction(conditionType) {
      // if (conditionType === 'input') {
      //   return this.conditionTypeOption
      // } else {
      //   // find feature that have input type in feature data
      //   let inputTypefeature = this.featureData.find(
      //     (item) => item.conditionType === 'input'
      //   )
      //   if (inputTypefeature) {
      //     return this.conditionTypeOption.filter(
      //       (item) => item.label !== 'input'
      //     )
      //   } else {
      //     return this.conditionTypeOption
      //   }
      // }
      return this.conditionTypeOption
    },
    selectedRowClass(item) {
      if (item.selected === true) return 'row-selected'
    },
    openDeleteFeatureModal() {
      this.deleteSelected = this.featureData.filter(
        (item) => item.selected === true
      )
      if (
        this.deleteSelected.length < this.featureData.length &&
        this.featureData.length >= 1 &&
        this.deleteSelected.length >= 1
      ) {
        this.isShowDeleteFeatureModal = true
      } else if (this.deleteSelected.length === this.featureData.length) {
        ;(this.isShowDeleteFeatureModal = false),
          this.$bvToast.toast("You can't delete all feature", {
            variant: 'danger',
            toaster: 'b-toaster-bottom-left',
            noCloseButton: true,
          })
      } else if (this.deleteSelected.length < 1) {
        ;(this.isShowDeleteFeatureModal = false),
          this.$bvToast.toast('Please select any feature', {
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
      this.isShowCreateNewFeatureModal = true
    },
    closeAddFeatureModal() {
      this.isShowCreateNewFeatureModal = false
    },
    async onDeleteFeature() {
      this.deleteSelected = this.featureData.filter(
        (item) => item.selected === true
      )
      for (let i = 0; i < this.deleteSelected.length; i++) {
        await this.$axios.delete(
          'feature/' +
            this.deleteSelected[i].id +
            '/' +
            this.deleteSelected[i].feature
        )
      }
      this.$bvToast.toast('Please go back to setting of all groups again', {
        variant: 'success',
        toaster: 'b-toaster-bottom-left',
        noCloseButton: true,
      })
      this.$bvToast.toast('Deleted successfully', {
        variant: 'success',
        toaster: 'b-toaster-bottom-left',
        noCloseButton: true,
      })
      await this.getFeatureData()
      if (this.featureData.length === 0) {
        this.totalFeature = 0
      }
    },
    editFeature(data) {
      console.log('bgbgbg', data)
      this.changedFeatureName[data.index] = data.feature
      this.changedConditionType[data.index] = data.conditionType
      this.changedQuestion[data.index] = data.question
      // data.item.editable = true
      data.editable = true
    },
    cancleEditFeature(data) {
      data.editable = false
    },
    async saveFeature(data) {
      if (
        this.changedFeatureName[data.index] &&
        this.changedConditionType[data.index] &&
        this.changedQuestion[data.index]
      )
        if (english.test(this.changedFeatureName[data.index])) {
          data.feature = this.changedFeatureName[data.index]
          data.conditionType = this.changedConditionType[data.index]
          data.question = this.changedQuestion[data.index]
          await this.$axios.patch('feature', {
            id: data.id,
            Name: data.feature,
            Type: data.conditionType,
            Question: data.question,
          })
          this.$bvToast.toast('Please go back to setting of all groups again', {
            variant: 'success',
            toaster: 'b-toaster-bottom-left',
            noCloseButton: true,
          })
          this.$bvToast.toast('Saved successfully', {
            variant: 'success',
            toaster: 'b-toaster-bottom-left',
            noCloseButton: true,
          })
          data.editable = false
        } else {
          this.$bvToast.toast('Please fill in English only', {
            variant: 'danger',
            toaster: 'b-toaster-bottom-left',
            noCloseButton: true,
          })
        }
      else {
        this.$bvToast.toast('Please fill all required fills', {
          variant: 'danger',
          toaster: 'b-toaster-bottom-left',
          noCloseButton: true,
        })
      }
    },
    async getFeatureData() {
      let featureNameIdData = await this.$axios.get('feature')
      this.allFeatureData = featureNameIdData.data.map((item) => {
        return {
          feature: item.Name,
          id: item.id,
        }
      })

      let { data } = await this.$axios.get('logic/linelogic')
      this.featureData = data

      let sortedFeatureData = []

      let firstFeatureDataSorted = this.featureData.find(
        (item) => item.Previous === null
      )
      sortedFeatureData.push(firstFeatureDataSorted)

      let lastFeatureDataSorted = this.featureData.find(
        (item) => item.Next === null
      )
      // console.log('sortedFeatureData', sortedFeatureData)

      this.featureData = data.filter(
        (item) => item.Previous !== null && item.Next !== null
      )

      for (let i = 0; i < this.featureData.length; i++) {
        let nextFeature = sortedFeatureData[sortedFeatureData.length - 1].Next
        let currentFeature = this.featureData.find(
          (item) => item.id === nextFeature
        )
        sortedFeatureData.push(currentFeature)
      }

      sortedFeatureData.push(lastFeatureDataSorted)

      this.featureData = sortedFeatureData
      // console.log('feature data after sorted', this.featureData)

      this.featureData = this.featureData.map((item) => {
        return {
          feature: item.id,
          question: item.Question,
          conditionType: item.Type,
          next: item.Next,
          previous: item.Previous,
          selected: false,
          editable: false,
        }
      })

      for (let j = 0; j < this.featureData.length; j++) {
        for (let i = 0; i < this.allFeatureData.length; i++) {
          if (this.allFeatureData[i].feature === this.featureData[j].feature) {
            this.featureData[j]['id'] = this.allFeatureData[i].id
          }
        }
      }

      // console.log('feature data after push Id', this.featureData)

      if (this.featureData.length === 0) {
        this.totalFeature = 0
      } else {
        this.totalFeature = this.featureData.length
      }
      // console.log('feature data after push Id', this.featureData)
    },
  },
}
</script>

<style lang="scss">
#Feature-table > tbody > tr {
  cursor: pointer;
  border: none;
}
#Feature-table > tbody > tr:hover {
  background-color: #ebeff2;
}
#Feature-table > tbody > tr:active {
  background-color: #ebeff2;
}

.featurethSelect-Class,
.featuretdSelect-Class {
  width: 15%;
}
.featurethFeature-Class,
.featuretdFeature-Class {
  width: 20%;
}
.featurethConditionType-Class,
.featuretdConditionType-Class {
  width: 15%;
}
.featurethQuestion-Class,
.featurethQuestion-Class {
  width: 25%;
}
.featurethAction-Class,
.featuretdAction-Class {
  width: 20%;
}

table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

td, th {
  border-bottom: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}
</style>
