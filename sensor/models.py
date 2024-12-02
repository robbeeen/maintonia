from django.db import models

# Create your models here.
from django.db import models

class SensorReading(models.Model):
    test_format = models.CharField(max_length=255, blank=True, null=True)
    test_mode = models.CharField(max_length=255, blank=True, null=True)
    test_type = models.CharField(max_length=255, blank=True, null=True)
    record_number = models.CharField(max_length=255, blank=True, null=True)
    test_referance = models.CharField(max_length=255, blank=True, null=True)
    test_result = models.CharField(max_length=255, blank=True, null=True)
    display_count1 = models.CharField(max_length=255, blank=True, null=True)
    display_count2 = models.CharField(max_length=255, blank=True, null=True)
    display_count3 = models.CharField(max_length=255, blank=True, null=True)
    display_count4 = models.CharField(max_length=255, blank=True, null=True)
    display_count5 = models.CharField(max_length=255, blank=True, null=True)
    display_count6 = models.CharField(max_length=255, blank=True, null=True)
    display_count7 = models.CharField(max_length=255, blank=True, null=True)
    display_count8 = models.CharField(max_length=255, blank=True, null=True)
    live_mode = models.CharField(max_length=255, blank=True, null=True)
    bt = models.CharField(max_length=255, blank=True, null=True)
    bt_percentage = models.CharField(max_length=255, blank=True, null=True)
    raw_count1 = models.CharField(max_length=255, blank=True, null=True)
    raw_count2 = models.CharField(max_length=255, blank=True, null=True)
    raw_count3 = models.CharField(max_length=255, blank=True, null=True)
    raw_count4 = models.CharField(max_length=255, blank=True, null=True)
    raw_count5 = models.CharField(max_length=255, blank=True, null=True)
    raw_count6 = models.CharField(max_length=255, blank=True, null=True)
    raw_count7 = models.CharField(max_length=255, blank=True, null=True)
    raw_count8 = models.CharField(max_length=255, blank=True, null=True)
    print_count1 = models.CharField(max_length=255, blank=True, null=True)
    print_count2 = models.CharField(max_length=255, blank=True, null=True)
    print_count3 = models.CharField(max_length=255, blank=True, null=True)
    print_count4 = models.CharField(max_length=255, blank=True, null=True)
    print_count5 = models.CharField(max_length=255, blank=True, null=True)
    print_count6 = models.CharField(max_length=255, blank=True, null=True)
    print_count7 = models.CharField(max_length=255, blank=True, null=True)
    print_count8 = models.CharField(max_length=255, blank=True, null=True)
    record_name = models.CharField(max_length=255, blank=True, null=True)
    oil_grade = models.CharField(max_length=255, blank=True, null=True)
    use_date = models.CharField(max_length=255, blank=True, null=True)
    set_date = models.CharField(max_length=255, blank=True, null=True)
    flush_time = models.CharField(max_length=255, blank=True, null=True)
    test_total_count = models.CharField(max_length=255, blank=True, null=True)
    test_duration_count = models.CharField(max_length=255, blank=True, null=True)
    mc_running_hr = models.CharField(max_length=255, blank=True, null=True)
    last_shutdown = models.CharField(max_length=255, blank=True, null=True)
    last_power_on = models.CharField(max_length=255, blank=True, null=True)
    wifi_ip_address = models.CharField(max_length=255, blank=True, null=True)
    host_name = models.CharField(max_length=255, blank=True, null=True)
    bt_brightness = models.CharField(max_length=255, blank=True, null=True)
    communication_status = models.CharField(max_length=255, blank=True, null=True)
    sensor_status = models.CharField(max_length=255, blank=True, null=True)
    sensor_raw_value = models.CharField(max_length=255, blank=True, null=True)
    battery_per = models.CharField(max_length=255, blank=True, null=True)
    battery_state = models.CharField(max_length=255, blank=True, null=True)
    bt_raw_vtg = models.CharField(max_length=255, blank=True, null=True)
    bt_time_to_discharge = models.CharField(max_length=255, blank=True, null=True)
    system_power_consumption = models.CharField(max_length=255, blank=True, null=True)
    power_ic_last_data_received_on = models.CharField(max_length=255, blank=True, null=True)
    device_ip_address = models.CharField(max_length=255, blank=True, null=True)
    device_mac_id = models.CharField(max_length=255, blank=True, null=True)
    diagnostic_result = models.CharField(max_length=255, blank=True, null=True)
    median_set_time_grade1 = models.CharField(max_length=255, blank=True, null=True)
    median_set_time_grade2 = models.CharField(max_length=255, blank=True, null=True)
    median_set_time_grade3 = models.CharField(max_length=255, blank=True, null=True)
    median_set_time_grade4 = models.CharField(max_length=255, blank=True, null=True)
    single_test_set_time_grade1 = models.CharField(max_length=255, blank=True, null=True)
    single_test_set_time_grade2 = models.CharField(max_length=255, blank=True, null=True)
    single_test_set_time_grade3 = models.CharField(max_length=255, blank=True, null=True)
    single_test_set_time_grade4 = models.CharField(max_length=255, blank=True, null=True)
    select_cycle_time = models.CharField(max_length=255, blank=True, null=True)
    fixed_cycle_time = models.CharField(max_length=255, blank=True, null=True)
    below_hun_manipulation = models.CharField(max_length=255, blank=True, null=True)
    above_hun_manipulation = models.CharField(max_length=255, blank=True, null=True)
    ppm_set_manipulation = models.CharField(max_length=255, blank=True, null=True)
    nas_to_gost_manipulation1 = models.CharField(max_length=255, blank=True, null=True)
    nas_to_gost_manipulation2 = models.CharField(max_length=255, blank=True, null=True)
    nas_to_gost_manipulation3 = models.CharField(max_length=255, blank=True, null=True)
    nas_to_gost_manipulation4 = models.CharField(max_length=255, blank=True, null=True)
    manipulation_25miron_argohy = models.CharField(max_length=255, blank=True, null=True)
    manipulation_38miron_argohy = models.CharField(max_length=255, blank=True, null=True)
    manipulation_50miron_argohy = models.CharField(max_length=255, blank=True, null=True)
    manipulation_70miron_argohy = models.CharField(max_length=255, blank=True, null=True)
    sensor_calibration_date = models.CharField(max_length=255, blank=True, null=True)
    sensor_sr_number = models.CharField(max_length=255, blank=True, null=True)
    sd_delay = models.CharField(max_length=255, blank=True, null=True)
    ch_dch = models.CharField(max_length=255, blank=True, null=True)
    bt_low_cut_v = models.CharField(max_length=255, blank=True, null=True)
    bt_hi_cut_v = models.CharField(max_length=255, blank=True, null=True)
    cpu_temp = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.record_number