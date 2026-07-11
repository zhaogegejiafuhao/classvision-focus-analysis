<template>
    <div class="component-5578_149018">
        <div id="5578_149018" class="Pixso-symbol-5578_149018">
            <div
                id="5578_149019"
                class="Pixso-symbol-5578_149019"
                v-if="Format === 'Outline' && Weight === 'Regular'"
            >
                <slot name="slot_5578_149020">
                    <div
                        id="5578_149020"
                        class="Pixso-vector-5578_149020"
                    ></div>
                </slot>
            </div>
            <div
                id="5578_149025"
                class="Pixso-symbol-5578_149025"
                v-if="Format === 'Outline' && Weight === 'Bold'"
            >
                <slot name="slot_5578_149026">
                    <div
                        id="5578_149026"
                        class="Pixso-vector-5578_149026"
                    ></div>
                </slot>
            </div>
            <div
                id="5578_149027"
                class="Pixso-symbol-5578_149027"
                v-if="Format === 'Outline' && Weight === 'Fill'"
            >
                <slot name="slot_5578_149028">
                    <div
                        id="5578_149028"
                        class="Pixso-vector-5578_149028"
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
.Pixso-symbol-5578_149018 {
}
.Pixso-symbol-5578_149019 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5578_149020 {
    width: 81.24%;
    height: 87.47%;
    background-image: url(@/assets/images/Vector17.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 9.38%;
    right: 9.38%;
    top: 6.26%;
    bottom: 6.27%;
}
.Pixso-symbol-5578_149025 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5578_149026 {
    width: 84.38%;
    height: 90.62%;
    background-image: url(@/assets/images/Vector15.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 4.69%;
    bottom: 4.69%;
}
.Pixso-symbol-5578_149027 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5578_149028 {
    width: 81.24%;
    height: 87.47%;
    background-image: url(@/assets/images/Vector16.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 9.38%;
    right: 9.38%;
    top: 6.26%;
    bottom: 6.27%;
}
</style>
