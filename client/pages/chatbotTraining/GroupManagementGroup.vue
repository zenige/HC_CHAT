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
                <div class="txt_hc_bighead_18p">Group name</div>
              </div>
            </div>
          </div>
          <div class="col-md-12">
            <hr class="mt-1 mb-3" />
          </div>
        </div>
        <div class="pt-1 pt-md-1">
          <!-- Feature card -->
          <div class="pb-3 pt-1 card_vld_wrapper">
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
                        <div class="col-12 col-md-12 pb_me-4 mb-2">
                          <div class="txt_vla_feature_title">
                            1.) Feature:
                            <span>มีไข้</span>
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
                              <select
                                v-model="featureCondition"
                                class="form-control border-gray border"
                                style="curser: pointer"
                              >
                                <option
                                  v-for="option in conditionOptions"
                                  :key="option.label"
                                  :value="option.value"
                                >
                                  {{ option.value }}
                                </option>
                              </select>
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
                                v-model="value"
                                @copy.prevent
                                @paste.prevent
                              />
                            </div>
                          </div>
                          <div class="col-12 col-md-6 pb_me-4">
                            <div class="txt_vla_feature_content pb-1">
                              Only one of these
                            </div>
                            <div class="form-group mb-0 w-100">
                              <div class="selectBox" @click="showCheckboxes()">
                                <select
                                  v-model="featureOnlyOneOfThese"
                                  class="form-control border-gray border"
                                ></select>
                                <div class="overSelect"></div>
                              </div>
                              <div id="checkboxes">
                                <label class="onlyOneOfThese_label">
                                  <b-form-checkbox id="one">
                                    First checkbox
                                  </b-form-checkbox>
                                </label>
                                <label class="onlyOneOfThese_label">
                                  <b-form-checkbox id="two">
                                    Second checkbox
                                  </b-form-checkbox>
                                </label>
                                <label class="onlyOneOfThese_label">
                                  <b-form-checkbox id="three">
                                    Third checkbox
                                  </b-form-checkbox>
                                </label>
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
    </div>
    <div class="row">
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
    isShowDeleteGroupModal: false,
    isLoading: false,
    question: '',
    value: 0,
    conditionOptions: [
      {
        label: 'yes',
        value: 'Yes',
      },
      {
        label: 'no',
        value: 'No',
      },
    ],
    featureOptions: [
      {
        feature: 'มีไข้',
        value: 'มีไข้',
      },
      {
        feature: 'ไอ',
        value: 'ไอ',
      },
    ],
    featureCondition: null,
    featureOnlyOneOfThese: null,
    expanded: false,
  }),
  computed: {
    previousUrl() {
      return '/chatbot-training/group-management'
    },
  },
  mounted() {
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
    showCheckboxes() {
      let checkboxes = document.getElementById('checkboxes')
      if (!this.expanded) {
        checkboxes.style.display = 'flex'
        this.expanded = true
      } else {
        checkboxes.style.display = 'none'
        this.expanded = false
      }
    },
  },
}
</script>

<style lang="scss">
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
#checkboxes {
  display: none;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  background: #ffffff;
  border: 1px solid rgba(0, 0, 0, 0.15);
  box-shadow: 0px 0px 8px rgba(0, 0, 0, 0.2);
}

#checkboxes label {
  width: 100%;
  margin-bottom: 0;
  padding: 0.5rem;
}

#checkboxes label:hover {
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
