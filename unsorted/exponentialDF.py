import pandas as pd
import numpy as np

T_SIZE = 2100
OP_SUREK_1_PKT_kestirim_hb_kestirim_gyro_mrad_s_s16 = []
OP_SUREK_1_PKT_kestirim_hb_kestirim_ivme_cm_s2_s16 = []
times = np.linspace(start=0, stop=T_SIZE - 1, num=T_SIZE, dtype=np.int32)

OP_SUREK_1_PKT_kestirim_hb_kestirim_ivme_cm_s2_s16.append(np.random.random(T_SIZE))
OP_SUREK_1_PKT_kestirim_hb_kestirim_ivme_cm_s2_s16.append(np.random.random(T_SIZE))
OP_SUREK_1_PKT_kestirim_hb_kestirim_ivme_cm_s2_s16.append(np.random.random(T_SIZE))
OP_SUREK_1_PKT_kestirim_hb_kestirim_gyro_mrad_s_s16.append(np.random.random(T_SIZE))
OP_SUREK_1_PKT_kestirim_hb_kestirim_gyro_mrad_s_s16.append(np.random.random(T_SIZE))
OP_SUREK_1_PKT_kestirim_hb_kestirim_gyro_mrad_s_s16.append(np.random.random(T_SIZE))
OP_SUREK_1_PKT_sensor_hb_pab_alfa_mrad_s16 = np.random.random(T_SIZE)
OP_SUREK_1_PKT_sensor_hb_pab_beta_mrad_s16 = np.random.random(T_SIZE)
OP_SUREK_1_PKT_sensor_hb_pab_pitot_pa_s16 = np.random.random(T_SIZE)
OP_SUREK_1_PKT_kestirim_hb_kestirim_yatis_mrad_s16 = np.random.random(T_SIZE)
OP_SUREK_1_PKT_kestirim_hb_kestirim_dikilme_mrad_s16 = np.random.random(T_SIZE)
OP_SUREK_1_PKT_kestirim_hb_kestirim_bas_mrad_u16 = np.random.random(T_SIZE)
OP_SUREK_1_PKT_kestirim_hb_kestirim_alfa_mrad_s16 = np.random.random(T_SIZE)
OP_SUREK_1_PKT_kestirim_hb_kestirim_beta_mrad_s16 = np.random.random(T_SIZE)
OP_SUREK_1_PKT_kestirim_hb_kestirim_harman_dusey_hiz_cm_s_s16 = np.random.random(T_SIZE)
OP_SUREK_1_PKT_kestirim_hb_kestirim_hava_hizi_cm_s_u16 = np.random.random(T_SIZE)
OP_SUREK_1_PKT_kestirim_hb_kestirim_baro_irtifa_m_s16 = np.random.random(T_SIZE)
OP_SUREK_1_PKT_sensor_hb_radar_irtifa_dm_s16 = np.random.random(T_SIZE)
attitude = []

test = 0
j = 0
for i in range(T_SIZE):
    if i < T_SIZE / 4:
        test = test + int(np.power(i, 1.5))
        attitude.append(test)
        continue
    elif i > T_SIZE / 4 and i < T_SIZE / 2:
        attitude.append(test)
        # j = i
        continue
    else:
        if test - int(np.power(j, 1.45)) > 0:
            test = test - int(np.power(j, 1.45))
        else:
            test = 0
        attitude.append(test)
        j = j + 1
        continue


myData = {
    "OP_SUREK_1_PKT_kestirim_hb_kestirim_ivme_cm_s2_s16[0]": OP_SUREK_1_PKT_kestirim_hb_kestirim_ivme_cm_s2_s16[
        0
    ],
    "OP_SUREK_1_PKT_kestirim_hb_kestirim_ivme_cm_s2_s16[2]": OP_SUREK_1_PKT_kestirim_hb_kestirim_ivme_cm_s2_s16[
        1
    ],
    "OP_SUREK_1_PKT_kestirim_hb_kestirim_ivme_cm_s2_s16[1]": OP_SUREK_1_PKT_kestirim_hb_kestirim_ivme_cm_s2_s16[
        2
    ],
    "OP_SUREK_1_PKT_kestirim_hb_kestirim_gyro_mrad_s_s16[0]": OP_SUREK_1_PKT_kestirim_hb_kestirim_gyro_mrad_s_s16[
        0
    ],
    "OP_SUREK_1_PKT_kestirim_hb_kestirim_gyro_mrad_s_s16[1]": OP_SUREK_1_PKT_kestirim_hb_kestirim_gyro_mrad_s_s16[
        1
    ],
    "OP_SUREK_1_PKT_kestirim_hb_kestirim_gyro_mrad_s_s16[2]": OP_SUREK_1_PKT_kestirim_hb_kestirim_gyro_mrad_s_s16[
        2
    ],
    "OP_SUREK_1_PKT_sensor_hb_pab_alfa_mrad_s16": OP_SUREK_1_PKT_sensor_hb_pab_alfa_mrad_s16,
    "OP_SUREK_1_PKT_sensor_hb_pab_beta_mrad_s16": OP_SUREK_1_PKT_sensor_hb_pab_beta_mrad_s16,
    "OP_SUREK_1_PKT_sensor_hb_pab_pitot_pa_s16 ": OP_SUREK_1_PKT_sensor_hb_pab_pitot_pa_s16,
    "OP_SUREK_1_PKT_kestirim_hb_kestirim_yatis_mrad_s16": OP_SUREK_1_PKT_kestirim_hb_kestirim_yatis_mrad_s16,
    "OP_SUREK_1_PKT_kestirim_hb_kestirim_dikilme_mrad_s16": OP_SUREK_1_PKT_kestirim_hb_kestirim_dikilme_mrad_s16,
    "OP_SUREK_1_PKT_kestirim_hb_kestirim_bas_mrad_u16": OP_SUREK_1_PKT_kestirim_hb_kestirim_bas_mrad_u16,
    "OP_SUREK_1_PKT_kestirim_hb_kestirim_alfa_mrad_s16": OP_SUREK_1_PKT_kestirim_hb_kestirim_alfa_mrad_s16,
    "OP_SUREK_1_PKT_kestirim_hb_kestirim_beta_mrad_s16": OP_SUREK_1_PKT_kestirim_hb_kestirim_beta_mrad_s16,
    "OP_SUREK_1_PKT_kestirim_hb_kestirim_harman_dusey_hiz_cm_s_s16": OP_SUREK_1_PKT_kestirim_hb_kestirim_harman_dusey_hiz_cm_s_s16,
    "OP_SUREK_1_PKT_kestirim_hb_kestirim_hava_hizi_cm_s_u16": OP_SUREK_1_PKT_kestirim_hb_kestirim_hava_hizi_cm_s_u16,
    "OP_SUREK_1_PKT_kestirim_hb_kestirim_baro_irtifa_m_s16": OP_SUREK_1_PKT_kestirim_hb_kestirim_baro_irtifa_m_s16,
    "OP_SUREK_1_PKT_sensor_hb_radar_irtifa_dm_s16": OP_SUREK_1_PKT_sensor_hb_radar_irtifa_dm_s16,
    "OP_SUREK_1_PKT_sensor_hb_lazer_irtifa_dm_s16": attitude,
}
csvFile = pd.DataFrame(myData)
# print(csvFile.columns)
csvFile.to_csv("exponential2.csv", index=False)
print("Success.")
