<template>
    <div class="component-6041_60635">
        <div id="6041_60635" class="Pixso-symbol-6041_60635">
            <div
                id="6041_60636"
                class="Pixso-symbol-6041_60636"
                v-if="Format === 'Outline' && Weight === 'Regular'"
            >
                <slot name="slot_6041_60637">
                    <div id="6041_60637" class="Pixso-vector-6041_60637"></div>
                </slot>
            </div>
            <div
                id="6041_60638"
                class="Pixso-symbol-6041_60638"
                v-if="Format === 'Outline' && Weight === 'Bold'"
            >
                <slot name="slot_6041_60639">
                    <div id="6041_60639" class="Pixso-vector-6041_60639"></div>
                </slot>
            </div>
            <div
                id="6041_60640"
                class="Pixso-symbol-6041_60640"
                v-if="Format === 'Outline' && Weight === 'Fill'"
            >
                <slot name="slot_6041_60641">
                    <div id="6041_60641" class="Pixso-vector-6041_60641"></div>
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
.Pixso-symbol-6041_60635 {
}
.Pixso-symbol-6041_60636 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-6041_60637 {
    width: 81.24%;
    height: 81.24%;
    background-image: url(@/assets/images/Vector371.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 9.38%;
    right: 9.38%;
    top: 9.38%;
    bottom: 9.38%;
}
.Pixso-symbol-6041_60638 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-6041_60639 {
    width: 84.38%;
    height: 84.38%;
    background-image: url(@/assets/images/Vector369.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-symbol-6041_60640 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-6041_60641 {
    width: 81.24%;
    height: 81.24%;
    background-image: url(@/assets/images/Vector370.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 9.38%;
    right: 9.38%;
    top: 9.38%;
    bottom: 9.38%;
}
</style>
