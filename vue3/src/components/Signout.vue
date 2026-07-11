<template>
    <div class="component-5578_150690">
        <div id="5578_150690" class="Pixso-symbol-5578_150690">
            <div
                id="5578_150691"
                class="Pixso-symbol-5578_150691"
                v-if="Format === 'Outline' && Weight === 'Regular'"
            >
                <slot name="slot_5578_150692">
                    <div
                        id="5578_150692"
                        class="Pixso-vector-5578_150692"
                    ></div>
                </slot>
            </div>
            <div
                id="5578_150697"
                class="Pixso-symbol-5578_150697"
                v-if="Format === 'Outline' && Weight === 'Bold'"
            >
                <slot name="slot_5578_150698">
                    <div
                        id="5578_150698"
                        class="Pixso-vector-5578_150698"
                    ></div>
                </slot>
            </div>
            <div
                id="5578_150699"
                class="Pixso-symbol-5578_150699"
                v-if="Format === 'Outline' && Weight === 'Fill'"
            >
                <slot name="slot_5578_150700">
                    <div
                        id="5578_150700"
                        class="Pixso-vector-5578_150700"
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
.Pixso-symbol-5578_150690 {
}
.Pixso-symbol-5578_150691 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5578_150692 {
    width: 75%;
    height: 75%;
    background-image: url(@/assets/images/Vector113.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 15.63%;
    right: 9.37%;
    top: 12.5%;
    bottom: 12.5%;
}
.Pixso-symbol-5578_150697 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5578_150698 {
    width: 78.13%;
    height: 78.12%;
    background-image: url(@/assets/images/Vector111.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 14.06%;
    right: 7.81%;
    top: 10.94%;
    bottom: 10.94%;
}
.Pixso-symbol-5578_150699 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5578_150700 {
    width: 75%;
    height: 75%;
    background-image: url(@/assets/images/Vector112.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 15.63%;
    right: 9.37%;
    top: 12.5%;
    bottom: 12.5%;
}
</style>
