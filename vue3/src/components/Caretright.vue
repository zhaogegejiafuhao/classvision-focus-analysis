<template>
    <div class="component-5577_144067">
        <div id="5577_144067" class="Pixso-symbol-5577_144067">
            <div
                id="5577_144068"
                class="Pixso-symbol-5577_144068"
                v-if="Format === 'Outline' && Weight === 'Regular'"
            >
                <slot name="slot_5577_144069">
                    <div
                        id="5577_144069"
                        class="Pixso-vector-5577_144069"
                    ></div>
                </slot>
            </div>
            <div
                id="5577_144074"
                class="Pixso-symbol-5577_144074"
                v-if="Format === 'Outline' && Weight === 'Bold'"
            >
                <slot name="slot_5577_144075">
                    <div
                        id="5577_144075"
                        class="Pixso-vector-5577_144075"
                    ></div>
                </slot>
            </div>
            <div
                id="5577_144076"
                class="Pixso-symbol-5577_144076"
                v-if="Format === 'Outline' && Weight === 'Fill'"
            >
                <slot name="slot_5577_144077">
                    <div
                        id="5577_144077"
                        class="Pixso-vector-5577_144077"
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
.Pixso-symbol-5577_144067 {
}
.Pixso-symbol-5577_144068 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5577_144069 {
    width: 37.51%;
    height: 68.76%;
    background-image: url(@/assets/images/Vector14.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 34.37%;
    right: 28.12%;
    top: 15.62%;
    bottom: 15.62%;
}
.Pixso-symbol-5577_144074 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5577_144075 {
    width: 40.65%;
    height: 71.89%;
    background-image: url(@/assets/images/Vector12.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 32.8%;
    right: 26.55%;
    top: 14.05%;
    bottom: 14.06%;
}
.Pixso-symbol-5577_144076 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5577_144077 {
    width: 37.5%;
    height: 68.76%;
    background-image: url(@/assets/images/Vector13.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 34.38%;
    right: 28.12%;
    top: 15.62%;
    bottom: 15.62%;
}
</style>
