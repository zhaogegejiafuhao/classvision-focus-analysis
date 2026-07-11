<template>
    <div class="component-5578_149150">
        <div id="5578_149150" class="Pixso-symbol-5578_149150">
            <div
                id="5578_149151"
                class="Pixso-symbol-5578_149151"
                v-if="Format === 'Outline' && Weight === 'Regular'"
            >
                <slot name="slot_5578_149152">
                    <div
                        id="5578_149152"
                        class="Pixso-vector-5578_149152"
                    ></div>
                </slot>
            </div>
            <div
                id="5578_149157"
                class="Pixso-symbol-5578_149157"
                v-if="Format === 'Outline' && Weight === 'Bold'"
            >
                <slot name="slot_5578_149158">
                    <div
                        id="5578_149158"
                        class="Pixso-vector-5578_149158"
                    ></div>
                </slot>
            </div>
            <div
                id="5578_149159"
                class="Pixso-symbol-5578_149159"
                v-if="Format === 'Outline' && Weight === 'Fill'"
            >
                <slot name="slot_5578_149160">
                    <div
                        id="5578_149160"
                        class="Pixso-vector-5578_149160"
                    ></div>
                </slot>
            </div>
        </div>
    </div>
</template>
<script lang="ts" setup>
const props = defineProps({
    Format: { type: String },
    Weight: { type: String }
});
</script>
<style>
.Pixso-symbol-5578_149150 {
}
.Pixso-symbol-5578_149151 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5578_149152 {
    width: 93.74%;
    height: 75.06%;
    background-image: url(@/assets/images/Vector23.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 3.13%;
    right: 3.13%;
    top: 12.47%;
    bottom: 12.47%;
}
.Pixso-symbol-5578_149157 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5578_149158 {
    width: 96.89%;
    height: 78.13%;
    background-image: url(@/assets/images/Vector21.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 1.55%;
    right: 1.56%;
    top: 10.9%;
    bottom: 10.97%;
}
.Pixso-symbol-5578_149159 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5578_149160 {
    width: 93.74%;
    height: 75.06%;
    background-image: url(@/assets/images/Vector22.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 3.13%;
    right: 3.13%;
    top: 12.47%;
    bottom: 12.47%;
}
</style>
