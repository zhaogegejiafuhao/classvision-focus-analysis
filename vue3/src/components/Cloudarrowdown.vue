<template>
    <div class="component-5578_149613">
        <div id="5578_149613" class="Pixso-symbol-5578_149613">
            <div
                id="5578_149614"
                class="Pixso-symbol-5578_149614"
                v-if="Format === 'Outline' && Weight === 'Regular'"
            >
                <slot name="slot_5578_149615">
                    <div
                        id="5578_149615"
                        class="Pixso-vector-5578_149615"
                    ></div>
                </slot>
            </div>
            <div
                id="5578_149620"
                class="Pixso-symbol-5578_149620"
                v-if="Format === 'Outline' && Weight === 'Bold'"
            >
                <slot name="slot_5578_149621">
                    <div
                        id="5578_149621"
                        class="Pixso-vector-5578_149621"
                    ></div>
                </slot>
            </div>
            <div
                id="5578_149622"
                class="Pixso-symbol-5578_149622"
                v-if="Format === 'Outline' && Weight === 'Fill'"
            >
                <slot name="slot_5578_149623">
                    <div
                        id="5578_149623"
                        class="Pixso-vector-5578_149623"
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
.Pixso-symbol-5578_149613 {
}
.Pixso-symbol-5578_149614 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5578_149615 {
    width: 93.75%;
    height: 68.74%;
    background-image: url(@/assets/images/Vector53.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 3.12%;
    right: 3.13%;
    top: 15.64%;
    bottom: 15.62%;
}
.Pixso-symbol-5578_149620 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5578_149621 {
    width: 96.91%;
    height: 71.89%;
    background-image: url(@/assets/images/Vector51.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 1.53%;
    right: 1.56%;
    top: 14.06%;
    bottom: 14.05%;
}
.Pixso-symbol-5578_149622 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5578_149623 {
    width: 93.74%;
    height: 68.74%;
    background-image: url(@/assets/images/Vector52.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 3.13%;
    right: 3.13%;
    top: 15.63%;
    bottom: 15.63%;
}
</style>
