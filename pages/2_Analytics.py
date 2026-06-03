import streamlit as st
from utils import dataset_distribution_chart, training_history_chart

st.title('Dataset Analytics')
st.caption('Overview of the data used to train CocoaGuard GH')
st.divider()

st.subheader('Dataset Distribution')

col1, col2, col3 = st.columns(3)
with col1:
    st.metric('Total Images', '5,360')
with col2:
    st.metric('CSSVD Images', '2,491')
with col3:
    st.metric('Healthy Images', '2,869')

fig = dataset_distribution_chart(2491, 2869)
st.plotly_chart(fig, use_container_width=True)

st.divider()

st.subheader('Training History')

tab1, tab2 = st.tabs(['Phase 1 — Head Training', 'Phase 2 — Fine Tuning'])

with tab1:
    train_acc_1 = [0.6396, 0.7127, 0.7438, 0.7559, 0.7654, 0.7836,
                0.7947, 0.7907, 0.8053, 0.8043, 0.8111, 0.8025,
                0.8103, 0.8204, 0.8174, 0.8179, 0.8267, 0.8219,
                0.8252, 0.8356, 0.8315]

    val_acc_1 =   [0.7161, 0.7727, 0.7986, 0.8163, 0.8280, 0.8351,
                0.8292, 0.8410, 0.8386, 0.8351, 0.8386, 0.8386,
                0.8410, 0.8469, 0.8457, 0.8516, 0.8386, 0.8363,
                0.8398, 0.8398, 0.8398]

    train_loss_1 = [0.6931, 0.5817, 0.5240, 0.5002, 0.4853, 0.4557,
                    0.4387, 0.4397, 0.4191, 0.4212, 0.4150, 0.4178,
                    0.4032, 0.3983, 0.4016, 0.4005, 0.3960, 0.3780,
                    0.3774, 0.3649, 0.3748]

    val_loss_1 =  [0.5656, 0.4862, 0.4420, 0.4201, 0.4032, 0.3938,
                0.3817, 0.3790, 0.3703, 0.3720, 0.3647, 0.3855,
                0.3710, 0.3642, 0.3766, 0.3651, 0.3800, 0.3747,
                0.3729, 0.3696, 0.3681]
    
    fig_acc = training_history_chart('Accuracy', train_acc_1, val_acc_1)
    st.plotly_chart(fig_acc, use_container_width=True)

    fig_loss = training_history_chart('Loss', train_loss_1, val_loss_1)
    st.plotly_chart(fig_loss, use_container_width=True)    

with tab2:
    train_acc_2 = [0.8172, 0.8290, 0.8371, 0.8308, 0.8411, 0.8411,
                0.8431, 0.8487, 0.8494, 0.8545, 0.8552, 0.8575,
                0.8638, 0.8608, 0.8603, 0.8583, 0.8575]

    val_acc_2 =   [0.8481, 0.8469, 0.8504, 0.8410, 0.8504, 0.8504,
                0.8528, 0.8504, 0.8504, 0.8539, 0.8516, 0.8492,
                0.8528, 0.8539, 0.8539, 0.8539, 0.8539]

    train_loss_2 = [0.3952, 0.3802, 0.3702, 0.3655, 0.3584, 0.3496,
                    0.3517, 0.3396, 0.3397, 0.3344, 0.3249, 0.3281,
                    0.3203, 0.3254, 0.3207, 0.3172, 0.3160]

    val_loss_2 =  [0.3591, 0.3616, 0.3496, 0.3663, 0.3472, 0.3552,
                0.3390, 0.3552, 0.3494, 0.3368, 0.3577, 0.3681,
                0.3487, 0.3498, 0.3497, 0.3502, 0.3466]
    
    fig_acc_2 = training_history_chart('Accuracy', train_acc_2, val_acc_2)
    st.plotly_chart(fig_acc_2, use_container_width=True)

    fig_loss_2 = training_history_chart('Loss', train_loss_2, val_loss_2)
    st.plotly_chart(fig_loss_2, use_container_width=True)
