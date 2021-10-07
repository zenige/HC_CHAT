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
                >
                </b-form-input>
                <div
                  class="form-control-feedback"
                  :disabled="!filter"
                  @click="filter = null"
                  style="cursor: pointer"
                >
                  <i class="icon-cross3 txt_grey" style="height: 22px"></i>
                </div>
              </div>
            </div>
          </div>
          <div class="col-4 col-md-8 text-right">
            <button
              @click="openAddWordModal()"
              class="hcb-btn btn btn_hcb_green btn-block"
            >
              Add Word
            </button>
            <button
              @click="openDeleteWordModal()"
              class="hcb-btn btn btn_hcb_red btn-block"
            >
              Delete
            </button>
          </div>
        </div>
        <div class="col-md-12" style="padding-top: 2rem; padding-bottom: 1rem">
          <div class="row d-flex align-items-center">
            <div class="txt_hc_head_total">
              Total words
              <span class="txt_vla_grey">({{ totalTrainedWord }})</span>
            </div>
          </div>
          <div>
            Sorting By: <b>{{ sortBy }}</b
            >, Sort Direction:
            <b>{{ sortDesc ? 'Descending' : 'Ascending' }}</b>
          </div>
          <div>
            Current page: <b>{{ currentPage }}</b>
          </div>
          <div>
            Data: <b>{{ trainedWordData.length }}</b>
          </div>
        </div>
        <div class="col-md-12">
          <div class="row d-flex align-items-center justify-content-center">
            <b-table
              responsive
              id="trainedWord-table"
              :items="trainedWordData"
              :fields="fields"
              :per-page="0"
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
              <template #cell(question)="data">
                <div
                  v-if="data.item.editable === false"
                  class="d-flex justify-content-start"
                >
                  <div class="word-data-text">
                    {{ data.item.question }}
                  </div>
                </div>
                <div v-if="data.item.editable === true">
                  <b-form-textarea
                    autofocus
                    v-model="changedQuestionData"
                    rows="3"
                    max-rows="6"
                    no-auto-shrink
                  />
                </div>
              </template>
              <template #cell(answer)="data">
                <div v-if="data.item.editable === false">
                  <div class="word-data-text">
                    {{ data.item.answer }}
                  </div>
                </div>
                <b-form-textarea
                  autofocus
                  v-if="data.item.editable === true"
                  v-model="changedAnswerData"
                  rows="3"
                  max-rows="6"
                  no-auto-shrink
                />
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
                    @click="editWord(data)"
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
                    @click="saveWord(data)"
                    class="hcb-btn-light btn btn_hcb_green_light mr-2 btn-block"
                  >
                    Save
                  </button>
                  <div @click="cancleEditWord(data)" class="txt_grey_cancel">
                    Cancel
                  </div>
                </div>
              </template>
            </b-table>
            <div style="margin-top: 0.5rem">
              <b-pagination
                v-model="currentPage"
                :total-rows="totalTrainedWord"
                :per-page="perPage"
                aria-controls="trainedWord-table"
                first-number
                last-number
                align="center"
                class="myPaginattion"
              ></b-pagination>
            </div>
          </div>
        </div>

        <DeleteWordModal
          :isOpen="isShowDeleteWordModal"
          :onCancel="closeDeleteWordModal"
          :onDelete="onDeleteWord"
        ></DeleteWordModal>
        <AddNewWordModal
          :isOpen="isShowAddNewWordModal"
          :onCancel="closeAddWordModal"
          @getTrainedWordData="getTrainedWordData"
          :currentPage="currentPage"
          :perPage="perPage"
          :sortBy="sortBy"
          :sortDesc="sortDesc"
          :filter="filter"
        ></AddNewWordModal>
      </div>
    </div>
  </div>
</template>

<script>
const ASCENDING = 'ASCENDING'
const DESCENDING = 'DESCENDING'

export default {
  components: {
    DeleteWordModal: () => import('~/components/modals/DeleteWordModal.vue'),
    AddNewWordModal: () => import('~/components/modals/AddNewWordModal.vue'),
    Loader: () => import('~/components/Loader.vue'),
  },
  props: {},
  data() {
    return {
      sortBy: 'question',
      sortDesc: false,
      filter: null,
      isLoading: false,
      isShowDeleteWordModal: false,
      isShowAddNewWordModal: false,
      edit: false,
      selectAll: false,
      selectedRow: {},
      perPage: 10,
      currentPage: 1,
      deleteSelected: [],
      totalTrainedWord: 0,
      changedQuestionData: '',
      changedAnswerData: '',
      fields: [
        {
          key: 'selected',
          label: 'Select',
          thClass: 'trainedWordthSelect-Class',
          tdClass: 'trainedWordtdSelect-Class',
        },
        {
          key: 'question',
          label: 'Question',
          sortable: true,
          thClass: 'trainedWordthQuestion-Class',
          tdClass: 'trainedWordtdQuestion-Class',
        },
        {
          key: 'answer',
          label: 'Answer',
          sortable: true,
          thClass: 'trainedWordthAnswer-Class',
          tdClass: 'trainedWordtdAnswer-Class',
        },
        {
          key: 'action',
          label: 'Action',
          sortable: false,
          thClass: 'trainedWordthConfident-Class',
          tdClass: 'trainedWordtdConfident-Class',
        },
      ],
      trainedWordData: [],
    }
  },
  watch: {
    selectAll(value) {
      this.trainedWordData.map(function (item) {
        item.selected = value
        return item
      })
    },
    currentPage(value) {
      if (!this.filter) {
        this.perPage = 10
        this.getTrainedWordData(
          this.filter,
          value,
          this.perPage,
          this.sortBy,
          this.sortDesc ? DESCENDING : ASCENDING
        )
      }
    },
    filter(value) {
      if (value) {
        this.currentPage = 1
        this.perPage = this.trainedWordData.length
        setTimeout(() => {
          this.getTrainedWordData(
            value,
            this.currentPage,
            this.perPage,
            this.sortBy,
            this.sortDesc ? DESCENDING : ASCENDING
          )
        }, 250)
      } else if (!value) {
        this.currentPage = 1
        this.perPage = 10
        this.getTrainedWordData(
          value,
          this.currentPage,
          this.perPage,
          this.sortBy,
          this.sortDesc ? DESCENDING : ASCENDING
        )
      }
    },
    sortBy(value) {
      console.log(value)
      if (value) {
        this.getTrainedWordData(
          this.filter,
          this.currentPage,
          this.perPage,
          value,
          this.sortDesc ? DESCENDING : ASCENDING
        )
      } else if (!value) {
        this.getTrainedWordData(
          this.filter,
          this.currentPage,
          this.perPage,
          'question',
          this.sortDesc ? DESCENDING : ASCENDING
        )
        this.sortBy = 'question'
      }
    },
    sortDesc(value) {
      if (!value) {
        this.getTrainedWordData(
          this.filter,
          this.currentPage,
          this.perPage,
          this.sortBy,
          ASCENDING
        )
      } else if (value) {
        this.getTrainedWordData(
          this.filter,
          this.currentPage,
          this.perPage,
          this.sortBy,
          DESCENDING
        )
      }
    },
  },
  async mounted() {
    await this.getTrainedWordData(
      this.filter,
      this.currentPage,
      this.perPage,
      this.sortBy,
      ASCENDING
    )
    this.isLoading = true
  },
  computed: {},
  methods: {
    selectedRowClass(item) {
      if (item.selected === true) return 'row-selected'
    },
    openDeleteWordModal() {
      this.deleteSelected = this.trainedWordData.filter(
        (item) => item.selected === true
      )
      if (this.deleteSelected.length >= 1) {
        this.isShowDeleteWordModal = true
      } else {
        ;(this.isShowDeleteWordModal = false),
          this.$bvToast.toast('Please select any word', {
            variant: 'danger',
            toaster: 'b-toaster-bottom-left',
            noCloseButton: true,
          })
      }
    },
    closeDeleteWordModal() {
      this.selectAll = false
      this.isShowDeleteWordModal = false
    },
    openAddWordModal() {
      this.isShowAddNewWordModal = true
    },
    closeAddWordModal() {
      this.isShowAddNewWordModal = false
    },
    async onDeleteWord() {
      this.deleteSelected = this.trainedWordData.filter(
        (item) => item.selected === true
      )
      await this.$axios.delete('train/trained/delete/many', {
        data: this.deleteSelected,
      })
      await this.getTrainedWordData(
        this.filter,
        this.currentPage,
        10,
        orderBy,
        'question',
        ASCENDING
      )
      if (this.trainedWordData.length === 0) {
        this.totalTrainedWord = 0
      }
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
      await this.$axios.patch('train/trained/' + data.item.id, {
        question: data.item.question,
        answer: data.item.answer,
      })
    },
    async getTrainedWordData(filter, page, limit, orderBy, sortBy) {
      let { data } = await this.$axios.get('train/trained', {
        params: {
          filter: filter,
          pages: page,
          limit: limit,
          order_by: orderBy,
          sort_by: sortBy,
        },
      })
      this.trainedWordData = data.map((item) => {
        // collect total trained word data
        if (item.total) {
          return (
            {
              id: undefined,
            },
            (this.totalTrainedWord = item.total)
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
      this.trainedWordData = this.trainedWordData.filter(function (element) {
        return element.id !== undefined
      })
      if (this.trainedWordData.length === 0) {
        this.totalTrainedWord = 0
      }
    },
  },
}
</script>

<style lang="scss">
.trainedWordthSelect-Class,
.trainedWordtdSelect-Class {
  width: 15%;
}
.trainedWordthQuestion-Class,
.trainedWordtdQuestion-Class {
  width: 32.5%;
}
.trainedWordthAnswer-Class,
.trainedWordtdAnswer-Class {
  width: 32.5%;
}
.trainedWordthAction-Class,
.trainedWordtdAction-Class {
  width: 20%;
}
</style>
