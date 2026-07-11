<template>
    <div class="component-5578_150571">
        <div id="5578_150571" class="Pixso-symbol-5578_150571">
            <div
                id="5578_150572"
                class="Pixso-symbol-5578_150572"
                v-if="Format === 'Outline' && Weight === 'Regular'"
            >
                <slot name="slot_5578_150573">
                    <div
                        id="5578_150573"
                        class="Pixso-vector-5578_150573"
                    ></div>
                </slot>
            </div>
            <div
                id="5578_150578"
                class="Pixso-symbol-5578_150578"
                v-if="Format === 'Outline' && Weight === 'Bold'"
            >
                <slot name="slot_5578_150579">
                    <div
                        id="5578_150579"
                        class="Pixso-vector-5578_150579"
                    ></div>
                </slot>
            </div>
            <div
                id="5578_150580"
                class="Pixso-symbol-5578_150580"
                v-if="Format === 'Outline' && Weight === 'Fill'"
            >
                <slot name="slot_5578_150581">
                    <div
                        id="5578_150581"
                        class="Pixso-vector-5578_150581"
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
.Pixso-symbol-5578_150571 {
}
.Pixso-symbol-5578_150572 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5578_150573 {
    width: 81.34%;
    height: 81.34%;
    background-image: url(@/assets/images/Vector107.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 9.29%;
    right: 9.37%;
    top: 9.29%;
    bottom: 9.37%;
}
.Pixso-symbol-5578_150578 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5578_150579 {
    width: 84.48%;
    height: 84.48%;
    background-image: url(@/assets/images/Vector105.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 7.73%;
    right: 7.79%;
    top: 7.73%;
    bottom: 7.79%;
}
.Pixso-symbol-5578_150580 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5578_150581 {
    width: 81.25%;
    height: 81.28%;
    background-image: url(@/assets/images/Vector106.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 9.38%;
    right: 9.37%;
    top: 9.35%;
    bottom: 9.37%;
}
</style>
