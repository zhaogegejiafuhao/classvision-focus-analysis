<template>
    <div class="component-5577_144034">
        <div id="5577_144034" class="Pixso-symbol-5577_144034">
            <div
                id="5577_144035"
                class="Pixso-symbol-5577_144035"
                v-if="Format === 'Outline' && Weight === 'Regular'"
            >
                <slot name="slot_5577_144036">
                    <div
                        id="5577_144036"
                        class="Pixso-vector-5577_144036"
                    ></div>
                </slot>
            </div>
            <div
                id="5577_144041"
                class="Pixso-symbol-5577_144041"
                v-if="Format === 'Outline' && Weight === 'Bold'"
            >
                <slot name="slot_5577_144042">
                    <div
                        id="5577_144042"
                        class="Pixso-vector-5577_144042"
                    ></div>
                </slot>
            </div>
            <div
                id="5577_144043"
                class="Pixso-symbol-5577_144043"
                v-if="Format === 'Outline' && Weight === 'Fill'"
            >
                <slot name="slot_5577_144044">
                    <div
                        id="5577_144044"
                        class="Pixso-vector-5577_144044"
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
.Pixso-symbol-5577_144034 {
}
.Pixso-symbol-5577_144035 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5577_144036 {
    width: 37.51%;
    height: 68.76%;
    background-image: url(@/assets/images/Vector24.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 28.12%;
    right: 34.37%;
    top: 15.62%;
    bottom: 15.62%;
}
.Pixso-symbol-5577_144041 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5577_144042 {
    width: 40.64%;
    height: 71.89%;
    background-image: url(@/assets/images/Vector26.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 26.55%;
    right: 32.81%;
    top: 14.06%;
    bottom: 14.05%;
}
.Pixso-symbol-5577_144043 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5577_144044 {
    width: 37.51%;
    height: 68.76%;
    background-image: url(@/assets/images/Vector25.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 28.12%;
    right: 34.37%;
    top: 15.62%;
    bottom: 15.62%;
}
</style>
