<template>
  <div class="hc_navbar content p-0 group-management-group">
    <div class="container pt-3 pt-md-3 pb-0 plr_15p">
      <div class="row">
        <div class="col-12 text-center">
          <div class="d-flex justify-content-start">
            <div class="">
              <div
                @click="previousUrl()"
                class="txt_grey_light arrow_back_2 d-xl-block"
                style="cursor: pointer"
              >
                <img
                  src="~assets/hc-libs/images/vl/arrow_back.png"
                  class="w-50p"
                />
              </div>
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
            :id="feature.refId"
            :class="[
              'pb-3 pt-1 card_vld_wrapper',
              { inValidaFeature: feature.state.validData === false },
            ]"
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
                                <b-form-input
                                  type="text"
                                  placeholder=""
                                  class="form-control border-gray border"
                                  v-model="feature.question"
                                  disabled
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
                                  v-for="option in getConditionOptions(feature)"
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
                                @change="changeMoreLessOption(index)"
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
                                v-model="feature.moreLessUserValue"
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
                @click="onSubmitForm()"
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
    formValid: false,
  }),
  watch: {},
  computed: {},
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
    previousUrl() {
      this.$router.push(this.localePath('/chatbot-training/group-management'))
    },
    openDeleteGroupModal() {
      this.isShowDeleteGroupModal = true
    },
    closeDeleteGroupModal() {
      this.isShowDeleteGroupModal = false
    },

    getOptionsFeatures(label) {
      if (this.dataOptions.length > 0) {
        const result = this.dataOptions.filter(
          (item) => item.label !== label && item.conditionType !== 'input'
        )
        return result
      } else {
        return []
      }
    },

    getConditionOptions(feature) {
      if (feature.conditionType === 'input') {
        if (feature.condition === 'input') {
          const resultOr = this.conditionOptions.filter(
            (item) =>
              item.label === 'Input' ||
              item.label === 'Any' ||
              item.label === 'Please select a condition'
          )
          return resultOr
        } else {
          // find feature that have input type in feature data
          let inputTypefeature = this.userData.find(
            (item) => item.condition === 'input'
          )
          if (inputTypefeature) {
            return this.conditionOptions.filter(
              (item) =>
                item.label !== 'Input' &&
                item.label !== 'Yes' &&
                item.label !== 'No'
            )
          } else {
            return this.conditionOptions.filter(
              (item) => item.label !== 'Yes' && item.label !== 'No'
            )
          }
        }
      } else if (feature.conditionType !== 'input') {
        if (feature.orFeatureData) {
          const resultOr = this.conditionOptions.filter(
            (item) => item.label !== 'Input' && item.label !== 'Any'
          )
          return resultOr
        } else {
          const resultOr = this.conditionOptions.filter(
            (item) => item.label !== 'Input'
          )
          return resultOr
        }
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
    },

    async getAllGroupData() {
      let { data } = await this.$axios.get('group')

      this.allGroupData = data.map((item) => {
        item.data = item.data.replaceAll("'", '"')

        let group = JSON.parse(item.data)
        if (item.condition) {
          group['condition'] = item.condition
        }
        if (item.value) {
          group['value'] = item.value
        }
        return group
      })
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
    },

    async getOrCondition() {
      let { data } = await this.$axios.get('group/orcondition')
      if (data.length > 0) {
        this.orCondition = data[0]
        this.orConditionId = this.orCondition.id
        const key = 'id'
        delete this.orCondition[key]
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
                feature['TypeValue'] = 'input'
                feature['value'] = group[feature.feature]
                feature['condition'] = group.condition
                feature['userValue'] = group.value
              } else {
                feature['TypeValue'] = group[feature.feature]
              }
            } else if (group.Relation) {
              feature['Relation'] = group.Relation
              feature['TypeValue'] = 'Relation'
            }
            const dataFromAllLineLogicData = this.allLineLogicData.find(
              (f) => f.id === feature.feature
            )
            feature['Next'] = dataFromAllLineLogicData.Next
            feature['Previous'] = dataFromAllLineLogicData.Previous
            feature['Type'] = dataFromAllLineLogicData.Type
          }
        }
      }

      let sortedFeatureData = []

      const firstFeatureDataSorted = this.allFeatureData.find(
        (item) => item.Previous === null
      )
      sortedFeatureData.push(firstFeatureDataSorted)

      const lastFeatureDataSorted = this.allFeatureData.find(
        (item) => item.Next === null
      )

      this.allFeatureData = this.allFeatureData.filter(
        (item) => item.Previous !== null && item.Next !== null
      )

      for (let i = 0; i < this.allFeatureData.length; i++) {
        const nextFeature = sortedFeatureData[sortedFeatureData.length - 1].Next
        const currentFeature = this.allFeatureData.find(
          (item) => item.feature === nextFeature
        )
        sortedFeatureData.push(currentFeature)
      }
      sortedFeatureData.push(lastFeatureDataSorted)

      this.allFeatureData = sortedFeatureData

      for (let i = 0; i < this.allFeatureData.length; i++) {
        this.dataOptions.push({
          label: this.allFeatureData[i].feature,
          value: this.allFeatureData[i].feature,
          conditionType: this.allFeatureData[i].Type,
        })
      }
    },

    setInitialUserData() {
      for (let i = 0; i < this.allFeatureData.length; i++) {
        let feature = {
          featureName: this.allFeatureData[i].feature,
          question: this.allFeatureData[i].Question,
          conditionType: this.allFeatureData[i].Type,
          condition: this.allFeatureData[i].TypeValue,
          moreLessOption: null,
          moreLessValue: null,
          moreLessUserValue: null,
          onlyOneOfTheseFeatureData: null,
          orFeatureData: null,
          refId: this.generateID(),
          state: {
            conditionState: true,
            moreLessOptionState: false,
            moreLessValueState: false,
            onlyOneOfTheseFeatureState: true,
            orFeatureState: true,
            validData: true,
          },
        }
        // if feature have relation
        if (this.allFeatureData[i].Relation) {
          const relation = this.allFeatureData[i].Relation[0]
          const relation_filter = relation.filter(
            (name) => name !== this.allFeatureData[i].feature
          ) // result filter -> [travel]
          feature.onlyOneOfTheseFeatureData = relation_filter[0]
          feature.state.conditionState = false
          feature.condition = null
        }
        if ('condition' in this.allFeatureData[i]) {
          feature.moreLessOption = this.allFeatureData[i].condition
          feature.moreLessValue = this.allFeatureData[i].value
          feature.moreLessUserValue = this.allFeatureData[i].userValue
        }
        this.userData.push(feature)
        if (this.userData[i].conditionType === 'input') {
          if (this.userData[i].condition === 'input') {
            this.userData[i].state.moreLessOptionState = true
            this.userData[i].state.onlyOneOfTheseFeatureState = false
            this.userData[i].state.orFeatureState = false
          } else {
            this.userData[i].moreLessOption = false
            this.userData[i].state.moreLessOptionState = false
            this.userData[i].state.onlyOneOfTheseFeatureState = false
            this.userData[i].state.orFeatureState = false
          }
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
          } else if (item.conditionType === 'input') {
            return {
              ...item,
              state: {
                ...item.state,
                orFeatureState: false,
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
        if (
          this.pairOnly1 === this.pairOr1 ||
          this.pairOnly1 === this.pairOr2
        ) {
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
            } else if (item.conditionType === 'input') {
              return {
                ...item,
                orFeatureData: null,
                onlyOneOfTheseFeatureData: null,
                state: {
                  ...item.state,
                  onlyOneOfTheseFeatureState: false,
                  conditionState: true,
                },
              }
            } else {
              return {
                ...item,
                orFeatureData: null,
                onlyOneOfTheseFeatureData: null,
                state: {
                  ...item.state,
                  onlyOneOfTheseFeatureState: true,
                  conditionState: true,
                },
              }
            }
          })
          this.pairOr1 = null
          this.pairOr2 = null
          await this.$axios.delete('group/orcondition/' + this.orConditionId)
        } else {
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
            } else if (item.conditionType === 'input') {
              return {
                ...item,
                orFeatureData: null,
                onlyOneOfTheseFeatureData: null,
                state: {
                  ...item.state,
                  onlyOneOfTheseFeatureState: false,
                  conditionState: true,
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
        }
      } else {
        this.userData = this.userData.map((item) => {
          if (item.conditionType === 'input') {
            return {
              ...item,
              onlyOneOfTheseFeatureData: null,
              state: {
                ...item.state,
                onlyOneOfTheseFeatureState: false,
                conditionState: true,
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
          } else if (item.conditionType === 'input') {
            return {
              ...item,
              onlyOneOfTheseFeatureData: null,
              orFeatureData: null,
              state: {
                ...item.state,
                orFeatureState: false,
              },
            }
          } else {
            return {
              ...item,
              onlyOneOfTheseFeatureData: null,
              orFeatureData: null,
              state: {
                ...item.state,
                orFeatureState: true,
                conditionState: true,
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
          if (item.conditionType === 'input') {
            return {
              ...item,
              orFeatureData: null,
              state: {
                ...item.state,
                orFeatureState: false,
              },
            }
          }
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
    },
    changeCondition(index) {
      if (this.userData[index].conditionType === 'input') {
        if (this.userData[index].condition === 'input') {
          this.userData[index].state.moreLessOptionState = true
          this.userData[index].state.onlyOneOfTheseFeatureState = false
          this.userData[index].state.orFeatureState = false
          this.userData[index].state.moreLessValueState = true
        } else {
          this.userData[index].moreLessOption = null
          this.userData[index].state.moreLessOptionState = false
          this.userData[index].moreLessUserValue = null
          this.userData[index].state.onlyOneOfTheseFeatureState = false
          this.userData[index].state.orFeatureState = false
          this.userData[index].state.moreLessValueState = false
        }
      } else {
        this.userData[index].state.moreLessOptionState = false
        this.userData[index].moreLessOption = null
        this.userData[index].moreLessValue = null
        this.userData[index].moreLessUserValue = null
      }
    },
    changeMoreLessOption(index) {
      if (!this.userData[index].moreLessOption) {
        this.userData[index].state.moreLessValueState = false
        this.userData[index].moreLessUserValue = null
      }
    },
    changeMoreLessValue(index) {
      if (this.userData[index].moreLessUserValue < 0) {
        this.$bvToast.toast('Value can not less than zero', {
          variant: 'danger',
          toaster: 'b-toaster-bottom-left',
          noCloseButton: true,
        })
        this.userData[index].moreLessUserValue = 0
      }
    },
    async onSaveGroup() {
      let moreLessOptionFlag = false
      let moreOrLess = ''
      let moreOrLessVal = 0
      let relationArr = [[]]
      for (let i of this.userData) {
        if (i.onlyOneOfTheseFeatureData) {
          relationArr[0].push(i.featureName)
          this.finalUserData['Relation'] = relationArr
        } else if (i.condition === 'input') {
          let transformValue = 0
          if (i.moreLessUserValue >= 0 && i.moreLessUserValue < 22) {
            transformValue = 2
          } else if (i.moreLessUserValue <= 30) {
            transformValue = 3
          } else if (i.moreLessUserValue <= 40) {
            transformValue = 4
          } else if (i.moreLessUserValue <= 50) {
            transformValue = 5
          } else if (i.moreLessUserValue <= 60) {
            transformValue = 6
          } else if (i.moreLessUserValue > 60) {
            transformValue = 7
          }
          this.finalUserData[i.featureName] = transformValue
          if (i.moreLessOption) {
            moreLessOptionFlag = true
            moreOrLess = i.moreLessOption
            moreOrLessVal = i.moreLessUserValue
          } else {
            moreLessOptionFlag = false
          }
        } else {
          this.finalUserData[i.featureName] = i.condition
          this.finalUserData['group'] = this.groupName
        }
      }
      let bodyGroup = {}
      if (moreLessOptionFlag === true) {
        bodyGroup['data'] = this.finalUserData
        bodyGroup['condition'] = moreOrLess
        bodyGroup['value'] = moreOrLessVal
      } else {
        bodyGroup['data'] = this.finalUserData
      }
      await this.$axios.post('group/groupid/' + this.groupName, bodyGroup)
      this.$bvToast.toast('Saved successfully', {
        variant: 'success',
        toaster: 'b-toaster-bottom-left',
        noCloseButton: true,
      })
      window.location.reload()
    },
    async onSubmitForm() {
      await new Promise((resolve) => {
        this.formValid = this.userData
          .map((item, index) => {
            if (item.onlyOneOfTheseFeatureData) {
              if (!item.condition) {
                this.userData[index].state.validData = true
                return this.userData[index]
              } else {
                this.userData[index].state.validData = false
                document.getElementById(item.refId).scrollIntoView()
                return this.userData[index]
              }
            } else {
              if (item.condition) {
                if (item.condition === 'input') {
                  if (item.moreLessOption) {
                    if (item.moreLessUserValue) {
                      this.userData[index].state.validData = true
                      return this.userData[index]
                    } else {
                      this.userData[index].state.validData = false
                      document.getElementById(item.refId).scrollIntoView()
                      return this.userData[index]
                    }
                  } else {
                    this.userData[index].state.validData = false
                    document.getElementById(item.refId).scrollIntoView()
                    return this.userData[index]
                  }
                }
                this.userData[index].state.validData = true
                return this.userData[index]
              } else {
                this.userData[index].state.validData = false
                document.getElementById(item.refId).scrollIntoView()
                return this.userData[index]
              }
            }
          })
          .every((item) => {
            if (item.state.validData === true) {
              return true
            } else {
              return false
            }
          })
        resolve(this.formValid)
      }).then((valid) => {
        if (valid) {
          this.onSaveGroup()
        } else {
          this.$bvToast.toast('Please fill all required fields', {
            variant: 'danger',
            toaster: 'b-toaster-bottom-left',
            noCloseButton: true,
          })
        }
      })
    },
    async onDeleteGroup() {
      await this.$axios.delete('group/' + this.groupName)
      this.$router.push(this.localePath('/chatbot-training/group-management'))
    },
    generateID() {
      let result_id = ''
      const length = 10
      const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
      for (let i = 0; i < length; i++) {
        result_id += characters.charAt(
          Math.floor(Math.random() * characters.length)
        )
      }
      return result_id
    },
  },
}
</script>

<style lang="scss">
.inValidaFeature {
  border: 2px solid rgb(255, 93, 93);
  box-shadow: 1px 1px 5px rgb(255, 121, 121);
  border-radius: 10px;
}

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
