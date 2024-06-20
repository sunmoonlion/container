const { createApp, ref, onMounted } = Vue;

const app = createApp({
    setup() {
        // Reactive state
        const username = ref('');
        const email = ref('');
        const password = ref();
        const password2 = ref('');
        const mobile = ref('');
        const allow = ref(false);
        const image_code_url = ref('');
        const uuid = ref('');
        const image_code = ref('');
        const sms_code_tip = ref('获取短信验证码'); 
        const send_flag = ref(false);
        const sms_code = ref('');

        // Validation states
        const error_name = ref(false);
        const error_email = ref(false);
        const error_password = ref(false);
        const error_password2 = ref(false);
        const error_mobile = ref(false);
        const error_allow = ref(false);
        const error_image_code = ref(false);
        const error_sms_code = ref(false);

        // Error messages
        const error_name_message = ref('');
        const error_mobile_message = ref('');
        const error_allow_message = ref('');
        const error_image_code_message = ref('');
        const error_sms_code_message = ref('');

        // Methods
        const send_sms_code = () => {
            if (send_flag.value) {
                return;
            }
            send_flag.value = true;

            check_mobile();
            check_image_code();
            if (error_mobile.value || error_image_code.value) {
                send_flag.value = false;
                return;
            }

            const url = `/sms_codes/${mobile.value}/?image_code=${image_code.value}&uuid=${uuid.value}`;
            axios.get(url, { responseType: 'json' })
                .then(response => {
                    if (response.data.code === '0') {
                        let num = 60;
                        const t = setInterval(() => {
                            if (num === 1) {
                                clearInterval(t);
                                sms_code_tip.value = '获取短信验证码';
                                generate_image_code();
                                send_flag.value = false;
                            } else {
                                num -= 1;
                                sms_code_tip.value = `${num}秒`;
                            }
                        }, 1000);
                    } else {
                        if (response.data.code === '4001') {
                            error_image_code_message.value = response.data.errmsg;
                            error_image_code.value = true;
                        } else {
                            error_sms_code_message.value = response.data.errmsg;
                            error_sms_code.value = true;
                        }
                        send_flag.value = false;
                    }
                })
                .catch(error => {
                    console.log(error.response);
                    send_flag.value = false;
                });
        };

        const generate_image_code = () => {
            uuid.value = generateUUID();
            image_code_url.value = `/image_codes/${uuid.value}/`;
            console.log('New UUID:', uuid.value);
            console.log('New Image Code URL:', image_code_url.value);
        };
        

        const check_username = () => {
            const re = /^[a-zA-Z0-9_-]{5,20}$/;
            if (re.test(username.value)) {
                error_name.value = false;
            } else {
                error_name_message.value = '请输入5-20个字符的用户名';
                error_name.value = true;
            }

            if (!error_name.value) {
                const url = `/usernames/${username.value}/count/`;
                axios.get(url, { responseType: 'json' })
                    .then(response => {
                        if (response.data.count === 1) {
                            error_name_message.value = '用户名已存在';
                            error_name.value = true;
                        } else {
                            error_name.value = false;
                        }
                    })
                    .catch(error => {
                        console.log(error.response);
                    });
            }
        };

        const check_email = () => {
            const re = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
            if (re.test(email.value)) {
                error_email.value = false;
            } else {
                error_email.value = true;
            }
        };

        const check_password = () => {
            const re = /^[0-9A-Za-z]{8,20}$/;
            if (re.test(password.value)) {
                error_password.value = false;
            } else {
                error_password.value = true;
            }
        };

        const check_password2 = () => {
            if (password.value !== password2.value) {
                error_password2.value = true;
            } else {
                error_password2.value = false;
            }
        };

        const check_mobile = () => {
            const re = /^1[3-9]\d{9}$/;
            if (re.test(mobile.value)) {
                error_mobile.value = false;
            } else {
                error_mobile_message.value = '您输入的手机号格式不正确';
                error_mobile.value = true;
            }

            if (!error_mobile.value) {
                const url = `/mobiles/${mobile.value}/count/`;
                axios.get(url, { responseType: 'json' })
                    .then(response => {
                        if (response.data.count === 1) {
                            error_mobile_message.value = '手机号已存在';
                            error_mobile.value = true;
                        } else {
                            error_mobile.value = false;
                        }
                    })
                    .catch(error => {
                        console.log(error.response);
                    });
            }
        };

        // 校验图形验证码吗
        const check_image_code = () => {
            if (image_code.length != 4) {
                error_image_code_message = '请输入图形验证码';
                error_image_code = true;
            } else {
                error_image_code = false;
            }
        };
        // 校验短信验证码
        const check_sms_code = () => {
            if(sms_code.length != 6){
                error_sms_code_message = '请填写短信验证码';
                error_sms_code = true;
            } else {
                error_sms_code = false;
            }
        };

        const check_allow = () => {
            if (!allow.value) {
                error_allow.value = true;
            } else {
                error_allow.value = false;
            }
        };

        const on_submit = (event) => {
            check_username();
            check_password();
            check_password2();
            check_mobile();
            check_image_code();
            check_sms_code();
            check_allow();

            if (error_name.value || error_password.value || error_password2.value || error_mobile.value || error_allow.value || error_image_code || error_sms_code) {
                event.preventDefault();
            }
        };

        // 在页面加载完执行的逻辑
        onMounted(() => {
            generate_image_code();
        });

        return {
            username,
            email,
            password,
            password2,
            mobile,
            allow,
            image_code_url,
            uuid,
            image_code,
            sms_code_tip,
            send_flag,
            sms_code,
            error_name,
            error_email,
            error_password,
            error_password2,
            error_mobile,
            error_allow,
            error_image_code,
            error_sms_code,
            error_name_message,
            error_mobile_message,
            error_allow_message,
            error_image_code_message,
            error_sms_code_message,
            send_sms_code,
            generate_image_code,
            check_username,
            check_email,
            check_password,
            check_password2,
            check_mobile,
            check_image_code,
            check_sms_code,
            check_allow,
            on_submit
        };
    }
});

app.config.compilerOptions.delimiters = ['[[',']]'];

app.mount('#app');
