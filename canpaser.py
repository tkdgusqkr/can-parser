import os
import shutil
import csv

# 원본 파일들이 있는 최상위 폴더 아마 D or E 드라이브지 않을까?
base_directory = 'can'

for folder_name in os.listdir(base_directory): # 최상위 폴더에 있는 모든 하위폴더 처리
    source_directory = os.path.join(base_directory, folder_name)
    
    if not os.path.isdir(source_directory):
        continue
    
    New_directory = os.path.join(base_directory, 'organize', folder_name)

    # 새 폴더가 존재하면 삭제하고 새로 만듬
    if os.path.exists(New_directory):
        shutil.rmtree(New_directory)
    
    os.makedirs(New_directory)
    
    Detail_file_list = sorted(os.listdir(source_directory))
    
    # 'START'가 포함된 파일의 인덱스 생성
    start_indices = []
    
    # 파일 목록에서 'START'가 포함된 파일의 인덱스 찾기
    for i, filename in enumerate(Detail_file_list):
        if 'START' in filename:
            start_indices.append(i)
    
    for i in range(len(start_indices)): # 파일 생성

        start = start_indices[i] - 1  # 현재 'START' 파일 전부터
        
        # 마지막 'START' 파일 이후의 파일 범위 처리
        if i + 1 < len(start_indices):
            end = start_indices[i + 1] - 2 # 다음 'START' 파일의 -2 까지
        else:
            end = len(Detail_file_list) - 1 # 마지막 'START' 파일 이후엔 끝까지

        start_file_name = Detail_file_list[start_indices[i]]
        foldername = Detail_file_list[start]
        new_folder_name = f"{foldername}"
        new_folder_path = os.path.join(New_directory, new_folder_name)
        
        os.makedirs(new_folder_path, exist_ok=True)
        
               
        for filename in Detail_file_list[start:end + 1]:
            if 'START' not in filename:
                source_file = os.path.join(source_directory, filename)
                destination_file = os.path.join(new_folder_path, filename)
                shutil.copy(source_file, destination_file)
        
        # print(f"파일들이 {new_folder_path}에 저장되었습니다.")
    
    # print(f"모든 파일이 {New_directory}에 저장되었습니다.")

Org_file_list = sorted(os.listdir(base_directory + '/organize/'))
for folder in Org_file_list:
    folder_src = base_directory + '/organize/' + folder
    folder_dst = base_directory + '/org_dst/' + folder

    # 하위 디렉토리 목록 생성
    directories = [name for name in os.listdir(folder_src) if os.path.isdir(os.path.join(folder_src, name))]

    for directory in directories:
        file_src = os.path.join(folder_src, directory) + '/'
        file_dst = os.path.join(folder_dst, directory) + '/'
        
        # 디렉터리가 존재하지 않으면 생성
        if not os.path.exists(file_dst):
            os.makedirs(file_dst)
        
        # 기존 파일 삭제
        if os.path.exists(file_dst):
            for file in os.scandir(file_dst):
                os.remove(file.path) 
        
        # 파일 열기
        f_utc = open(file_dst + directory + '_utc.csv', 'w', newline='')
        f_imu_error = open(file_dst + directory + '_imu_error.csv', 'w', newline='')
        f_error_list = open(file_dst + directory + '_error_list.csv', 'w', newline='')
        f_imu_status = open(file_dst + directory + '_imu_status.csv', 'w', newline='')
        f_start_up = open(file_dst + directory + '_start_up.csv', 'w', newline='')
        f_pack_power = open(file_dst + directory + '_pack_power.csv', 'w', newline='')
        f_free_acc = open(file_dst + directory + '_free_acc.csv', 'w', newline='')
        f_gry_hr = open(file_dst + directory + '_gry_hr.csv', 'w', newline='')
        f_velocity = open(file_dst + directory + '_velocity.csv', 'w', newline='')
        f_euler_angle = open(file_dst + directory + '_euler_angle.csv', 'w', newline='')
        f_acc_hr = open(file_dst + directory + '_acc_hr.csv', 'w', newline='')
        f_coordinate = open(file_dst + directory + '_coordinate.csv', 'w', newline='')
        f_altitude = open(file_dst + directory + '_altitude.csv', 'w', newline='')
        f_pack_status = open(file_dst + directory + '_pack_status.csv', 'w', newline='')
        f_pack_cv = open(file_dst + directory + '_pack_cv.csv', 'w', newline='')
        f_pack_ocv = open(file_dst + directory + '_pack_ocv.csv', 'w', newline='')
        f_pack_temp = open(file_dst + directory + '_pack_temp.csv', 'w', newline='')
        f_pack_soc = open(file_dst + directory + '_pack_soc.csv', 'w', newline='')
        f_amk_set_point1_rl = open(file_dst + directory + '_amk_set_point1_rl.csv', 'w', newline='')
        f_amk_actual_values1_rl = open(file_dst + directory + '_amk_actual_values1_rl.csv', 'w', newline='')
        f_amk_actual_values2_rl = open(file_dst + directory + '_amk_actual_values2_rl.csv', 'w', newline='')
        f_amk_set_point1_fl = open(file_dst + directory + '_amk_set_point1_fl.csv', 'w', newline='')
        f_amk_actual_values1_fl = open(file_dst + directory + '_amk_actual_values1_fl.csv', 'w', newline='')
        f_amk_actual_values2_fl = open(file_dst + directory + '_amk_actual_values2_fl.csv', 'w', newline='')
        f_amk_set_point1_fr = open(file_dst + directory + '_amk_set_point1_fr.csv', 'w', newline='')
        f_amk_actual_values1_fr = open(file_dst + directory + '_amk_actual_values1_fr.csv', 'w', newline='')
        f_amk_actual_values2_fr = open(file_dst + directory + '_amk_actual_values2_fr.csv', 'w', newline='')
        f_amk_set_point1_rr = open(file_dst + directory + '_amk_set_point1_rr.csv', 'w', newline='')
        f_amk_actual_values1_rr = open(file_dst + directory + '_amk_actual_values1_rr.csv', 'w', newline='')
        f_amk_actual_values2_rr = open(file_dst + directory + '_amk_actual_values2_rr.csv', 'w', newline='')
        f_steering_and_pedal = open(file_dst + directory + '_steering_and_pedal.csv', 'w', newline='')
        f_gear_temp = open(file_dst + directory + '_gear_temp.csv', 'w', newline='')
        f_front_shock = open(file_dst + directory + '_front_shock.csv', 'w', newline='')
        f_rear_shock = open(file_dst + directory + '_rear_shock.csv', 'w', newline='')

        writer = csv.writer(f_utc)
        writer.writerow(['year', 'month', 'day', 'hour', 'min', 'sec', 'tenthms'])
        writer = csv.writer(f_imu_error)
        writer.writerow(['time', 'error_code'])
        # writer = csv.writer(f_error_list)
        # writer.writerow(['time', 'status_word'])
        writer = csv.writer(f_imu_status)
        writer.writerow(['time', 'status_word'])
        # writer = csv.writer(f_start_up)
        # writer.writerow(['time', 'start_up'])
        writer = csv.writer(f_pack_power)
        writer.writerow(['time', 'current (A)', 'voltage (V)', 'ccl (A)', 'dcl (A)'])
        writer = csv.writer(f_free_acc)
        writer.writerow(['time', 'acc_x (m/s\u00B2)', 'acc_y (m/s\u00B2)', 'acc_z (m/s\u00B2)'])
        writer = csv.writer(f_gry_hr)
        writer.writerow(['time', 'gyr_x (rad/s)', 'gyr_y (rad/s)', 'gyr_z (rad/s)'])
        writer = csv.writer(f_velocity)
        writer.writerow(['time', 'vel_x (m/s)', 'vel_y (m/s)', 'vel_z (m/s)'])
        writer = csv.writer(f_euler_angle)
        writer.writerow(['time', 'roll (\u00B0)', 'pitch (\u00B0)', 'yaw (\u00B0)'])
        writer = csv.writer(f_acc_hr)
        writer.writerow(['time', 'acc_x (m/s\u00B2)', 'acc_y (m/s\u00B2)', 'acc_z (m/s\u00B2)'])
        writer = csv.writer(f_coordinate)
        writer.writerow(['time', 'lat (\u00B0)', 'lon (\u00B0)'])
        writer = csv.writer(f_altitude)
        writer.writerow(['time', 'alt_ellipsoid (m)'])
        writer = csv.writer(f_pack_status)
        writer.writerow(['time', 'failsafe_status', 'dtc_status1', 'dtc_status2', 'cl_status'])
        writer = csv.writer(f_pack_cv)
        writer.writerow(['time', 'highest_cv_id', 'highest_cv (V)', 'average_cv (v)', 'lowest_cv_id', 'lowest_cv (V)'])
        writer = csv.writer(f_pack_ocv)
        writer.writerow(['time', 'highest_ocv_id', 'highest_ocv (V)', 'average_ocv (V)', 'lowest_ocv_id', 'lowest_ocv (V)'])
        writer = csv.writer(f_pack_temp)
        writer.writerow(['time', 'highest_temp_id', 'highest_temp (C)', 'average_temp (C)', 'lowest_temp_id', 'lowest_temp (C)', 'resistance (mOhm)'])
        writer = csv.writer(f_pack_soc)
        writer.writerow(['time', 'soc (%)', 'adaptive_soc (%)', 'adaptive_tot_cap (Ah)', 'open_voltage (V)'])
        writer = csv.writer(f_amk_set_point1_rl)
        writer.writerow(['time', 'AMK_bInverterOn', 'AMK_bDcOn', 'AMK_bEnable', 'AMK_bErrorReset', 'AMK_Torque_setpoint (Nm)', 'AMK_TorqueLimitPositv (Nm)', 'AMK_TorqueLimitNegativ (Nm)'])
        writer = csv.writer(f_amk_actual_values1_rl)
        writer.writerow(['time', 'AMK_bSystemReady', 'AMK_bError', 'AMK_bWarn', 'AMK_bQuitDcOn', 'AMK_bDcOn', 'AMK_bQuitInverterOn', 'AMK_bInverterOn', 'AMK_bDerating', 'AMK_ActualVelocity (rpm)', 'AMK_TorqueCurrent', 'AMK_MagnetizingCurrent'])
        writer = csv.writer(f_amk_actual_values2_rl)
        writer.writerow(['time', 'AMK_TempMotor (C)', 'AMK_TempInverter (C)', 'AMK_ErrorInfo', 'AMK_TempIGBT (C)'])
        writer = csv.writer(f_amk_set_point1_fl)
        writer.writerow(['time', 'AMK_bInverterOn', 'AMK_bDcOn', 'AMK_bEnable', 'AMK_bErrorReset', 'AMK_Torque_setpoint (Nm)', 'AMK_TorqueLimitPositv (Nm)', 'AMK_TorqueLimitNegativ (Nm)'])
        writer = csv.writer(f_amk_actual_values1_fl)
        writer.writerow(['time', 'AMK_bSystemReady', 'AMK_bError', 'AMK_bWarn', 'AMK_bQuitDcOn', 'AMK_bDcOn', 'AMK_bQuitInverterOn', 'AMK_bInverterOn', 'AMK_bDerating', 'AMK_ActualVelocity (rpm)', 'AMK_TorqueCurrent', 'AMK_MagnetizingCurrent'])
        writer = csv.writer(f_amk_actual_values2_fl)
        writer.writerow(['time', 'AMK_TempMotor (C)', 'AMK_TempInverter (C)', 'AMK_ErrorInfo', 'AMK_TempIGBT (C)'])
        writer = csv.writer(f_amk_set_point1_fr)
        writer.writerow(['time', 'AMK_bInverterOn', 'AMK_bDcOn', 'AMK_bEnable', 'AMK_bErrorReset', 'AMK_Torque_setpoint (Nm)', 'AMK_TorqueLimitPositv (Nm)', 'AMK_TorqueLimitNegativ (Nm)'])
        writer = csv.writer(f_amk_actual_values1_fr)
        writer.writerow(['time', 'AMK_bSystemReady', 'AMK_bError', 'AMK_bWarn', 'AMK_bQuitDcOn', 'AMK_bDcOn', 'AMK_bQuitInverterOn', 'AMK_bInverterOn', 'AMK_bDerating', 'AMK_ActualVelocity (rpm)', 'AMK_TorqueCurrent', 'AMK_MagnetizingCurrent'])
        writer = csv.writer(f_amk_actual_values2_fr)
        writer.writerow(['time', 'AMK_TempMotor (C)', 'AMK_TempInverter (C)', 'AMK_ErrorInfo', 'AMK_TempIGBT (C)'])
        writer = csv.writer(f_amk_set_point1_rr)
        writer.writerow(['time', 'AMK_bInverterOn', 'AMK_bDcOn', 'AMK_bEnable', 'AMK_bErrorReset', 'AMK_Torque_setpoint (Nm)', 'AMK_TorqueLimitPositv (Nm)', 'AMK_TorqueLimitNegativ (Nm)'])
        writer = csv.writer(f_amk_actual_values1_rr)
        writer.writerow(['time', 'AMK_bSystemReady', 'AMK_bError', 'AMK_bWarn', 'AMK_bQuitDcOn', 'AMK_bDcOn', 'AMK_bQuitInverterOn', 'AMK_bInverterOn', 'AMK_bDerating', 'AMK_ActualVelocity (rpm)', 'AMK_TorqueCurrent', 'AMK_MagnetizingCurrent'])
        writer = csv.writer(f_amk_actual_values2_rr)
        writer.writerow(['time', 'AMK_TempMotor (C)', 'AMK_TempInverter (C)', 'AMK_ErrorInfo', 'AMK_TempIGBT (C)'])
        writer = csv.writer(f_steering_and_pedal)
        writer.writerow(['time', 'steering_angle (\u00B0)', 'apps (%)', 'bpps (%)', 'brake_pressure0 (bar)', 'brake_pressure1 (bar)'])
        writer = csv.writer(f_gear_temp)
        writer.writerow(['time', 'fl_temp (C)', 'fr_temp (C)', 'rl_temp (C)', 'rr_temp (C)'])
        writer = csv.writer(f_front_shock)
        writer.writerow(['time', 'left_roll (\u00B0)', 'right_roll (\u00B0)'])
        writer = csv.writer(f_rear_shock)
        writer.writerow(['time', 'left_roll (\u00B0)', 'right_roll (\u00B0)'])

        files = os.listdir(file_src)
        
        time = 0

        for file in files:
            f = open(file_src + file)
            lines = csv.reader(f)
            
            for line in lines:
                if len(line) < 4:
                    continue
                
                if len(line[0]) < 4:
                    continue
                
                time += (int(line[0], 16) / 10)
                
                if line[3] == '00000001':
                    if len(line) < 12:
                        continue
                    year = int(line[4], 16)
                    month = int(line[5], 16)
                    day = int(line[6], 16)
                    hour = int(line[7], 16)
                    minute = int(line[8], 16)
                    second = int(line[9], 16)
                    tenthms = int(line[10], 16)
                    writer = csv.writer(f_utc)
                    writer.writerow([year, month, day, hour, minute, second, tenthms])
                if line[3] == '00000120':
                    if len(line) < 5:
                        continue
                    error_code = int(line[4], 16)
                    writer = csv.writer(f_imu_error)
                    writer.writerow([time, error_code])
                if line[3] == '00000130':
                    if len(line) < 12:
                        continue
                if line[3] == '00000220':
                    if len(line) < 8:
                        continue
                    status_word = int(line[4] + line[5] + line[6] + line[7], 16)
                    writer = csv.writer(f_imu_status)
                    writer.writerow([time, status_word])
                if line[3] == '00000230':
                    if len(line) < 12:
                        continue
                if line[3] == '00000300':
                    if len(line) < 12:
                        continue
                    current = int(line[5] + line[4], 16)
                    if current > 32767:
                        current -= 65536
                    current /= 10
                    voltage = int(line[7] + line[6], 16)
                    voltage /= 10
                    ccl = int(line[9] + line[8], 16)
                    dcl = int(line[11] + line[10], 16)
                    writer = csv.writer(f_pack_power)
                    writer.writerow([time, current, voltage, ccl, dcl])
                if line[3] == '00000320':
                    if len(line) < 10:
                        continue
                    acc_x = int(line[4] + line[5], 16)
                    if acc_x > 32767:
                        acc_x -= 65536
                    acc_x /= 2^8
                    acc_y = int(line[6] + line[7], 16)
                    if acc_y > 32767:
                        acc_y -= 65536
                    acc_y /= 2^8
                    acc_z = int(line[8] + line[9], 16)
                    if acc_z > 32767:
                        acc_z -= 65536
                    acc_z /= 2^8
                    writer = csv.writer(f_free_acc)
                    writer.writerow([time, acc_x, acc_y, acc_z])
                if line[3] == '00000321':
                    if len(line) < 10:
                        continue
                    gyr_x = int(line[4] + line[5], 16)
                    if gyr_x > 32767:
                        gyr_x -= 65536
                    gyr_x /= 2^9
                    gyr_y = int(line[6] + line[7], 16)
                    if gyr_y > 32767:
                        gyr_y -= 65536
                    gyr_y /= 2^9
                    gyr_z = int(line[8] + line[9], 16)
                    if gyr_z > 32767:
                        gyr_z -= 65536
                    gyr_z /= 2^9
                    writer = csv.writer(f_gry_hr)
                    writer.writerow([time, gyr_x, gyr_y, gyr_z])
                if line[3] == '00000322':
                    if len(line) < 10:
                        continue
                    vel_x = int(line[4] + line[5], 16)
                    if vel_x > 32767:
                        vel_x -= 65536
                    vel_x /= 2^6
                    vel_y = int(line[6] + line[7], 16)
                    if vel_y > 32767:
                        vel_y -= 65536
                    vel_y /= 2^6
                    vel_z = int(line[8] + line[9], 16)
                    if vel_z > 32767:
                        vel_z -= 65536
                    vel_z /= 2^6
                    writer = csv.writer(f_velocity)
                    writer.writerow([time, vel_x, vel_y, vel_z])
                if line[3] == '00000323':
                    if len(line) < 10:
                        continue
                    roll = int(line[4] + line[5], 16)
                    if roll > 32767:
                        roll -= 65536
                    roll /= 2^7
                    pitch = int(line[6] + line[7], 16)
                    if pitch > 32767:
                        pitch -= 65536
                    pitch /= 2^7
                    yaw = int(line[8] + line[9], 16)
                    if yaw > 32767:
                        yaw -= 65536
                    yaw /= 2^7
                    writer = csv.writer(f_euler_angle)
                    writer.writerow([time, roll, pitch, yaw])
                if line[3] == '00000420':
                    if len(line) < 10:
                        continue
                    acc_x = int(line[4] + line[5], 16)
                    if acc_x > 32767:
                        acc_x -= 65536
                    acc_x /= 2^8
                    acc_y = int(line[6] + line[7], 16)
                    if acc_y > 32767:
                        acc_y -= 65536
                    acc_y /= 2^8
                    acc_z = int(line[8] + line[9], 16)
                    if acc_z > 32767:
                        acc_z -= 65536
                    acc_z /= 2^8
                    writer = csv.writer(f_acc_hr)
                    writer.writerow([time, acc_x, acc_y, acc_z])
                if line[3] == '00000421':
                    if len(line) < 12:
                        continue
                    lat = int(line[4] + line[5] + line[6] + line[7], 16)
                    if lat > 2147483647:
                        lat -= 4294967296
                    lat /= 2^24
                    lon = int(line[8] + line[9] + line[10] + line[11], 16)
                    if lon > 2147483647:
                        lon -= 4294967296
                    lon /= 2^24
                    writer = csv.writer(f_coordinate)
                    writer.writerow([time, lat, lon])
                if line[3] == '00000422':
                    if len(line) < 8:
                        continue
                    alt_ellipsoid = int(line[4] + line[5] + line[6] + line[7], 16)
                    if alt_ellipsoid > 2147483647:
                        alt_ellipsoid -= 4294967296
                    alt_ellipsoid /= 2^15
                    writer = csv.writer(f_altitude)
                    writer.writerow([time, alt_ellipsoid])
                if line[3] == '00020000':
                    if len(line) < 12:
                        continue
                    failsafe_status = int(line[5] + line[4], 16)
                    dtc_status1 = int(line[7] + line[6], 16)
                    dtc_status2 = int(line[9] + line[8], 16)
                    cl_status = int(line[11] + line[10], 16)
                    writer = csv.writer(f_pack_status)
                    writer.writerow([time, failsafe_status, dtc_status1, dtc_status2, cl_status])
                if line[3] == '00040000':
                    if len(line) < 12:
                        continue
                    highest_cv_id = int(line[4], 16)
                    highest_cv = int(line[6] + line[5], 16)
                    average_cv = int(line[8] + line[7], 16)
                    lowest_cv_id = int(line[9], 16)
                    lowest_cv = int(line[11] + line[10], 16)
                    writer = csv.writer(f_pack_cv)
                    writer.writerow([time, highest_cv_id, highest_cv, average_cv, lowest_cv_id, lowest_cv])
                if line[3] == '00040001':
                    if len(line) < 12:
                        continue
                    highest_ocv_id = int(line[4], 16)
                    highest_ocv = int(line[6] + line[5], 16)
                    highest_ocv /= 10000
                    average_ocv = int(line[8] + line[7], 16)
                    average_ocv /= 10000
                    lowest_ocv_id = int(line[9], 16)
                    lowest_ocv = int(line[11] + line[10], 16)
                    lowest_ocv /= 10000
                    writer = csv.writer(f_pack_ocv)
                    writer.writerow([time, highest_ocv_id, highest_ocv, average_ocv, lowest_ocv_id, lowest_ocv])
                if line[3] == '00040002':
                    if len(line) < 12:
                        continue
                    highest_temp_id = int(line[4], 16)
                    highest_temp = int(line[5], 16)
                    average_temp = int(line[6], 16)
                    lowest_temp_id = int(line[7], 16)
                    lowest_temp = int(line[8], 16)
                    resistance = int(line[10] + line[9], 16)
                    writer = csv.writer(f_pack_temp)
                    writer.writerow([time, highest_temp_id, highest_temp, average_temp, lowest_temp_id, lowest_temp, resistance])
                if line[3] == '00040003':
                    if len(line) < 12:
                        continue
                    soc = int(line[4], 16)
                    soc /= 2
                    adaptive_soc = int(line[5], 16)
                    adaptive_soc /= 2
                    adaptive_tot_cap = int(line[7] + line[6], 16)
                    adaptive_tot_cap /= 10
                    open_voltage = int(line[9] + line[8], 16)
                    open_voltage /= 10
                    writer = csv.writer(f_pack_soc)
                    writer.writerow([time, soc, adaptive_soc, adaptive_tot_cap, open_voltage])
                if line[3] == '00040100':
                    if len(line) < 12:
                        continue
                    amk_control = int(line[5], 16)
                    amk_b_inverter_on = (amk_control) & 0b1
                    amk_b_dc_on = (amk_control >> 1) & 0b1
                    amk_b_enable = (amk_control >> 2) & 0b1
                    amk_b_error_reset = (amk_control >> 3) & 0b1
                    amk_torque_setpoint = int(line[7] + line[6], 16)
                    if amk_torque_setpoint > 32767:
                        amk_torque_setpoint -= 65536
                    amk_torque_setpoint /= 100
                    amk_torque_limit_positv = int(line[9] + line[8], 16)
                    if amk_torque_limit_positv > 32767:
                        amk_torque_limit_positv -= 65536
                    amk_torque_limit_positv /= 100
                    amk_torque_limit_negativ = int(line[11] + line[10], 16)
                    if amk_torque_limit_negativ > 32767:
                        amk_torque_limit_negativ -= 65536
                    amk_torque_limit_negativ /= 100
                    writer = csv.writer(f_amk_set_point1_rl)
                    writer.writerow([time, amk_b_inverter_on, amk_b_dc_on, amk_b_enable, amk_b_error_reset, amk_torque_setpoint, amk_torque_limit_positv, amk_torque_limit_negativ])
                if line[3] == '00040101':
                    if len(line) < 12:
                        continue
                    amk_status = int(line[5], 16)
                    amk_b_system_ready = (amk_status) & 0b1
                    amk_b_error = (amk_status >> 1) & 0b1
                    amk_b_warn = (amk_status >> 2) & 0b1
                    amk_b_quit_dc_on = (amk_status >> 3) & 0b1
                    amk_b_dc_on = (amk_status >> 4) & 0b1
                    amk_b_quit_inverter_on = (amk_status >> 5) & 0b1
                    amk_b_inverter_on = (amk_status >> 6) & 0b1
                    amk_b_derating = (amk_status >> 7) & 0b1
                    amk_actual_velocity = int(line[7] + line[6], 16)
                    if amk_actual_velocity > 32767:
                        amk_actual_velocity -= 65536
                    amk_torque_current = int(line[9] + line[8], 16)
                    if amk_torque_current > 32767:
                        amk_torque_current -= 65536
                    amk_magnetizing_current = int(line[11] + line[10], 16)
                    if amk_magnetizing_current > 32767:
                        amk_magnetizing_current -= 65536
                    writer = csv.writer(f_amk_actual_values1_rl)
                    writer.writerow([time, amk_b_system_ready, amk_b_error, amk_b_warn, amk_b_quit_dc_on, amk_b_dc_on, amk_b_quit_inverter_on, amk_b_inverter_on, amk_b_derating, amk_actual_velocity, amk_torque_current, amk_magnetizing_current])
                if line[3] == '00040102':
                    if len(line) < 12:
                        continue
                    amk_temp_motor = int(line[5] + line[4], 16)
                    if amk_temp_motor > 32767:
                        amk_temp_motor -= 65536
                    amk_temp_motor /= 10
                    amk_temp_inverter = int(line[7] + line[6], 16)
                    if amk_temp_inverter > 32767:
                        amk_temp_inverter -= 65536
                    amk_temp_inverter /= 10
                    amk_error_info = int(line[9] + line[8], 16)
                    amk_temp_igbt = int(line[11] + line[10], 16)
                    if amk_temp_igbt > 32767:
                        amk_temp_igbt -= 65536
                    amk_temp_igbt /= 10
                    writer = csv.writer(f_amk_actual_values2_rl)
                    writer.writerow([time, amk_temp_motor, amk_temp_inverter, amk_error_info, amk_temp_igbt])
                if line[3] == '00040103':
                    if len(line) < 12:
                        continue
                    amk_control = int(line[5], 16)
                    amk_b_inverter_on = (amk_control) & 0b1
                    amk_b_dc_on = (amk_control >> 1) & 0b1
                    amk_b_enable = (amk_control >> 2) & 0b1
                    amk_b_error_reset = (amk_control >> 3) & 0b1
                    amk_torque_setpoint = int(line[7] + line[6], 16)
                    if amk_torque_setpoint > 32767:
                        amk_torque_setpoint -= 65536
                    amk_torque_setpoint /= 100
                    amk_torque_limit_positv = int(line[9] + line[8], 16)
                    if amk_torque_limit_positv > 32767:
                        amk_torque_limit_positv -= 65536
                    amk_torque_limit_positv /= 100
                    amk_torque_limit_negativ = int(line[11] + line[10], 16)
                    if amk_torque_limit_negativ > 32767:
                        amk_torque_limit_negativ -= 65536
                    amk_torque_limit_negativ /= 100
                    writer = csv.writer(f_amk_set_point1_fl)
                    writer.writerow([time, amk_b_inverter_on, amk_b_dc_on, amk_b_enable, amk_b_error_reset, amk_torque_setpoint, amk_torque_limit_positv, amk_torque_limit_negativ])
                if line[3] == '00040104':
                    if len(line) < 12:
                        continue
                    amk_status = int(line[5], 16)
                    amk_b_system_ready = (amk_status) & 0b1
                    amk_b_error = (amk_status >> 1) & 0b1
                    amk_b_warn = (amk_status >> 2) & 0b1
                    amk_b_quit_dc_on = (amk_status >> 3) & 0b1
                    amk_b_dc_on = (amk_status >> 4) & 0b1
                    amk_b_quit_inverter_on = (amk_status >> 5) & 0b1
                    amk_b_inverter_on = (amk_status >> 6) & 0b1
                    amk_b_derating = (amk_status >> 7) & 0b1
                    amk_actual_velocity = int(line[7] + line[6], 16)
                    if amk_actual_velocity > 32767:
                        amk_actual_velocity -= 65536
                    amk_torque_current = int(line[9] + line[8], 16)
                    if amk_torque_current > 32767:
                        amk_torque_current -= 65536
                    amk_magnetizing_current = int(line[11] + line[10], 16)
                    if amk_magnetizing_current > 32767:
                        amk_magnetizing_current -= 65536
                    writer = csv.writer(f_amk_actual_values1_fl)
                    writer.writerow([time, amk_b_system_ready, amk_b_error, amk_b_warn, amk_b_quit_dc_on, amk_b_dc_on, amk_b_quit_inverter_on, amk_b_inverter_on, amk_b_derating, amk_actual_velocity, amk_torque_current, amk_magnetizing_current])
                if line[3] == '00040105':
                    if len(line) < 12:
                        continue
                    amk_temp_motor = int(line[5] + line[4], 16)
                    if amk_temp_motor > 32767:
                        amk_temp_motor -= 65536
                    amk_temp_motor /= 10
                    amk_temp_inverter = int(line[7] + line[6], 16)
                    if amk_temp_inverter > 32767:
                        amk_temp_inverter -= 65536
                    amk_temp_inverter /= 10
                    amk_error_info = int(line[9] + line[8], 16)
                    amk_temp_igbt = int(line[11] + line[10], 16)
                    if amk_temp_igbt > 32767:
                        amk_temp_igbt -= 65536
                    amk_temp_igbt /= 10
                    writer = csv.writer(f_amk_actual_values2_fl)
                    writer.writerow([time, amk_temp_motor, amk_temp_inverter, amk_error_info, amk_temp_igbt])
                if line[3] == '00040106':
                    if len(line) < 12:
                        continue
                    amk_control = int(line[5], 16)
                    amk_b_inverter_on = (amk_control) & 0b1
                    amk_b_dc_on = (amk_control >> 1) & 0b1
                    amk_b_enable = (amk_control >> 2) & 0b1
                    amk_b_error_reset = (amk_control >> 3) & 0b1
                    amk_torque_setpoint = int(line[7] + line[6], 16)
                    if amk_torque_setpoint > 32767:
                        amk_torque_setpoint -= 65536
                    amk_torque_setpoint /= 100
                    amk_torque_limit_positv = int(line[9] + line[8], 16)
                    if amk_torque_limit_positv > 32767:
                        amk_torque_limit_positv -= 65536
                    amk_torque_limit_positv /= 100
                    amk_torque_limit_negativ = int(line[11] + line[10], 16)
                    if amk_torque_limit_negativ > 32767:
                        amk_torque_limit_negativ -= 65536
                    amk_torque_limit_negativ /= 100
                    writer = csv.writer(f_amk_set_point1_fr)
                    writer.writerow([time, amk_b_inverter_on, amk_b_dc_on, amk_b_enable, amk_b_error_reset, amk_torque_setpoint, amk_torque_limit_positv, amk_torque_limit_negativ])
                if line[3] == '00040107':
                    if len(line) < 12:
                        continue
                    amk_status = int(line[5], 16)
                    amk_b_system_ready = (amk_status) & 0b1
                    amk_b_error = (amk_status >> 1) & 0b1
                    amk_b_warn = (amk_status >> 2) & 0b1
                    amk_b_quit_dc_on = (amk_status >> 3) & 0b1
                    amk_b_dc_on = (amk_status >> 4) & 0b1
                    amk_b_quit_inverter_on = (amk_status >> 5) & 0b1
                    amk_b_inverter_on = (amk_status >> 6) & 0b1
                    amk_b_derating = (amk_status >> 7) & 0b1
                    amk_actual_velocity = int(line[7] + line[6], 16)
                    if amk_actual_velocity > 32767:
                        amk_actual_velocity -= 65536
                    amk_torque_current = int(line[9] + line[8], 16)
                    if amk_torque_current > 32767:
                        amk_torque_current -= 65536
                    amk_magnetizing_current = int(line[11] + line[10], 16)
                    if amk_magnetizing_current > 32767:
                        amk_magnetizing_current -= 65536
                    writer = csv.writer(f_amk_actual_values1_fr)
                    writer.writerow([time, amk_b_system_ready, amk_b_error, amk_b_warn, amk_b_quit_dc_on, amk_b_dc_on, amk_b_quit_inverter_on, amk_b_inverter_on, amk_b_derating, amk_actual_velocity, amk_torque_current, amk_magnetizing_current])
                if line[3] == '00040108':
                    if len(line) < 12:
                        continue
                    amk_temp_motor = int(line[5] + line[4], 16)
                    if amk_temp_motor > 32767:
                        amk_temp_motor -= 65536
                    amk_temp_motor /= 10
                    amk_temp_inverter = int(line[7] + line[6], 16)
                    if amk_temp_inverter > 32767:
                        amk_temp_inverter -= 65536
                    amk_temp_inverter /= 10
                    amk_error_info = int(line[9] + line[8], 16)
                    amk_temp_igbt = int(line[11] + line[10], 16)
                    if amk_temp_igbt > 32767:
                        amk_temp_igbt -= 65536
                    amk_temp_igbt /= 10
                    writer = csv.writer(f_amk_actual_values2_fr)
                    writer.writerow([time, amk_temp_motor, amk_temp_inverter, amk_error_info, amk_temp_igbt])
                if line[3] == '00040109':
                    if len(line) < 12:
                        continue
                    amk_control = int(line[5], 16)
                    amk_b_inverter_on = (amk_control) & 0b1
                    amk_b_dc_on = (amk_control >> 1) & 0b1
                    amk_b_enable = (amk_control >> 2) & 0b1
                    amk_b_error_reset = (amk_control >> 3) & 0b1
                    amk_torque_setpoint = int(line[7] + line[6], 16)
                    if amk_torque_setpoint > 32767:
                        amk_torque_setpoint -= 65536
                    amk_torque_setpoint /= 100
                    amk_torque_limit_positv = int(line[9] + line[8], 16)
                    if amk_torque_limit_positv > 32767:
                        amk_torque_limit_positv -= 65536
                    amk_torque_limit_positv /= 100
                    amk_torque_limit_negativ = int(line[11] + line[10], 16)
                    if amk_torque_limit_negativ > 32767:
                        amk_torque_limit_negativ -= 65536
                    amk_torque_limit_negativ /= 100
                    writer = csv.writer(f_amk_set_point1_rr)
                    writer.writerow([time, amk_b_inverter_on, amk_b_dc_on, amk_b_enable, amk_b_error_reset, amk_torque_setpoint, amk_torque_limit_positv, amk_torque_limit_negativ])
                if line[3] == '0004010A':
                    if len(line) < 12:
                        continue
                    amk_status = int(line[5], 16)
                    amk_b_system_ready = (amk_status) & 0b1
                    amk_b_error = (amk_status >> 1) & 0b1
                    amk_b_warn = (amk_status >> 2) & 0b1
                    amk_b_quit_dc_on = (amk_status >> 3) & 0b1
                    amk_b_dc_on = (amk_status >> 4) & 0b1
                    amk_b_quit_inverter_on = (amk_status >> 5) & 0b1
                    amk_b_inverter_on = (amk_status >> 6) & 0b1
                    amk_b_derating = (amk_status >> 7) & 0b1
                    amk_actual_velocity = int(line[7] + line[6], 16)
                    if amk_actual_velocity > 32767:
                        amk_actual_velocity -= 65536
                    amk_torque_current = int(line[9] + line[8], 16)
                    if amk_torque_current > 32767:
                        amk_torque_current -= 65536
                    amk_magnetizing_current = int(line[11] + line[10], 16)
                    if amk_magnetizing_current > 32767:
                        amk_magnetizing_current -= 65536
                    writer = csv.writer(f_amk_actual_values1_rr)
                    writer.writerow([time, amk_b_system_ready, amk_b_error, amk_b_warn, amk_b_quit_dc_on, amk_b_dc_on, amk_b_quit_inverter_on, amk_b_inverter_on, amk_b_derating, amk_actual_velocity, amk_torque_current, amk_magnetizing_current])
                if line[3] == '0004010B':
                    if len(line) < 12:
                        continue
                    amk_temp_motor = int(line[5] + line[4], 16)
                    if amk_temp_motor > 32767:
                        amk_temp_motor -= 65536
                    amk_temp_motor /= 10
                    amk_temp_inverter = int(line[7] + line[6], 16)
                    if amk_temp_inverter > 32767:
                        amk_temp_inverter -= 65536
                    amk_temp_inverter /= 10
                    amk_error_info = int(line[9] + line[8], 16)
                    amk_temp_igbt = int(line[11] + line[10], 16)
                    if amk_temp_igbt > 32767:
                        amk_temp_igbt -= 65536
                    amk_temp_igbt /= 10
                    writer = csv.writer(f_amk_actual_values2_rr)
                    writer.writerow([time, amk_temp_motor, amk_temp_inverter, amk_error_info, amk_temp_igbt])
                if line[3] == '00040300':
                    if len(line) < 12:
                        continue
                    steering_angle = int(line[5] + line[4], 16)
                    if steering_angle > 32767:
                        steering_angle -= 65536
                    steering_angle /= 100
                    apps = int(line[6], 16)
                    bpps = int(line[7], 16)
                    brake_pressure0 = int(line[8] + line[9], 16)
                    brake_pressure0 /= 10
                    brake_pressure1 = int(line[10] + line[11], 16)
                    brake_pressure1 /= 10
                    writer = csv.writer(f_steering_and_pedal)
                    writer.writerow([time, steering_angle, apps, bpps, brake_pressure0, brake_pressure1])
                if line[3] == '00040301':
                    if len(line) < 12:
                        continue
                    fl_temp = int(line[5] + line[4], 16)
                    fr_temp = int(line[7] + line[6], 16)
                    rl_temp = int(line[9] + line[8], 16)
                    rr_temp = int(line[11] + line[10], 16)
                    writer = csv.writer(f_gear_temp)
                    writer.writerow([time, fl_temp, fr_temp, rl_temp, rr_temp])
                if line[3] == '00040302':
                    if len(line) < 12:
                        continue
                    left_roll = int(line[5] + line[4], 16)
                    if left_roll > 32767:
                        left_roll -= 65536
                    left_roll /= 100
                    right_roll = int(line[7] + line[6], 16)
                    if right_roll > 32767:
                        right_roll -= 65536
                    right_roll /= 100
                    writer = csv.writer(f_front_shock)
                    writer.writerow([time, left_roll, right_roll])
                if line[3] == '00040303':
                    if len(line) < 12:
                        continue
                    left_roll = int(line[5] + line[4], 16)
                    if left_roll > 32767:
                        left_roll -= 65536
                    left_roll /= 100
                    right_roll = int(line[7] + line[6], 16)
                    if right_roll > 32767:
                        right_roll -= 65536
                    right_roll /= 100
                    writer = csv.writer(f_rear_shock)
                    writer.writerow([time, left_roll, right_roll])

        f_utc.close()
        f_imu_error.close()
        f_imu_status.close()
        f_pack_power.close()
        f_free_acc.close()
        f_gry_hr.close()
        f_velocity.close()
        f_euler_angle.close()
        f_acc_hr.close()
        f_coordinate.close()
        f_altitude.close()
        f_pack_status.close()
        f_pack_cv.close()
        f_pack_ocv.close()
        f_pack_temp.close()
        f_pack_soc.close()
        f_amk_set_point1_rl.close()
        f_amk_actual_values1_rl.close()
        f_amk_actual_values2_rl.close()
        f_amk_set_point1_fl.close()
        f_amk_actual_values1_fl.close()
        f_amk_actual_values2_fl.close()
        f_amk_set_point1_fr.close()
        f_amk_actual_values1_fr.close()
        f_amk_actual_values2_fr.close()
        f_amk_set_point1_rr.close()
        f_amk_actual_values1_rr.close()
        f_amk_actual_values2_rr.close()
        f_steering_and_pedal.close()
        f_gear_temp.close()
        f_front_shock.close()
        f_rear_shock.close()
    
print('end')