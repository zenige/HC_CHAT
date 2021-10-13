<template>
  <div class="hc_navbar content p-0 group-management-group">
    <div class="container pt-3 pt-md-3 pb-0 plr_15p">
      <div class="row">
        <div class="col-12 text-center">
          <div class="d-flex justify-content-start">
            <div class="">
              <nuxt-link
                :to="previousUrl"
                class="txt_grey_light arrow_back_2 d-xl-block"
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

        <div class="pt-1 pt-md-1">
          <!-- Feature card -->
          <div
            v-for="(feature, index) in userData"
            :key="index"
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
                            <span>{{ feature.featureName }}</span>
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
                                  v-model="feature.question"
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
                                v-model="feature.condition"
                                class="form-control border-gray border"
                                style="curser: pointer"
                                :disabled="!feature.state.conditionState"
                                @change="changeCondition(index)"
                              >
                                <b-form-select-option
                                  v-for="option in getConditionOptions(index)"
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
                                v-model="feature.moreLessOption"
                                class="form-control border-gray border"
                                style="curser: pointer"
                                :disabled="!feature.state.moreLessOptionState"
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
                                v-model="feature.moreLessValue"
                                @copy.prevent
                                @paste.prevent
                                :disabled="!feature.moreLessOption"
                                @change="changeMoreLessValue(index)"
                              />
                            </div>
                          </div>
                          <div class="col-12 col-md-6 pb_me-4">
                            <div class="txt_vla_feature_content pb-1">
                              Only one of these (Other features)
                            </div>
                            <div class="form-group mb-0 w-100">
                              <b-form-select
                                v-model="feature.onlyOneOfTheseFeatureData"
                                class="form-control border-gray border"
                                style="curser: pointer"
                                :disabled="
                                  !feature.state.onlyOneOfTheseFeatureState
                                "
                                @change="onChangeOnlyPairFeature(index)"
                              >
                                <b-form-select-option
                                  v-for="option in getOptionsFeatures(
                                    feature.featureName
                                  )"
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
                              <b-form-select
                                v-model="feature.orFeatureData"
                                class="form-control border-gray border"
                                style="curser: pointer"
                                :disabled="!feature.state.orFeatureState"
                                @change="onChangeOrPairFeature(index)"
                              >
                                <b-form-select-option
                                  v-for="option in getOptionsFeatures(
                                    feature.featureName
                                  )"
                                  :key="option.label"
                                  :value="option.value"
                                  >{{ option.label }}</b-form-select-option
                                >
                              </b-form-select>
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
    moreLessValue: null,
    allFeatureData: [],
    allLineLogicData: [],
    allGroupData: [],
    conditionOptions: [
      {
        label: 'Please select a condition',
        value: null,
      },
      {
        label: 'Yes',
        value: 'true',
      },
      {
        label: 'No',
        value: 'false',
      },
      {
        label: 'Any',
        value: 'ANY',
      },
      {
        label: 'Input',
        value: 'input',
      },
    ],
    conditionSelected: '',
    moreLessOptions: [
      {
        label: 'Please select an option',
        value: null,
      },
      {
        label: 'More than',
        value: 'morethan',
      },
      {
        label: 'Less than',
        value: 'lessthan',
      },
    ],
    moreLessSelected: '',
    orFeatureSelected: '',
    isOnlyOneOfThese: false,
    isOr: false,
    featureCondition: null,
    featureOnlyOneOfThese: null,
    expanded: false,
    selectedOnlyOneOfThese: null,
    selectedOrFeature: null,
    userData: [],
    dataOptions: [
      {
        label: 'Please select a feature',
        value: null,
      },
    ],
    pairOr1: '',
    pairOr2: '',
    pairOnly1: '',
    pairOnly2: '',
    orConditionId: null,
    newMoreLessvalue: [],
    finalUserData: {},
  }),
  watch: {},
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
    await this.setInitialUserData()
    this.isLoading = true
  },
  methods: {
    openDeleteGroupModal() {
      this.isShowDeleteGroupModal = true
    },
    closeDeleteGroupModal() {
      this.isShowDeleteGroupModal = false
    },

    getOptionsFeatures(label) {
      if (this.dataOptions.length > 0) {
        const result = this.dataOptions.filter((item) => item.label !== label)
        return result
      } else {
        return []
      }
    },

    getConditionOptions(index) {
      if (this.userData[index].orFeatureData !== null) {
        const resultOr = this.conditionOptions.filter(
          (item) => item.label !== 'Any' && item.label !== 'Input'
        )
        return resultOr
      } else {
        return this.conditionOptions
      }
    },

    async getAllFeatureData() {
      let { data } = await this.$axios.get('feature')
      this.allFeatureData = data.map((item) => {
        return {
          feature: item.Name,
          id: item.id,
        }
      })
      console.log('All feature data', this.allFeatureData)
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
      console.log('All group data', this.allGroupData)
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
      }
      console.log('All Line Logic data', this.allLineLogicData)
    },
    async getOrCondition() {
      let { data } = await this.$axios.get('group/orcondition')
      if (data.length > 0) {
        this.orCondition = data[0]
        this.orConditionId = this.orCondition.id
        const key = 'id'
        delete this.orCondition[key]
        console.log(this.orCondition)
      }
    },

    isNumeric(value) {
      return /^-?\d+$/.test(value)
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

      for (let i = 0; i < this.allFeatureData.length; i++) {
        this.dataOptions.push({
          label: this.allFeatureData[i].feature,
          value: this.allFeatureData[i].feature,
        })
      }
      console.log('data option', this.dataOptions)

      console.log('all feature data after mergeData', this.allFeatureData)
      console.log('all group data after mergeData', this.allGroupData)
    },

    setInitialUserData() {
      for (let i = 0; i < this.allFeatureData.length; i++) {
        const feature = {
          question: this.allFeatureData[i].Question,
          condition: this.allFeatureData[i].Type,
          featureName: this.allFeatureData[i].feature,
          moreLessOption: null,
          moreLessValue: null,
          onlyOneOfTheseFeatureData: null,
          orFeatureData: null,
          state: {
            conditionState: true,
            moreLessOptionState: false,
            moreLessValueState: false,
            onlyOneOfTheseFeatureState: true,
            orFeatureState: true,
          },
        }
        this.userData.push(feature)
        if (this.userData[i].condition === 'input') {
          this.userData[i].state.moreLessOptionState = true
        } else {
          this.userData[i].state.moreLessOptionState = false
          this.userData[i].moreLessOption = null
          this.userData[i].moreLessValue = null
        }
      }
      this.setPairOrFeature()
    },
    setPairOrFeature() {
      if (this.orCondition) {
        let keyobject = Object.keys(this.orCondition)
        this.pairOr1 = keyobject[0]
        this.pairOr2 = keyobject[1]
        this.userData = this.userData.map((item) => {
          if (item.featureName === this.pairOr1) {
            return {
              ...item, // copy all data
              orFeatureData: this.pairOr2,
              onlyOneOfTheseFeatureData: null,
              state: {
                ...item.state,
                orFeatureState: true,
              },
            }
          } else if (item.featureName === this.pairOr2) {
            return {
              ...item,
              orFeatureData: this.pairOr1,
              onlyOneOfTheseFeatureData: null,
              state: {
                ...item.state,
                orFeatureState: true,
              },
            }
          } else {
            return {
              ...item,
              state: {
                ...item.state,
                orFeatureState: true,
              },
            }
          }
        })
      }
    },
    async onChangeOnlyPairFeature(index) {
      // เก็บค่าของ only feature ที่ user เลือก ของ index นั้น ๆ
      this.pairOnly1 = this.userData[index].onlyOneOfTheseFeatureData
      // ถ้ามีค่า
      if (this.pairOnly1) {
        this.userData = this.userData.map((item) => {
          if (item.featureName === this.pairOnly1) {
            return {
              ...item,
              onlyOneOfTheseFeatureData: this.userData[index].featureName,
              orFeatureData: null,
              condition: null,
              state: {
                ...item.state,
                onlyOneOfTheseFeatureState: true,
                conditionState: false,
              },
            }
          } else if (item.featureName === this.userData[index].featureName) {
            this.pairOnly2 = item.featureName
            return {
              ...item,
              orFeatureData: null,
              condition: null,
              state: {
                ...item.state,
                onlyOneOfTheseFeatureState: true,
                conditionState: false,
              },
            }
          } else {
            return {
              ...item,
              onlyOneOfTheseFeatureData: null,
              state: {
                ...item.state,
                onlyOneOfTheseFeatureState: true,
                conditionState: true,
              },
            }
          }
        })
      } else {
        this.userData = this.userData.map((item) => {
          return {
            ...item,
            onlyOneOfTheseFeatureData: null,
            state: {
              ...item.state,
              onlyOneOfTheseFeatureState: true,
              conditionState: true,
            },
          }
        })
      }
    },
    async onChangeOrPairFeature(index) {
      // เก็บค่าของ or feature ที่ user เลือก ของ index นั้น ๆ
      this.pairOr1 = this.userData[index].orFeatureData
      // ถ้ามีค่า
      if (this.pairOr1) {
        this.userData = this.userData.map((item) => {
          if (item.featureName === this.pairOr1) {
            return {
              ...item,
              orFeatureData: this.userData[index].featureName,
              onlyOneOfTheseFeatureData: null,
              state: {
                ...item.state,
                orFeatureState: true,
                conditionState: true,
              },
            }
          } else if (item.featureName === this.userData[index].featureName) {
            this.pairOr2 = item.featureName
            return {
              ...item,
              onlyOneOfTheseFeatureData: null,
              state: {
                ...item.state,
                orFeatureState: true,
                conditionState: true,
              },
            }
          } else {
            return {
              ...item,
              orFeatureData: null,
              state: {
                ...item.state,
                orFeatureState: true,
              },
            }
          }
        })
        let body = {
          [this.pairOr1]: 'true',
          [this.pairOr2]: 'true',
        }
        await this.$axios.post('group/orcondition/', body)
      } else {
        this.userData = this.userData.map((item) => {
          return {
            ...item,
            orFeatureData: null,
            state: {
              ...item.state,
              orFeatureState: true,
            },
          }
        })
        await this.$axios.delete('group/orcondition/' + this.orConditionId)
      }
      // if (this.userData[index].orFeatureData) {
      //   this.userData[index].onlyOneOfTheseFeatureData = null
      // }
    },

    changeCondition(index) {
      if (this.userData[index].condition === 'input') {
        this.userData[index].state.moreLessOptionState = true
      } else {
        this.userData[index].state.moreLessOptionState = false
        this.userData[index].moreLessOption = null
        this.userData[index].moreLessValue = null
      }
    },
    changeMoreLessValue(index) {
      if (this.userData[index].moreLessValue < 0) {
        this.$bvToast.toast('Value can not less than zero', {
          variant: 'danger',
          toaster: 'b-toaster-bottom-left',
          noCloseButton: true,
        })
        this.userData[index].moreLessValue = 0
      }
    },
    async onSaveGroup() {
      // let notNullCondition = this.userData.every(
      //   (item) => item.condition && item.condition !== null
      // )
      // if (notNullCondition) {
      //   this.$bvToast.toast('Saved successfully', {
      //     variant: 'success',
      //     toaster: 'b-toaster-bottom-left',
      //     noCloseButton: true,
      //   })
      //   console.log('user data', this.userData)
      // } else {
      //   this.$bvToast.toast('Please fill all Condition fields', {
      //     variant: 'danger',
      //     toaster: 'b-toaster-bottom-left',
      //     noCloseButton: true,
      //   })
      // }
      let moreLessOptionFlag = false
      let moreOrLess = ''
      let relationArr = [[]]
      for (let i of this.userData) {
        if (i.onlyOneOfTheseFeatureData) {
          relationArr[0].push(i.featureName)
          this.finalUserData['Relation'] = relationArr
        } else if (i.condition === 'input') {
          let transformValue = 0
          if (i.moreLessValue >= 0 && i.moreLessValue < 22) {
            transformValue = 2
          } else if (i.moreLessValue <= 30) {
            transformValue = 3
          } else if (i.moreLessValue <= 40) {
            transformValue = 4
          } else if (i.moreLessValue <= 50) {
            transformValue = 5
          } else if (i.moreLessValue <= 60) {
            transformValue = 6
          } else if (i.moreLessValue > 60) {
            transformValue = 7
          }
          this.finalUserData[i.featureName] = transformValue
          if (i.moreLessOption) {
            moreLessOptionFlag = true
            moreOrLess = i.moreLessOption
          }
        } else {
          this.finalUserData[i.featureName] = i.condition
          this.finalUserData['group'] = this.groupName
        }
      }
      let bodyGroup = []
      if (moreLessOptionFlag === true) {
        bodyGroup.push({
          data: this.finalUserData,
        })
        bodyGroup.push({
          condition: moreOrLess,
        })
      } else {
        bodyGroup.push({
          data: this.finalUserData,
        })
      }
      await this.$axios.post('group/groupid/' + this.groupName, bodyGroup)
      this.$bvToast.toast('Saved successfully', {
        variant: 'success',
        toaster: 'b-toaster-bottom-left',
        noCloseButton: true,
      })
    },

    onDeleteGroup() {
      console.log('delete group')
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
