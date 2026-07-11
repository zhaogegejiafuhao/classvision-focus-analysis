<template>
    <div class="component-5577_144100">
        <div id="5577_144100" class="Pixso-symbol-5577_144100">
            <div
                id="5577_144101"
                class="Pixso-symbol-5577_144101"
                v-if="Format === 'Outline' && Weight === 'Regular'"
            >
                <slot name="slot_5577_144102">
                    <div
                        id="5577_144102"
                        class="Pixso-vector-5577_144102"
                    ></div>
                </slot>
            </div>
            <div
                id="5577_144107"
                class="Pixso-symbol-5577_144107"
                v-if="Format === 'Outline' && Weight === 'Bold'"
            >
                <slot name="slot_5577_144108">
                    <div
                        id="5577_144108"
                        class="Pixso-vector-5577_144108"
                    ></div>
                </slot>
            </div>
            <div
                id="5577_144109"
                class="Pixso-symbol-5577_144109"
                v-if="Format === 'Outline' && Weight === 'Fill'"
            >
                <slot name="slot_5577_144110">
                    <div
                        id="5577_144110"
                        class="Pixso-vector-5577_144110"
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
.Pixso-symbol-5577_144100 {
}
.Pixso-symbol-5577_144101 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5577_144102 {
    width: 68.76%;
    height: 37.51%;
    background-image: url(@/assets/images/Vector8.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 15.62%;
    right: 15.62%;
    top: 28.12%;
    bottom: 34.37%;
}
.Pixso-symbol-5577_144107 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5577_144108 {
    width: 71.9%;
    height: 40.65%;
    background-image: url(@/assets/images/Vector6.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 14.05%;
    right: 14.05%;
    top: 26.55%;
    bottom: 32.8%;
}
.Pixso-symbol-5577_144109 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5577_144110 {
    width: 68.76%;
    height: 37.5%;
    background-image: url(@/assets/images/Vector7.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 15.62%;
    right: 15.62%;
    top: 28.12%;
    bottom: 34.38%;
}
</style>
