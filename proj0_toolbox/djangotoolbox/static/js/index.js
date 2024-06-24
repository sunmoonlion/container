const { createApp, ref, onMounted } = Vue;

const app = createApp({
  setup() {
    const loggedIn = ref(false);
    const username = ref('');

    onMounted(() => {
      // 从 Cookie 中获取用户名
      const user = getCookie('username');
      if (user) {
        loggedIn.value = true;
        username.value = user;
      }
    });

    return {
      loggedIn,
      username
    };
  }
});

app.mount('#app');
