<template>
    <div class="component-6041_61896">
        <div id="6041_61896" class="Pixso-symbol-6041_61896">
            <div
                id="6041_61897"
                class="Pixso-symbol-6041_61897"
                v-if="Format === 'Outline' && Weight === 'Regular'"
            >
                <slot name="slot_6041_61898">
                    <div id="6041_61898" class="Pixso-vector-6041_61898"></div>
                </slot>
            </div>
            <div
                id="6041_61903"
                class="Pixso-symbol-6041_61903"
                v-if="Format === 'Outline' && Weight === 'Bold'"
            >
                <slot name="slot_6041_61904">
                    <div id="6041_61904" class="Pixso-vector-6041_61904"></div>
                </slot>
            </div>
            <div
                id="6041_61905"
                class="Pixso-symbol-6041_61905"
                v-if="Format === 'Outline' && Weight === 'Fill'"
            >
                <slot name="slot_6041_61906">
                    <div id="6041_61906" class="Pixso-vector-6041_61906"></div>
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
.Pixso-symbol-6041_61896 {
}
.Pixso-symbol-6041_61897 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-6041_61898 {
    width: 81.25%;
    height: 81.24%;
    background-image: url(@/assets/images/Vector344.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 9.37%;
    right: 9.38%;
    top: 9.38%;
    bottom: 9.38%;
}
.Pixso-symbol-6041_61903 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-6041_61904 {
    width: 84.38%;
    height: 84.38%;
    background-image: url(@/assets/images/Vector342.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-symbol-6041_61905 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-6041_61906 {
    width: 81.25%;
    height: 81.24%;
    background-image: url(@/assets/images/Vector343.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 9.37%;
    right: 9.38%;
    top: 9.38%;
    bottom: 9.38%;
}
</style>
