const { createApp, ref, reactive, onMounted, watch } = Vue;

const app = createApp({
  setup() {
    const username = ref(getCookie('username')); 
    const is_show_edit = ref(false);
    const form_address = reactive({
      receiver: '',
      province_id: '',
      city_id: '',
      district_id: '',
      place: '',
      mobile: '',
      tel: '',
      email: '',
    });

    const provinces = ref([]);
    const cities = ref([]);
    const districts = ref([]);
    const addresses = ref([]);
    const default_address_id = ref('');

    const editing_address_index = ref('');
    const edit_title_index = ref('');
    const new_title = ref('');

    const error_receiver = ref(false);
    const error_place = ref(false);
    const error_mobile = ref(false);
    const error_tel = ref(false);
    const error_email = ref(false);

    const get_provinces = async () => {
      try {
        const response = await axios.get('/areas/', { responseType: 'json' });
        if (response.data.code === '0') {
          provinces.value = response.data.province_list;
        } else {
          provinces.value = [];
        }
      } catch (error) {
        console.error(error);
        provinces.value = [];
      }
    };

    const show_add_site = () => {
      is_show_edit.value = true;
      clear_all_errors();
      Object.assign(form_address, {
        receiver: '',
        province_id: '',
        city_id: '',
        district_id: '',
        place: '',
        mobile: '',
        tel: '',
        email: '',
      });
      editing_address_index.value = '';
    };

    const show_edit_site = (index) => {
      is_show_edit.value = true;
      clear_all_errors();
      editing_address_index.value = index.toString();
      Object.assign(form_address, JSON.parse(JSON.stringify(addresses.value[index])));
    };

    const check_receiver = () => {
      error_receiver.value = !form_address.receiver;
    };

    const check_place = () => {
      error_place.value = !form_address.place;
    };

    const check_mobile = () => {
      const re = /^1[3-9]\d{9}$/;
      error_mobile.value = !re.test(form_address.mobile);
    };

    const check_tel = () => {
      if (form_address.tel) {
        const re = /^(0[0-9]{2,3}-)?([2-9][0-9]{6,7})+(-[0-9]{1,4})?$/;
        error_tel.value = !re.test(form_address.tel);
      } else {
        error_tel.value = false;
      }
    };

    const check_email = () => {
      if (form_address.email) {
        const re = /^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$/;
        error_email.value = !re.test(form_address.email);
      } else {
        error_email.value = false;
      }
    };

    const clear_all_errors = () => {
      error_receiver.value = false;
      error_place.value = false;
      error_mobile.value = false;
      error_tel.value = false;
      error_email.value = false;
    };

    const save_address = async () => {
      if (error_receiver.value || error_place.value || error_mobile.value || error_email.value || !form_address.province_id || !form_address.city_id || !form_address.district_id) {
        alert('信息填写有误！');
      } else {
        try {
          if (editing_address_index.value === '') {
            const url = '/addresses/create/';
            const response = await axios.post(url, form_address, {
              headers: { 'X-CSRFToken': getCookie('csrftoken') },
              responseType: 'json'
            });
            if (response.data.code == '0') {
              addresses.value.unshift(response.data.address);
              is_show_edit.value = false;
            } else if (response.data.code == '4101') {
              location.href = '/login/?next=/addresses/';
            } else {
              alert(response.data.errmsg);
            }
          } else {
            const url = `/addresses/${addresses.value[editing_address_index.value].id}/`;
            const response = await axios.put(url, form_address, {
              headers: { 'X-CSRFToken': getCookie('csrftoken') },
              responseType: 'json'
            });
            if (response.data.code == '0') {
              addresses.value[editing_address_index.value] = response.data.address;
              is_show_edit.value = false;
            } else if (response.data.code == '4101') {
              location.href = '/login/?next=/addresses/';
            } else {
              alert(response.data.errmsg);
            }
          }
        } catch (error) {
          alert(error.response);
        }
      }
    };

    const delete_address = async (index) => {
      const url = `/addresses/${addresses.value[index].id}/`;
      try {
        const response = await axios.delete(url, {
          headers: { 'X-CSRFToken': getCookie('csrftoken') },
          responseType: 'json'
        });
        if (response.data.code == '0') {
          addresses.value.splice(index, 1);
        } else if (response.data.code == '4101') {
          location.href = '/login/?next=/addresses/';
        } else {
          alert(response.data.errmsg);
        }
      } catch (error) {
        console.log(error.response);
      }
    };

    const set_default = async (index) => {
      const url = `/addresses/${addresses.value[index].id}/default/`;
      try {
        const response = await axios.put(url, {}, {
          headers: { 'X-CSRFToken': getCookie('csrftoken') },
          responseType: 'json'
        });
        if (response.data.code == '0') {
          default_address_id.value = addresses.value[index].id;
        } else if (response.data.code == '4101') {
          location.href = '/login/?next=/addresses/';
        } else {
          alert(response.data.errmsg);
        }
      } catch (error) {
        console.log(error.response);
      }
    };

    const show_edit_title = (index) => {
      edit_title_index.value = index;
    };

    const cancel_title = () => {
      edit_title_index.value = '';
      new_title.value = '';
    };

    const save_title = async (index) => {
      if (!new_title.value) {
        alert("请填写标题后再保存！");
      } else {
        const url = `/addresses/${addresses.value[index].id}/title/`;
        try {
          const response = await axios.put(url, { title: new_title.value }, {
            headers: { 'X-CSRFToken': getCookie('csrftoken') },
            responseType: 'json'
          });
          if (response.data.code == '0') {
            addresses.value[index].title = new_title.value;
            cancel_title();
          } else if (response.data.code == '4101') {
            location.href = '/login/?next=/addresses/';
          } else {
            alert(response.data.errmsg);
          }
        } catch (error) {
          console.log(error.response);
        }
      }
    };

    watch(() => form_address.province_id, async (newVal) => {
      if (newVal) {
        const url = `/areas/?area_id=${newVal}`;
        try {
          const response = await axios.get(url, { responseType: 'json' });
          if (response.data.code == '0') {
            cities.value = response.data.sub_data.subs;
          } else {
            cities.value = [];
          }
        } catch (error) {
          cities.value = [];
        }
      }
    });

    watch(() => form_address.city_id, async (newVal) => {
      if (newVal) {
        const url = `/areas/?area_id=${newVal}`;
        try {
          const response = await axios.get(url, { responseType: 'json' });
          if (response.data.code == '0') {
            districts.value = response.data.sub_data.subs;
          } else {
            districts.value = [];
          }
        } catch (error) {
          districts.value = [];
        }
      }
    });

    const initializeData = async () => {
      await get_provinces();
      addresses.value = window.addresses;
      default_address_id.value = window.default_address_id;
      
      }

    onMounted(initializeData);

    return {
      username,
      is_show_edit,
      form_address,
      provinces,
      cities,
      districts,
      addresses,
      default_address_id,
      editing_address_index,
      edit_title_index,
      new_title,
      error_receiver,
      error_place,
      error_mobile,
      error_tel,
      error_email,
      show_add_site,
      show_edit_site,
      check_receiver,
      check_place,
      check_mobile,
      check_tel,
      check_email,
      clear_all_errors,
      save_address,
      delete_address,
      set_default,
      show_edit_title,
      cancel_title,
      save_title
    };
  }
});

app.config.compilerOptions.delimiters = ['[[', ']]'];

app.mount('#app');
