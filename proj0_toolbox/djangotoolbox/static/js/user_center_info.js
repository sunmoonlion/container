const { createApp, ref, onMounted } = Vue;

const app = createApp({
    setup() {
        // 从模板获取变量并定义响应式变量
        const username = ref(window.username); // 假设 window.username 是在模板中定义的全局变量
        const mobile = ref(window.mobile); // 假设 window.mobile 是在模板中定义的全局变量
        const email = ref(window.emailValue); // 假设 window.emailValue 是在模板中定义的全局变量
        const email_active = ref(window.emailActiveValue === 'True'); // 假设 window.emailActiveValue 是在模板中定义的全局变量

        const set_email = ref("{{ email }}" === '');
        const error_email = ref(false);
        const send_email_btn_disabled = ref(false);
        const send_email_tip = ref('');
        const histories = ref([]);

        const loggedIn = ref(false);

        const check_email = () => {
            let re = /^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$/;
            if (re.test(email.value)) {
                error_email.value = false;
            } else {
                error_email.value = true;
            }
        };

        const cancel_email = () => {
            email.value = '';
            error_email.value = false;
        };

        const save_email = () => {
            check_email();

            if (!error_email.value) {
                let url = '/emails/';
                axios.put(url, { email: email.value }, {
                    headers: { 'X-CSRFToken': getCookie('csrftoken') },
                    responseType: 'json'
                })
                .then(response => {
                    if (response.data.code == '0') {
                        set_email.value = false;
                        send_email_btn_disabled.value = true;
                        send_email_tip.value = '已发送验证邮件';
                    } else if (response.data.code == '4101') {
                        location.href = '/login/?next=/info/';
                    } else {
                        console.log(response);
                    }
                })
                .catch(error => {
                    console.log(error.response);
                });
            }
        };

        const browse_histories = () => {
            let url = '/browse_histories/';
            axios.get(url, { responseType: 'json' })
            .then(response => {
                histories.value = response.data.skus;
                for (let i = 0; i < histories.value.length; i++) {
                    histories.value[i].url = '/detail/' + histories.value[i].id + '/';
                }
            })
            .catch(error => {
                console.log(error.response);
            });
        // };

        // onMounted(() => {
        //     // 从 Cookie 中获取用户名
        //     const user = getCookie('username');
        //     if (user) {
        //         loggedIn.value = true;
        //         username.value = user;
        //     }
        //     browse_histories();
        // });

        return {
            loggedIn,
            username,
            mobile,
            email,
            email_active,
            set_email,
            error_email,
            send_email_btn_disabled,
            send_email_tip,
            histories,
            check_email,
            cancel_email,
            save_email,
            browse_histories
        };
    }
}})

app.config.compilerOptions.delimiters = ['[[', ']]'];

app.mount('#app');
