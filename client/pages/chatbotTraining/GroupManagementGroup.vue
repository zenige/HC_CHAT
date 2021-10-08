<template>
  <div class="hc_navbar content p-0 group-management-group">
    <div class="container pt-3 pt-md-3 pb-0 plr_15p">
      <div class="row">
        <div class="col-12 text-center">
          <div class="d-flex justify-content-start">
            <div class="">
              <nuxt-link
                :to="previousUrl"
                class="txt_grey_light arrow_back_2 d-none d-xl-block"
                ><img
                  src="~assets/hc-libs/images/vl/arrow_back.png"
                  class="w-50p"
              /></nuxt-link>
            </div>
          </div>
        </div>
      </div>
    </div>

    <Loader v-if="!isLoading"></Loader>
    <div v-else>
      <div class="container pt-3 pt-md-3 plr_15p pb-4">
        <div class="row">
          <div class="col-md-12">
            <div class="row d-flex justify-content-between">
              <div class="col-12 col-md-8 col-lg-9">
                <div class="txt_hc_bighead_18p">Group: {{ groupName }}</div>
              </div>
            </div>
          </div>
          <div class="col-md-12">
            <hr class="mt-1 mb-3" />
          </div>
        </div>
        <div>
          <b>Selected:</b>
          <p>{{ conditionSelected }}</p>
        </div>
        <div>
          <b>More than or Less than Selected:</b>
          <p>{{ moreLessSelected }}</p>
        </div>
        <div>
          <b>value:</b>
          <p>{{ moreLessValue }}</p>
        </div>
        <div class="pt-1 pt-md-1">
          <!-- Feature card -->
          <div
            v-for="(feature, index) in allFeatureData"
            :key="feature.id"
            class="pb-3 pt-1 card_vld_wrapper"
          >
            <div class="task-item pb_me-4">
              <div class="card h-100 mb-0 position-relative">
                <div class="card-body p_card">
                  <div
                    class="
                      col-12 col-md-12
                      d-flex
                      align-items-center
                      pb-2 pb-md-0
                    "
                  >
                    <div class="container py-2 py-md-2">
                      <div class="row">
                        <div class="col-12 col-md-6 pb_me-4 mb-2">
                          <div class="txt_vla_feature_title">
                            {{ index + 1 }}.) Feature:
                            <span>{{ feature.feature }}</span>
                          </div>
                        </div>
                        <div class="row col-12 col-md-12 px-4">
                          <div class="col-12 col-md-6 pb_me-4">
                            <div class="txt_vla_feature_content pb-1">
                              Question
                            </div>
                            <div class="form-group mb-0 w-100">
                              <div class="d-flex" style="width: 100%">
                                <b-form-textarea
                                  type="text"
                                  placeholder=""
                                  class="form-control border-gray border"
                                  v-model="question"
                                />
                              </div>
                            </div>
                          </div>
                          <div class="col-12 col-md-6 pb_me-4">
                            <div class="txt_vla_feature_content pb-1">
                              Condition
                            </div>
                            <div class="form-group mb-0 w-100">
                              <b-form-select
                                v-model="conditionSelected"
                                class="form-control border-gray border"
                                style="curser: pointer"
                              >
                                <b-form-select-option
                                  v-for="option in conditionOptions"
                                  :key="option.label"
                                  :value="option.value"
                                  >{{ option.label }}</b-form-select-option
                                >
                              </b-form-select>
                            </div>
                          </div>
                          <div class="col-12 col-md-6 pb_me-4">
                            <div class="txt_vla_feature_content pb-1">
                              More than or Less than
                            </div>
                            <div class="form-group mb-0 w-100">
                              <b-form-select
                                v-model="moreLessSelected"
                                class="form-control border-gray border"
                                style="curser: pointer"
                                :disabled="conditionSelected !== 'input'"
                              >
                                <b-form-select-option
                                  v-for="option in moreLessOptions"
                                  :key="option.label"
                                  :value="option.value"
                                  >{{ option.label }}</b-form-select-option
                                >
                              </b-form-select>
                            </div>
                          </div>
                          <div class="col-12 col-md-6 pb_me-4">
                            <div class="form-group mb-0">
                              <div class="txt_vla_feature_content pb-1">
                                Value
                              </div>
                              <input
                                type="number"
                                min="0"
                                class="form-control border-gray border"
                                placeholder=""
                                v-model="moreLessValue"
                                @copy.prevent
                                @paste.prevent
                                :disabled="!moreLessSelected"
                              />
                            </div>
                          </div>
                          <div class="col-12 col-md-6 pb_me-4">
                            <div class="txt_vla_feature_content pb-1">
                              Only one of these (Other features)
                            </div>
                            <div class="form-group mb-0 w-100">
                              <b-form-select
                                v-model="moreLessSelected"
                                class="form-control border-gray border"
                                style="curser: pointer"
                                :disabled="conditionSelected !== 'input'"
                              >
                                <b-form-select-option
                                  v-for="option in moreLessOptions"
                                  :key="option.label"
                                  :value="option.value"
                                  >{{ option.label }}</b-form-select-option
                                >
                              </b-form-select>
                            </div>
                          </div>
                          <div class="col-12 col-md-6 pb_me-4">
                            <div class="txt_vla_feature_content pb-1">
                              Or (Other features)
                            </div>
                            <div class="form-group mb-0 w-100">
                              <div
                                class="selectBox2"
                                @click="showCheckboxes2()"
                                style="cursor: pointer"
                              >
                                <b-form-select
                                  class="form-control border-gray border"
                                ></b-form-select>
                                <div class="overSelect"></div>
                              </div>
                              <div id="checkboxes2">
                                <b-form-group
                                  v-slot="{ ariaDescribedby }"
                                  class="group_radio"
                                >
                                  <b-form-radio
                                    v-model="selectedOrFeature"
                                    :aria-describedby="ariaDescribedby"
                                    value="A"
                                    class="onlyOneOfThese_label"
                                    >Option A</b-form-radio
                                  >

                                  <b-form-radio
                                    v-model="selectedOrFeature"
                                    :aria-describedby="ariaDescribedby"
                                    value="B"
                                    >Option B</b-form-radio
                                  >
                                </b-form-group>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <!-- /Feature card -->
          </div>
        </div>
      </div>
      <div class="row mb-4">
        <div class="col-12 pb-2">
          <div class="d-flex justify-content-center align-items-center">
            <div class="m_width_250p">
              <a
                @click="onSaveGroup()"
                class="
                  btn btn-block btn_hc_light_border btn_hcb_green_light
                  h2dot5
                  m_width_250p
                "
                >Save</a
              >
            </div>
          </div>
        </div>
        <div class="col-12">
          <div class="d-flex justify-content-center align-items-center">
            <div class="m_width_400p">
              <a
                @click="openDeleteGroupModal()"
                class="btn btn-block h2dot5 m_width_400p delete_group"
                >Delete group</a
              >
            </div>
          </div>
        </div>
      </div>
    </div>

    <DeleteGroupModal
      :isOpen="isShowDeleteGroupModal"
      :onCancel="closeDeleteGroupModal"
      :onDelete="onDeleteGroup"
    ></DeleteGroupModal>
  </div>
</template>

<script>
export default {
  components: {
    DeleteGroupModal: () => import('~/components/modals/DeleteGroupModal.vue'),
    Loader: () => import('~/components/Loader.vue'),
  },
  data: () => ({
    groupName: '',
    isShowDeleteGroupModal: false,
    isLoading: false,
    question: '',
    value: 0,
    orCondition: {},
    moreLessValue: 0,
    allFeatureData: [],
    allLineLogicData: [],
    allGroupData: [],
    conditionOptions: [
      {
        label: 'Yes',
        value: 'yes',
      },
      {
        label: 'No',
        value: 'no',
      },
      {
        label: 'Any',
        value: 'any',
      },
      {
        label: 'Input',
        value: 'input',
      },
    ],
    conditionSelected: '',
    moreLessOptions: [
      {
        label: 'More than',
        value: 'moreThan',
      },
      {
        label: 'Less than',
        value: 'lessThan',
      },
    ],
    moreLessSelected: '',
    onlyOneOfTheseFeatureOptions: [],
    onlyOneOfTheseFeatureSelected: '',
    orFeatureOptions: [],
    orFeatureSelected: '',
    featureCondition: null,
    featureOnlyOneOfThese: null,
    expanded: false,
    selectedOnlyOneOfThese: null,
    selectedOrFeature: null,
  }),
  watch: {
    conditionSelected(value) {
      if (value !== 'input') {
        this.moreLessSelected = null
        this.moreLessValue = null
      }
    },
    moreLessValue(value) {
      if (value < 0) {
        this.$bvToast.toast('Value can not less than zero', {
          variant: 'danger',
          toaster: 'b-toaster-bottom-left',
          noCloseButton: true,
        })
        this.moreLessValue = 0
      }
    },
  },
  computed: {
    previousUrl() {
      return '/chatbot-training/group-management'
    },
  },
  async mounted() {
    this.groupName = this.$route.params.groupId
    await this.getAllFeatureData()
    await this.getAllGroupData()
    await this.getAllLineLogicData()
    await this.getOrCondition()
    await this.mergeData()
    this.isLoading = true
  },
  methods: {
    openDeleteGroupModal() {
      this.isShowDeleteGroupModal = true
    },
    closeDeleteGroupModal() {
      this.isShowDeleteGroupModal = false
    },
    onDeleteGroup() {
      console.log('delete group')
    },
    onSaveGroup() {
      console.log('save group')
    },
    // showCheckboxes(index) {
    //   let checkboxes = document.getElementById(`checkboxes${index}`)
    //   if (!this.expanded) {
    //     checkboxes.style.display = 'flex'
    //     this.expanded = true
    //   } else {
    //     checkboxes.style.display = 'none'
    //     this.expanded = false
    //   }
    // },
    // showCheckboxes2() {
    //   let checkboxes = document.getElementById('checkboxes2')
    //   if (!this.expanded) {
    //     checkboxes.style.display = 'flex'
    //     this.expanded = true
    //   } else {
    //     checkboxes.style.display = 'none'
    //     this.expanded = false
    //   }
    // },

    async getAllFeatureData() {
      let { data } = await this.$axios.get('feature')
      this.allFeatureData = data.map((item) => {
        return {
          feature: item.Name,
          id: item.id,
        }
      })
    },
    async getAllGroupData() {
      let { data } = await this.$axios.get('group')
      this.allGroupData = data.map((item) => {
        item.data = item.data.replaceAll("'", '"')

        let group = JSON.parse(item.data)
        if (item.condition) {
          group['condition'] = item.condition
        }
        return group
      })
      console.log(this.allGroupData)
    },
    async getAllLineLogicData() {
      let { data } = await this.$axios.get('logic/linelogic')
      this.allLineLogicData = data

      for (let [i, logic] of this.allLineLogicData.entries()) {
        for (let feature of this.allFeatureData) {
          if (logic.id === feature.feature) {
            feature['Question'] = logic.Question
          }
        }
        // console.log(feature)
        // this.allFeatureData[i]['Question'] = feature.Question
      }
    },
    async getOrCondition() {
      let { data } = await this.$axios.get('group/orcondition')
        this.orCondition = data[0]
        console.log(this.orCondition)



    },

    mergeData() {
      for (let [i, feature] of this.allFeatureData.entries()) {
        for (let group of this.allGroupData) {
          if (group.group === this.groupName) {
            if (group[feature.feature]) {
              if (this.isNumeric(group[feature.feature])) {
                feature['Type'] = 'input'
                feature['value'] = group[feature.feature]
                feature['condition'] = group.condition
                
              } else {
                feature['Type'] = group[feature.feature]
              }
            } else if (group.Relation) {
              feature['Relation'] = group.Relation
              feature['Type'] = 'Relation'
            }
          }
        }
      }
      console.log(this.allFeatureData)
    },
    isNumeric(value) {
      return /^-?\d+$/.test(value)
    },
  },
}
</script>

<style lang="scss">
.txt_vla_feature_title {
  font-size: 16px;
}
.group_radio {
  width: 100%;
  padding: 0;
}
.overSelect {
  position: absolute;
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;
}
.selectBox {
  position: relative;
}
.selectBox select {
  width: 100%;
}
#checkboxes,
#checkboxes2 {
  display: none;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  background: #ffffff;
  border: 1px solid rgba(0, 0, 0, 0.15);
  box-shadow: 0px 0px 8px rgba(0, 0, 0, 0.2);
}

#checkboxes label,
#checkboxes2 label {
  width: 100%;
  margin-bottom: 0;
  padding: 0.5rem;
}

#checkboxes label:hover,
#checkboxes2 label:hover {
  background-color: #ebeff2;
}

.hc_navbar {
  input::-webkit-outer-spin-button,
  input::-webkit-inner-spin-button {
    -webkit-appearance: none;
  }
}
.class-topic-task-list {
  .task-item {
    width: 100%;
  }

  .dropdown-toggle {
    color: var(--healthcare-primary) !important;
    padding: 0 0 0 16px;
    font-size: 20px;

    &-no-caret {
      background: #fff;
      width: 32px;
      height: 30px;
      padding: 0 8px;
      border-radius: 50%;
      display: block;
      color: #ccc !important;
    }

    &:hover {
      opacity: 0.75;
    }
  }
}
</style>
