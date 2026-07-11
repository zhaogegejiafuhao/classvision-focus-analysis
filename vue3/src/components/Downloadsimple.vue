<template>
    <div class="component-5578_150229">
        <div id="5578_150229" class="Pixso-symbol-5578_150229">
            <div
                id="5578_150230"
                class="Pixso-symbol-5578_150230"
                v-if="Format === 'Outline' && Weight === 'Regular'"
            >
                <slot name="slot_5578_150231">
                    <div
                        id="5578_150231"
                        class="Pixso-vector-5578_150231"
                    ></div>
                </slot>
            </div>
            <div
                id="5578_150236"
                class="Pixso-symbol-5578_150236"
                v-if="Format === 'Outline' && Weight === 'Bold'"
            >
                <slot name="slot_5578_150237">
                    <div
                        id="5578_150237"
                        class="Pixso-vector-5578_150237"
                    ></div>
                </slot>
            </div>
            <div
                id="5578_150238"
                class="Pixso-symbol-5578_150238"
                v-if="Format === 'Outline' && Weight === 'Fill'"
            >
                <slot name="slot_5578_150239">
                    <div
                        id="5578_150239"
                        class="Pixso-vector-5578_150239"
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
.Pixso-symbol-5578_150229 {
}
.Pixso-symbol-5578_150230 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5578_150231 {
    width: 75%;
    height: 74.99%;
    background-image: url(@/assets/images/Vector83.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 9.38%;
    bottom: 15.63%;
}
.Pixso-symbol-5578_150236 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5578_150237 {
    width: 78.12%;
    height: 78.13%;
    background-image: url(@/assets/images/Vector81.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 7.81%;
    bottom: 14.06%;
}
.Pixso-symbol-5578_150238 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5578_150239 {
    width: 75%;
    height: 74.99%;
    background-image: url(@/assets/images/Vector82.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 9.38%;
    bottom: 15.63%;
}
</style>
