<template>
    <div class="component-5577_144001">
        <div id="5577_144001" class="Pixso-symbol-5577_144001">
            <div
                id="5577_144002"
                class="Pixso-symbol-5577_144002"
                v-if="Format === 'Outline' && Weight === 'Regular'"
            >
                <slot name="slot_5577_144003">
                    <div
                        id="5577_144003"
                        class="Pixso-vector-5577_144003"
                    ></div>
                </slot>
            </div>
            <div
                id="5577_144008"
                class="Pixso-symbol-5577_144008"
                v-if="Format === 'Outline' && Weight === 'Bold'"
            >
                <slot name="slot_5577_144009">
                    <div
                        id="5577_144009"
                        class="Pixso-vector-5577_144009"
                    ></div>
                </slot>
            </div>
            <div
                id="5577_144010"
                class="Pixso-symbol-5577_144010"
                v-if="Format === 'Outline' && Weight === 'Fill'"
            >
                <slot name="slot_5577_144011">
                    <div
                        id="5577_144011"
                        class="Pixso-vector-5577_144011"
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
.Pixso-symbol-5577_144001 {
}
.Pixso-symbol-5577_144002 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5577_144003 {
    width: 68.76%;
    height: 37.51%;
    background-image: url(@/assets/images/Vector20.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 15.62%;
    right: 15.62%;
    top: 34.37%;
    bottom: 28.12%;
}
.Pixso-symbol-5577_144008 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5577_144009 {
    width: 71.9%;
    height: 40.64%;
    background-image: url(@/assets/images/Vector19.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 14.05%;
    right: 14.05%;
    top: 32.8%;
    bottom: 26.56%;
}
.Pixso-symbol-5577_144010 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5577_144011 {
    width: 68.76%;
    height: 37.5%;
    background-image: url(@/assets/images/Vector18.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 15.62%;
    right: 15.62%;
    top: 34.38%;
    bottom: 28.12%;
}
</style>
