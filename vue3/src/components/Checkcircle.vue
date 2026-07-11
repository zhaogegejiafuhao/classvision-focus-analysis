<template>
    <div class="component-5578_149537">
        <div id="5578_149537" class="Pixso-symbol-5578_149537">
            <div
                id="5578_149538"
                class="Pixso-symbol-5578_149538"
                v-if="Format === 'Outline' && Weight === 'Regular'"
            >
                <slot name="slot_5578_149539">
                    <div
                        id="5578_149539"
                        class="Pixso-vector-5578_149539"
                    ></div>
                </slot>
            </div>
            <div
                id="5578_149544"
                class="Pixso-symbol-5578_149544"
                v-if="Format === 'Outline' && Weight === 'Bold'"
            >
                <slot name="slot_5578_149545">
                    <div
                        id="5578_149545"
                        class="Pixso-vector-5578_149545"
                    ></div>
                </slot>
            </div>
            <div
                id="5578_149546"
                class="Pixso-symbol-5578_149546"
                v-if="Format === 'Outline' && Weight === 'Fill'"
            >
                <slot name="slot_5578_149547">
                    <div
                        id="5578_149547"
                        class="Pixso-vector-5578_149547"
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
.Pixso-symbol-5578_149537 {
}
.Pixso-symbol-5578_149538 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5578_149539 {
    width: 81.24%;
    height: 81.24%;
    background-image: url(@/assets/images/Vector47.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 9.38%;
    right: 9.38%;
    top: 9.38%;
    bottom: 9.38%;
}
.Pixso-symbol-5578_149544 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5578_149545 {
    width: 84.38%;
    height: 84.38%;
    background-image: url(@/assets/images/Vector45.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-symbol-5578_149546 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5578_149547 {
    width: 81.24%;
    height: 81.24%;
    background-image: url(@/assets/images/Vector46.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 9.38%;
    right: 9.38%;
    top: 9.38%;
    bottom: 9.38%;
}
</style>
