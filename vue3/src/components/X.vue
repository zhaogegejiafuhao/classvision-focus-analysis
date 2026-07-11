<template>
    <div class="component-5579_151149">
        <div id="5579_151149" class="Pixso-symbol-5579_151149">
            <div
                id="5579_151150"
                class="Pixso-symbol-5579_151150"
                v-if="Format === 'Outline' && Weight === 'Regular'"
            >
                <slot name="slot_5579_151151">
                    <div
                        id="5579_151151"
                        class="Pixso-vector-5579_151151"
                    ></div>
                </slot>
            </div>
            <div
                id="5579_151156"
                class="Pixso-symbol-5579_151156"
                v-if="Format === 'Outline' && Weight === 'Bold'"
            >
                <slot name="slot_5579_151157">
                    <div
                        id="5579_151157"
                        class="Pixso-vector-5579_151157"
                    ></div>
                </slot>
            </div>
            <div
                id="5579_151158"
                class="Pixso-symbol-5579_151158"
                v-if="Format === 'Outline' && Weight === 'Fill'"
            >
                <slot name="slot_5579_151159">
                    <div
                        id="5579_151159"
                        class="Pixso-vector-5579_151159"
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
.Pixso-symbol-5579_151149 {
}
.Pixso-symbol-5579_151150 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5579_151151 {
    width: 62.5%;
    height: 62.5%;
    background-image: url(@/assets/images/Vector150.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 18.75%;
    right: 18.75%;
    top: 18.75%;
    bottom: 18.75%;
}
.Pixso-symbol-5579_151156 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5579_151157 {
    width: 65.64%;
    height: 65.65%;
    background-image: url(@/assets/images/Vector148.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 17.18%;
    right: 17.18%;
    top: 17.17%;
    bottom: 17.18%;
}
.Pixso-symbol-5579_151158 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5579_151159 {
    width: 75%;
    height: 75%;
    background-image: url(@/assets/images/Vector149.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
}
</style>
