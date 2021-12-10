const HEALTHCARE_ROUTE = [
  {
    name: 'Healthcare Chatbot homepage',
    path: '/',
    component: 'pages/index.vue',
  },
  {
    name: 'Login',
    path: '/login',
    component: 'pages/authentication/Login.vue',
  },
  {
    name: 'Register',
    path: '/register',
    component: 'pages/authentication/Register.vue',
  },
  // {
  //   name: 'Forgot Password',
  //   path: '/forgot-password',
  //   component: 'pages/forgot-password/index.vue',
  // },
  // {
  //   name: 'Reset Password',
  //   path: '/reset-password',
  //   component: 'pages/reset-password/index.vue',
  // },
  // {
  //   name: 'Resend email',
  //   path: '/resend-verify',
  //   component: 'pages/resend-verify/index.vue',
  // },
  // {
  //   name: 'verify',
  //   path: '/verify',
  //   component: 'pages/verify/index.vue',
  // },
]

const CHATBOT_TRAINING_ROUTE = [
  {
    name: 'Learned word',
    path: '/chatbot-training/learned-word',
    component: 'pages/chatbotTraining/TrainedWord.vue',
  },
  {
    name: 'Feature management',
    path: '/chatbot-training/feature-management',
    component: 'pages/chatbotTraining/FeatureManagement.vue',
  },
  {
    name: 'Group management',
    path: '/chatbot-training/group-management',
    component: 'pages/chatbotTraining/GroupManagement.vue',
  },
  {
    name: 'Group management group',
    path: '/chatbot-training/group-management/group/:groupId',
    component: 'pages/chatbotTraining/GroupManagementGroup.vue',
  },
]

const DASHBOARD_ROUTE = [
  {
    name: 'All patient group',
    path: '/dashboard/all-patient-group',
    component: 'pages/dashboard/PatientGroup.vue',
  },
  {
    name: 'Patient in group',
    path: '/dashboard/patient-in-group/:groupId',
    component: 'pages/dashboard/PatientInGroup.vue',
  },
]

const SKIN_DISEASE = [
  {
    name: 'Eczema',
    path: '/Questionnaire/Eczema',
    component: 'pages/skinDisease/Eczema.vue',
  },
  {
    name: 'Atopic Dermatitis',
    path: '/Questionnaire/AtopicDermatitis',
    component: 'pages/skinDisease/AtopicDermatitis.vue',
  },
  {
    name: 'Tinea Ringworm Candidiasis',
    path: '/Questionnaire/TineaRingworm',
    component: 'pages/skinDisease/TineaRingworm.vue',
  },
]

const USER = [
  // {
  //   name: 'My Course',
  //   path: '/user/my-course',
  //   component: 'pages/user/my-course.vue',
  // },
  {
    name: 'User Profile',
    path: '/user/profile',
    component: 'pages/user/Profile.vue',
  },
]

const routesConfig = [
  ...CHATBOT_TRAINING_ROUTE,
  ...HEALTHCARE_ROUTE,
  ...DASHBOARD_ROUTE,
  ...USER,
  ...SKIN_DISEASE,
]

export { CHATBOT_TRAINING_ROUTE, HEALTHCARE_ROUTE }

export default routesConfig
