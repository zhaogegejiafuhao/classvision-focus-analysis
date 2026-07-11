<template>
    <div class="component-1_1157">
        <div id="1_1157" class="Pixso-symbol-1_1157">
            <div
                id="1_1158"
                class="Pixso-symbol-1_1158"
                v-if="Style === 'Filled'"
            >
                <slot name="slot_1_1163">
                    <div id="1_1163" class="Pixso-vector-1_1163"></div>
                </slot>
            </div>
            <div
                id="1_1159"
                class="Pixso-symbol-1_1159"
                v-if="Style === 'Outlined'"
            >
                <slot name="slot_1_1164">
                    <div id="1_1164" class="Pixso-vector-1_1164"></div>
                </slot>
            </div>
            <div
                id="1_1160"
                class="Pixso-symbol-1_1160"
                v-if="Style === 'Round'"
            >
                <slot name="slot_1_1165">
                    <div id="1_1165" class="Pixso-vector-1_1165"></div>
                </slot>
            </div>
            <div
                id="1_1161"
                class="Pixso-symbol-1_1161"
                v-if="Style === 'Sharp'"
            >
                <slot name="slot_1_1166">
                    <div id="1_1166" class="Pixso-vector-1_1166"></div>
                </slot>
            </div>
            <div
                id="1_1162"
                class="Pixso-symbol-1_1162"
                v-if="Style === 'Two Tone'"
            >
                <slot name="slot_1_1167">
                    <div id="1_1167" class="Pixso-vector-1_1167"></div>
                </slot>
                <slot name="slot_1_1168">
                    <div id="1_1168" class="Pixso-vector-1_1168"></div>
                </slot>
                <slot name="slot_1_1169">
                    <div id="1_1169" class="Pixso-vector-1_1169"></div>
                </slot>
                <slot name="slot_1_1170">
                    <div id="1_1170" class="Pixso-vector-1_1170"></div>
                </slot>
                <slot name="slot_1_1171">
                    <div id="1_1171" class="Pixso-vector-1_1171"></div>
                </slot>
            </div>
        </div>
    </div>
</template>
<script lang="ts" setup>
const props = defineProps({
    Style: { type: String }
});
</script>
<style>
.Pixso-symbol-1_1157 {
}
.Pixso-symbol-1_1158 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-1_1163 {
    width: 83.34%;
    height: 83.34%;
    background-image: url(@/assets/images/Vector7.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 8.33%;
    right: 8.33%;
    top: 8.33%;
    bottom: 8.33%;
}
.Pixso-symbol-1_1159 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-1_1164 {
    width: 83.34%;
    height: 83.34%;
    background-image: url(@/assets/images/Vector6.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 8.33%;
    right: 8.33%;
    top: 8.33%;
    bottom: 8.33%;
}
.Pixso-symbol-1_1160 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-1_1165 {
    width: 83.34%;
    height: 83.34%;
    background-image: url(@/assets/images/Vector5.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 8.33%;
    right: 8.33%;
    top: 8.33%;
    bottom: 8.33%;
}
.Pixso-symbol-1_1161 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-1_1166 {
    width: 83.34%;
    height: 83.34%;
    background-image: url(@/assets/images/Vector.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 8.33%;
    right: 8.33%;
    top: 8.33%;
    bottom: 8.33%;
}
.Pixso-symbol-1_1162 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-1_1167 {
    width: 66.66%;
    height: 66.66%;
    background-image: url(@/assets/images/Vector4.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 16.67%;
    right: 16.67%;
    top: 16.67%;
    bottom: 16.67%;
}
.Pixso-vector-1_1168 {
    width: 12.5%;
    height: 12.5%;
    background-image: url(@/assets/images/Vector3.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 58.33%;
    right: 29.17%;
    top: 33.33%;
    bottom: 54.17%;
}
.Pixso-vector-1_1169 {
    width: 83.34%;
    height: 83.34%;
    background-image: url(@/assets/images/Vector2.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 8.33%;
    right: 8.33%;
    top: 8.33%;
    bottom: 8.33%;
}
.Pixso-vector-1_1170 {
    width: 12.5%;
    height: 12.5%;
    background-image: url(@/assets/images/Vector0.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 29.17%;
    right: 58.33%;
    top: 33.33%;
    bottom: 54.17%;
}
.Pixso-vector-1_1171 {
    width: 42.58%;
    height: 14.59%;
    background-image: url(@/assets/images/Vector1.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 28.71%;
    right: 28.71%;
    top: 58.33%;
    bottom: 27.08%;
}
</style>
